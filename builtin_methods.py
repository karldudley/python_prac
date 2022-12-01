# MAP
def add_two(x):
    return x + 2

# map or filter does not automatically return a list, so you have to force it
mapped_data = map(add_two, [2, 4, 17])
print(list(mapped_data))

for data in mapped_data:
    print(data)

# FILTER
def starts_with_f(val):
    return val[0] == "f"

filtered_data = filter(starts_with_f, ["flower", "fantastic", "incredible"])
print(list(filtered_data))
