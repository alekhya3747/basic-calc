

def test():
    print("Hello World")
    name = input ("what is your name? ")
    print("\n My name is " + name) 
    sum = 2+2
    print(sum)
    
def tester():
     print("alekhya")
     
def additionAlekhya(num1,num2,operator):
    #if num1.isdigit() or num1.isfloat() and num2.isdigit() or num2.isfloat():
    if (isinstance(int(num1),int) or isinstance(float(num1),float)) and (isinstance(int(num2),int) or isinstance(float(num2),float)):
        if operator == "+":
            print(int(num1) + int(num2))
        elif operator == "-":
            print(int(num1) - int(num2))  
        elif operator == "*":
            print(int(num1) * int(num2))
        elif operator == "/":
            print(int(int(num1) / int(num2)))
        else:
            print("please enter valid operator")              
        
    else:
        print("please enter valid numbers")    
        
#def numtype(numb1):
#    if isinstance(numb1,int):
     
          
    
    
    
     

if __name__ =="__main__":
    firstNumber = input("please enter number 1 ")
    secondNumber = input("please enter number 2 ")
    operator = input("please enter desired operation")
    additionAlekhya(firstNumber,secondNumber,operator)
    
    
 
        