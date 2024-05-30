import sys

print("Enter your last name:")
print("**", end="")
sys.stdout.flush()
lastName = sys.stdin.readline().strip()

print("Enter your first name:")
print("**", end="")
sys.stdout.flush()
firstName = sys.stdin.readline().strip()

print(firstName)
print(lastName)