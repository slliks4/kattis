x = input()


def foo(x):
    # Clean X to remove all Zero
    cleaned_x = x.replace("0", "")

    # Base Case
    if len(cleaned_x) == 1:
        return cleaned_x

    # Get their multiple
    new_x = 1
    for i in cleaned_x:
        new_x *= int(i)

    # Recursive Call
    return foo(str(new_x))


print(foo(x))
