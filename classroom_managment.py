classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def look_for_student(name):
    for i,item in enumerate(classroom):
        if item['name']==name:
            return i


def add_student(name, email=None):
    classroom.append(student:={'name':name,'email':email if email!=None else f"{name.lower()}@gmail.com",'grades':[]})


def delete_student(name):
    del classroom[look_for_student(name)]


def set_email(name, email):
    classroom[look_for_student(name)]['email']=email



def add_grade(name, profession, grade):
    classroom[look_for_student(name)]['grades'].append((profession,grade))




def avg_grade(name, profession):
    grades=classroom[look_for_student(name)]['grades']
    sum,count=0,0
    for item in grades:
        if(item[0]==profession):
            sum+=item[1]
            count+=1
    return sum/count





def get_professions(name):
    grades=classroom[look_for_student(name)]['grades']
    prof=set()
    for item in grades:
        prof.add(item[0])

    return list(prof)
