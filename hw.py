var1 = int(input("Number 1: "))
var2 = int(input("Number 2: "))
sign = input("Enter math operator: ")
result = None

if sign == "+":
    result = var1+var2
    print(result)
elif sign == "-":
    result = var1-var2
    print(result)
elif sign == "*":
    result = var1*var2
    print(result)
elif sign == "\\" or sign=='/':
    result = var1/var2
    print(result)
else:
    print("Nezinomas veiksmas")
