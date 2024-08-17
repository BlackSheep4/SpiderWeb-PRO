import sys

def option1():
    print("You chose option 1!")

def option2():
    print("You chose option 2!")

def option3():
    print("You chose option 3!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == 'option1':
            option1()
        elif option == 'option2':
            option2()
        elif option == 'option3':
            option3()
        else:
            print("Invalid option selected!")
    else:
        print("No option provided!")
