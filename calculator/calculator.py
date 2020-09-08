def add(x,y):
    """
    计算加法
    """
    x = float(x)
    y = float(y)
    return x+y

def minus(x,y):
    x = float(x)
    y = float(y)
    return x-y

def multiply(x,y):
    x = float(x)
    y = float(y)
    return x*y

def divided(x,y):
    x = float(x)
    y = float(y)
    try:
        return x/y
    except ZeroDivisionError:
        print("被除数不能为0")

def operation(str):
    pass


while True:
    print("________________________________")
    print("| 选项：                        |")
    print("| 输入：add，计算两个数相加        |")
    print("| 输入：minus，计算两个数相减      |")
    print("| 输入：multiply，计算两个数相乘   |")
    print("| 输入：divided，计算两个数相除    |")
    print("| 输入：quit，退出计算程序         |")
    print("--------------------------------")

    print("\b")
    user_input = input("请输入：")

    if user_input == "quit":
        break

    elif user_input == "add":
        print("计算加法：")
        x = input("请输入第一个数字：")
        y = input("请输入第二个数字：")
        result = add(x,y)
        print(x +" + "+y +" = "+"%s"%result)
        Isagain  = input("需要继续计算吗(y/n)？")

        if Isagain == "y":
            continue
        else:
            print("计算结束")
            break

    elif user_input == "minus":
        print("计算减法：")
        x = input("请输入第一个数字：")
        y = input("请输入第二个数字：")
        result = minus(x, y)
        print(x + " - " + y + " = " + "%s" % result)
        print("计算结束")
        break

    elif user_input == "multiply":
        print("计算乘法")
        x = input("请输入第一个数字：")
        y = input("请输入第二个数字：")
        result = multiply(x, y)
        print(x + " x " + y + " = " + "%s" % result)
        print("计算结束")
        break

    elif user_input == "divided":
        print("计算除法")
        x = input("请输入被除数：")
        y = input("请输入除数： ")
        result = divided(x, y)
        print(x + " ➗ " + y + " = " + "%s" % result)
        print("计算结束")
        break

    else:
        print("输入有误，请根据提示重新输入。")




