import pandas as pd
import pickle


def user_type_group(enrollment):

    group = enrollment.groupby('enrollment_role_type')
    dic = dict()
    for i in group.groups.keys():
        users = group.get_group(i)
        if i == 'DesignerEnrollment':
            dic['designer'] = users['user_id'].tolist()
            print('designer', len(dic['designer']))
        elif i == 'ObserverEnrollment':
            dic['observer'] = users['user_id'].tolist()
            print('observer', len(dic['observer']))
        elif i == 'StudentEnrollment':
            dic['student'] = users['user_id'].tolist()
            print('student', len(dic['student']))
        elif i == 'StudentViewEnrollment':
            dic['studentview'] = users['user_id'].tolist()
            print('studentview', len(dic['studentview']))
        elif i == 'TaEnrollment':
            dic['ta'] = users['user_id'].tolist()
            print('ta', len(dic['ta']))
        elif i == 'TeacherEnrollment':
            dic['teacher'] = users['user_id'].tolist()
            print('teacher', len(dic['teacher']))
    f = open('user_id_groups.pkl', 'wb')
    pickle.dump(dic, f)
    f.close()


def user_racial_group():
    student_demo = pd.read_csv('/deepedu/research/jenny/final/edw_student_demographics/edw_student_demographics_000', header=0, sep='\t')
    student_demo = student_demo.loc[:, ['canvas_global_user_id', 'race_ethnicity_rollup_2']].drop_duplicates()
    student_group = student_demo.groupby('race_ethnicity_rollup_2')
    group_dict = dict()
    for i in student_group.groups.keys():
        students = student_group.get_group(i)
        group_dict[i] = students['canvas_global_user_id'].tolist()
        print(i, len(students['canvas_global_user_id']))
    f = open('user_racial_groups.pkl', 'wb')
    pickle.dump(group_dict, f)
    f.close()


def courses():
    courses = pd.read_csv('/deepedu/research/jenny/final/courses/courses_000', header=0, sep='\t')
    courses_Spring_2020 = courses.loc[courses['term_name']=='2020 Spring']['canvas_global_course_id'].drop_duplicates()
    print('Spring 2020 ', len(courses_Spring_2020))
    courses = courses['canvas_global_course_id'].drop_duplicates()
    print('All ', len(courses))


def course_sections():
    course_sections = pd.read_csv('/deepedu/research/jenny/final/course_section/course_section_000', header=0, sep='\t')
    course_sections_Spring_2020 = course_sections.loc[course_sections['term_name']=='2020 Spring']['canvas_course_section_global_id'].drop_duplicates()
    print('Spring 2020', len(course_sections_Spring_2020))
    course_sections = course_sections['canvas_course_section_global_id'].drop_duplicates()
    print('All ', len(course_sections))


def dropped_students_2020():
    enrollments = pd.read_csv('/deepedu/research/jenny/final/enrollments/enrollments_000', header=0, sep='\t')
    dropped_students_2020 = enrollments.loc[(enrollments['term_name']=='2020 Spring')&(enrollments['enrollment_state']=='deleted')]
    student_demo = pd.read_csv('/deepedu/research/jenny/final/edw_student_demographics/edw_student_demographics_000', header=0, sep='\t')
    student_demo = student_demo.loc[:, ['canvas_global_user_id', 'race_ethnicity_rollup_2']].drop_duplicates()
    student_demo = pd.merge(dropped_students_2020, student_demo, left_on='user_id', right_on='canvas_global_user_id', how='inner')
    student_group = student_demo.groupby('race_ethnicity_rollup_2')
    group_dict = dict()
    for i in student_group.groups.keys():
        students = student_group.get_group(i)
        group_dict[i] = students['canvas_global_user_id'].tolist()
        print(i, len(students['canvas_global_user_id']))
    f = open('dropped_user_racial_groups.pkl', 'wb')
    pickle.dump(group_dict, f)
    f.close()

if __name__ == '__main__':
    #enrollments = pd.read_csv('/deepedu/research/jenny/final/enrollments/enrollments_000_active_students', header=0, sep='\t')
    #enrollments = enrollments.loc[:, ['user_id', 'enrollment_role_type']].drop_duplicates()
    #user_type_group(enrollments)
    #user_racial_group()
    #courses()
    #course_sections()
    dropped_students_2020()

 


