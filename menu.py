def calc_menu():
    stop_work = False
    while(stop_work != True):
        print("Какую операцию вы хотите произвести?")
        print("1 - сложение; 2 - вычитание; 3 - умножение; 4 - деление; 5 - выход")
        user_input = int(input())
        if(user_input == 1 ):
            import addition
            addition.Addit           
            print('')
        elif(user_input == 2):
            import substraction
            substraction.Substract
            print('')
        elif(user_input == 3):
            import multiplication
            multiplication.Multi
            print('')
        elif(user_input == 4):
            import division
            division.Divi
            print('')
        elif(user_input == 5):
            print("Завершение работы")
            stop_work = True
        else:
            print("ВВедено некорректное значение")
calc_menu()