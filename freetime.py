from cmu_auth import authenticate
import base64, ics
from courses import *
import dateutil.parser

# dictionary of all user's jsons
users = { "Varun": [ { "location": "WEH- 7500", "end_time": "2016-01-12T16:20:00", "course": "15214", "section": "1", "start_time": "2016-01-12T15:00:00", "duration": "1:20:00", "title": "15214: Principles of Software Construction: Objects, Design, and Concurrency", "instructors": [ "Bloch", "Garrod" ] }, { "location": "WEH- 7500", "end_time": "2016-01-14T16:20:00", "course": "15214", "section": "1", "start_time": "2016-01-14T15:00:00", "duration": "1:20:00", "title": "15214: Principles of Software Construction: Objects, Design, and Concurrency", "instructors": [ "Bloch", "Garrod" ] }, { "location": "GHC- 4101", "end_time": "2016-01-13T11:20:00", "course": "15214", "section": "B", "start_time": "2016-01-13T10:30:00", "duration": "0:50:00", "title": "15214: Principles of Software Construction: Objects, Design, and Concurrency", "instructors": [ "Garrod" ] }, { "location": "GHC- 4401", "end_time": "2016-01-12T10:20:00", "course": "15251", "section": "1", "start_time": "2016-01-12T09:00:00", "duration": "1:20:00", "title": "15251: Great Theoretical Ideas in Computer Science", "instructors": [ "Haeupler", "O'Donnell" ] }, { "location": "GHC- 4401", "end_time": "2016-01-14T10:20:00", "course": "15251", "section": "1", "start_time": "2016-01-14T09:00:00", "duration": "1:20:00", "title": "15251: Great Theoretical Ideas in Computer Science", "instructors": [ "Haeupler", "O'Donnell" ] }, { "location": "DH- 2210", "end_time": "2016-01-13T19:50:00", "course": "15251", "section": "1", "start_time": "2016-01-13T18:30:00", "duration": "1:20:00", "title": "15251: Great Theoretical Ideas in Computer Science", "instructors": [ "Haeupler", "O'Donnell" ] }, { "location": "GHC- 4211", "end_time": "2016-01-15T11:20:00", "course": "15251", "section": "B", "start_time": "2016-01-15T10:30:00", "duration": "0:50:00", "title": "15251: Great Theoretical Ideas in Computer Science", "instructors": [ "TBA" ] }, { "location": "DH- 2315", "end_time": "2016-01-11T12:20:00", "course": "73100", "section": "1", "start_time": "2016-01-11T11:30:00", "duration": "0:50:00", "title": "73100: Principles of Economics", "instructors": [ "Kushnir", "Sleet" ] }, { "location": "DH- 2315", "end_time": "2016-01-13T12:20:00", "course": "73100", "section": "1", "start_time": "2016-01-13T11:30:00", "duration": "0:50:00", "title": "73100: Principles of Economics", "instructors": [ "Kushnir", "Sleet" ] }, { "location": "PH- A18C", "end_time": "2016-01-15T12:20:00", "course": "73100", "section": "E", "start_time": "2016-01-15T11:30:00", "duration": "0:50:00", "title": "73100: Principles of Economics", "instructors": [ "TBA" ] }, { "location": "BH- 136A", "end_time": "2016-01-11T13:20:00", "course": "80180", "section": "1", "start_time": "2016-01-11T12:30:00", "duration": "0:50:00", "title": "80180: Nature of Language", "instructors": [ "Werner" ] }, { "location": "BH- 136A", "end_time": "2016-01-13T13:20:00", "course": "80180", "section": "1", "start_time": "2016-01-13T12:30:00", "duration": "0:50:00", "title": "80180: Nature of Language", "instructors": [ "Werner" ] }, { "location": "WEH- 5302", "end_time": "2016-01-15T14:20:00", "course": "80180", "section": "E", "start_time": "2016-01-15T13:30:00", "duration": "0:50:00", "title": "80180: Nature of Language", "instructors": [ "Werner" ] }, { "location": "BH- A51", "end_time": "2016-01-12T14:50:00", "course": "85241", "section": "B", "start_time": "2016-01-12T13:30:00", "duration": "1:20:00", "title": "85241: Social Psychology", "instructors": [ "Helgeson" ] }, { "location": "BH- A51", "end_time": "2016-01-14T14:50:00", "course": "85241", "section": "B", "start_time": "2016-01-14T13:30:00", "duration": "1:20:00", "title": "85241: Social Psychology", "instructors": [ "Helgeson" ] } ] }

