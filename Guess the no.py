print("This is a guess game programme")
print("Enter any two digit number")
k = int(input())
"""print ("Total guess you have 9")"""
g = 1
game_over = False
n =20
while not game_over:
    if k==n:
        print(f"You had guessed the correct number, you guessed in {g} time")
        game_over= True
    elif (k >20 and k <=100):
        print("Enter a smaller number")
        g=g+1
        k=int(input())
        print("Guess again")
    elif(k<20 and k>100):
        print("Enter a greater number")
        g=g+1
        k=int(input())
        print("Guess again")
    else:
        print("Invalid input")







