import streamlit as st
import time
from datetime import datetime, timedelta
import pandas as pd
import altair as alt

# Set page configuration
st.set_page_config(
    page_title="Study Schedule Timer",
    page_icon="⏱️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .timer-display {
        font-size: 4rem;
        font-weight: bold;
        text-align: center;
    }
    .session-title {
        font-size: 2rem;
        text-align: center;
        font-weight: bold;
    }
    .subject-tag {
        background-color: #e3f2fd;
        padding: 5px 10px;
        border-radius: 5px;
        display: inline-block;
        font-weight: bold;
    }
    .completed {
        text-decoration: line-through;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'current_session' not in st.session_state:
    st.session_state.current_session = 'study'
if 'end_time' not in st.session_state:
    st.session_state.end_time = None
if 'sessions_completed' not in st.session_state:
    st.session_state.sessions_completed = 0
if 'breaks_completed' not in st.session_state:
    st.session_state.breaks_completed = 0
if 'total_study_time' not in st.session_state:
    st.session_state.total_study_time = 0
if 'study_log' not in st.session_state:
    st.session_state.study_log = []
if 'current_subject' not in st.session_state:
    st.session_state.current_subject = ""
if 'subjects' not in st.session_state:
    st.session_state.subjects = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Timer Settings")
    study_duration = st.number_input("Study Duration (min)", min_value=1, max_value=120, value=25)
    break_duration = st.number_input("Short Break (min)", min_value=1, max_value=30, value=5)
    long_break_duration = st.number_input("Long Break (min)", min_value=5, max_value=60, value=15)
    sessions_before_long_break = st.number_input("Sessions before Long Break", min_value=1, max_value=10, value=4)

    # Subject and Task Management
    st.header("📋 Manage Subjects")
    new_subject = st.text_input("Add a subject")
    if st.button("Add Subject") and new_subject:
        if new_subject not in st.session_state.subjects:
            st.session_state.subjects.append(new_subject)
            st.success(f"Added: {new_subject}")

    if st.session_state.subjects:
        st.session_state.current_subject = st.selectbox("Select Subject", options=st.session_state.subjects)

    st.header("✅ Tasks")
    new_task = st.text_input("Add a Task")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success(f"Added: {new_task}")

# Timer section
col1, col2 = st.columns([2, 1])

with col1:
    if st.session_state.timer_running:
        session_type = "Study Session" if st.session_state.current_session == 'study' else "Break Time"
        session_color = "#A8E6CF" if st.session_state.current_session == 'study' else "#FFD3B6"

        st.markdown(f"<div style='text-align: center; font-size: 24px; background: {session_color}; padding: 10px; border-radius: 10px;'>{session_type}</div>", unsafe_allow_html=True)

        if st.session_state.current_session == 'study' and st.session_state.current_subject:
            st.markdown(f"<div class='subject-tag'>{st.session_state.current_subject}</div>", unsafe_allow_html=True)

        timer_display = st.empty()

        # Timer logic
        while st.session_state.end_time and datetime.now() < st.session_state.end_time:
            remaining = st.session_state.end_time - datetime.now()
            mins, secs = divmod(remaining.seconds, 60)
            timer_display.markdown(f"<div class='timer-display'>{mins:02d}:{secs:02d}</div>", unsafe_allow_html=True)
            st.progress(1 - (remaining.seconds / (study_duration * 60 if st.session_state.current_session == 'study' else (long_break_duration * 60 if st.session_state.sessions_completed % sessions_before_long_break == 0 else break_duration * 60))))
            time.sleep(1)

        # After timer completes
        if st.session_state.current_session == 'study':
            st.session_state.sessions_completed += 1
            st.session_state.total_study_time += study_duration
            if st.session_state.current_subject:
                st.session_state.study_log.append({"date": datetime.now().strftime("%Y-%m-%d"), "subject": st.session_state.current_subject, "duration": study_duration})
            st.session_state.current_session = 'break'
            if st.session_state.sessions_completed % sessions_before_long_break == 0:
                st.session_state.end_time = datetime.now() + timedelta(minutes=long_break_duration)
            else:
                st.session_state.end_time = datetime.now() + timedelta(minutes=break_duration)
        else:
            st.session_state.current_session = 'study'
            st.session_state.end_time = datetime.now() + timedelta(minutes=study_duration)

        st.rerun()

    else:
        if st.button("Start Study Session", use_container_width=True):
            st.session_state.timer_running = True
            st.session_state.current_session = 'study'
            st.session_state.end_time = datetime.now() + timedelta(minutes=study_duration)
            st.rerun()

with col2:
    st.subheader("📊 Stats")
    st.metric("Study Sessions", st.session_state.sessions_completed)
    st.metric("Total Study Time", f"{st.session_state.total_study_time} min")

st.header("📈 Study Analytics")
if st.session_state.study_log:
    log_df = pd.DataFrame(st.session_state.study_log)
    chart = alt.Chart(log_df).mark_bar().encode(x='subject', y='duration', color='subject').properties(title='Study Time by Subject', width=600, height=300)
    st.altair_chart(chart, use_container_width=True)
    st.dataframe(log_df)

if st.button("Reset Data"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
