print('''
              _,-""""-..__
         |`,-'_. `  ` ``  `--'""".
         ;  ,'  | ``  ` `  ` ```  `.
       ,-'   ..-' ` ` `` `  `` `  ` |==.
     ,'    ^    `  `    `` `  ` `.  ;
    `}_,-^-   _ .  ` \ `  ` __ `   ;  
       `"---"' `-`. ` \---""`.`.  `;
                  \\` ;       ; `. `,
                   ||`;      / / | |
      jrei        //_;`    ,_;' ,_;"      
''')
print("Welcome to the adventure game!\nYour mission is to find the treasure and not die!")

cross_road = input("You are at a cross in the road, which direction do you want to go? Left or right? (left, right):  ").lower()
if cross_road == "right":
    print("Gameover you fell in a sinkhole")
elif cross_road == "left":
    print("You mad it safe down the road!")
    swim = input("You have come to a river, do you want to swim now or wait for it to slow down? (Swim, Wait):  ").lower()
    if swim == "swim":
        print("Gameover you drowned")
    elif swim == "wait":
        print("You noticed a house while waiting for the water to slow down!")
        house = input("You walk to the house, now which door do you want to open? (Red, Yellow, Blue):  ").lower()
        if house == "red" or house == "blue":
            print("Gameover you were swarmed by insects")
        elif house == "yellow":
            print("You won the game and found the treasure!")