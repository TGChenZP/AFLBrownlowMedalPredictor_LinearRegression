def return_tp(result):
    """ Helper function for just returning the true positive/true negative values"""
    
    return tuple([result[i][i] for i in range(len(result))])