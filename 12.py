n = int(input())
players = dict()
for x in range(n):
    words = input().split() #esta diciendo que sea un input y que lo separe
    name = words[0] #name esta mirando a la posición "0" en words
    goals = int(words[2])
    spades = int(words[6])
    points = goals*4 + spades*2 #esta multiplicando cada una por el valor de cada una y sumandolos
    players[name] = points
maximun = max(players.values())
best = [k for k, v in players.items() if v == maximun]
if len(best) == 1:
    mvp = best[0]
    print(mvp + " is the MVP with " + str(players[mvp]) +" points!")
else:
    print("DRAW")