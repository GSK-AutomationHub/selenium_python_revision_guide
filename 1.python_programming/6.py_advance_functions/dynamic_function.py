
study_topics = ['physics','chemistry','maths','english','mechatronics']

student_info = {
    'student_name':'Rohit',
    'roll_no':'007',
    'college':'Boston University',
    'interest':'python programming'
}

def university_student_details(*args, **kwargs):
    return {'positional':args,'keyword':kwargs}

sr1 = university_student_details(*study_topics, **student_info )
print(sr1)
print(sr1.get('keyword')['college'])

sr2= university_student_details('maths','physics','english',
                                name='Ricky',roll_no='008',college='Boston University',interest='game application')
print(sr2)
student_subjects = sr2.get('positional')
student_details = sr2.get('keyword')
print(type(student_subjects),student_subjects)
print(type(student_details),student_details)