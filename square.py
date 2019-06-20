def square_num(num):
    if num < 0:
        num = num*-1
    val = 0
    for i in range(num):
        val = val + num
    return val
