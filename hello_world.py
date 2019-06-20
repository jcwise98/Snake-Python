import square
square = square.square_num


class HelloWorld:
    def __init__(self, var):
        self.num = var
        self.phrase = "Hello World!"


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

            result = square(userNum)
            print("\nYour given number squared is:", result)
            break
        except ValueError:
            userInput = input("Please enter a number\n")

    userInput = input("Enter a number to continue\nPress Q to exit...\n")
    flag = check_exit_false(userInput)

print("Goodbye...")
