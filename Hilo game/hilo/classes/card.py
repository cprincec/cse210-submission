from random import randint

class Card:
    """Card with numbers written on it.

    The responsibility of card is to keep track of the current card and next card 
    and points awarded for each guess.
   
    Attributes:
        current_card (int): The number on current card.
        next_card (int): The number on next card.
        point (int): The number of points for each guess.
    """

    def __init__(self):
        """Constructs a new instance of Card with current_card, next_card and point attributes.

        Args:
            self (Card): An instance of Card.
        """
        self.current_card = 0
        self.next_card = 0
        self.point = 0

    def guess(self):
        """Generates new random values for current and next cards and calculates the points.
        
        Args:
            self (Card): An instance of Card.
        """

        self.current_card = randint(1, 13)
        self.next_card = randint(1, 13)
        print(f"\nThen current card is {self.current_card}")
        guess = input("Will the next card be higher or lower than current card? [h/l]: ")
        while (guess != "h" and guess != "l"):
            print("Invalid input! \nEnter h/l.")
            guess = input("Will the next card be higher or lower than current card? [h/l]: ")
        if self.next_card > self.current_card and guess == "h":
            self.point += 100 
        elif self.next_card < self.current_card and guess == "h":
            self.point -= 75
        elif self.next_card > self.current_card and guess == "l":
            self.point -= 75
        elif self.next_card < self.current_card and guess == "l":
            self.point += 100
        