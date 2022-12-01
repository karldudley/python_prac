# Basic if statement
temperature = 14;

if temperature > 13:
    print("It's too hot!")
print("Hello")

# Basic if/else statement
temperature = 13;

if temperature > 13:
    print("It's too hot!")
else:
    print("It's nice and cool")

# Basic if/elif statement
if temperature > 13:
    print("It's too hot!")
elif temperature == 13:
    print("It's exactly 13 degrees")
else:
    print("It's nice and cool")

# Basic if/else ternary statement
print("higher") if 3 > 5 else print("lower")

# if/else statements with logical operators
forecast = "rain"

# OR
if temperature > 13 or forecast == "rain":
    print("Stay inside")
else:
    print("Go outside")

# AND
if temperature > 13 and forecast == "rain":
    print("Stay inside")
else:
    print("Go outside")

# NOT
if not forecast == "rain":
    print("Go outside")
