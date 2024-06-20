# def weather_app():
#     pass
#     # print('The weather is so nice outside.')
#

# weather_app()
# print("Hello World")
#
#
# def calculator():
#     return 2 * 3
#
#
# print(calculator())
# calculator()


# num = 100
# def summary_calculator(a, b, c):
#     return (a * b) + c
#
#
# print(summary_calculator(2, 3, 100))
# print(summary_calculator(5, 5, 50))
# print(summary_calculator(15, 15, 25))
#
#
# def validate_name(name):
#     return name
#
#
# print(validate_name("Abdulkarim"))
# print(validate_name("Darina"))
# print(validate_name("Elizaveta"))


# def validate_age(age):
# #         if age < 0:
# #             raise ValueError("Age cannot be a negative value")
# #         return age
# #
# # #     try:
# # #         if age < 0:
# # #             raise ValueError("Age cannot be a negative value")
# # #     except ValueError as valueErrorMessage:
# # #        print(valueErrorMessage)
# # #        return age
# #
# #
# # validate_age(-6)

def validate_name(name):
    if name == str(name):
        print(name)
    elif name != str(name):
        raise TypeError(f"The name should be a string data type. Got {type(name)} {name} instead.")


validate_name({1})

x, y, z = 1, 2, 3

print(x, y, z)