from random import choices

ntrials=15000
player1wins=0
ndicep1=3
ndicep2=2
totalp1=0
totalp2=0


#player 2 rolls first
for j in range(ntrials):
    dice=choices(range(1,7),k=ndicep2)
    dice.sort(reverse=True)
    totalp2=dice[0]+dice[1]
    if dice[0] == dice[1]:
        print("p2 win equal")
        continue


#player 1 rolls second

    dice=choices(range(1,7),k=ndicep1)
    dice.sort(reverse=True)
    totalp1=dice[0]+dice[1]

    if totalp2 >= totalp1:
        print("p2 wins")

    else:
        print("p1 wins")
        player1wins = player1wins + 1

print("Player 1 wins",(player1wins/ntrials)*100,"%")