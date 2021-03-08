# TODO: Add entry point code here


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

 