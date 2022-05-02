import random
user_action = input('Enter a choice of rock, paper, or scissors... choose wisely!')
possible_action = ['rock', 'paper', 'scissors']
computer_action = random.choice(possible_action)
print('You chose '+ user_action + '. Computer chose ' + computer_action)

def apple():
    while True:
        try:
            if user_action not in computer_action:
                raise ValueError
        except ValueError:
            print("Your must enter rock, paper, or scissors")
            break    #this stops running try except function


if user_action.lower() ==computer_action:
    print('Both players selected ' + user_action + '. It is a tie')
elif user_action.lower() == 'rock':
    if computer_action == 'scissors':
        print('Rock smashes scissors. YOU WIN!!!')
    else:
        print('Paper covers rock. YOU LOSE!!!')

elif user_action.lower() == 'scissors':
    if computer_action == 'paper':
        print('Scissors cuts paper. YOU WIN!!!')
    else:
        print('Rock crushes scissors. YOU LOSE!!!')

elif user_action.lower() == 'paper':
    if computer_action == 'rock':
        print('Paper covers rock. YOU WIN!!!')
    else:
        print('scissors cuts paper. YOU LOSE!!!')

apple()







