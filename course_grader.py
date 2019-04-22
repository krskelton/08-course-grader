import math

def course_grader(test_scores):
    # Your code here
    length_of_list = len(test_scores)    
    average_score = sum(test_scores) / length_of_list
    pass_fail = ""
    
    for test_score in test_scores:               
        if average_score >= 70 and test_score > 50:
            pass_fail = "pass"            
        elif average_score < 70 or test_score < 50:
            pass_fail = "fail"
            return pass_fail         
    return pass_fail
