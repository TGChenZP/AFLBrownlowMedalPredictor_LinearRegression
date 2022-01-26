def feature_selection2(cols, select_mode, BT_OT):
    """ Helper function for feature selection based on rules of Feature Selection. First parameter is the , second parameter is the micro rules of feature 
    selection (1, 2, 3, 4), third parameter denotes whether macro rule of feature selection is 'BT_OT' """
    
    out = list()
    
    # dictionary listing items that cannot coexist with each other
    nonallowed = {'Kicks': ["Disposals"],
         'Handballs': ["Disposals"],
         'Disposals': ["Kicks", "Handballs", 'Ineffective Disposals', 'Contested Possessions', 'Uncontested Possessions', 'Effective Disposals'],
         'Marks': ["Uncontested Marks", 'Marks Outside 50', 'Marks Inside 50', 'Contested Marks'],
         'Tackles': ['Tackles Inside 50', 'Tackles Outside 50'],
         'Goal Assists': ["Score Involvements"],
         'Clearances': ["Centre Clearances", "Stoppage Clearances"],
         'Contested Possessions': ["Disposals"],
         'Uncontested Possessions': ["Disposals"],
         'Effective Disposals': ["Disposals"],
         'Contested Marks': ['Marks'],
         'Marks Inside 50': ['Marks'],
         'Centre Clearances': ['Clearances'],
         'Stoppage Clearances': ['Clearances'],
         'Score Involvements': ['Behind Assists', 'Goal Assists'],
         'Tackles Inside 50': ["Tackles"],
         'Uncontested Marks': ["Marks"],
         'Marks Outside 50': ["Marks"],
         'Tackles Outside 50': ["Tackles"],
         'Behind Assists BTN': ["Score Involvements"],
         'Ineffective Disposals': ["Disposals"]}    
    
    if select_mode == 1 and not BT_OT: # Micro mode 1: return all that is seen
        return cols
    
    illegal = list()
    
    if select_mode == 3: # Micro mode 3: ban summary statistics
        banned = ['Disposals', 'Marks', 'Tackles', 'Clearances', 'Score Involvements']
        illegal.extend(banned)
        
    elif select_mode == 4: # Micro mode 4: ban Disposals
        illegal.append('Disposals')
    
    
    
    if BT_OT and select_mode != 1:
        
        for col in cols:
            col_ = strip_end(col)

            if col_ not in illegal:

                if col_ in nonallowed:

                    for i in range(len(nonallowed[col_])):
                        illegal.append(nonallowed[col_][i])
                
                illegal.append(col_)
                out.append(col)
    
    
    elif BT_OT and select_mode == 1: 
        
        for col in cols:
            col_ = strip_end(col)

            if col_ not in illegal:
                
                # BT or OT: i.e. once BT uses something, then put the col's root name in illegal so OT can't be selected even if it surpassed FT_val
                illegal.append(col_) 
                out.append(col)
        
    else:
        
        for col in cols:
            col_ = strip_end(col)

            if col_ not in illegal:

                if col_ in nonallowed:

                    for i in range(len(nonallowed[col_])):
                        illegal.append(nonallowed[col_][i])

                out.append(col)
    
    return out






def strip_end(string):
    """ Helper function to remove the 'BTS' 'BTN' tag from end """
    
    tmp = string.split()
    out = str()
    
    for i in range(len(tmp)-1):
        out += tmp[i]
        out += ' '
    
    return out[:-1]