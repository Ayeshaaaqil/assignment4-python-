import streamlit as st
import random

st.set_page_config(page_title="Mad Libs Game", page_icon="📝")

st.title("🎮 Mad Libs Game")
st.subheader("Fill in the blanks to create a funny story!")

# Story templates
stories = [
    {
        "title": "A Day at the Zoo",
        "template": """
        Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
        It {verb_past1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}.
        I got some peanuts and passed them through the cage to a gigantic gray {noun3}
        towering above my head. Feeding that animal made me {adjective3} but I was
        careful to not {verb1} too close to the fence. Next time I'll remember to bring my {noun4}!
        """
    },
    {
        "title": "Space Adventure",
        "template": """
        I'm an astronaut preparing for a mission to {noun1}. Before takeoff, I need to {verb1} my
        {adjective1} spacesuit and check the {noun2} levels. The captain is very {adjective2}
        about safety protocols. During the journey, we'll {verb2} {adverb1} through the
        galaxy, looking for signs of {adjective3} life forms. I'm most excited to see the
        {noun3} that scientists discovered last year. They say it {verb_past1} {adverb2}
        when approached by humans. I've packed my lucky {noun4} for good measure!
        """
    },
    {
        "title": "The Mystery",
        "template": """
        There's a {adjective1} mystery in the town of {noun1}. Detective {noun2} has been
        trying to {verb1} the case for weeks. The clues are {adjective2} and seem to lead
        nowhere. Yesterday, a {adjective3} {noun3} was found near the scene that might
        {verb2} the case wide open. The detective {verb_past1} {adverb1} around the evidence,
        looking for fingerprints. If this mystery isn't solved soon, the whole town will {verb3}!
        """
    }
]

# Sidebar for story selection
with st.sidebar:
    st.header("Choose a Story")
    story_index = st.radio("Select a story template:", 
                          options=range(len(stories)), 
                          format_func=lambda x: stories[x]["title"])
    
    if st.button("Random Story"):
        story_index = random.randint(0, len(stories) - 1)
        st.rerun()

selected_story = stories[story_index]
st.markdown(f"### {selected_story['title']}")

# Create a form to collect inputs
with st.form("mad_libs_form"):
    st.write("Fill in the words:")
    
    # Parse the template to find required inputs
    template = selected_story["template"]
    placeholders = []
    current = ""
    inside_bracket = False
    
    for char in template:
        if char == '{':
            inside_bracket = True
            current = ""
        elif char == '}':
            inside_bracket = False
            placeholders.append(current)
        elif inside_bracket:
            current += char
    
    # Remove duplicates while preserving order
    unique_placeholders = []
    for item in placeholders:
        if item not in unique_placeholders:
            unique_placeholders.append(item)
    
    # Create input fields for each unique placeholder
    inputs = {}
    cols = st.columns(2)
    
    for i, placeholder in enumerate(unique_placeholders):
        with cols[i % 2]:
            label = placeholder.replace("_", " ").title()
            inputs[placeholder] = st.text_input(label, key=placeholder)
    
    submit = st.form_submit_button("Generate Story!")

# Generate and display the story
if submit:
    # Check if all fields are filled
    if all(inputs.values()):
        completed_story = selected_story["template"]
        
        # Replace placeholders with user inputs
        for placeholder, value in inputs.items():
            completed_story = completed_story.replace(f"{{{placeholder}}}", value)
        
        st.success("Your Mad Libs story is ready!")
        st.markdown("## Your Story")
        st.markdown(completed_story)
        
        # Add some fun reactions
        st.balloons()
    else:
        st.error("Please fill in all the fields!")

# Instructions
with st.expander("How to Play"):
    st.write("""
    1. Choose a story template from the sidebar
    2. Fill in all the requested words (nouns, verbs, adjectives, etc.)
    3. Click 'Generate Story' to see your creation
    4. Have fun and get creative with your words!
    
    **Word Types:**
    - **Noun**: Person, place, or thing (e.g., teacher, beach, computer)
    - **Verb**: Action word (e.g., run, jump, type)
    - **Verb Past**: Past tense action (e.g., ran, jumped, typed)
    - **Adjective**: Describes a noun (e.g., happy, blue, giant)
    - **Adverb**: Describes a verb (e.g., quickly, loudly, carefully)
    """)

# Add a footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")