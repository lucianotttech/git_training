from library import Animal


def print_numbers():
    for index in range(10):
        print(index + 1)


print('Hello Wlrod')

print_numbers()

felix = Animal("grey")
print("Felix's color is: {}".format(felix.color))
felix.run()
