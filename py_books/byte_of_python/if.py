number = 23
running = True
while running:
    guess = int(input('输入一个数字：'))
    if guess == number:
        print("恭喜你猜对了")
        running = False
    elif guess < number:
        print("小了")
    else:
        print("大了")

print("done")
