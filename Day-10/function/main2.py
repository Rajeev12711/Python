def fun(first, last):
    if first == "" or last == "":
        return "You didn't Enter first or Last Name."
    first = first.title()
    last = last.title()
    return f"Your full Name is {first} {last}"

print(fun(input("Enter Your First name: \n"), input("Enter Your Last Name: \n")))