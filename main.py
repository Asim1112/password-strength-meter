import streamlit as st
import secrets

# Applying custom styles
st.markdown(""" 
    <style>
            body {
                background-color: #0D0D0D;
                color: #FFD700;
                font-family: "Arial", sans-serif;
            }

            .stTextInput > div > div input {
                background-color: white;
                color: #2E8B57;
                border-radius: 10px;
                padding: 12px 15px;
                border: 2px solid #8A2BE2;
            }

            .stButton > button {
                background: linear-gradient(135deg, #1F487E , #5D737E);
                color: #F0F8FF;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 12px;
                border: none;
                transition: 0.3s;
                cursor: pointer; 
            }

            .stButton > button:hover {
                background: linear-gradient(135deg, #1A3742, #3A6D85);
                color: white;
            
            }
    </style>
""", 
    unsafe_allow_html=True)




#Title
st.markdown("""
<h1 style='
    text-align: center;
    font-size: 3rem;
    font-wight: bold;
    margin-bottom: 20px;
    background: linear-gradient(135deg, #6A11CB, #2575FC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 2px 2px 8px rgba(106, 17, 203, 0.5)
  '>
    Password Strength Meter
    </h1>
 """,
 unsafe_allow_html=True)


# special characters for password validation
special_characters = "!@#$%^&*"

# input for password
password = st.text_input("Enter your password:", type = "password", key="password_input")


    
if st.button("Check Strength"):

    if password:
        score = 0
        
        # password length check
        if len(password) < 6:
            st.write("Your password is **Too Short** (Use at least 8 characters)")
            score = 1
        elif 6 <= len(password) < 10:
            st.write("Your password strength is **Moderate** (Can be improved)")
            score = 2
        elif len(password) >= 10:
            st.write("Your password length is **Strong**")
            score += 3


        # uppercase and lowercase letters
        if any(char.isupper() for char in password) and any(char.islower() for char in password):
            st.write("Password contains **Uppercase and Lowercase** letters")
            score += 2
        else:
            st.write("Password must include **both Uppercase and Lowercase** letters")


        # checking numbers
        if any(char.isdigit() for char in password):
            st.write("Password contains **at least one Number**")
            score += 2
        else:
            st.write("Password must include **at least one Number**")


        # special characters
        if any(char in special_characters for char in password):
            st.write("Password contains **at least one Special Character**")
            score += 2
        else:
            st.write("Password must have **at least one Special Character**")

        
        
        
        # Determine Strength Category
        strength = ""
        color = ""
        progress = 0

        if score <= 4:
            strength = "Weak"
            color = "red"
            progress = 30
        elif 5 <= score <= 7:
            strength = "Moderate"
            color = "orange"
            progress = 60
        else:
            strength = "Strong"
            color = "green"
            progress = 100


        # Display password strength message
        st.markdown(f"<h3 style='color: {color}; text-align: center;'> {strength} Password</h3>", unsafe_allow_html=True)


        # Progress bar
        st.progress(progress / 100)


        # Tips for improvements
        if strength == "Weak":
            st.subheader("How to improve your password:")
            if len(password) < 8:
                st.write("Use at least **8 characters**")
            if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
                st.write("Include **both uppercase and lowercase letters**.")
            if not any(char.isdigit() for char in password):
                st.write(" - Add at least **one number (0-9)**.")
            if not any(char in special_characters for char in password):
                st.write(" - Use a **special character (!@#$%^&*)**.")

            st.write("**Try again with a stronger password**")



# function to generate a strong password
def generate_password(length = 12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.subheader("Suggested Strong Password:")
    st.code(strong_password, language="")






