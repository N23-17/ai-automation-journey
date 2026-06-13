def greet():
    print("Hello Imran")

greet()
#parameters
def moni(name):
    print(f"Hello {name}!")
moni("Utulele")
#return values
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 5)

print(result)
#example
def square(number):
    return number * number

result = square(4)

print(square(square(4)))