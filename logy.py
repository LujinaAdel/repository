import random
import time

# Function to help print messages with a short delay
def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

# Function to fight a monster
def fight_monster(player_blood):
    monster_power = random.randint(10, 30)
    player_attack = random.randint(5, 25)
    print_pause("You are fighting the monster!")
    print_pause(f"You dealt {player_attack} damage.")
    print_pause(f"The monster struck back with {monster_power} damage.")
    net_blood = max(player_blood - monster_power, 0)
    score = player_attack
    return net_blood, score

# Function to handle a random event (monster or healing potion)
def random_event(player_blood):
    event = random.choice(["monster", "potion"])
    if event == "monster":
        return fight_monster(player_blood)
    elif event == "potion":
        heal = random.randint(15, 30)
        player_blood = min(player_blood + heal, 100)
        print_pause("You found a healing potion!")
        print_pause(f"It restored {heal} blood.")
        print_pause(f"Your blood is now: {player_blood}")
        return player_blood, 0

# Function for a random intro event at the start of the game
def random_intro_event():
    events = ["bonus", "trap", "nothing"]
    event = random.choice(events)
    if event == "bonus":
        bonus = random.randint(10, 20)
        print_pause("Lucky start! You found some old coins.")
        print_pause(f"You gained {bonus} points.")
        return 0, bonus
    elif event == "trap":
        damage = random.randint(5, 15)
        print_pause("Oh no! A trap was triggered at the entrance.")
        print_pause(f"You lost {damage} blood.")
        return -damage, 0
    else:
        print_pause("You entered the house... it seems quiet for now.")
        return 0, 0

# Function to end the game
def game_over(win, final_score=0, final_blood=0):
    if win:
        print("Congratulations! You won!")
    else:
        print("Game over. You lost.")
    print(f"Final Score: {final_score} | Final Blood: {final_blood}")
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        game()
    else:
        print("Thanks for playing!")

# Function to handle winning the game
def win_game(score, blood):
    print("You survived and found a safe way out of the forest.")
    game_over(True, score, blood)

# Main game loop
def game():
    print_pause("Welcome to the Hunter House Adventure!")
    print_pause("Your goal is to find the door")
    print_pause("that sets you free (door number 3).")
    print_pause("But be careful... monsters lurk behind some doors!")

    blood = 100
    score = 0

    # Start with a random event
    blood_change, score_change = random_intro_event()
    blood = max(blood + blood_change, 0)
    score += score_change

    while True:
        print_pause(f"Blood: {blood} | Score: {score}")
        print_pause("Doors in front of you: [1], [2], [3]")
        choice = input("Choose a door (1, 2, or 3): ").strip()

        if choice == "3":
            win_game(score, blood)
            break
        elif choice in ["1", "2"]:
            blood, earned_score = random_event(blood)
            score += earned_score
            print_pause(f"After the event, your blood is now: {blood}")
            if blood <= 0:
                game_over(False, score, blood)
                break
        else:
            print_pause("Invalid choice. Please choose 1, 2, or 3.")

# Start the game
game()

