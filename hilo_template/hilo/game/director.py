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
        
        