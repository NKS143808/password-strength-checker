import re

print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if re.search(r"[A-Z]", password):
    strength += 1

if re.search(r"[a-z]", password):
    strength += 1

if re.search(r"\d", password):
    strength += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1

print("\nPassword Analysis")
print("-" * 30)

if strength == 5:
    print("✅ Very Strong Password")
elif strength == 4:
    print("🟢 Strong Password")
elif strength == 3:
    print("🟡 Medium Password")
elif strength == 2:
    print("🟠 Weak Password")
else:
    print("🔴 Very Weak Password")
