import tbc 
def main():
    hero = tbc.Character("Branlyn", 15, 60, 10, 3)
    monster = tbc.Character("Migo", 10, 40, 15, 2 )
    hero.printStats()
    monster.printStats()
    tbc.basicFight(hero, monster)

if __name__ == "__main__":

    main()
    