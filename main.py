def zero_division_error() -> float:
    user_input1 = int(input("Enter a number: "))
    user_input2 = int(input("Enter a number: "))

    if user_input1 or user_input1 == 0:
        raise ZeroDivisionError("You can't division zero")

    return user_input1 / user_input2


print(zero_division_error())