# the one user's json, which you are comparing. This is taken from Rishub's data.
my_data = [{'course': u'15150', 'end_time': '2016-01-12T13:20:00', 'title': '15150: Principles of Functional Programming', 'duration': '1:20:00', 'start_time': '2016-01-12T12:00:00', 'instructors': [u'Erdmann'], 'section': u'1', 'location': u'DH- 2315'}, {'course': u'15150', 'end_time': '2016-01-14T13:20:00', 'title': '15150: Principles of Functional Programming', 'duration': '1:20:00', 'start_time': '2016-01-14T12:00:00', 'instructors': [u'Erdmann'], 'section': u'1', 'location': u'DH- 2315'}, {'course': u'15150', 'end_time': '2016-01-13T11:50:00', 'title': '15150: Principles of Functional Programming', 'duration': '1:20:00', 'start_time': '2016-01-13T10:30:00', 'instructors': [u'TBA'], 'section': u'D', 'location': u'GHC- 5208'}, {'course': u'15251', 'end_time': '2016-01-12T10:20:00', 'title': '15251: Great Theoretical Ideas in Computer Science', 'duration': '1:20:00', 'start_time': '2016-01-12T09:00:00', 'instructors': [u'Haeupler', u"O'Donnell"], 'section': u'1', 'location': u'GHC- 4401'}, {'course': u'15251', 'end_time': '2016-01-14T10:20:00', 'title': '15251: Great Theoretical Ideas in Computer Science', 'duration': '1:20:00', 'start_time': '2016-01-14T09:00:00', 'instructors': [u'Haeupler', u"O'Donnell"], 'section': u'1', 'location': u'GHC- 4401'}, {'course': u'15251', 'end_time': '2016-01-13T19:50:00', 'title': '15251: Great Theoretical Ideas in Computer Science', 'duration': '1:20:00', 'start_time': '2016-01-13T18:30:00', 'instructors': [u'Haeupler', u"O'Donnell"], 'section': u'1', 'location': u'DH- 2210'}, {'course': u'15251', 'end_time': '2016-01-15T14:20:00', 'title': '15251: Great Theoretical Ideas in Computer Science', 'duration': '0:50:00', 'start_time': '2016-01-15T13:30:00', 'instructors': [u'TBA'], 'section': u'E', 'location': u'DH- 1217'}, {'course': u'36217', 'end_time': '2016-01-12T16:20:00', 'title': '36217: Probability Theory and Random Processes', 'duration': '1:20:00', 'start_time': '2016-01-12T15:00:00', 'instructors': [u"O'Connell"], 'section': u'A', 'location': u'PH- 100'}, {'course': u'36217', 'end_time': '2016-01-14T16:20:00', 'title': '36217: Probability Theory and Random Processes', 'duration': '1:20:00', 'start_time': '2016-01-14T15:00:00', 'instructors': [u"O'Connell"], 'section': u'A', 'location': u'PH- 100'}, {'course': u'79104', 'end_time': '2016-01-11T14:20:00', 'title': '79104: The Modern Nation-state through Film', 'duration': '0:50:00', 'start_time': '2016-01-11T13:30:00', 'instructors': [u'Law'], 'section': u'2', 'location': u'PH- 100'}, {'course': u'79104', 'end_time': '2016-01-13T14:20:00', 'title': '79104: The Modern Nation-state through Film', 'duration': '0:50:00', 'start_time': '2016-01-13T13:30:00', 'instructors': [u'Law'], 'section': u'2', 'location': u'PH- 100'}, {'course': u'79104', 'end_time': '2016-01-15T13:20:00', 'title': '79104: Global Histories', 'duration': '0:50:00', 'start_time': '2016-01-15T12:30:00', 'instructors': [u'McGrath'], 'section': u'T', 'location': u'GHC- 4211'}, {'course': u'79305', 'end_time': '2016-01-11T10:20:00', 'title': '79305: Moneyball Nation: Data in American Life', 'duration': '0:50:00', 'start_time': '2016-01-11T09:30:00', 'instructors': [u'Phillips'], 'section': u'1', 'location': u'PH- 125C'}, {'course': u'79305', 'end_time': '2016-01-13T10:20:00', 'title': '79305: Moneyball Nation: Data in American Life', 'duration': '0:50:00', 'start_time': '2016-01-13T09:30:00', 'instructors': [u'Phillips'], 'section': u'1', 'location': u'PH- 125C'}, {'course': u'79305', 'end_time': '2016-01-15T12:20:00', 'title': '79305: Moneyball Nation: Data in American Life', 'duration': '0:50:00', 'start_time': '2016-01-15T11:30:00', 'instructors': [u'Phillips'], 'section': u'B', 'location': u'PH- A20'}, {'course': u'80180', 'end_time': '2016-01-11T13:20:00', 'title': '80180: Nature of Language', 'duration': '0:50:00', 'start_time': '2016-01-11T12:30:00', 'instructors': [u'Werner'], 'section': u'1', 'location': u'BH- 136A'}, {'course': u'80180', 'end_time': '2016-01-13T13:20:00', 'title': '80180: Nature of Language', 'duration': '0:50:00', 'start_time': '2016-01-13T12:30:00', 'instructors': [u'Werner'], 'section': u'1', 'location': u'BH- 136A'}, {'course': u'80180', 'end_time': '2016-01-15T15:20:00', 'title': '80180: Nature of Language', 'duration': '0:50:00', 'start_time': '2016-01-15T14:30:00', 'instructors': [u'Werner'], 'section': u'F', 'location': u'WEH- 5310'}]

# my_data = get_courses("rishubj", "password")

def freetime(users, my_data):

	freet =  [[[] for j in range(20)] for i in range(7)]

	# datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
	# begin = dateutil.parser.parse("2016-01-11T08:00:00-05:00")

	for name in users:
		for day in range(7):
			begin = datetime(2016,1,10+day,8,0)
			endtime = datetime(2016,1,10+day,8,30)
			for hour in range(20):
				time_avail = True
				for my_event in my_data:
					start = dateutil.parser.parse(my_event["start_time"])
					end = dateutil.parser.parse(my_event["end_time"])
					if (start<=begin and begin<end) or (start<endtime and endtime<=end):
						time_avail=False
						break
				if time_avail:
					ufree=True
					for event in users[name]:
						start = dateutil.parser.parse(event["start_time"])
						end = dateutil.parser.parse(event["end_time"])
						if (start<=begin and begin<end) or (start<endtime and endtime<=end):
							ufree=False
							break
					if ufree:
						freet[day][hour].append(name)

				begin += timedelta(minutes=30)
				endtime += timedelta(minutes=30)
	return freet


print freetime(users, my_data)