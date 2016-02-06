from cmu_auth import authenticate
import base64, ics
from icalendar import Calendar, Event
from datetime import datetime, timedelta

def get_courses(username, password, semester = 'S16'):

    s = authenticate('https://s3.andrew.cmu.edu/sio/index.html', username, password )
    ics_file = s.get('https://s3.andrew.cmu.edu/sio/secure/export/schedule/{0}_semester.ics?semester={0}'.format(semester)).text
    c = ics.Calendar(ics_file)

    cal = Calendar.from_ical(ics_file)

    day_map = {'SU': 0, 'MO': 1, 'TU': 2, 'WE': 3, 'TH': 4, 'FR': 5, 'SA': 6}
    courses = []
    for event in cal.walk():
        if event.name != 'VEVENT': continue

        days = list(map(lambda day: day_map[day], event.get('rrule').get('byday')))

        begin = event.get('dtstart').dt
        end = event.get('dtend').dt

        for day in days:
            delta = timedelta(days = day - begin.isoweekday())

            course_title, tmp = event.get('summary').split(" :: ")
            course_number, course_section = tmp.split(" ")
            instructors = [x.strip() for x in (event.get('description').split('\n\n')[1].split(":")[1].split(';'))]
            location = event.get('location').strip()
            start_time = begin + delta
            end_time = end + delta
            duration = end_time - start_time

            courses.append({
                'title': "{}: {}".format(course_number, course_title),
                'start_time': start_time.isoformat(),
                'end_time': end_time.isoformat(),
                'location': location,
                'duration': str(duration),
                'course': course_number,
                'section': course_section,
                'instructors': instructors
            })


    return courses

    # courses = {}
    #
    # for event in c.events:
    #     course_title, tmp = event.name.split(" :: ")
    #     course_number, course_section = tmp.split(" ")
    #     instructors = [x.strip() for x in (event.description.split('\n\n')[1].split(":")[1].split(';'))]
    #     location = event.location
    #     begin = event.begin
    #     end = event.end
    #     duration = event.duration
    #
    #     current_class = {'begin': str(begin), 'end': str(end), 'duration': str(duration), 'location': location, 'section': course_section}
    #
    #     instructors = set(instructors)
    #     instructors.discard("TBA")
    #
    #     if course_number in courses:
    #         courses[course_number]['classes'].append(current_class)
    #         instructors.update(set(courses[course_number]['instructors']))
    #         courses[course_number]['instructors'] = list(instructors)
    #     else:
    #         courses[course_number] = {'title': course_title, 'number': course_number, 'instructors': list(instructors), 'classes': [current_class]}
    #
    # return courses
