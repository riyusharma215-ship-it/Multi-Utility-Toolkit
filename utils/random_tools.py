import random
import string

def simulate_sampling():
    dataset = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
    print(f"Original Dataset: {dataset}")
    # Requirement: Simulate random sampling
    samples = random.sample(dataset, 3)
    print(f"Random Sampling (3 items): {samples}")

def create_random_password():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "@#$%"
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {pwd}")

def generate_random_otp():
    print(f"Generated OTP: {random.randint(1000, 9999)}")