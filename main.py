file = input("Please enter a file path (Remember that on Windows, only forward slashes should be used when writing the"
             " path, that is '/'):\n")
try:
    open(file, "r")
    with open(file, "w") as file:
        file.write("SOPHIA MODIIFIED THIS FILE.")
        print("File modified and saved")
except FileNotFoundError:
    print("File not found, please check file path.")
