import random

courses = ['physics', 'chemistry', 'maths', 'compsci', 'english', 'paining', 'photograpy']

colors = ['green', 'yellow', 'white', 'blue', 'pink', 'red']

careers = ['software engg', 'project mgmt', 'doctor', 'lawyer', 'TV Anchor', 'Arm Forces']

random_courses = random.sample(courses,2)
print(random_courses)

random_colors = random.choice(colors)
print(random_colors)

career_choices = random.choices(careers,k=2)
print(career_choices)

print(dir(random))
print(help(random.gauss))