from Game import Game

def play_game():
    game= Game()
    
    human=game.human
    pc=game.pc
    
    game.turn=human
    
    human_amount=human.place_initial_bet()
    human.update_amount_bet(human_amount)
    
    pc_amount=pc.auto_match_or_raise(human_amount)
    pc.update_amount_bet(human_amount)
 
    if pc_amount=="l":
        print("Towel throwing Human won")
        return
    
    game.turn=human
    game.pot=pc_amount+human_amount
    
    k=0
    
    print("--------------------------------")
    print("Starting the first betting round")
    print("--------------------------------")
    while True:
        
        #human and PC -> call,raise,fold
        if k >= 1 and pc.amount == human.amount:
           print("Betting round one completed")
           break
        
        k=k+1
        
        amount=human.call_fold_raise(player=pc)
        #2 betting rounds. If the player raises in the first round, then there is a second betting round. If the player calls in the first round, then there is no second betting round.
    
    
play_game()