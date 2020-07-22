a = int(input("input a:"))


def get_rectangle_data(length):
    return 4 * length, length ** 2, length * 2 ** (1 / 2)


print(get_rectangle_data(a))
