import math
def cal():
    while True:
        print("Scientific Calculator")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Power(a^b)")
        print("6.Square Root")
        print("7.Modulus")
        print("8.sin(x)")
        print("9.cos(x)")
        print("10.tan(x)")
        print("11.log(x)to the base 10")
        print("12.ln(x)")
        print("13.Exit")
        choice=input("Enter choice:")
        if choice=='13':
            print("Extiting Calculator")
            break
        
        if choice in['1','2','3','4','5','7']:
            try:
                num1=float(input("Enter first number: "))
                num2=float(input("Enter second number: "))
            except:
                print("Invalid input!")
                continue
        if choice=='1':
            print("Result:",num1+num2)
        elif choice=='2':
            print("Result:",num1-num2)
        elif choice=='3':
            print("Result:",num1*num2)
        elif choice=='4':
            if num2!=0:
                print("Result:",num1/num2)
            else:
                print("Error:Cannot divide by zero")

        elif choice=='5':
            print("Result:", math.pow(num1, num2))

        elif choice == '7':
            try:
                print("Result:",num1%num2)
            except:
                print("Error in modulus")
        elif choice=='6':
            try:
                num=float(input("Enter number: "))
                if num >= 0:
                    print("Result:", math.sqrt(num))
                else:
                    print("Error:Negative number")
            except:
                print("Invalid input")
        elif choice in ['8','9','10']:
            try:
                angle=float(input("Enter angle in degrees: "))
                radians=math.radians(angle)
                if choice=='8':
                    print("sin(",angle,")=", math.sin(radians))
                elif choice=='9':
                    print("cos(",angle,")=", math.cos(radians))
                elif choice=='10':
                    print("tan(",angle,")=", math.tan(radians))
            except:
                print("Invalid input")
        elif choice=='11':
            try:
                num=float(input("Enter number: "))
                if num>0:
                    print("log(",num,")=",math.log10(num))
                else:
                    print("Error")
            except:
                print("Invalid input")
        elif choice=='12':
            try:
                num=float(input("Enter number: "))
                if num>0:
                    print("ln(",num,")=",math.log(num))
                else:
                    print("Error")
            except:
                print("Invalid input") 

        else:
            print("Invalid choice")
cal()
