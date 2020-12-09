squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares=[value**2 for value in range(1,11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[-4:])
for player in players[0:3]:
    print(player.title())
players_1=players[:]
players_1.append("liona")
print(players_1)

foods=("beats","chiken","milk","noodles","seas")
for food in foods:
    print(food)
foods=("beats","chiken","milk","1","2")
for food in foods:
    print(food)
