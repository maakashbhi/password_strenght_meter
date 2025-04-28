import streamlit as st
import re
import random
from password_strength import PasswordStats

# 🔒 Common weak passwords that should be blocked
BLACKLISTED_PASSWORDS = {
    "password", "123456", "password123", "qwerty", "letmein", "admin", "welcome"
}

# 🔧 Generate a strong password suggestion
def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# ✅ Check password strength using rules and PasswordStats
def check_password_strength(password):
    stats = PasswordStats(password)
    feedback = []
    is_strong = True

    # ❌ Check if password is blacklisted
    if password.lower() in BLACKLISTED_PASSWORDS:
        feedback.append("❌ This password is too common. Choose a more secure one.")
        is_strong = False
        return feedback, is_strong

    # 🔍 Password analysis
    if stats.strength() >= 0.66:
        feedback.append("✅ Strong Password!")
    else:
        is_strong = False
        feedback.append("❌ Weak Password - Improve it using the suggestions below:")
        if len(password) < 8:
            feedback.append("❌ Password should be at least 8 characters long.")
        if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
            feedback.append("❌ Include both uppercase and lowercase letters.")
        if not re.search(r"\d", password):
            feedback.append("❌ Add at least one number (0-9).")
        if not re.search(r"[!@#$%^&*]", password):
            feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return feedback, is_strong

# 🚀 Streamlit App
st.title("🔐 Password Strength Meter")
st.write("Enter your password to check its strength and get suggestions for improvement.")

password = st.text_input("Enter your password:", type="password")

if password:
    feedback, is_strong = check_password_strength(password)
    
    # Display feedback
    for message in feedback:
        st.write(message)
    
    # Show strength meter
    if is_strong:
        st.success("Your password is strong! 🎉")
    else:
        st.warning("Your password needs improvement.")
        if st.button("Generate Strong Password"):
            suggested_password = generate_strong_password()
            st.code(suggested_password)
            st.write("💡 Copy this suggested password or use it as inspiration for creating your own.") 