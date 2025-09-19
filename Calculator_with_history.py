#simple calculator

HISTORY_FILE = "history.txt"

def show_history():
    file=open(HISTORY_FILE,'r')
    lines=file.readlines()
    if len(lines)==0:
        print("NO HISTORY FOUND !")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open(HISTORY_FILE,'w')
    file.close()
    print("HISTORY IS CLEARED.")

def save_to_history(equation, result):
    file=open(HISTORY_FILE,'a')
    file.write(equation +" = "+ str(result) + "\n")
    file.close()

def calculator(user_inpute):
    parts = user_inpute.split()
    print(parts)
    if len(parts)!= 3:
        print('INVALID INPUTE. User formate:nnumber operator number(eg.8 + 8)')
        return
    
    num1= float(parts[0])
    op= parts[1]
    num2= float(parts[2])

    if op == "+":
        result= num1 + num2
    elif op == "-":
        result= num1 - num2
    elif op == "*":
        result= num1 * num2
    elif op == "/":
        if num2 == 0:
            print('can not divided by zero')
        result= num1 / num2
    else:
        print('INVALID OPERATOR. USE ONLY(+,-,*,/)')
        return
    if int(result) == result:
        result= int(result)
    print("RESULT :- ",result)
    save_to_history(user_inpute, result)

def main():
    print('=== SIMPLE CALCULATOR === \n')
    while True:
        user_inpute = input("Enter equation (+,-,*,/) or command (history, clear, exit):")
        if user_inpute == 'exit':
            break
        elif user_inpute == 'history':
            show_history()
        elif user_inpute == 'clear':
            clear_history()
        else:
            calculator(user_inpute)

main()