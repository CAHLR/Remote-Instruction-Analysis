import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import matplotlib.dates as mdates
import datetime
import matplotlib.ticker as ticker
import sys
sys.path.insert(0, '/home/jenny/remote_learning_code_Spring_2019')
from utils import parse_args

sys.argv = ['-f']
args = parse_args()

term_20 = args.semester_2020_Spring
start_date_20 = args.start_date_2020_Spring
remote_date_20 = args.remote_date_2020_Spring
end_date_20 = args.end_date_2020_Spring

term_19 = args.semester_2019_Spring
start_date_19 = args.start_date_2019_Spring
end_date_19 = args.end_date_2019_Spring

term_18 = args.semester_2018_Spring
start_date_18 = args.start_date_2018_Spring
end_date_18 = args.end_date_2018_Spring

term_17 = args.semester_2017_Spring
start_date_17 = args.start_date_2017_Spring
end_date_17 = args.end_date_2017_Spring


def process_submission(term, start_date, end_date, cutoff_date=None):
    # load submissions
    submission = pd.read_csv(args.submissions, sep='\t', header=0)
    print(submission.iloc[1])
    exit()
    submission = submission.loc[submission['term_name'] == term]

    submission = submission.loc[
        submission['graded_at'].notnull(), ['user_id', 'assignment_id', 'graded_at']]  # no duplicate exists
    # load assignments and mapping them to submissions
    assignments = pd.read_csv(args.assignments, sep='\t', header=0)
    assignments = assignments.loc[assignments['term_name'] == term]
    assignments = assignments.loc[:, ['assignment_id', 'asn_due_at']]  # no duplicate exists
    assignment_submission = pd.merge(assignments, submission, on='assignment_id')

    # print(assignments, submission)
    # merge assignment_submissions to assignments_override_user_rollups
    assignments_override_user_rollups = pd.read_csv(args.assignments_overrides_user_rollups, sep='\t',
                                                    header=0)  # duplicates exist
    assignments_override_user_rollups = assignments_override_user_rollups.loc[
        assignments_override_user_rollups['term_name'] == term]
    assignments_override_user_rollups = assignments_override_user_rollups.loc[
        assignments_override_user_rollups['due_at'].notnull()].drop_duplicates()
    assignments_override_user_rollups = assignments_override_user_rollups.loc[:, ['assignment_id', 'user_id', 'due_at']]
    assignments_submission_override = pd.merge(assignment_submission, assignments_override_user_rollups,
                                               on=['user_id', 'assignment_id'], how='left')

    # get new due date based on assignment_override

    assignments_submission_override['new_due_date'] = assignments_submission_override[['asn_due_at', 'due_at']].apply(
        lambda x: x['asn_due_at'] if pd.isnull(x['due_at']) else x['due_at'], axis=1)
    assignments_submission_override = assignments_submission_override.loc[
        assignments_submission_override['new_due_date'].notnull(), ['assignment_id', 'user_id', 'new_due_date',
                                                                    'graded_at']]
    # calculate days taken to grade assignments
    assignments_submission_override['graded_at'] = pd.to_datetime(assignments_submission_override['graded_at'],
                                                                  format='%Y-%m-%d %H:%M:%S.%f')
    assignments_submission_override['graded_at1'] = assignments_submission_override['graded_at'].apply(
        lambda x: x.date())
    assignments_submission_override['new_due_date'] = pd.to_datetime(assignments_submission_override['new_due_date'],
                                                                     format='%Y-%m-%d %H:%M:%S.%f')
    assignments_submission_override['new_due_date1'] = assignments_submission_override['new_due_date'].apply(
        lambda x: x.date())
    assignments_submission_override['days_grading'] = assignments_submission_override['graded_at1'] - \
                                                      assignments_submission_override['new_due_date1']
    assignments_submission_override['days_grading'] = assignments_submission_override['days_grading'] / np.timedelta64(
        1, 'D')

    # assignments_submission_override = assignments_submission_override[assignments_submission_override['days_grading']>0]
    # assignments_submission_override['days_grading'] = assignments_submission_override['days_grading'].apply(lambda x: x if x > 0 else 0)
    assignments_submission_override = assignments_submission_override.loc[
        (assignments_submission_override['new_due_date'] >= start_date) & (
                    assignments_submission_override['graded_at'] >= start_date)]
    assignments_submission_override = assignments_submission_override.loc[
        (assignments_submission_override['new_due_date'] <= end_date) & (
                    assignments_submission_override['graded_at'] <= end_date)]
    if cutoff_date:
        assignments_submission_before = assignments_submission_override.loc[
            assignments_submission_override['new_due_date'] < cutoff_date]
        assignments_submission_after = assignments_submission_override.loc[
            assignments_submission_override['new_due_date'] >= cutoff_date]
        return assignments_submission_before, assignments_submission_after
    else:
        return assignments_submission_override


assignments_submission_override_17 = process_submission(term_17, start_date_17, end_date_17)