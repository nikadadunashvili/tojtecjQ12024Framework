# The trading application that checks the eligibility of symbol (ticker) when a client enters it.
# The current use is allowed to trade only TW symbol.

# 2. The AAPL is not tradable anymore. make sure clients cant place an order using this symbol,
# when AAPL is entered, gracefully reject their message saying that - "this security is not tradable anymore"

# def entering_symbol():
#     symbol = input("Enter a symbol: ")
#     while True:
#         try:
#             if symbol.upper() == "AAPL":
#                 raise Exception("Error: This security is not tradable at this time please try again later when it will "
#                             "become tradable again")
#             elif symbol.upper() == "TW":
#                 print("You are allowed to trade this symbol. Order placed successfully")
#                 break
#             elif symbol.upper() != "AAPL" or symbol.upper() != "TW":
#                 print("You,re not allowed to trade this symbol")
#         except Exception as exception:
#             print(exception)
#             break
#         else:
#             symbol = input("Enter another symbol. ")
#
#
#
# entering_symbol()


# 1. The trading application that checks the eligibility of symbol (ticker) when a client enters it.
# The current user is allowed to trade only TW symbol

# 2. The AAPL is not tradable anymore.
# Make sure clients can't place an order using this symbol.
# When AAPL is entered, gracefully reject their message saying that - "This security is non-tradable anymore"

def entering_symbol():
    symbol = input("Enter a symbol: ").upper()  # Originally when symbol is entered in lowercase,
    # it will be automatically covered to upper

    while True:
        if symbol == "AAPL":  # In this line it will check the symbol entered by the user
            # which is already converted at the time of entering the symbol.
            # That is handled by the next line after defining the function

            try:  # The loop will go inside this try block and raise an exception
                # only if the user enters aapl symbol in any format.
                raise Exception(f"Error: The {symbol} symbol is not tradable at this time. "
                                "Please try again later when it will become tradable again")

            # Then after capturing that exception it will place it in except block and return it to the user.
            # It's done to prevent the system from crashing
            except Exception as exception:
                print(exception)
                break  # Once the condition is true, the break statement will terminate the loop.

        elif symbol == "TW":
            # if the 1st condition in the "if" statement is false, it will come to this block and execute.
            print(f"You are allowed to trade {symbol} symbol. Order placed successfully.")
            break  # Once the condition of "elif" statement becomes true the break statement will terminate the loop

        else:  # If none of the condition in "if" and "elif" are true,
            # then the program will alert the user that they are not allowed to trade that symbol.
            # The symbol = input() in this else block will be responsible for allowing the user to enter another symbol.
            # In case of otherwise (if we don't have that) it will run into an infinite loop.
            symbol = input(f"You are not allowed to trade {symbol} symbol. Enter another symbol. ")


entering_symbol()

