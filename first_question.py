

from sqlalchemy import true


def is_even(value):
    return not int(bin(value)[-1])


if __name__ == "__main__":
    print(is_even(-1200998830))