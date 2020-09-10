import numpy as jenga

def main():
    probability_factor = 100
    print("----------------")
    print("LET'S PLAY JENGA")
    print("----------------\n")
    i = 1
    print("--------------------------------------")
    print("PROBABILITY THAT THE TOWER WILL STAND: ", end="")
    print("%", probability_factor)
    print("--------------------------------------\n")
    # for i in range (1, 10):
    while i > 0:
        # odd user moves here
        if i % 2 != 0:
            selection = input("YOUR TURN (l, m, h): ")
            if selection == 'l':
                random_int = jenga.random.randint(0, 4) 
            elif selection == 'm':
                random_int = jenga.random.randint(4, 8)
            elif selection == 'h':
                random_int = jenga.random.randint(8, 11)
            else:
                random_int = jenga.random.randint(0, 11)

            risk_factor = random_int * 10
            print("Your move was: ", risk_factor, end="")
            print("% risky!\n")
            
        # even computer moves here
        else:
            random_int = jenga.random.randint(0, 11)
            risk_factor = random_int * 10
            print("Computer's move was:", risk_factor, end="")
            print("% risky!\n")
        
        # probability factor here
        new_risk = risk_factor / 100 * 20
        probability_factor = probability_factor - new_risk
        if probability_factor > 0:
            print("--------------------------------------")
            print("PROBABILITY THAT THE TOWER WILL STAND: ", end="")
            print("%", probability_factor)
            print("--------------------------------------\n")
        if probability_factor <= 0:
            print("OH NO! THE TOWER FELL! ", end="")
            if i % 2 == 0:
                print("YOU WIN!")
                break
            else:
                print("COMPUTER WINS!")
                break
        i += 1
main()
