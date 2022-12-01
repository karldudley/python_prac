print("Welcome to Rock, Paper, Scissors!")
user_input = input("Please choose rock, paper or scissors: ")
cpu_input = "paper"
print(f"You chose {user_input}.")
print(f"Your CPU oponent chose {cpu_input}.")

if (user_input == "rock" and cpu_input == "paper"):
    print("Rock loses to paper. You lose!")
elif (user_input == "paper" and cpu_input == "paper"):
    print("You both chose paper. It's a draw.")
elif (user_input == "scissors" and cpu_input == "paper"):
    print("Scissors cut paper. You win!")
else:
    print("Something went wrong :-(")
