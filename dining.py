import requests
import json

r = requests.get('http://apis.scottylabs.org/dining/v1/locations')

d = r.json()

# 0 is Sunday, 6 is Saturday

def restaurants_available(day, starth, startm, endh, endm):
	rests = []
	for x in d["locations"]:
		for s in x["times"]:

			# TODO: return the intervals for which the restaurants are open
			# This only returns the restaurants open for the entire duration
			if ((s["start"]["day"] ==day and s["end"]["day"] == day and
				(starth>s["start"]["hour"] or (starth==s["start"]["hour"] and startm>=s["start"]["min"])) and
				(endh<s["end"]["hour"] or (endh==s["end"]["hour"] and endm<=s["end"]["min"]))) or

				(s["start"]["day"] < day and s["end"]["day"] ==day and
				(endh<s["end"]["hour"] or (endh==s["end"]["hour"] and endm<=s["end"]["min"]))) or

				(s["start"]["day"] == day and s["end"]["day"] > day and
				(starth>s["start"]["hour"] or (starth==s["start"]["hour"] and startm>=s["start"]["min"]))) or

				(s["start"]["day"] < day and s["end"]["day"] > day)):
				# rests.append(x["name"].endcode('utf-8'))
				rests.append(x["name"].encode('utf8').decode('utf8'))
	s = list(set(rests))
	print(s)
	return s

restaurants_available(5,20,1,21,2)