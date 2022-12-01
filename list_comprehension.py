# 1
starts_with_f = [val for val in ["flower", "fantastic", "incredible"] if val[0] == "f"]
print(starts_with_f)

# 2
data = ["flower", "fantastic", "incredible"]
first_letter = [val[0].upper() for val in data]
print (first_letter)

# 3
number_range = range(1, 11, 2)
multiply_list = [val * 2 for val in number_range]
print(multiply_list)
