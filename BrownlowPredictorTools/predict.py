import pandas as pd
import numpy as np



def predict(test_games, lm, selected_features, choice):
    """ takes test_games and model to output predictions as a list and observations as a Series """
    
    prediction = list()
    
    testdata_y = pd.DataFrame()
    
    for file in test_games:
        
        # Open test game file
        df = pd.read_csv(f'./Data/{choice}/{file}')
        
        # Initialise a list for this game
        tmp = [0 for i in range(len(df))]
        
        # Make predictions
        x_final = df[selected_features].replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        y_pred = lm.predict(x_final)
        
        # Collect the actual observations
        testdata_y = pd.concat([testdata_y, df['Brownlow Votes']], axis=0)
        
        # Find top 3 scoring players for the game and allocate 3, 2, 1 votes to their respective index on the tmp list
        enumerated = [(i, score) for i, score in enumerate(y_pred)]
        enumerated.sort(key = lambda x:x[1], reverse = True)
        
        tmp[enumerated[0][0]] = 3
        tmp[enumerated[1][0]] = 2
        tmp[enumerated[2][0]] = 1
        
        # Can un-comment to observe what actual scores the linear regression is outputting 
        # print(enumerated[0:3])
        # print(enumerated[-3:])
        
        prediction = prediction + tmp
    
    return prediction, testdata_y





def predict_mass(test_games, lm, selected_features, choice):
    """ same as predict except returns both the predict and observations in one dataframe """
    
    prediction = list()
    
    testdata_y = pd.DataFrame()
    
    for file in test_games:
        
        # Open test game file
        df = pd.read_csv(f'./Data/{choice}/{file}')
        
        # Initialise a list for this game
        tmp = [0 for i in range(len(df))]
        
        # Make predictions
        x_final = df[selected_features].replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        y_pred = lm.predict(x_final)
        
        # Collect the actual observations
        testdata_y = pd.concat([testdata_y, df['Brownlow Votes']], axis=0)
        
        # Find top 3 scoring players for the game and allocate 3, 2, 1 votes to their respective index on the tmp list
        enumerated = [(i, score) for i, score in enumerate(y_pred)]
        enumerated.sort(key = lambda x:x[1], reverse = True)
        
        tmp[enumerated[0][0]] = 3
        tmp[enumerated[1][0]] = 2
        tmp[enumerated[2][0]] = 1
        
        # Can un-comment to observe what actual scores the linear regression is outputting 
#         print(enumerated[0:3])
#         print(enumerated[-3:])
        
        prediction = prediction + tmp
        
    out = pd.DataFrame({'predictions': prediction, 'observations': list(testdata_y[testdata_y.columns[0]])})
    
    return out