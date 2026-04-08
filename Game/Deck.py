from Card import Card
import random

class Deck ():
    
    def __init__(self):
        
        ranks = Card.RANKS
        suites = Card.SUITES
        deck=[]# datatype is an array of card objects
        
        for rank in ranks:
            for suite in suites:
                card = Card(suite=suite, rank=rank)
                deck.append(card)
        self.deck = deck
   
    def shuffle(self):
        newDeck=[]
        deck=self.deck
        while True:
            if len(deck) ==1:
                card=deck[0]
                newDeck.append(card)
                break
            n=random.randint(0, len(deck)-1)
            
            card=deck[n]
            deck.pop(n)
            newDeck.append(card)
            
        print("new Deck length", len(newDeck))
        print("old Deck length", len(deck))
        for card in newDeck:
            card.printCard()
            print("---")
            self.deck=newDeck
   
    def burn_card(self):
        # take top card puts it below the deck
        print("before burning deck")
        self.print_deck()
        print("after burning deck")
        top_card=self.deck[0]
        self.deck.pop(0)
        self.deck.append(top_card)
        self.print_deck()
    def give_card(self):
        # take a card out of the deck from the end deck and give to player
        top_card=self.deck[0]
        self.deck.pop(0)
        return top_card
        pass
    
if __name__ == "__main__":
        d1= Deck()
        d1.shuffle()
        #d1.burn_card()
        card=d1.give_card()
        print("card given")
        card.printCard()
        d1.print_deck()
        

        
                