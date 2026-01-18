import random

def SnakesAndLadders():
    playerPositions = {}
    ladderAmont = 3
    snakeCount = 3
    winningSquare = 100
    boardMaxSquare = 99 
    snakes = []
    ladders = []
    while True:
        try:
            numPlayers = int(input("Enter count of players: "))
            if numPlayers <= 0:
                print("Please enter a positive number of players.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for _ in range(numPlayers):
        while True:
            playerName = input("Enter your name: ")
            if playerName in playerPositions:
                print(f"Name '{playerName}' is already taken. Choose another.")
                continue
            if not playerName:
                print("Name cannot be empty.")
                continue
            playerPositions[playerName] = 0
            break
    
    print("\nWelcome players:", playerPositions.keys())
    print("-" * 30)
    usedSquares = set()
    usedSquares.add(0) 
    usedSquares.add(winningSquare)

    def generate_unique_points(amount, is_snake):
        features = []
        for _ in range(amount):
            while True:
                start = random.randint(1, boardMaxSquare)
                stop = random.randint(1, boardMaxSquare)
                if is_snake:
                    if start <= stop: continue
                else:
                    if stop <= start: continue
                if start not in usedSquares and stop not in usedSquares:
                    features.append([start, stop])
                    usedSquares.add(start)
                    usedSquares.add(stop)
                    break
        return features

    snakes = generate_unique_points(snakeCount, is_snake=True)
    ladders = generate_unique_points(ladderAmont, is_snake=False)
    
    print(f"Game set up with {len(ladders)} ladders and {len(snakes)} snakes.")
    
    game_over = False
    players_list = list(playerPositions.keys())
    player_index = 0

    while not game_over:
        current_player = players_list[player_index]
        current_place = playerPositions[current_player]
        
        print(f"\n{current_player}'s turn. Current position: {current_place}")
        print(playerPositions) 
        
        enter = input("Roll a cube by pressing Enter. ")
        
        num_cube = random.randint(1, 6)
        print(f"-> {current_player} rolled a {num_cube}.")
       
        new_place = current_place + num_cube

        if new_place > winningSquare:
            new_place = winningSquare - (new_place - winningSquare)
            print(f"-> Bounced back! Moving to {new_place}.")
            
        playerPositions[current_player] = new_place

        moved_by_feature = False
        for start, stop in snakes:
            if new_place == start:
                playerPositions[current_player] = stop
                print(f"-> Oh no, {current_player} got bitten by a snake! Slid down to {stop}.")
                moved_by_feature = True
                break
        
        if not moved_by_feature:
            for start, stop in ladders:
                if new_place == start:
                    playerPositions[current_player] = stop
                    print(f"-> {current_player} climbed a ladder! Jumped up to {stop}.")
                    moved_by_feature = True
                    break
        
        current_place = playerPositions[current_player]

        if current_place == winningSquare:
            print(f"\n*** FINISHED GAME! Congratulations, {current_player} wins! ***")
            game_over = True
            break

        player_index = (player_index + 1) % len(players_list)





            







    
