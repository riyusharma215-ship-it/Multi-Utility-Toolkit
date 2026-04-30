import os

def create_file(fname):
    with open(fname, 'w') as f:
        pass
    print("File created successfully!")

def write_to_file(fname):
    data = input("Enter data to write: ")
    with open(fname, 'w') as f:
        f.write(data)
    print("Data written successfully!")

def read_from_file(fname):
    if os.path.exists(fname):
        with open(fname, 'r') as f:
            print(f"File Content:\n{f.read()}")
    else:
        print("File not found!")

def append_to_file(fname):
    data = input("Enter data to append: ")
    with open(fname, 'a') as f:
        f.write("\n" + data)
    print("Data appended successfully!")