from cmu_auth import authenticate
import base64, ics

def get_courses(username, password, semester = 'S16'):

    s = authenticate('https://s3.andrew.cmu.edu/sio/index.html', username, password )
    c = ics.Calendar(s.get('https://s3.andrew.cmu.edu/sio/secure/export/schedule/{0}_semester.ics?semester={0}'.format(semester)).text)

    courses = {}

    for event in c.events:
        course_title, tmp = event.name.split(" :: ")
        course_number, course_section = tmp.split(" ")
        instructors = [x.strip() for x in (event.description.split('\n\n')[1].split(":")[1].split(';'))]
        location = event.location
        begin = event.begin
        end = event.end
        duration = event.duration

        current_class = {'begin': str(begin), 'end': str(end), 'duration': str(duration), 'location': location, 'section': course_section}

        if course_section.isdigit():
            if course_number in courses:
                courses[course_number]['classes'].append(current_class)
                courses[course_number]['instructors'] = instructors
            else:
                courses[course_number] = {'title': course_title, 'number': course_number, 'instructors': instructors, 'classes': [current_class]}
        else:
            if course_number in courses:
                courses[course_number]['classes'].append(current_class)
            else:
                courses[course_number] = {'title': course_title, 'number': course_number, 'instructors': [], 'classes': [current_class]}

        return courses
