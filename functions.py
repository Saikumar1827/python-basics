# def fun_name():
#     print("Hello")

# print(fun_name())

# def mult(a, b):
#     return a * b  # default is none
# res = mult('3.0', 3)
# print(res)


def mult(a, b, *args, **kwargs):
    # *args -> pass any no: of position arguments
    # **kwargs -> pass any no: keyword arguments
    print(f"a:{a}, b:{b}, args:{args}, kwargs:{kwargs}")
    return a * b # default is None

# a=4, b=5 are keyword arguments, as they contains keys and values
# '3.0', 3 are called as positional arguments
res = mult('3.0', 3, 4, 5, c=10, d=20)
print(res)

"""
When we specify data type in function but if we give different data type when passing the values what happen
"""

# def abc(a:int, b:float) -> float:
#     return a + b
# print(abc(1, 2.0)) # don't do like this

def calc(a, b, operation):
    if operation == "add":
        return a + b
    if operation == "sub":
        return a - b
    if operation == "mult":
        return a * b
    if operation == "div":
        return a % b

values = tuple(input("Enter 2 numbers: "))
operation = input("Enter operation to perform (add, sub, mult, div): ")
print(values)
print(tuple(map(int, values)))
# res = calc(a, b, operation)



