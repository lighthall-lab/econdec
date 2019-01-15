# Move utility functions for data transformation here

def sum_oscillations(row):
    if row['ia-id'] in stock_ia_list:
        return sum([row['fsa-ia-02'],row['fsa-ia-25'],row['fsa-ia-27']])
    elif row['ia-id'] in bond_ia_list:
        return sum([row['fsa-ia-01'],row['fsa-ia-24'],row['fsa-ia-26']])

def oscillation_rate(row):
    return float(row['oscillations'] / row['choicert'])

def score_relative_stress(row):
    if row[4] < 5: return -1
    if row[4] > 5: return 1
    if row[4] == 5: return 0
    
def numeralize_sleep(row):
    try:
        if isinstance(row[2],basestring) and '-' in row[2]:
            values = row[2].split('-')
            return np.average([float(values[0]),float(values[1])])
        else:
            return float(row[2])
    except ValueError as e:
        print(e)
        return(row[2])
    
def score_relative_sleep(row):
    try:
        if float(row[1]) < float(row[2]): return -1
        if float(row[1]) > float(row[2]): return 1
        if float(row[1]) == float(row[2]): return 0
    except ValueError as e:
        print(e)
        return('NaN')
    
def convert_prob(row):
    good_prob = row['TrueProbGood']
    bad_prob = (1.00 - good_prob)
    return bad_prob

def convert_check(row):
    subj_resp = row['ProbGood']
    bad_prob = row['TrueProbGood']
    old_check = row['EstWithinRange?']
    new_check = 1 if (bad_prob+.05) >= (subj_resp*.01) >= (bad_prob-.05) else 0
    return new_check


def __init__(self):
    pass