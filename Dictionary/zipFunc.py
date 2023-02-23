names = ['Tom', 'Bob', 'Mick']
ages = [25, 15, 36]

NA_dict = dict(zip(names, ages))
print(NA_dict)

NA_list = list(zip(names, ages))
print(NA_list)

# comprenentions
NA_dict2 = {
    name: age + 10
    for name, age in zip(names, ages)
}
print(NA_dict2)