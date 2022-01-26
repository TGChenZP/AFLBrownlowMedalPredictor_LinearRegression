import pandas as pd
from collections import defaultdict as dd
import numpy as np



def wholeseason(final_test_games, lm, selected_features, choice):
    """ Helper function for running emperical test - returns tuple of leaderboard of players for the season (with votes) """
    
    players = dd(int) # tally
    
    for file in final_test_games:
        
        # Open each final test season's game
        df = pd.read_csv(f'./Data/{choice}/{file}')
        
        # Run predictions
        x_final = df[selected_features].replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        y_pred = lm.predict(x_final)
        
        # Find top 3 scoring players of the game
        enumerated = [(i, score) for i, score in enumerate(y_pred)]
        enumerated.sort(key = lambda x:x[1], reverse = True)
        
        # Find their (top 3 players) names and insert them into the tally by adding 3 votes, 2 votes and 1 vote respectively
        for j in range(3):
            players[df.loc[enumerated[j][0]]['Player']] += (3-j)
    
    # Sort the leaderboard so top pollers are ranked first
    leaderboard = sorted(list(players.items()), reverse = True, key = lambda x:x[1])
    
    return leaderboard
