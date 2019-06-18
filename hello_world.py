

class HelloWorld:
    def __init__(self, var):
        self.num = var
        self.phrase = "Hello World!"


def square_num(num):
    if num < 0:
        num = num*-1
    val = 0
    for i in range(num):
        val = val + num
    return val


def check_exit_false(var):
    return (var != 'Q') and (var != 'q')


flag = True
userInput = input("What number do you wish to give?\n")

while flag:
    while True:
        try:
            userNum = int(userInput)
            hw = HelloWorld(userNum)
            print("Your given number is:", hw.num)
            for i in range(hw.num):
                print(hw.phrase, i+1)

            result = square_num(userNum)
            print("\nYour given number squared is:", result)
            break
        except ValueError:
            userInput = input("Please enter a number\n")

    userInput = input("Enter a number to continue\nPress Q to exit...\n")
    flag = check_exit_false(userInput)

print("Goodbye...")
