from logicDB import *
from latex_to_logic import *
from logic_to_latex import *

# DEBUG
test_mode = True


def menu():
    flag = True
    while flag is True:
        print('(1) Logic to LaTex')
        print('(2) LaTex to Logic\n')
        choice1 = input('Option: ')

        if choice == 1:
            print('(1) Proof')
            print('(2) Single line')
            choice2 = input('Option: ')
            flag = False

        elif choice == 2:
            print('(1) Proof')
            print('(2) Single line')
            choice2 = input('Option: ')
            flag = False

        else:
            print('Invalid input please try again')

        return choice1, choice2


def main():

    if test_mode is True:
        choice1 = 1
        choice2 = 1
    else:
        choice1, choice2 = menu()

    if choice1 == 1 and choice2 == 1:
        print('Logic to LaTex - Proof')

        # logic = swap(conversions, logic)
        # logic_print(logic)

    elif choice1 == 1 and choice2 == 2:
        print('Logic to LaTex - Single line')

    elif choice1 == 2 and choice2 == 1:
        print('LaTex to Logic - Proof')

    elif choice1 == 2 and choice2 == 2:
        print('LaTex to Logic - Proof')


if __name__ == "__main__":
    main()