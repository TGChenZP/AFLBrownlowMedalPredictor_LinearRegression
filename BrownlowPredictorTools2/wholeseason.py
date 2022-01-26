import pandas as pd
from collections import defaultdict as dd
import numpy as np



def wholeseason(final_test_games, lm1, lm2, selected_features1, selected_features2, choice):
    """ Helper function for running emperical test - returns tuple of leaderboard of players for the season (with votes) """
    
    players = dd(int)
    
    for file in final_test_games:
        
        # Open each final test season's game
        df = pd.read_csv(f'./Data/{choice}/{file}')
        
        # Run predictions for step 1
        x_final = df[selected_features1].replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        y_pred = lm1.predict(x_final)
        
        # find top 3 scoring players of the game for step 1 - the predicted votegetters
        enumerated = [(i, score) for i, score in enumerate(y_pred)]
        enumerated.sort(key = lambda x:x[1], reverse = True)
        
        # Find index for the predicted votegetters and make relevant dataframe
        secondround = [x[0] for x in enumerated[0:3]]
        
        df2 = df.iloc[secondround]
        df2.index = list(range(3))
        
        # Run predictions for step 2
        y_pred2 = lm2.predict(df2[selected_features2])
        
        # Rank the top 3 players of the game from highest score to lowest
        enumerated2 = [(i, score) for i, score in enumerate(y_pred2)]
        enumerated2.sort(key = lambda x:x[1], reverse = True)
        
         # Find their (top 3 players) names and insert them into the tally by adding 3 votes, 2 votes and 1 vote respectively
        for j in range(3):
            index = secondround[enumerated2[j][0]]
            players[df.loc[index]['Player']] += (3-j)
    
    # Sort the leaderboard so top pollers are ranked first
    leaderboard = sorted(list(players.items()), reverse = True, key = lambda x:x[1])
    
    return leaderboard