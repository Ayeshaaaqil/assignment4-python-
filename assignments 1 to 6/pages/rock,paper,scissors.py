import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Rock Paper Scissors Game",
    page_icon="✂️",
    layout="centered"
)

# Initialize session state for score tracking
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'ties' not in st.session_state:
    st.session_state.ties = 0
if 'game_history' not in st.session_state:
    st.session_state.game_history = []

# Title and description
st.title("✊ Rock Paper Scissors ✌️")
st.markdown("Play the classic game against the computer!")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "User"
    else:
        return "Computer"

# Function to get emoji for choice
def get_emoji(choice):
    if choice == "Rock":
        return "✊"
    elif choice == "Paper":
        return "✋"
    else:  # Scissors
        return "✌️"

# Game interface
st.markdown("### Make your choice:")

# Create columns for the buttons
col1, col2, col3 = st.columns(3)

# Game logic
user_choice = None

with col1:
    if st.button("✊ Rock", use_container_width=True):
        user_choice = "Rock"

with col2:
    if st.button("✋ Paper", use_container_width=True):
        user_choice = "Paper"

with col3:
    if st.button("✌️ Scissors", use_container_width=True):
        user_choice = "Scissors"

# Process the game if user made a choice
if user_choice:
    # Computer makes a random choice
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    # Determine the winner
    winner = determine_winner(user_choice, computer_choice)
    
    # Update scores
    if winner == "User":
        st.session_state.user_score += 1
        result_message = "You win! 🎉"
    elif winner == "Computer":
        st.session_state.computer_score += 1
        result_message = "Computer wins! 💻"
    else:
        st.session_state.ties += 1
        result_message = "It's a tie! 🤝"
    
    # Add to game history
    st.session_state.game_history.append({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": winner
    })
    
    # Display the result
    st.markdown("---")
    st.markdown("### Result:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### You chose: {get_emoji(user_choice)} {user_choice}")
    with col2:
        st.markdown(f"### Computer chose: {get_emoji(computer_choice)} {computer_choice}")
    
    st.markdown(f"## {result_message}")

# Display the scoreboard
st.markdown("---")
st.markdown("### Scoreboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("You", st.session_state.user_score)
with col2:
    st.metric("Ties", st.session_state.ties)
with col3:
    st.metric("Computer", st.session_state.computer_score)

# Reset button
if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.game_history = []
    st.experimental_rerun()

# Game history
if st.session_state.game_history:
    st.markdown("---")
    st.markdown("### Game History")
    
    for i, game in enumerate(reversed(st.session_state.game_history[-5:])):
        st.markdown(f"**Game {len(st.session_state.game_history) - i}**: "
                   f"You chose {get_emoji(game['user_choice'])} vs Computer's {get_emoji(game['computer_choice'])} - "
                   f"{'You won!' if game['result'] == 'User' else 'Computer won!' if game['result'] == 'Computer' else 'Tie!'}")