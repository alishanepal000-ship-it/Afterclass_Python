
#Indentaiton: white space or tab space inside if block
#eg: if True:
        #print("")

choice=["scissors","paper","rock"]

player1=input("Enter rock, paper or scissor:")
player2=input("Enter rock, paper or scissor:")

if player1==player2:
    print('Draw')

elif(player1=='rock' and player2=='scissor') or (player1=='paper' and player2=='rock') or (player1=='scissor'and player2=='paper'):
    print('player1 wins')

else:
    print('player2 wins')


# print(choice)