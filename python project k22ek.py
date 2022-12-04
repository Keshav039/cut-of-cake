# print when user hit worng word or when program starts
import os
def help():
      print("""
            
                Welcome To Cake Cutter and Calculater !!
                If you Want To Enter in The Program Please Follow the following Steps!
                [1] For all access 
                [2] Only Angle Finder
                [3] Only for Finding Total Number Of Pieces
                [4] clear screen
                [5] Exit
    
            """)
#for finding the equal engal between all the pieces
def Angle_finder(number_of_cuts):
    if(number_of_cuts >0):
        Equal_angle =360/number_of_cuts
        print('The equal angle between every peice is :',Equal_angle,'Deg')
    elif number_of_cuts ==0:
        print('Cut The Cake First !')
    else:
        print('Invalid Cuts !')
    
# for finding the total equal pieces
def Equal_pieces(number_of_cuts):
    if(number_of_cuts >0):
        total_pieces = number_of_cuts*2
        print('The total equal pieces of the cake are:',total_pieces,'Pieces')
    elif number_of_cuts ==0:
        print('Cut the cake first !')
    else:
        print('Invalid Cuts !')
        
# run every time and ask for the user input to run
def porgram_starter():
    help()
    while True:
        try:
            user_command = int(input('Enter Opration No.:: '))
        except ValueError:
            print("Please enter correct operation")
            continue      
        if user_command == 1:
            print("""---------------------------------This Will Calculate All The Values-----------------------------------""")
            try:    
                user_cuts = int(input('Enter Pieces/Angle you want to do of cake: '))
            except ValueError:
                print("Please enter correct operation")
                continue      
            all_Peices(user_cuts)
        elif user_command == 2:
            print("""---------------------------------This Will Calculate Only Angle-----------------------------------""")
            try:
                user_cuts = int(input('Enter angle number you want to do of cake: '))
            except ValueError:
                print("Please enter correct operation")
                continue 
            Angle_finder(user_cuts)
        elif user_command == 3:
            print("""---------------------------------This Will Calculate Only Total Peices-----------------------------------""")
            try:
                user_cuts = int(input('Enter Pieces you want to do of cake: '))
            except ValueError:
                print("Please enter correct operation")
                continue 
            Equal_pieces(user_cuts)
            #clearing screen
        elif user_command == 4:
            os.system('cls')
        #for exit() cake cutter
        elif user_command == 5:
            print("""---------------------------------Are you sure you want to exit!-----------------------------------
                            y/n
                            y = yes!
                            n = no !            
            
            """)
            confirmation = input("Enter y/n: ")

            if(confirmation == 'y'):
                exit()
        else:
            os.system('cls')
       
def all_Peices(number_of_cuts):
    if(number_of_cuts >0):
        Equal_pieces(number_of_cuts)
        Angle_finder(number_of_cuts)
    elif number_of_cuts ==0:
        print('Cut The Cake First !')
    else:
        print('Invalid Cuts !')

#Running all the functions !!
if __name__ =="__main__":
    porgram_starter()

