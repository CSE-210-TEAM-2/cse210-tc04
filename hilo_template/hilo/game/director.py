from game.dealer import Dealer

class Director:

     # ********************** Will inizialite the game 
    def __init__(self):

        """"Class Constructor: will inizialite a dictionary and the num_throws to count
         the amount of times he is going to throw it"""

        self.keep_playing = True
        self.guess  = True
        self.dealer = Dealer()
        self.score = 300


    # ********************** Start Game 
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()
            self.do_updates()
           

    # ********************** Get imputs
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the cards.
        """

        self.dealer.deal_cards()
        
             
        
    # ********************** do outputs
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dealer will get a card and do the score 

        """
        print(f"\nThe Card is : {self.dealer.cards[0]}")
        self.dealer.guess()        

    
        # ********************** Do updates

        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.
        """

        print(f"Next Card was : {self.dealer.cards[1]}") 

        self.score = self.dealer.get_points()

        print(f"Your score is {self.score}")

                
        if self.dealer.can_deal():
            choice = input("Keep playing? [y/n] ")
            if choice == "n":
                print("Thanks for playing have a nice day")
            self.keep_playing = (choice == "y")
        else:
            
            self.keep_playing = False
            print("You Lost but Thanks for Playing!!")

    


       
    




