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

    # ❌ Check if password is blacklisted
    if password.lower() in BLACKLISTED_PASSWORDS:
        print("❌ This password is too common. Choose a more secure one.")
        return

    # 🔍 Password analysis begins
    print("\n🔍 Password Analysis:")
    if stats.strength() >= 0.66:
        print("✅ Strong Password!")
    else:
        print("❌ Weak Password - Improve it using the suggestions below:")
        if len(password) < 8:
            print("❌ Password should be at least 8 characters long.")
        if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
            print("❌ Include both uppercase and lowercase letters.")
        if not re.search(r"\d", password):
            print("❌ Add at least one number (0-9).")
        if not re.search(r"[!@#$%^&*]", password):
            print("❌ Include at least one special character (!@#$%^&*).")
        print(f"\n💡 Suggested strong password: {generate_strong_password()}")

# 🚀 Program Entry Point
if __name__ == "__main__":
    password = input("🔐 Enter your password: ")
    check_password_strength(password)
