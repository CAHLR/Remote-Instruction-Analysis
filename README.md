# Remote-Instruction-Analysis
Comparing pre (2019 Spring, 2018 Spring, 2017 Spring) and post (2020 Spring) pandemic student and instructor engagement analytics from university-wide LMS logs.

* Set up hyperparameters in file [utils.py](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/utils.py), which includes name, start date, end date of each semester, when remote instruction took place, and directories of LMS logs.


* Before the start of analysis, run the following code to preprocess users.

	* `python preprocess_user.py`

	* 	Two files will be generated:

		* user\_id\_groups.pkl: a dictionary mapping each role into user_IDs of that role. (roles including designer, observer, student, studentview, ta, teacher)
		* user\_racial\_groups.pkl: a dictionary mapping each racial group into student_IDs of that race.

### Instructor Engagement:
* **Assignments released per day over the semester:** 

	* Run [instructional\_quality/assignments\_rate.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/assignments_rate.ipynb)

* **Number of late excused submissions:**
	* Run  [student\_engagement/excused\_submission.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement/excused_submission.ipynb)

* **Instructor changes to due dates after release (i.e., reactive extensions)**
	* Run [instructional\_quality/instructor\_override\_grade_asn.ipynb ](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/instructor_override_grade_asn.ipynb)

* **Instructor changes to due dates before release (i.e., proactive extensions)**
	* Run [instructional\_quality/instructor\_override\_grade\_asn.ipynb ](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/instructor_override_grade_asn.ipynb)

* **Instructional staff announcements**
	*  Run [instructional\_quality/Rate\_instructional\_announcements.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/Rate_instructional_announcements.ipynb)

* **Assignment submission types (2020, 2019, 2018, 2017)**
	*  Run [instructional\_quality/submission\_type\_changes.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/submission_type_changes.ipynb)

* **Instructor time to grade assignments after submission**
	* Run [instructional\_quality/instructor\_grade\_time.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/instructor_grade_time.ipynb)

* **Instructor comments on submissions**
	* Run [instructional\_quality/instructor\_comments.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/instructor_comments.ipynb)

* **Length of instructor comments (in bytes)**
	* Run [instructional\_quality/instructor\_comments.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/instructor_comments.ipynb)


### Student Engagement:
* **Number of submissions per day**
	* Run [student\_engagement/Rate\_submission\_completed.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement/Rate_submission_completed.ipynb)

* **Number of student late submissions**
	* Run [student\_engagement/late\_submission.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement/late_submission.ipynb)

* **Total number of daily student events**
	* Run [student\_engagement/student\_actions.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement/student_actions.ipynb)

* **Number of course drops per day**
	* Run [student\_engagement/Drop\_out\_rate.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement/Drop_out_rate.ipynb)

* **Student discussion activity over the semester **
	* Run [student\_engagement/Student\_discussion\_trend.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement/Student_discussion_trend.ipynb)

* **Student discussion activity over the semester on graded/ungraded topics** 
	* Run [student\_engagement/Student\_discussion\_trend (graded or ungraded).ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement/Student_discussion_trend%20(graded%20or%20ungraded).ipynb) 

* **Average grade on assignments turned in per day**
	* Run [student\_engagement/assignment\_GPA.ipynb ](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement/assignment_GPA.ipynb)

* **Assignment category proportions (Spring 2020)**
	* Run [instructional\_quality/assignment\_group\_Spring20.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/instructional_quality/assignment_group_Spring20.ipynb)

### Student Engagement by Race:
* **Percentage of active students per week**
	* Run [student\_engagement\_race/active\_student\_race\_proportion.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement_race/active_student_race_proportion.ipynb)

* **Weekly student events**
	* Run [student\_engagement\_race/student\_actions\_race.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement_race/student_actions_race.ipynb)

* **Weekly proportion of submission**
	* Run [student_engagement\_race/Rate\_submission\_completed\_race.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement_race/Rate_submission_completed_race.ipynb)

* **Average grade on assignments turned in per day**
	* Run [student\_engagement\_race/assignment\_GPA\_race\_weekly.ipynb](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/student_engagement_race/assignment_GPA_race_weekly.ipynb)

### Enrollment Analysis:
* **Did student grades in Fall 2020 classes differ if the prerequisite for the class was satisfied in the emergency remote instruction semester?**
	* Run [enrollment\_analysis/preprocess\_edw.py ](https://github.com/CAHLR/Remote-Instruction-Analysis/blob/main/enrollment_analysis/preprocess_edw.py), the results will be saved in a file named results.pkl.














	


 

