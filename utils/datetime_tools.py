import datetime
import time

def display_current():
    now = datetime.datetime.now()
    print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_diff():
    try:
        d1 = input("Enter the first date (YYYY-MM-DD): ")
        d2 = input("Enter the second date (YYYY-MM-DD): ")
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
        print(f"Difference: {abs((date2 - date1).days)} days")
    except ValueError:
        print("Error: Use YYYY-MM-DD format.")

def run_stopwatch():
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    print(f"Elapsed: {round(time.time() - start, 2)} seconds")

def countdown_timer():
    sec = int(input("Enter seconds for countdown: "))
    for i in range(sec, 0, -1):
        print(f"Time left: {i}s", end="\r")
        time.sleep(1)
    print("Time's up!          ")