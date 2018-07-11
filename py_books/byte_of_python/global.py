x = 50


def func(y=1):
    global x
    print(x)
    x = 2
    print(x)

    print("y=", y)


func()
print(x)

func(5)
