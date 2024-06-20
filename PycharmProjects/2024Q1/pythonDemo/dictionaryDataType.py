dictionary = {"FirstName": "Dadu", "Address": "420 Test st", "Age": 18}
print(dictionary)

dictionary.pop("Age")
print(dictionary)
print(dictionary.get("FirstName"))

new_dictionary = {1: "Something", "Academy": 2024}

dictionary.update(new_dictionary)
print(dictionary.items())
print(dictionary.keys())



