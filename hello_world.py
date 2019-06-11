class HelloWorld:
    x = 5
    def __init__(self,var):
        self.num = var + self.x
        self.phrase = "Hello World"

hw = HelloWorld(4)
print("Var + x is: ", hw.num)
for i in range(hw.num):
    print(hw.phrase, i)