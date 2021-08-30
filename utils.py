import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--semester_2020_Spring', type=str, default='2020 Spring', help='2020 Spring semester')
    parser.add_argument('--start_date_2020_Spring', type=str, default='2020-01-14', help='start date of 2020 Spring')
    parser.add_argument('--first_week_end_date_2020_Spring', type=str, default='2020-01-21', help='end date of the first week of 2020 Spring')
    parser.add_argument('--remote_date_2020_Spring', type=str, default='2020-03-10', help='remote instruction date of 2020 Spring')
    parser.add_argument('--last_week_start_date_2020_Spring', type=str, default='2020-05-08', help='start date of the last week of 2020 Spring')
    parser.add_argument('--end_date_2020_Spring', type=str, default='2020-05-15', help='end date of 2020 Spring')

    parser.add_argument('--semester_2019_Spring', type=str, default='2019 Spring', help='2019 Spring semester')
    parser.add_argument('--start_date_2019_Spring', type=str, default='2019-01-15', help='start date of 2019 Spring')
    parser.add_argument('--cutoff_date_2019_Spring', type=str, default='2019-03-10', help='cutoff date of 2019 Spring')
    parser.add_argument('--end_date_2019_Spring', type=str, default='2019-05-17', help='end date of 2019 Spring')

    parser.add_argument('--semester_2018_Spring', type=str, default='2018 Spring', help='2018 Spring semester')
    parser.add_argument('--start_date_2018_Spring', type=str, default='2018-01-09', help='start date of 2018 Spring')
    parser.add_argument('--cutoff_date_2018_Spring', type=str, default='2018-03-10', help='cutoff date of 2018 Spring')
    parser.add_argument('--end_date_2018_Spring', type=str, default='2018-05-11', help='end date of 2018 Spring')

    parser.add_argument('--semester_2017_Spring', type=str, default='2017 Spring', help='2017 Spring semester')
    parser.add_argument('--start_date_2017_Spring', type=str, default='2017-01-10', help='start date of 2017 Spring')
    parser.add_argument('--cutoff_date_2017_Spring', type=str, default='2017-03-10', help='cutoff date of 2017 Spring')
    parser.add_argument('--end_date_2017_Spring', type=str, default='2017-05-12', help='end date of 2017 Spring')

    # 2017-2020
    parser.add_argument('--submissions', type=str,
                       default='/deepedu/research/jenny/final/submissions/submissions_000')
    parser.add_argument('--submission_comments', type=str,
                       default='/deepedu/research/jenny/final/submission_comments/submission_comments_000')
    parser.add_argument('--enrollments', type=str,
                       default='/deepedu/research/jenny/final/enrollments/enrollments_000')
    parser.add_argument('--edw_student_majors', type=str,
                       default='/deepedu/research/jenny/final/edw_student_majors/edw_student_majors_000')
    parser.add_argument('--edw_student_grades', type=str,
                       default='/deepedu/research/jenny/final/edw_student_grades/edw_student_grades_000')
    parser.add_argument('--edw_student_demographics', type=str,
                       default='/deepedu/research/jenny/final/edw_student_demographics/edw_student_demographics_000')
    parser.add_argument('--edw_course_lists', type=str,
                       default='/deepedu/research/jenny/final/edw_course_lists/edw_course_lists_000')
    parser.add_argument('--discussion_topics', type=str,
                       default='/deepedu/research/jenny/final/discussion_topics/discussion_topics_000')
    parser.add_argument('--discussion_entry', type=str,
                       default='/deepedu/research/jenny/final/discussion_entry/discussion_entry_000')
    parser.add_argument('--courses', type=str,
                       default='/deepedu/research/jenny/final/courses/courses_000')
    parser.add_argument('--course_section', type=str,
                       default='/deepedu/research/jenny/final/course_section/course_section_000')
    parser.add_argument('--assignments', type=str,                                                                        
                       default='/deepedu/research/jenny/final/assignments/assignments_000')
    parser.add_argument('--assignments_overrides', type=str,
                       default='/deepedu/research/jenny/final/assignments_overrides/assignments_overrides_000')
    parser.add_argument('--assignments_overrides_user_rollups', type=str,
                       default='/deepedu/research/jenny/final/assignments_override_user_rollups/assignments_overrides_user_rollups_000')
    parser.add_argument('--assignment_groups', type=str,
                       default='/deepedu/research/jenny/final/assignment_groups/assignment_groups000')


    return parser.parse_args()
