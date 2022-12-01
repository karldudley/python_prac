# Functions can be stores in variables and passed as arguments

def print_loud_message(message):
    loud_message = message.upper()
    print(loud_message)
    return True;

print_loud_message("hello")

# LOCAL scope
def greet():
    message = "Hello"
    print("Local", message)
greet()

# GLOBAL scope
message = "Hello"

def greet_g():
    print("Global", message)
greet_g()

# 
c = 1

def add():
    # tells python to access the globally declared variable c - will look for a local c without it
    global c
    c = c + 2
    print(c)
add()

# Local -> Enclosing -> Global -> Built in
