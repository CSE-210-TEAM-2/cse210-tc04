import random




class Dealer:
def __init__(self):

        """"Class Constructor: will inizialite a dictionary and the num_throws to count
         the amount of times he is going to throw it"""

        self.cards = []
        self.num_throws = 0
        self.points = 300

    def can_draw(self):

        """
        determines whether or not the Dealer can draw again. 
        It returns a boolean value that is true if get_points are greater than 0, Otherwise, it returns false.
        """

        if self.points > 0: 
            return True
        
        else:
            return False
#************************ THROW cards **************************

    def deal_cards(self):

        """ This function will play that basically will get 2 cards randomly from 1 to 13 
        and saved in my list cards"""

        self.cards.clear()
        
        for number in range(2):
            result = random.randint(1,13)
            self.cards.append(result)

        self.num_throws +=1
        
#"************************ GET POINTS FUNCTION **************************"
    def get_points(self):

        """ This method will return the total points that the user has"""

        return self.points

#"************************ User Guess **************************"

    def guess(self):
        """
        This Method will compute if the user guessed right or not and will update the score
        if user got it right or not
        """

        choice = input("Higher or lower? [h/l] : ")
        next_card = "h"

        if self.cards[0] < self.cards[1]:
            next_card = "h"

        if self.cards[0] > self.cards[1]:
            next_card = "l"
        
        
        if choice == next_card:
            self.points +=100
        else:
            self.points -= 75
        


