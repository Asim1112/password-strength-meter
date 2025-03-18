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
    background-color: #F0F5FA; /* Cool Light Gray */
    color: #1A3A5A; /* Royal Blue */
    font-size: 16px;
    font-weight: bold;
    border-radius: 10px;
    padding: 12px 15px;
    border: 2px solid #0056A6; /* Bold Blue */
    outline: none;
    transition: all 0.3s ease-in-out;
    box-shadow: inset 0px 2px 5px rgba(0, 86, 166, 0.2);
}

.stTextInput > div > div input:focus {
    border-color: #0077C8; /* Vibrant Blue */
    box-shadow: 0px 0px 10px rgba(0, 86, 166, 0.5);
    background-color: #E6EFF8; /* Frosty Light Blue */
}


.stButton > button {
    background: #E0F7FA; /* Pale Blue */
    color: #003366; /* Deep Navy */
    font-size: 16px;
    font-weight: bold;
    padding: 10px 14px;
    border-radius: 12px;
    border: 2px solid #0077B6;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 4px 8px rgba(0, 119, 182, 0.3);
}

.stButton > button:hover {
    background: #B2EBF2;
    border-color: #0099CC;
    box-shadow: 0px 8px 16px rgba(0, 119, 182, 0.5);
    transform: scale(1.05); /* Slight zoom effect */
}


    </style>
""", 
    unsafe_allow_html=True)




#Title
st.markdown("""
<style>
@keyframes flicker {
    0% { opacity: 1; }
    50% { opacity: 0.8; text-shadow: 0 0 10px #0ff, 0 0 20px #00f; }
    100% { opacity: 1; }
}
.flicker {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #0ff;
    text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #00f;
    animation: flicker 1.5s infinite alternate;
}
</style>

<h1 class='flicker'>Password Strength Meter</h1>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .password-container {
        text-align: center;
        margin-bottom: 10px;
    }
    .password-label {
        font-size: 16px;
        font-weight: bold;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# special characters for password validation
special_characters = "!@#$%^&*"

# input for password
st.markdown('<div class="password-container"><span class="password-label">Enter your password:</span></div>', unsafe_allow_html=True)
password = st.text_input("", type="password", key="password_input")


    
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






