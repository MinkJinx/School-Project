import time

q = 0

while q == 0:
    # Game Introduction
    print("Welcome to the Pokemon Battle Game!")
    print("Choose your Pokemon and battle against an opponent until one faints!\n")

    # Define the list of Pokemons and their moves with damage values
    pokemons = {
        "Charmander": {"HP": 100, "Moves": {"Ember": 15, "Scratch": 10, "Flamethrower": 25, "Fire Fang": 20}},
        "Bulbasaur": {"HP": 100, "Moves": {"Vine Whip": 15, "Tackle": 10, "Razor Leaf": 20, "Solar Beam": 30}},
        "Squirtle": {"HP": 100, "Moves": {"Water Gun": 15, "Tackle": 10, "Bubble": 10, "Hydro Pump": 25}},
        "Pikachu": {"HP": 100, "Moves": {"Thunder Shock": 15, "Quick Attack": 10, "Thunderbolt": 25, "Iron Tail": 20}},
        "Geodude": {"HP": 120, "Moves": {"Rock Throw": 15, "Tackle": 10, "Earthquake": 30, "Rock Slide": 25}},
        "Pidgey": {"HP": 80, "Moves": {"Gust": 10, "Quick Attack": 10, "Wing Attack": 20, "Air Slash": 25}},
        "Eevee": {"HP": 90, "Moves": {"Quick Attack": 10, "Bite": 15, "Swift": 20, "Hyper Beam": 35}},
        "Machop": {"HP": 110, "Moves": {"Karate Chop": 15, "Low Kick": 20, "Seismic Toss": 25, "Cross Chop": 30}}
    }

    # Define cooldown duration for each move
    cooldown_duration_player = 3
    cooldown_duration_opponent = 3
    
    # Choose game mode
    print("Choose your game mode:")
    print("1. Player vs Computer")
    print("2. Player vs Player")
    game_mode = input("Enter the number of your chosen mode (1 or 2): ")

    if game_mode == '1':
        # PvC Mode
        print("Player vs Computer Mode Selected!")
        # Display available Pokemons
        print("Choose your Pokemon:")
        pokemon_list = list(pokemons.keys())
        for i in range(len(pokemon_list)):
            print(str(i + 1) + ". " + pokemon_list[i])

        player_choice = input("Enter the number of your chosen Pokemon (1-8): ")
        if player_choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid choice! Game Over!")
            exit()

        player_pokemon = pokemon_list[int(player_choice) - 1]
        player_hp = pokemons[player_pokemon]["HP"]
        player_moves = pokemons[player_pokemon]["Moves"]
        print("\nYou chose " + player_pokemon + " with " + str(player_hp) + " HP!")

        # Select opponent Pokemon randomly
        opponent_index = int(time.time()) % 8
        opponent_pokemon = pokemon_list[opponent_index]
        if opponent_pokemon == player_pokemon:
            opponent_index = (opponent_index + 1) % 8
            opponent_pokemon = pokemon_list[opponent_index]
        opponent_hp = pokemons[opponent_pokemon]["HP"]
        opponent_moves = pokemons[opponent_pokemon]["Moves"]
        print("Your opponent is " + opponent_pokemon + " with " + str(opponent_hp) + " HP!\n")

        # Initialize cooldown trackers
        player_cooldowns = {move: 0 for move in player_moves}
        opponent_cooldowns = {move: 0 for move in opponent_moves}

        # Battle loop
        battle_over = False
        while not battle_over:
            # Player's turn
            print(player_pokemon + "'s moves:")
            moves_list1 = list(player_moves.keys())
            for i in range(len(moves_list1)):
                move = moves_list1[i]
                if player_cooldowns[move] > 0:
                    cooldown_status = " (Cooldown: " + str(player_cooldowns[move]) + " turns)"
                    
                else:
                      cooldown_status =("")
                print(str(i + 1) + ". " + move + " (Damage: " + str(player_moves[move]) + ")" + cooldown_status)

            attack_choice1 = input("\nEnter the number of your chosen attack (1-4): ")
            if attack_choice1 not in ['1', '2', '3', '4']:
                print("Invalid choice! You missed your turn!")
            else:
                player_attack = moves_list1[int(attack_choice1) - 1]
                if player_cooldowns[player_attack] > 0:
                    print("That move is on cooldown! You missed your turn!")
                else:
                    damage = player_moves[player_attack]
                    print("\n" + player_pokemon + " used " + player_attack + "!")
                    if damage > 20:
                        print("Boom! That was a powerful attack!")
                    elif opponent_hp <= 20:
                        print("Oh no! The opponent is close to fainting!")
                    else:
                        print("Nice hit!")
                    opponent_hp -= damage
                    print(opponent_pokemon + " took " + str(damage) + " damage! Remaining HP: " + str(opponent_hp))
                    player_cooldowns[player_attack] = cooldown_duration_player

            if opponent_hp <= 0:
                print("\n" + opponent_pokemon + " fainted! " + player_pokemon + " won the battle!")
                print("Congratulations! You won the battle!")
                print("Good try, Computer! Better luck next time.")
                break

            # Computer's turn
            time.sleep(2)
            print(opponent_pokemon + "'s moves:")
            moves_list2 = list(opponent_moves.keys())
            for i in range(len(moves_list2)):
                move = moves_list2[i]
                cooldown_status = " (Cooldown: " + str(opponent_cooldowns[move]) + " turns)" if opponent_cooldowns[move] > 0 else ""
                print(str(i + 1) + ". " + move + " (Damage: " + str(opponent_moves[move]) + ")" + cooldown_status)

            available_moves = [move for move in moves_list2 if opponent_cooldowns[move] == 0]
            if available_moves:
                computer_attack = available_moves[0]  # Simulate random choice with first available move
            else:
                print("\nComputer has no available moves and missed its turn!")
                computer_attack = moves_list2[0]  # Fallback in case all moves are on cooldown

            damage = opponent_moves[computer_attack]
            print("\n" + opponent_pokemon + " used " + computer_attack + "!")
            if damage > 20:
                print("Wow! That was a strong hit!")
            elif player_hp <= 20:
                print("Oh no! Your Pokemon is close to fainting!")
            else:
                print("The attack landed!")

            player_hp -= damage
            print(player_pokemon + " took " + str(damage) + " damage! Remaining HP: " + str(player_hp))
            opponent_cooldowns[computer_attack] = cooldown_duration_opponent

            if player_hp <= 0:
                print("\n" + player_pokemon + " fainted! " + opponent_pokemon + " won the battle!")
                print("Congratulations, Computer! You won the battle!")
                print("Good try! Better luck next time.")
                break

            # Reduce cooldowns
            for move in player_cooldowns:
                if player_cooldowns[move] > 0:
                    player_cooldowns[move] -= 1
            for move in opponent_cooldowns:
                if opponent_cooldowns[move] > 0:
                    opponent_cooldowns[move] -= 1

            print("\n--- Next Turn ---\n")

        print("Thank you for playing the Pokemon Battle Game!")

    elif game_mode == '2':
        # PvP Mode
        print("Player vs Player Mode Selected!")

        # Display available Pokemons
        print("Choose your Pokemon:")
        pokemon_list = list(pokemons.keys())
        for i in range(len(pokemon_list)):
            print(str(i + 1) + ". " + pokemon_list[i])

        # Player 1 chooses a Pokemon
        player1_choice = input("Player 1, enter the number of your chosen Pokemon (1-8): ")
        if player1_choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid choice! Game Over!")
            exit()

        player1_pokemon = pokemon_list[int(player1_choice) - 1]
        player1_hp = pokemons[player1_pokemon]["HP"]
        player1_moves = pokemons[player1_pokemon]["Moves"]
        print("\nPlayer 1 chose " + player1_pokemon + " with " + str(player1_hp) + " HP!")

        # Display available Pokemons for Player 2
        print("\nPlayer 2, choose a different Pokemon:")
        pokemon_list.remove(player1_pokemon)
        for i in range(len(pokemon_list)):
            print(str(i + 1) + ". " + pokemon_list[i])

        player2_choice = input("Player 2, enter the number of your chosen Pokemon (1-7): ")
        if player2_choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid choice! Game Over!")
            exit()

        player2_pokemon = pokemon_list[int(player2_choice) - 1]
        player2_hp = pokemons[player2_pokemon]["HP"]
        player2_moves = pokemons[player2_pokemon]["Moves"]
        print("\nPlayer 2 chose " + player2_pokemon + " with " + str(player2_hp) + " HP!")

        # Initialize cooldown trackers
        player1_cooldowns = {move: 0 for move in player1_moves}
        player2_cooldowns = {move: 0 for move in player2_moves}

        # Battle loop
        battle_over = False
        while not battle_over:
            # Player 1's turn
            print(player1_pokemon + "'s moves:")
            moves_list1 = list(player1_moves.keys())
            for i in range(len(moves_list1)):
                move = moves_list1[i]
                cooldown_status = " (Cooldown: " + str(player1_cooldowns[move]) + " turns)" if player1_cooldowns[move] > 0 else ""
                print(str(i + 1) + ". " + move + " (Damage: " + str(player1_moves[move]) + ")" + cooldown_status)

            attack_choice1 = input("\nPlayer 1, enter the number of your chosen attack (1-4): ")
            if attack_choice1 not in ['1', '2', '3', '4']:
                print("Invalid choice! Player 1 missed their turn!")
            else:
                player1_attack = moves_list1[int(attack_choice1) - 1]
                if player1_cooldowns[player1_attack] > 0:
                    print("That move is on cooldown! Player 1 missed their turn!")
                else:
                    damage = player1_moves[player1_attack]
                    print("\n" + player1_pokemon + " used " + player1_attack + "!")
                    if damage > 20:
                        print("Boom! What a devastating attack!")
                    elif player2_hp <= 20:
                        print("Oh no! Player 2's Pokemon is on the brink of fainting!")
                    else:
                        print("Nice strike!")
                    player2_hp -= damage
                    print(player2_pokemon + " took " + str(damage) + " damage! Remaining HP: " + str(player2_hp))
                    player1_cooldowns[player1_attack] = cooldown_duration_player

            if player2_hp <= 0:
                print("\n" + player2_pokemon + " fainted! " + player1_pokemon + " won the battle!")
                print("Congratulations Player 1! You won the battle!")
                print("Good try Player 2! Better luck next time.")
                break

            # Player 2's turn
            print(player2_pokemon + "'s moves:")
            moves_list2 = list(player2_moves.keys())
            for i in range(len(moves_list2)):
                move = moves_list2[i]
                cooldown_status = " (Cooldown: " + str(player2_cooldowns[move]) + " turns)" if player2_cooldowns[move] > 0 else ""
                print(str(i + 1) + ". " + move + " (Damage: " + str(player2_moves[move]) + ")" + cooldown_status)

            attack_choice2 = input("\nPlayer 2, enter the number of your chosen attack (1-4): ")
            if attack_choice2 not in ['1', '2', '3', '4']:
                print("Invalid choice! Player 2 missed their turn!")
            else:
                player2_attack = moves_list2[int(attack_choice2) - 1]
                if player2_cooldowns[player2_attack] > 0:
                    print("That move is on cooldown! Player 2 missed their turn!")
                else:
                    damage = player2_moves[player2_attack]
                    print("\n" + player2_pokemon + " used " + player2_attack + "!")
                    if damage > 20:
                        print("Wow! That was a powerful attack!")
                    elif player1_hp <= 20:
                        print("Oh no! Player 1's Pokemon is close to fainting!")
                    else:
                        print("Good hit!")
                    player1_hp -= damage
                    print(player1_pokemon + " took " + str(damage) + " damage! Remaining HP: " + str(player1_hp))
                    player2_cooldowns[player2_attack] = cooldown_duration_opponent

            if player1_hp <= 0:
                print("\n" + player1_pokemon + " fainted! " + player2_pokemon + " won the battle!")
                print("Congratulations Player 2! You won the battle!")
                print("Good try Player 1! Better luck next time.")
                break

            # Reduce cooldowns
            for move in player1_cooldowns:
                if player1_cooldowns[move] > 0:
                    player1_cooldowns[move] -= 1
            for move in player2_cooldowns:
                if player2_cooldowns[move] > 0:
                    player2_cooldowns[move] -= 1

            print("\n--- Next Turn ---\n")

        print("Thank you for playing the Pokemon Battle Game!")

    else:
        print("Invalid choice! Game Over!")

    question = input("Do you want to continue the game? (yes/no): ")
    if question.lower() == "yes":
        print("You don't seemed tired")
        q = 0
    elif question.lower() == "no":
        print("Thank You For Playing Our Game")
        q = 1
    else:
        print("Incorrect statement")
        break
