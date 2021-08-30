import pandas as pd
import sys
sys.path.insert(0, '/home/jenny/remote_learning_code_Spring_2017-2020')
from utils import parse_args
import json


if __name__=='__main__':
    args = parse_args()
    assign = pd.read_csv(args.assignments, header=0, sep='\t')
    submit = pd.read_csv(args.submissions, header=0, sep='\t')
    assign_sub = assign.loc[assign['assignment_id'].isin(submit['assignment_id'])]
    assign_sub = assign_sub['assignment_id'].drop_duplicates().tolist()
    valid_assign = {'assignment_id': assign_sub}
    f = open('assignment_with_submission.json', 'w')
    json.dump(valid_assign, f)