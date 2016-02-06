from cmu_auth import authenticate
import base64, ics, json
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import requests

def get_courses(username, password, semester = 'S16'):


    try:
        s = authenticate('https://s3.andrew.cmu.edu/sio/index.html', username, password )
    except KeyError:
        print("Incorrect Password")
        return None
    except:
        print("An error has occurred")
        return None

    user_data = requests.get("http://apis.scottylabs.org/directory/v1/andrewID/{}".format(username)).json()

    ics_file = s.get('https://s3.andrew.cmu.edu/sio/secure/export/schedule/{0}_semester.ics?semester={0}'.format(semester)).text

    cal = Calendar.from_ical(ics_file)

    with open('classes.json') as data_file:
        classes = json.load(data_file)


    day_map = {'SU': 0, 'MO': 1, 'TU': 2, 'WE': 3, 'TH': 4, 'FR': 5, 'SA': 6}
    course_data = {'user': user_data, 'courses': {}, 'schedule': []}
    for event in cal.walk():
        if event.name != 'VEVENT': continue

        days = list(map(lambda day: day_map[day], event.get('rrule').get('byday')))

        begin = event.get('dtstart').dt
        end = event.get('dtend').dt

        course_title, tmp = event.get('summary').split(" :: ")
        course_number, course_section = tmp.split(" ")
        instructors = [x.strip() for x in (event.get('description').split('\n\n')[1].split(":")[1].split(';'))]
        location = event.get('location').strip()

        if not (course_number in course_data['courses']):
            if (course_number in classes['courses']):
                course_data['courses'][course_number] = classes['courses'][course_number]

        for day in days:
            delta = timedelta(days = day - begin.isoweekday())

            start_time = begin + delta
            end_time = end + delta
            duration = end_time - start_time

            course_data['schedule'].append({
                'title': "{}: {}".format(course_number, course_title),
                'start': start_time.isoformat(),
                'end': end_time.isoformat(),
                'location': location,
                'duration': str(duration),
                'course': course_number,
                'section': course_section,
                'instructors': instructors
            })


    return course_data

    # c = ics.Calendar(ics_file)
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
