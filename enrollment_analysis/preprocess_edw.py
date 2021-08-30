import pandas as pd
import numpy as np
import pickle
# Identify all post-requisite courses in Fall 2020 with only a single prerequisite course specified.
#This should also be calculated for post-requisite courses in Fall 2019 and the intersection of these two sets should be used for both analyses.
# Another condition of selecting the post-requisite course is that its prerequisite was offered every Fall/Spring from 2018-2020.

#Calculate GPA of all grades on those courses among students who satisfied the prerequisite in Spring 2020 as compare to Fall 2019, as compared to Spring 2019, as compared to taking it anytime prior to that, as compared to never having taken it.

def post_reqs(enrolled_courses, prereqs):  # intersection of post req courses in enrollment and prereqs list
    #enrolled_courses = enrolled_courses.loc[:, ['course_names', 'canvas_global_course_id']].drop_duplicates()
    #course_id = dict(zip(enrolled_courses['course_names'], enrolled_courses['canvas_global_course_id']))
    prereqs = prereqs.loc[prereqs['target'].isin(enrolled_courses['course_name'])&prereqs['prereqs'].isin(enrolled_courses['course_name'])]
    #prereqs['target'] = prereqs['target'].apply(lambda x: course_id[x])
    #prereqs['prereqs'] = prereqs['prereqs'].apply(lambda x: course_id[x])
    return prereqs


def postreqs_one_prereqs(prereqs):  # post req courses which have only 1 prerequisite course
    prereqs_group = prereqs.groupby('target').size().reset_index()
    prereqs_group.columns = ['target', 'num_prereqs']
    prereqs_one = prereqs_group.loc[prereqs_group['num_prereqs'] == 1]
    post = prereqs_one['target'].tolist()
    prereqs = prereqs.loc[prereqs['target'].isin(post)]
    return prereqs


def select_enrollment(enroll_user, valid_pairs):
    scores_20 = [[[], []], [[], []], [[], []], [[], []], [[], []], [[], []]]  # Fall 2020, Spring 2020, Fall 2019, Spring 2019-Spring 2017, never
    scores_19 = [[[], []], [[], []], [[], []], [[], []], [[], []], [[], []]]   # Fall 2019, Spring 2019, Fall 2018, Spring 2018-Spring 2017, never
    flag = 0
    for i in enroll_user.groups.keys():
        user = enroll_user.get_group(i).drop_duplicates()
        flag += 1
        print(flag)
        #if flag == 100:
        #    break
        user_20_f = user.loc[user['semester_year_name_concat'] == '2020 Fall']
        user_20_s = user.loc[user['semester_year_name_concat'] == '2020 Spring']
        user_19_f = user.loc[user['semester_year_name_concat'] == '2019 Fall']
        user_19_s = user.loc[user['semester_year_name_concat'] == '2019 Spring']
        user_18_f = user.loc[user['semester_year_name_concat'] == '2018 Fall']
        user_18_s = user.loc[user['semester_year_name_concat'] == '2018 Spring']

        for post, pre in valid_pairs.itertuples(index=False):

            if post in user_20_f['course_name'].tolist():
                print(20)
                score = user_20_f.loc[user_20_f['course_name'] == post]
                post_score = score.iloc[0]['final_score']
                if score.iloc[0]['grade_subtype_desc'] == 'Credit' or score.iloc[0]['grade_subtype_desc'] == 'No Credit':
                    credit = True
                else:
                    credit = False
                if pre in user_20_s['course_name'].tolist():
                    if credit:
                        scores_20[0][1].append(post_score)
                    else:
                        scores_20[0][0].append(post_score)
                elif pre in user_19_f['course_name'].tolist():
                    if credit:
                        scores_20[1][1].append(post_score)
                    else:
                        scores_20[1][0].append(post_score)
                elif pre in user_19_s['course_name'].tolist():
                    if credit:
                        scores_20[2][1].append(post_score)
                    else:
                        scores_20[2][0].append(post_score)
                elif pre in user['course_name'].tolist():
                    if credit:
                        scores_20[3][1].append(post_score)
                    else:
                        scores_20[3][0].append(post_score)
                else:
                    if credit:
                        scores_20[4][1].append(post_score)
                    else:
                        scores_20[4][0].append(post_score)

            if post in user_19_f['course_name'].tolist():
                print(19)
                score = user_19_f.loc[user_19_f['course_name'] == post]
                post_score = score.iloc[0]['final_score']
                if score.iloc[0]['grade_subtype_desc'] == 'Credit' or score.iloc[0]['grade_subtype_desc'] == 'No Credit':
                    credit = True
                else:
                    credit = False
                if pre in user_19_s['course_name'].tolist():
                    if credit:
                        scores_19[0][1].append(post_score)
                    else:
                        scores_19[0][0].append(post_score)
                elif pre in user_18_f['course_name'].tolist():
                    if credit:
                        scores_19[1][1].append(post_score)
                    else:
                        scores_19[1][0].append(post_score)
                elif pre in user_18_s['course_name'].tolist():
                    if credit:
                        scores_19[2][1].append(post_score)
                    else:
                        scores_19[2][0].append(post_score)
                elif pre in user['course_name'].tolist():
                    if credit:
                        scores_19[3][1].append(post_score)
                    else:
                        scores_19[3][0].append(post_score)
                else:
                    if credit:
                        scores_19[4][1].append(post_score)
                    else:
                        scores_19[4][0].append(post_score)
    return scores_20, scores_19


