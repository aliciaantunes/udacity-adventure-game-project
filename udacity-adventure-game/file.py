import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("Welcome to Caos")
    print_pause("Over here you will see a battle")
    print_pause("THAT YOU MUST SURPASS")
    print_pause("Good Luck on your Journey")


def generate_scenario():
    weapons = ["Sword", "Shield", "Blessing", "Invisibility", "Wisdom"]
    scenario = random.sample(weapons, k=3)
    war_weapons = ["Sword", "Shield", "Blessing"]
    final_stage_weapons = ["Invisibility", "Wisdom",]
    final_weapons = [random.choice(war_weapons) if weapon in war_weapons
                     else random.choice(final_stage_weapons)
                     for weapon in scenario]
    return scenario, final_weapons


def print_scenario(scenario):
    print_pause("Now choose "
                "what weapon do you want? ")
    for i, weapon in enumerate(scenario, 1):
        print_pause(f"{i}. {weapon}")


def choose_option(scenario):
    while True:
        choice = input("Enter the number of the weapon you choose: ")
        if choice.isdigit() and 1 <= int(choice) <= len(scenario):
            return int(choice)
        else:
            print_pause("Invalid input. Please enter a weapon.")


def play_game():
    while True:
        intro()
        scenario, final_weapons = generate_scenario()
        print_scenario(scenario)
        option = choose_option(scenario)
        selected_weapon = scenario[option - 1]
        print_pause(f"You chose {selected_weapon}")
        if selected_weapon in final_weapons:
            final_stage()
        else:
            war_battle()

        while True:
            play_again = input("Do you want to play again? (yes/no) ").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print_pause("Thank you for playing!")
                return
            else:
                print_pause("Invalid input. Enter 'yes' or 'no'.")


def war_battle():
    print_pause("You are in a war battle!")
    print_pause("You need to defeat the enemy to win the battle.")
    enemy_health = 10
    player_health = 10
    while True:
        print_pause("Choose where to attack:")
        print_pause("1. Head")
        print_pause("2. Body")
        print_pause("3. Legs")
        attack_choice = input("Enter the number of the target: ")
        if attack_choice == "1":
            target = "Head"
        elif attack_choice == "2":
            target = "Body"
        elif attack_choice == "3":
            target = "Legs"
        else:
            print_pause("Invalid choice. Choose between 1 and 3.")
            continue
        player_damage = random.randint(1, 6)
        print_pause(f"You attacked the enemy's {target} "
                    f"and dealt {player_damage} damage.")
        enemy_health -= player_damage
        if enemy_health <= 0:
            print_pause("You defeated the enemy!")
            break
        enemy_damage = random.randint(1, 4)
        print_pause(f"The enemy attacked you and dealt {enemy_damage} damage.")
        player_health -= enemy_damage
        if player_health <= 0:
            print_pause("You were defeated by the enemy...")
            break


def final_stage():
    print_pause("You are in the final stage!")
    print_pause("You need to defeat the final boss to win the game.")
    boss_health = 20  # Saúde do chefe
    player_health = 15  # Sua saúde

    while True:
        print_pause("Choose where to defend:")
        print_pause("1. Head")
        print_pause("2. Body")
        print_pause("3. Legs")
        defense_choice = input("Enter the number of the target:")
        if defense_choice == "1":
            target = "Head"
        elif defense_choice == "2":
            target = "Body"
        elif defense_choice == "3":
            target = "Legs"
        else:
            print_pause("Invalid choice. Choose between 1 and 3.")
            continue

        boss_attack = random.randint(1, 3)
        print_pause(f"The boss prepares to attack...")
        print_pause(f"The boss attacks your {target}.")
        if target == "Head" and boss_attack == 1 or \
           target == "Body" and boss_attack == 2 or \
           target == "Legs" and boss_attack == 3:
            print_pause("You defended successfully.")
        else:
            player_damage = random.randint(2, 5)
            print_pause(f"failed to defend, took {player_damage} damage.")
            player_health -= player_damage

        if player_health <= 0:
            print_pause("You were defeated by the final boss...")
            print_pause("Game Over")
            break

        print_pause("Now it's your turn to attack!")
        player_attack = random.randint(1, 3)
        print_pause(f"You attacked the boss's {target}.")
        if target == "Head" and player_attack == 1 or \
           target == "Body" and player_attack == 2 or \
           target == "Legs" and player_attack == 3:
            boss_health -= random.randint(3, 6)
            print_pause("You hit the boss and dealt damage!")
        else:
            print_pause("You missed the boss.")
        if boss_health <= 0:
            print_pause("You defeated the final boss!")
            print_pause("Congratulations! You won the game!")
            break


play_game()
