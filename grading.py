def get_grade(score):
    '''Determines grade based on score'''
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    elif 0 <= score < 40:
        return "F"
    else:
        return "invalid score"
def student_result(name, score):
    ''''accepts name and score and returns full data'''
    grade = get_grade(score)
    return{'Name': name, 'score': score,'grade': grade }
 
    


