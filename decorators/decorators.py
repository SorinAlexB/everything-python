def verboseab(func):
    def inner(a,b):
        print("a + b = ", end='')
        return func(a,b)
    return inner

@verboseab
def sumab(a :float, b :float) -> None:
    print(a+b)

if __name__ == "__main__":
    sumab(1,2)


