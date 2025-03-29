import streamlit as st

def main():
    st.set_page_config(page_title="Python Mini Projects", page_icon="🐍", layout="wide")
    
    st.title("🚀 Python Mini Projects")
    st.markdown(
        """
        Welcome to a collection of fun and interactive Python mini-projects built using Streamlit! 🎉
        Explore various Python concepts through engaging games and utility tools.
        """,
        unsafe_allow_html=True
    )
    
    st.divider()
    st.subheader("📌 All Projects in One Place")
    
    # Dictionary of projects with emojis and descriptions
    projects = {
        "📖 Mad Libs Python Project": """
        A fun word-based game where you create a story by filling in the blanks!
        Enter nouns, verbs, and adjectives to generate a hilarious story.
        Perfect for learning Python string manipulation and user input handling.
        """,
        "🤖 Guess the Number Game (Computer vs User)": """
        Try to guess the number chosen by the computer!
        The app provides hints like 'too high' or 'too low' to guide you.
        A great way to learn about random number generation and loops.
        """,
        "🧠 Guess the Number Game (User vs Computer)": """
        The computer tries to guess your chosen number!
        You provide hints like 'higher' or 'lower' to help the computer.
        Learn about binary search algorithms and Python logic.
        """,
        "✂️ Rock, Paper, Scissors Game": """
        Play against the computer in this classic game!
        Choose rock, paper, or scissors and see who wins.
        A fun way to learn about conditional statements and game logic.
        """,
        "🪢 Hangman Game": """
        Guess the word before you run out of attempts!
        The app selects a random word, and you guess letters one by one.
        Learn about string manipulation and loops in Python.
        """,
        "⏳ Countdown Timer": """
        A simple timer to count down from a specified time.
        Set a duration and watch the timer count down to zero.
        Perfect for learning about Python's time module and user input.
        """,
        "🔐 Password Generator": """
        Generate strong and secure passwords instantly.
        Customize the length and complexity of your passwords.
        Learn about Python's random module and string manipulation.
        """
    }
    
    # Create a single container for all projects
    with st.container(border=True):
        st.markdown("### 🎯 Projects")  # Container heading
        
        for project_name, description in projects.items():
            st.markdown(f"**{project_name}**")  # Bold project name with emoji
            st.write(description)  # Project description (at least 3 lines)
            st.write("")  # Add spacing between projects
    
    
if __name__ == "__main__":
    main()