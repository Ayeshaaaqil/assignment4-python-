import streamlit as st
import random
import string

# Set page configuration
st.set_page_config(
    page_title="Hangman Game",
    page_icon="🎮",
    layout="centered"
)

# Define hangman stages (ASCII art)
HANGMAN_STAGES = [
    """
    -----
    |   |
    |
    |
    |
    |
    -------
    """,
    """
    -----
    |   |
    |   O
    |
    |
    |
    -------
    """,
    """
    -----
    |   |
    |   O
    |   |
    |
    |
    -------
    """,
    """
    -----
    |   |
    |   O
    |  /|
    |
    |
    -------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |
    |
    -------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  /
    |
    -------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    -------
    """
]

# Word bank
WORD_BANK = [
    "python", "streamlit", "coding", "programming", "developer",
    "algorithm", "function", "variable", "computer", "keyboard",
    "monitor", "software", "hardware", "database", "network",
    "internet", "application", "framework", "library", "debugging"
]

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = random.choice(WORD_BANK).upper()
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = set()
if 'attempts_left' not in st.session_state:
    st.session_state.attempts_left = 6
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'win' not in st.session_state:
    st.session_state.win = False
if 'games_played' not in st.session_state:
    st.session_state.games_played = 0
if 'games_won' not in st.session_state:
    st.session_state.games_won = 0

# Title
st.title("🎮 Hangman Game")
st.markdown("Guess the hidden word one letter at a time. Be careful - you only get 6 wrong guesses!")

# Function to display word progress
def display_word():
    return " ".join([letter if letter in st.session_state.guessed_letters else "_" for letter in st.session_state.word])

# Function to check for win
def check_win():
    return all(letter in st.session_state.guessed_letters for letter in st.session_state.word)

# Function to reset the game
def reset_game():
    st.session_state.word = random.choice(WORD_BANK).upper()
    st.session_state.guessed_letters = set()
    st.session_state.attempts_left = 6
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.games_played += 1

# Display hangman stage
st.markdown("### Hangman:")
st.text(HANGMAN_STAGES[6 - st.session_state.attempts_left])

# Display word progress
st.markdown("### Word to guess:")
st.markdown(f"<h2 style='text-align: center; letter-spacing: 3px;'>{display_word()}</h2>", unsafe_allow_html=True)

# Display attempts left
st.markdown(f"### Attempts left: {st.session_state.attempts_left}")

# Display guessed letters
if st.session_state.guessed_letters:
    st.markdown("### Letters guessed:")
    guessed_str = ", ".join(sorted(st.session_state.guessed_letters))
    st.markdown(f"<p style='text-align: center; font-size: 18px;'>{guessed_str}</p>", unsafe_allow_html=True)

# Game over or win message
if st.session_state.game_over:
    if st.session_state.win:
        st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.word}")
    else:
        st.error(f"😔 Game Over! The word was: {st.session_state.word}")
    
    if st.button("Play Again"):
        reset_game()
        st.rerun()
else:
    # Letter input
    st.markdown("### Guess a letter:")
    
    # Create a row of letter buttons
    cols = st.columns(7)
    alphabet = string.ascii_uppercase
    letter_index = 0
    
    for i in range(4):  # 4 rows of letters
        for j in range(7):  # 7 letters per row
            if letter_index < len(alphabet):
                letter = alphabet[letter_index]
                with cols[j]:
                    disabled = letter in st.session_state.guessed_letters
                    if st.button(letter, key=letter, disabled=disabled, use_container_width=True):
                        st.session_state.guessed_letters.add(letter)
                        
                        if letter not in st.session_state.word:
                            st.session_state.attempts_left -= 1
                            if st.session_state.attempts_left == 0:
                                st.session_state.game_over = True
                        
                        if check_win():
                            st.session_state.win = True
                            st.session_state.game_over = True
                            st.session_state.games_won += 1
                        
                        st.rerun()
                letter_index += 1

# Display game statistics
st.markdown("---")
st.markdown("### Game Statistics")
col1, col2 = st.columns(2)
with col1:
    st.metric("Games Played", st.session_state.games_played)
with col2:
    st.metric("Games Won", st.session_state.games_won)

# Option to start a new game with a different word
if not st.session_state.game_over:
    st.markdown("---")
    if st.button("Start New Game"):
        reset_game()
        st.rerun()

# Add a hint option
if not st.session_state.game_over:
    if st.button("Get a Hint"):
        unguessed = [letter for letter in st.session_state.word if letter not in st.session_state.guessed_letters]
        if unguessed:
            hint_letter = random.choice(unguessed)
            st.session_state.guessed_letters.add(hint_letter)
            st.session_state.attempts_left = max(st.session_state.attempts_left - 1, 0)
            
            if check_win():
                st.session_state.win = True
                st.session_state.game_over = True
                st.session_state.games_won += 1
            
            if st.session_state.attempts_left == 0:
                st.session_state.game_over = True
            
            st.rerun()
