### Scope ###

enemies = 1

def increase_enemies():
    enermies = 2
    print(f"enemies inside function: {enermies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion()
#print(potion_strength)  #<--- Exception

# Global Scope
player_health = 10

def drink_postion():
    potion_strength = 2
    print(player_health)

drink_postion()

# Modifying Global Scope

ticker = 'PTR4'

def change_ticker():
    global ticker
    ticker = 'B3SA'
    print(f"Ticker inside function: {ticker}")

change_ticker()
print(f"Ticker outside function: {ticker}")