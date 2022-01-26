import pandas as pd
from collections import defaultdict as dd
import numpy as np



def wholeseason(final_test_games, lm, selected_features, choice, pca):
    """ Helper function for running emperical test - returns tuple of leaderboard of players for the season (with votes) """
    
    players = dd(int)
    
    for file in final_test_games:
        
        df = pd.read_csv(f'./Data/{choice}/{file}')
        
        x_final = df[selected_features].replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        y_pred = lm.predict(pca.transform(x_final)) # must transform the data using same pca object as training object
        
        enumerated = [(i, score) for i, score in enumerate(y_pred)]
        enumerated.sort(key = lambda x:x[1], reverse = True)
        
        for j in range(3):
            players[df.loc[enumerated[j][0]]['Player']] += (3-j)
    
    leaderboard = sorted(list(players.items()), reverse = True, key = lambda x:x[1])
    
    return leaderboard

