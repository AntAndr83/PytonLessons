from . import div, add, mul, sub


if __name__ == '__main__':

    a, b = (input())
    while not a or b .isdigit():
        a, b = (input("not correct"))

div.div(a, b)
add.add(a, b)
mul.mul(a, b)
sub.sub(a, b)