if __name__ == '__main__':
    grade_map = {'A': 4, 'B':3, 'C':2, 'D':1, 'F':0, 'Credit': 2, 'No Credit': 0}
    enrollment = pd.read_csv('/deepedu/research/jenny/final/edw_student_grades/edw_student_grades_000', header=0, sep='\t')
    enrollment = enrollment.loc[(enrollment['grade_subtype_desc'].notnull())&(enrollment['grade_subtype_desc']!='Administrative Code')&(enrollment['grade_subtype_desc']!='Unknown')]
    course_names = enrollment['course_name'].str.split(' ')
    enrollment['course_name'] = course_names.str[:-1].apply(' '.join) + '_' + course_names.str[-1]
    enrollment['final_score'] = enrollment['grade_subtype_desc'].apply(lambda x: grade_map[x])
    enrolled_courses = enrollment.loc[:, ['course_name', 'course_subject_name_number']].drop_duplicates()
    enrolled_courses.to_csv('courses_edw.csv', index=False)
    prereqs = pd.read_csv('prereqs_pairs_abbr.csv', header=0)
    # find valid post reqs
    prereqs = postreqs_one_prereqs(prereqs)
    print("number of postreqs having only one prereq: ", len(prereqs))
    prereqs = post_reqs(enrolled_courses, prereqs)
    print("number of valid prereqs pairs according the enrollments: ", len(prereqs))

    # preprocess enrollment
    #enrollment = enrollment.merge(enrolled_courses, left_on='course_id', right_on='canvas_global_course_id')
    enrollment = enrollment.loc[:, ['canvas_global_user_id', 'course_name', 'semester_year_name_concat', 'grade_subtype_desc', 'final_score']]

    en = set(enrollment.loc[enrollment['semester_year_name_concat']=='2020 Fall']['course_name'].tolist())
    pre = set(prereqs['target'].tolist())
    print(len(en.intersection(pre)))

    en = set(enrollment.loc[enrollment['semester_year_name_concat'] == '2020 Spring']['course_name'].tolist())
    pre = set(prereqs['target'].tolist())
    print(len(en.intersection(pre)))
    en = set(enrollment.loc[enrollment['semester_year_name_concat'] == '2019 Fall']['course_name'].tolist())
    pre = set(prereqs['target'].tolist())
    print(len(en.intersection(pre)))
    #exit()

    # select enrollment for each semester
    enrollment_user = enrollment.groupby('canvas_global_user_id')
    scores_20, scores_19 = select_enrollment(enrollment_user, prereqs)
    for i in range(5):
        print('Letter grade: ', 'number: ', len(scores_20[i][0]), 'avg grade: ', np.mean(scores_20[i][0]))
        print('Pass/No-Pass: ', 'number: ', len(scores_20[i][1]), 'avg grade: ', np.mean(scores_20[i][1]))

    for i in range(5):
        print('Letter grade: ', 'number: ', len(scores_19[i][0]), 'avg grade: ', np.mean(scores_19[i][0]))
        print('Pass/No-Pass: ', 'number: ', len(scores_19[i][1]), 'avg grade: ', np.mean(scores_19[i][1]))

    # save results
    dic = {'scores_20': scores_20, 'scores_19': scores_19}
    f = open('results.pkl', 'wb')
    pickle.dump(dic, f)











