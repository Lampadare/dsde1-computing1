def multiply_dict(dictionary):
    for x in dictionary:
        dictionary[x] = dictionary[x] * 3
    return dictionary
print(multiply_dict({'Name': 1, 'Age': 3, 'Class': 55}))