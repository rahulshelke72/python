

def is_adult(age):
    if age > 18:
        return True
    else:
        return False


def is_adult2(age):
    return True if age > 18 else False

def main():
    print(is_adult(14))
    print(is_adult2(24))

if __name__ == "__main__":
    main()