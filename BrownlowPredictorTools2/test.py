import pandas as pd



def test1(predictions, testdata_y, nchoice):
    """ Calculates the tp/tn for no votes, have vote. Polymorphic as to how many choices there are """
    
    # instantiate tally
    result1 = list() # tp/tn/tp/fp calculated with respect to predictions (i.e. predicted 1, obs 0 => contribute to fp 1)
    result2 = list() # tp/tn/tp/fp calculated with respect to observations (i.e. predicted 1, obs 0 => contribute to fp 0)
    
    # Initialise the result1 and result2 tallys based on nchoice
    for i in range(nchoice):
        tmp1 = [0 for j in range(nchoice)]
        tmp2 = [0 for j in range(nchoice)]
        result1.append(tmp1)
        result2.append(tmp2)
        
    # Run through the predictions and add to tally according to whether it is tp/tn/fp/fn
    for i in range(len(predictions)):
        result1[predictions[i]][int(testdata_y.iloc[i][0])] += 1
        result2[int(testdata_y.iloc[i][0])][predictions[i]] += 1
    
     # Find the sum of each row and then take percentage based on it (because we are taking tp/fp/tn/fn with respect to either predictions or observations rather than total)
    for i in range(nchoice):
        
        sum_row1 = sum(result1[i])
        sum_row2 = sum(result2[i])
        
        for j in range(nchoice):
            result1[i][j] = result1[i][j]/sum_row1
            result2[i][j] = result2[i][j]/sum_row2
            
    return result1, result2





def test2(predictions, testdata_y, nchoice):
    """ Same as above except special adjustment for 1 vote, 2 votes 3 votes"""
    
    result1 = list()
    result2 = list()
    
    for i in range(nchoice):
        tmp1 = [0 for j in range(nchoice)]
        tmp2 = [0 for j in range(nchoice)]
        result1.append(tmp1)
        result2.append(tmp2)
    
    for i in range(len(predictions)):
        result1[predictions[i]-1][int(testdata_y.iloc[i][0])-1] += 1 # the use of -1 is a special adjustment
        result2[int(testdata_y.iloc[i][0])-1][predictions[i]-1] += 1
    
    for i in range(nchoice):
        
        sum_row1 = sum(result1[i])
        sum_row2 = sum(result2[i])
        
        for j in range(nchoice):
            result1[i][j] = result1[i][j]/sum_row1
            result2[i][j] = result2[i][j]/sum_row2
            
    return result1, result2





def test1_mass(out, adj_vote):
    """ Helper function for returning tp/tn for mass testing for step 1 (more efficient as does not collect other stats)"""
    
    tp0 = len(out[(out['predictions'] == out['observations'].astype(int)) & (out['predictions'] == 0)])/len(out[(out['predictions'] == 0)])
    tp1 = len(out[(out['predictions'] == out['observations'].astype(int)) & (out['predictions'] == 1)])/len(out[(out['predictions'] == adj_vote)])
    
    return (tp0, tp1,)





def test2_mass(out):
    """ Helper function for returning tp/tn for mass testing for step 2 (more efficient as does not collect other stats)"""
    
    tp1 = len(out[(out['predictions'] == out['observations'].astype(int)) & (out['predictions'] == 1)])/len(out[(out['predictions'] == 1)])
    tp2 = len(out[(out['predictions'] == out['observations'].astype(int)) & (out['predictions'] == 2)])/len(out[(out['predictions'] == 2)])
    tp3 = len(out[(out['predictions'] == out['observations'].astype(int)) & (out['predictions'] == 3)])/len(out[(out['predictions'] == 3)])
    
    return (tp1, tp2, tp3,)