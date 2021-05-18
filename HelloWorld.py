from library import Animal


def print_numbers():
    for index in range(10):
        print(index + 1)


def even_or_odd(number):
    print("Number {} is".format(number), end=" ")
    if(number % 2):
        print("odd")
    else:
        print("even")


print('Hello World')
even_or_odd(3)
even_or_odd(8)

print_numbers()

felix = Animal("grey")
print("Felix's color is: {}".format(felix.color))
felix.run()
