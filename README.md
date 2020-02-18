# ej-challenge
1. This took me about a day of work to complete figured any more than that and it would be too much time
2. Some of the hardest part was figuring out what exactly was asked. Heres a list of points of confusion and the assumptions i made. I would have made less assumptions and asked questions but this is the only time i have to complete this challenge before i am away from my computer for two weeks.:

    Persistence: I wasn't sure if you meant for me to put everything into the database and record every move. For individual games this didn't make sense unless we are trying to display metrics for each player. A thing which i realized after i ran out of time is part of the advanced part. I kept persistence to the browser level with the games, using a clunky global list while the users were saved to the sqlite database.

    Score: This may be just a flaw on my part, but i spent a lot of time trying to figure out how much of the game i actually had to implement. If i had to implement a full GUI this would have been much too much so i settled on specifically just allowing the user to calculate their own points and use this as a record system. I think because of modern video games it was hard for me to detach the scoring of the game and the idea of the game... trying to figure this out took up a lot of my time

    Number of Users: i was not sure if i was to make this a one player game or multiplayer game. I settled on two players with the ability to add two more at a time by going back to the start game screen (actually adding two more players is a bug but it worked in my favor a bit)

    Player Profile: i wasn't sure to what level the player profile needed to be personal i just used a basic profile of username and password

Known Bugs:
    1. You can log in the same player multiple times, though the score keeper will only update the first one
    2. only the top password input box actually records password when trying to create new user
    3. user data is not cleaned when creating a new user
    4. The zero in the input box for the score stays when typing your new number; need to make it go away. Made it this way so that 0 is default
    5. anything can be put in the score input boxes. if text is put in the scorekeeper will crash
