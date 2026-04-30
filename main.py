import uuid
import math
import random
from utils import datetime_tools, math_tools, random_tools, file_tools

def main():
    while True:
        print("\n" + "-*-"*30)
        print(" Welcome to Multi-Utility Toolkit")
        print("-"*30)
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("-"*30)
        
        choice = input("Enter choice: ")

        if choice == '1':
            print("\n1. Current Time\n2. Date Difference\n3. Stopwatch\n4. Countdown Timer\n5. Back")
            sub = input("Enter sub-choice: ")
            if sub == '1': datetime_tools.display_current()
            elif sub == '2': datetime_tools.calculate_diff()
            elif sub == '3': datetime_tools.run_stopwatch()
            elif sub == '4': datetime_tools.countdown_timer()

        elif choice == '2':
            print("\n1. Factorial\n2. Compound Interest\n3. Trigonometry\n4. Area\n5. Back")
            sub = input("Enter sub-choice: ")
            if sub == '1': math_tools.calculate_factorial()
            elif sub == '2': math_tools.solve_compound_interest()
            elif sub == '3': math_tools.trig_calculations()
            elif sub == '4': math_tools.area_geometric()

        elif choice == '3':
            print("\n1. Random Sampling\n2. Password Generator\n3. OTP Generator\n4. Back")
            sub = input("Enter sub-choice: ")
            if sub == '1': random_tools.simulate_sampling()
            elif sub == '2': random_tools.create_random_password()
            elif sub == '3': random_tools.generate_random_otp()

        elif choice == '4':
            print(f"\nGenerated UUID: {uuid.uuid4()}")

        elif choice == '5':
            print("\n1. Create\n2. Write\n3. Read\n4. Append\n5. Back")
            sub = input("Enter sub-choice: ")
            fname = "project7.txt"
            if sub == '1': file_tools.create_file(fname)
            elif sub == '2': file_tools.write_to_file(fname)
            elif sub == '3': file_tools.read_from_file(fname)
            elif sub == '4': file_tools.append_to_file(fname)

        elif choice == '6':
            mod = input("Explore (math/random): ")
            if mod == 'math': print(dir(math))
            elif mod == 'random': print(dir(random))

        elif choice == '7':
            print("\n=========================")
            print("Thank you for using the Toolkit!Goodbye!")
            print("=========================")
            break

if __name__ == "__main__":
    main()