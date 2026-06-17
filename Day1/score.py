#PEF 8 complaint code
MAX_SCORE = 100

def calculate_grade(score, max_score=MAX_SCORE):
    """Return a letter grade for the given score."""
    percentage = (score / max_score) * 100
    if percentage >= 90:
        return "A"
    elif percentage >=75:
        return "B"
    else:
        return "C"
print (calculate_grade(90))