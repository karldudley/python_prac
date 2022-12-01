print("This will always be run")

# __name__ is a variable that python sets to __main__
def main():
    print(f"First Module's Name: {__name__}")

if __name__ == '__main__':
    main()
