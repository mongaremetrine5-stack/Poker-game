import random
import time

class Player():
    def __init__(self,type="pc", cards=[],total_amount_bet=0,name="",amount=0):
            
            self.name=name
            self.player_typetype=type
            self.cards=cards
            self.total_amount_bet=total_amount_bet
            self.amount=amount

    def place_initial_bet(self):
        while True:
            amount= input(f"Place initial bet amount. Your current amount is {self.amount}:")

            if amount.isdigit():
                n=int(amount)
                if n>0 and n <= self.amount:
                    self.amount = self.amount-n
                    return n
                
                print("Invalid amount entered")
                print(f"Amount must range between 1 and {self.amount}")
                print("Try again")
            else:
                print(f"Kindly enter amount between 1 and {self.amount}")

    def call_fold_raise(self, player):
        choice=input("Press 1 to call \n Press 2 to fold \n Press 3 to raise")
        if choice =='1':
            return self.call(player)

        if choice == '2':
            return self.fold(player)

        if choice == '3':
            return self.raise_stake(player)
        print(f"Wrong choice {choice}. Choose 1,2 or 3")
        self.call_fold_raise(player)

    def call(self, player):
        print("call action")

    def fold(self, player):
        print("I fold!!")
        return "l"

    def raise_stake(self, player):
        print("raise amount")


    def auto_match_or_raise(self,amount):
        print("PC calculating move...")
        time.sleep(3)
        to_do=random.randint(1,2)
        raise_amount=amount+random.randint(10,250)

        if raise_amount>self.amount:
            to_do=1

        if to_do ==1:
            if self.amount>amount:
                self.amount=self.amount-amount
                print(f"Matching your action. Bet = {amount}")
                return amount
            else:
                return "l"

        self.amount=self.amount-raise_amount
        print("FEELING LUCKY. I raise by", raise_amount)
        return raise_amount


    def update_amount_bet(self,amount):
        self.total_amount_bet=self.total_amount_bet+amount
        
    def reset_amount_bet(self):
        self.total_amount_bet=0    


