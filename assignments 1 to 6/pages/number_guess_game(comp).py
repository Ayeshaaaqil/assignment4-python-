import streamlit as st
import random
import time
import math

# Set page configuration
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

# Initialize session state variables
if 'random_number' not in st.session_state:
    st.session_state.random_number = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = 0
if 'game_active' not in st.session_state:
    st.session_state.game_active = False
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'win' not in st.session_state:
    st.session_state.win = False
if 'history' not in st.session_state:
    st.session_state.history = []
if 'total_games' not in st.session_state:
    st.session_state.total_games = 0
if 'wins' not in st.session_state:
    st.session_state.wins = 0
if 'high_score' not in st.session_state:
    st.session_state.high_score = float('inf')
if 'range_min' not in st.session_state:
    st.session_state.range_min = 1
if 'range_max' not in st.session_state:
    st.session_state.range_max = 100
if 'hint_used' not in st.session_state:
    st.session_state.hint_used = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = 0
if 'clear_guess' not in st.session_state:
    st.session_state.clear_guess = False  # ✅ Flag for resetting input

# Function to start a new game
def start_new_game():
    difficulty = st.session_state.difficulty
    
    if difficulty == "Easy":
        range_min, range_max = 1, 50
        max_attempts = 10
    elif difficulty == "Medium":
        range_min, range_max = 1, 100
        max_attempts = 7
    elif difficulty == "Hard":
        range_min, range_max = 1, 500
        max_attempts = 9
    else:  
        range_min = st.session_state.custom_min
        range_max = st.session_state.custom_max
        range_size = range_max - range_min + 1
        max_attempts = math.ceil(math.log2(range_size)) + 2

    st.session_state.random_number = random.randint(range_min, range_max)
    st.session_state.range_min = range_min
    st.session_state.range_max = range_max
    st.session_state.attempts = 0
    st.session_state.max_attempts = max_attempts
    st.session_state.game_active = True
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.history = []
    st.session_state.hint_used = False
    st.session_state.start_time = time.time()
    st.session_state.elapsed_time = 0
    st.session_state.clear_guess = True  # ✅ Reset input when game starts

# Function to check the guess
def check_guess():
    try:
        guess = int(st.session_state.user_guess)
    except ValueError:
        st.error("Please enter a valid number!")
        return

    st.session_state.attempts += 1

    if guess == st.session_state.random_number:
        st.session_state.win = True
        st.session_state.game_over = True
        st.session_state.wins += 1
        st.session_state.elapsed_time = time.time() - st.session_state.start_time

        if st.session_state.attempts < st.session_state.high_score:
            st.session_state.high_score = st.session_state.attempts
    elif st.session_state.attempts >= st.session_state.max_attempts:
        st.session_state.game_over = True
        st.session_state.elapsed_time = time.time() - st.session_state.start_time

    if guess < st.session_state.random_number:
        feedback = "Too low!"
    elif guess > st.session_state.random_number:
        feedback = "Too high!"
    else:
        feedback = "Correct!"

    st.session_state.history.append((guess, feedback))

    # ✅ Reset input field after guess submission
    st.session_state.clear_guess = True


# Sidebar Settings
with st.sidebar:
    st.header("Game Settings")

    difficulty_options = ["Easy", "Medium", "Hard", "Custom"]
    st.selectbox("Select Difficulty", difficulty_options, key="difficulty")

    if st.session_state.difficulty == "Custom":
        st.number_input("Minimum Range", min_value=1, max_value=9999, value=1, key="custom_min")
        st.number_input("Maximum Range", min_value=2, max_value=10000, value=200, key="custom_max")

    if st.button("Start New Game"):
        start_new_game()
        st.session_state.total_games += 1

# Main Game Interface
if not st.session_state.game_active:
    st.info("👈 Select a difficulty level and click 'Start New Game' to begin!")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Range", f"{st.session_state.range_min} to {st.session_state.range_max}")
    with col2:
        st.metric("Attempts", f"{st.session_state.attempts}/{st.session_state.max_attempts}")

    # ✅ Use `st.session_state.clear_guess` to clear input field
    if st.session_state.clear_guess:
        st.session_state.user_guess = ""  # ✅ Reset manually
        st.session_state.clear_guess = False  # ✅ Reset flag

    user_input = st.text_input("Enter your guess:", key="user_guess")

    if st.button("Submit Guess"):
        check_guess()

    if st.session_state.game_over:
        if st.session_state.win:
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state.random_number} in {st.session_state.attempts} attempts!")
            st.balloons()
        else:
            st.error(f"Game Over! The number was {st.session_state.random_number}. Better luck next time!")

        st.info(f"Time taken: {st.session_state.elapsed_time:.1f} seconds")

        if st.button("Play Again"):
            start_new_game()
            st.session_state.total_games += 1

    if st.session_state.history:
        st.markdown("### Your Guesses")
        history_df = {"Attempt": [], "Guess": [], "Feedback": []}

        for i, (guess, feedback) in enumerate(st.session_state.history):
            history_df["Attempt"].append(i + 1)
            history_df["Guess"].append(guess)
            history_df["Feedback"].append(feedback)

        st.dataframe(history_df, use_container_width=True)

st.markdown("---")
st.markdown("Created with ❤️ using Streamlit") 
