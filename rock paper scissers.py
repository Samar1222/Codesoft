import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:

        print("Invalid choice. Please choose again.")
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    
    else:
        return 'computer'

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Your choice: {user_choice}\nComputer's choice: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie!")

    elif winner == 'user':
        print("You win!")

    else:
        print("You lose!")

    return winner

def play_game():
    user_score = computer_score = 0
    
    while True:
        result = play_round()
        if result == 'user':
            user_score += 1
            
        elif result == 'computer':
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game over!")
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()