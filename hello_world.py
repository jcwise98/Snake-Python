# Test class that has a property and a simple constructor.
# the constructor takes in an int and sets the num field equal to
# the x property plus the given value. Sets the phrase field to "Hello World"


class HelloWorld:
    x = 1

    def __init__(self, var):
        self.num = var + self.x
        self.phrase = "Hello World"


userNum = int(input("What number do you wish to give?"))
hw = HelloWorld(userNum)

print("Var + your given number is:", hw.num)
for i in range(hw.num):
    print(hw.phrase, i+1)


def square_num(num):
    val = 0
    for i in range(num):
        val = val + num
    return val


result = square_num(userNum)
print("\nYour given number squared is:", result)
