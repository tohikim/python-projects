import random

starting = 1000 
bank = 0
num_green = 5
num_red = 3
num_black = 1
num_white = 1

while True: 
    mode = input("Choose the difficulty: [1 : Easy], [2: Difficult]")
    if mode == "1":
        num_green = 6
        num_red = 4
        num_black = 0
        num_white = 0
        break
    elif mode != "1" or "2":
        print("Pick a correct mode!")
        continue
rounds = int(input("How many rounds would you like to play?: "))

bag = []
bag.extend(("green " * num_green).split())
bag.extend(("red " * num_red).split())
bag.extend(("black " * num_black).split())
bag.extend(("white " * num_white).split())

dr_marbles = []
results = {}
round_start_num = 0

bank = starting
for i in range(rounds):
    print(f'==== Round {i+1} ====')
    round_start_num = bank
    while True: 
        bet = int(input(f'How much do you bet? (Balance: ${bank}): $'))
        if bet > bank:
            print(f'You don\'t have enough cash!')
            continue
        while True: 
            draw = input("Enter 'd' to draw: ")
            if draw == "d": 
                marble = random.choice(bag)
                print(f'You drew... {marble}')
                if marble == "green":
                    bank += bet
                    dr_marbles.append(marble)
                    print(f'You won ${bet}! Your current balance is ${bank}.')
                elif marble == "red": 
                    bank -= bet
                    dr_marbles.append(marble)
                    print(f'You lost ${bet}! Your current balance is ${bank}.')
                elif marble == "black":
                    won_bet = bet * 9
                    bank += won_bet
                    dr_marbles.append(marble)
                    print(f'LUCKY🌟! You won ${won_bet}! (Balance:${bank})')
                elif marble == "white":
                    lost_bet = bet * 5
                    bank -= lost_bet
                    dr_marbles.append(marble)
                    print(f'SO UNLUCKY😭! You lost ${lost_bet}! (Balance: ${bank})')
                break
            else:
                print ("Please enter 'd' to draw")
                continue
        if bank <= round_start_num/2: 
            print("GAME OVER! You lost more than half of your money.")
            results[f'Round {i+1}'] = ("lost", len(dr_marbles), f'${round_start_num-bank}')
            break
        elif bank >= round_start_num *3: 
            print("YOU WON! You 3X your balance. Impressive 😎")
            results[f'Round {i+1}'] = ("won", len(dr_marbles), f'${bank-round_start_num}')
            break
        else: continue
    print(f'==== Round {i+1} Results ====')
    green_count = dr_marbles.count("green") or 0
    red_count = dr_marbles.count("red") or 0
    black_count = dr_marbles.count("black") or 0
    white_count = dr_marbles.count("white") or 0
    print(f'Game results: You drew {green_count} greens, {red_count} reds, {black_count} blacks, and {white_count} whites. ({len(dr_marbles)} streak)')
    dr_marbles = []
    if i+1 != rounds and bank == 0:
        print("==== GAME ENDED ==== \nNot enough funds. You can't play anymore!")
        break
    
print (f'=== FINAL RESULTS ===')
for game, info in results.items():
    print(f'{game}: You {info[0]} {info[2]}. (Streak: {info[1]})')
print (f'Bank total: ${bank}')

