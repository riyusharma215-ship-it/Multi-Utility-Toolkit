Multi-Utility Toolkit
Welcome to the Multi-Utility Toolkit, a modular Python application designed to handle a variety of daily computational tasks ranging from date calculations to random data generation. This project demonstrates clean modularity by separating specialized logic into dedicated utility files.

## Features
The toolkit is organized into five primary categories:

1. Datetime and Time Operations
Current Time: Displays the present date and time in YYYY-MM-DD HH:MM:SS format.

Date Difference: Calculates the absolute number of days between two user-provided dates.

Stopwatch: A simple manual timer to measure elapsed time between two "Enter" key presses.

2. Mathematical Operations
Factorial: Computes the factorial of a given integer using the math library.

Compound Interest: Calculates total accumulated value based on principal, rate, and time.

3. Random Data Generation
Password Generator: Creates a secure string of a specified length including letters, digits, and special symbols (@#$%).

OTP Generator: Generates a standard 4-digit numeric One-Time Password.

4. File Operations
CRUD Basics: Allows users to create, write to, and read from a file (defaulting to hello.txt).

5. System Utilities
UUID Generation: Generates a unique version 4 identifier.

Module Exploration: Uses dir() to inspect attributes of loaded modules like math or random.

## File Structure
The project is structured to keep the execution logic separate from the utility functions:

main.py: The entry point of the application containing the menu-driven interface.

utils/: A package containing the core logic:

datetime_tools.py: Logic for clocks and calendars.

file_tools.py: Logic for file system interaction.

math_tools.py: Logic for arithmetic and financial math.

random_tools.py: Logic for security and randomization.

## How to Use
Run the Application:
Execute the main script using Python:

Bash
python main.py
Navigate the Menu:
Enter the number corresponding to the tool you wish to use (1-7).

Follow Prompts:
Input the required data (like dates or numbers) when prompted by the sub-menus.

Exit:
Choose option 7 to safely close the toolkit.

## Requirements
Python 3.x

Standard Libraries: os, math, datetime, time, random, string, uuid


"# Multi-Utility-Toolkit" 
