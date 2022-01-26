import pandas as pd
import numpy as np



def predict(test_games, lm, selected_features, choice, pca):
    """ takes test_games and model and pca object to output predictions as a list and observations as a Series """
    
    prediction = list()
    
    testdata_y = pd.DataFrame()
    
    for file in test_games:
        
        df = pd.read_csv(f'./Data/{choice}/{file}')
        
        tmp = [0 for i in range(len(df))]
        
        x_final = df[selected_features].replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        y_pred = lm.predict(pca.transform(x_final)) # must transform the data using same pca object as training object
        
        testdata_y = pd.concat([testdata_y, df['Brownlow Votes']], axis=0)
        
        enumerated = [(i, score) for i, score in enumerate(y_pred)]
        enumerated.sort(key = lambda x:x[1], reverse = True)
        
        tmp[enumerated[0][0]] = 3
        tmp[enumerated[1][0]] = 2
        tmp[enumerated[2][0]] = 1
#         print(enumerated[0:3])
#         print(enumerated[-3:])
        
        prediction = prediction + tmp
        
    return prediction, testdata_y





def predict_mass(test_games, lm, selected_features, choice, pca):
    """ takes test_games and model and pca object to output predictions as a list and observations as a Series """
    
    prediction = list()
    
    testdata_y = pd.DataFrame()
    
    for file in test_games:
        
        df = pd.read_csv(f'./Data/{choice}/{file}')
        
        tmp = [0 for i in range(len(df))]
        
        x_final = df[selected_features].replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
        y_pred = lm.predict(pca.transform(x_final)) # must transform the data using same pca object as training object
        
        testdata_y = pd.concat([testdata_y, df['Brownlow Votes']], axis=0)
        
        enumerated = [(i, score) for i, score in enumerate(y_pred)]
        enumerated.sort(key = lambda x:x[1], reverse = True)
        
        tmp[enumerated[0][0]] = 3
        tmp[enumerated[1][0]] = 2
        tmp[enumerated[2][0]] = 1
#         print(enumerated[0:3])
#         print(enumerated[-3:])
        
        prediction = prediction + tmp

    out = pd.DataFrame({'predictions': prediction, 'observations': list(testdata_y[testdata_y.columns[0]])})
    
    return out