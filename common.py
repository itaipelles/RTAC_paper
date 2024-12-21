from scipy.stats import rankdata

def rank_transform_unbiased(x,y):
    x = rankdata(x)/(len(x)+1)
    y = rankdata(y)/(len(y)+1)
    return x,y