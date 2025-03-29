import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered"
)

# App title and description
st.title("🔐 Password Input")
st.markdown("Enter a secure password manually.")

# Manual password input
user_password = st.text_input("Enter Your Password", type="password")

# Check Password Strength button
if st.button("Check Password Strength"):
    if user_password:
        st.success("Password entered successfully!")
        
        # Password strength indicator
        strength = "Weak"
        if len(user_password) >= 12 and sum([
            any(c.isupper() for c in user_password),
            any(c.islower() for c in user_password),
            any(c.isdigit() for c in user_password),
            any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in user_password)
        ]) >= 3:
            strength = "Strong"
        elif len(user_password) >= 8 and sum([
            any(c.isupper() for c in user_password),
            any(c.islower() for c in user_password),
            any(c.isdigit() for c in user_password),
            any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in user_password)
        ]) >= 2:
            strength = "Medium"
        
        st.info(f"Password Strength: {strength}")
        
        # Tips for secure passwords
        with st.expander("Password Security Tips"):
            st.markdown("""
            - Use passwords of at least 12 characters
            - Include a mix of character types
            - Don't use personal information
            - Use different passwords for different accounts
            - Consider using a password manager
            """)
    else:
        st.error("Please enter a password first.")

# Footer
st.divider()
st.markdown("<p style='font-weight:bold; color:blue;'>Created by Ayesha Aaqil</p>", unsafe_allow_html=True)
