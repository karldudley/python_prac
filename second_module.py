# When you import something it runs the code
# __name__ changes because it is being run from an import
import first_module

# __name__ here is __main__ because it is being run directly by Python
print(f"Second Module's Name: {__name__}")
