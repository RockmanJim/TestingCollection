# 1、从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出。
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


n = int(input("Plz input your number: "))
print("%d! = %d" % (n, factorial(n)))
