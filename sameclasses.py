from cmu_auth import authenticate
import base64, ics
from courses import *
import dateutil.parser
from dining import *

# dictionary of all user's jsons
users = {'Rishub': {
'courses': {
  '36217': {
    'name': 'Probability Theory and Random Processes',
    'department': 'Statistics',
    'prereqs': '21-112 or 21-122 or 21-123 or 21-256 or 21-259',
    'units': 9.0,
    'lectures': [{
      'sections': [],
      'meetings': [{
        'end': '04:20PM',
        'begin': '03:00PM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'PH 100',
        'days': 'TR'
      }],
      'instructors': ["O'Connell"],
      'lecture': 'A'
    }, {
      'sections': [],
      'meetings': [{
        'end': '09:20AM',
        'begin': '08:30AM',
        'location': 'Doha, Qatar',
        'room': 'CMB 2052',
        'days': 'UTR'
      }],
      'instructors': ['Yilma'],
      'lecture': 'W'
    }],
    'semester': ['F', 'S', 'M'],
    'desc': 'This course provides an introduction to probability theory. It is designed for students in electrical and computer engineering. Topics include elementary probability theory, conditional probability and independence, random variables, distribution functions, joint and conditional distributions, limit theorems, and an introduction to random processes. Some elementary ideas in spectral analysis and information theory will be given. A grade of C or better is required in order to use this course as a pre-requisite for 36-226 and 36-410. Not open to students who have received credit for 36-225, or 36-625. Course Website: http://www.stat.cmu.edu/academics/courselist',
    'coreqs': ''
  },
  '79305': {
    'name': 'Moneyball Nation: Data in American Life',
    'department': 'History',
    'prereqs': '',
    'units': 9.0,
    'lectures': [{
      'sections': [{
        'section': 'A',
        'meetings': [{
          'end': '10:20AM',
          'begin': '09:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'PH A22',
          'days': 'F'
        }],
        'instructors': ['Phillips']
      }, {
        'section': 'B',
        'meetings': [{
          'end': '12:20PM',
          'begin': '11:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'PH A20',
          'days': 'F'
        }],
        'instructors': ['Phillips']
      }],
      'meetings': [{
        'end': '10:20AM',
        'begin': '09:30AM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'PH 125C',
        'days': 'MW'
      }],
      'instructors': ['Phillips'],
      'lecture': 'Lec'
    }],
    'semester': [],
    'desc': "From conducting clinical trials and evaluating prisoners parole cases to drafting professional ballplayers, we increasingly make decisions using mathematical concepts and models. This course surveys the development of-and resistance to-such tools by grounding them in the recent cultural history of the United States. Focusing on baseball, medicine, and the law, we'll explore how and why Americans have come to believe mathematical and computational methods can solve complicated problems, even in seemingly unrelated moral, political, and social domains. The course encourages students to think critically about the wider implications of these transformations by situating their development historically.",
    'coreqs': ''
  },
  '15150': {
    'name': 'Principles of Functional Programming',
    'department': 'Computer Science',
    'prereqs': '(15-151 or 21-127) and 15-112',
    'units': 10.0,
    'lectures': [{
      'sections': [{
        'section': 'A',
        'meetings': [{
          'end': '10:20AM',
          'begin': '09:00AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5210',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'B',
        'meetings': [{
          'end': '10:20AM',
          'begin': '09:00AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5208',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'C',
        'meetings': [{
          'end': '11:50AM',
          'begin': '10:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5210',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'D',
        'meetings': [{
          'end': '11:50AM',
          'begin': '10:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5208',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'E',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:00PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5210',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'F',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:00PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5208',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'G',
        'meetings': [{
          'end': '02:50PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5210',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'H',
        'meetings': [{
          'end': '02:50PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5208',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'I',
        'meetings': [{
          'end': '04:20PM',
          'begin': '03:00PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5210',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'J',
        'meetings': [{
          'end': '04:20PM',
          'begin': '03:00PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5208',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'K',
        'meetings': [{
          'end': '10:20AM',
          'begin': '09:00AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5207',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'L',
        'meetings': [{
          'end': '11:50AM',
          'begin': '10:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5207',
          'days': 'W'
        }],
        'instructors': ['Instructor TBA']
      }],
      'meetings': [{
        'end': '01:20PM',
        'begin': '12:00PM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'DH 2315',
        'days': 'TR'
      }],
      'instructors': ['Erdmann'],
      'lecture': 'Lec'
    }],
    'semester': ['F', 'S'],
    'desc': 'An introduction to programming based on a "functional" model of computation. The functional model is a natural generalization of algebra in which programs are formulas that describe the output of a computation in terms of its inputs—-that is, as a function. But instead of being confined to real- or complex-valued functions, the functional model extends the algebraic view to a very rich class of data types, including not only aggregates built up from other types, but also functions themselves as values. This course is an introduction to programming that is focused on the central concepts of function and type. One major theme is the interplay between inductive types, which are built up incrementally; recursive functions, which compute over inductive types by decomposition; and proof by structural induction, which is used to prove the correctness and time complexity of a recursive function. Another major theme is the role of types in structuring large programs into separate modules, and the integration of imperative programming through the introduction of data types whose values may be altered during computation. NOTE: students must achieve a C or better in order to use this course to satisfy the pre-requisite for any subsequent Computer Science course.',
    'coreqs': ''
  },
  '79104': {
    'name': 'Global Histories',
    'department': 'History',
    'prereqs': '',
    'units': 9.0,
    'lectures': [{
      'sections': [],
      'meetings': [{
        'end': '01:20PM',
        'begin': '12:30PM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'PH 100',
        'days': 'MW'
      }],
      'instructors': ['Law'],
      'lecture': 'Lec 1'
    }, {
      'sections': [],
      'meetings': [{
        'end': '02:20PM',
        'begin': '01:30PM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'PH 100',
        'days': 'MW'
      }],
      'instructors': ['Law'],
      'lecture': 'Lec 2'
    }, {
      'sections': [{
        'section': 'A',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 5409',
          'days': 'F'
        }],
        'instructors': ['Liu']
      }, {
        'section': 'B',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'DH 2122',
          'days': 'F'
        }],
        'instructors': ['Oren']
      }, {
        'section': 'C',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 6423',
          'days': 'F'
        }],
        'instructors': ['Busch']
      }, {
        'section': 'D',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 4623',
          'days': 'F'
        }],
        'instructors': ['Grant']
      }, {
        'section': 'E',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 4301',
          'days': 'F'
        }],
        'instructors': ['Soeder']
      }, {
        'section': 'G',
        'meetings': [{
          'end': '10:20AM',
          'begin': '09:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'BH 235A',
          'days': 'F'
        }],
        'instructors': ['Liu']
      }, {
        'section': 'H',
        'meetings': [{
          'end': '11:20AM',
          'begin': '10:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'PH A20',
          'days': 'F'
        }],
        'instructors': ['Grant']
      }, {
        'section': 'I',
        'meetings': [{
          'end': '12:20PM',
          'begin': '11:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'DH 2122',
          'days': 'F'
        }],
        'instructors': ['Oren']
      }, {
        'section': 'J',
        'meetings': [{
          'end': '12:20PM',
          'begin': '11:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 5316',
          'days': 'F'
        }],
        'instructors': ['Busch']
      }, {
        'section': 'L',
        'meetings': [{
          'end': '02:20PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 5310',
          'days': 'F'
        }],
        'instructors': ['McGrath']
      }, {
        'section': 'M',
        'meetings': [{
          'end': '02:20PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'DH 1209',
          'days': 'F'
        }],
        'instructors': ['Stepp']
      }, {
        'section': 'N',
        'meetings': [{
          'end': '02:20PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'BH 235A',
          'days': 'F'
        }],
        'instructors': ['Bradshaw']
      }, {
        'section': 'O',
        'meetings': [{
          'end': '02:20PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'DH 1117',
          'days': 'F'
        }],
        'instructors': ['Kittner']
      }, {
        'section': 'R',
        'meetings': [{
          'end': '11:20AM',
          'begin': '10:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 5310',
          'days': 'F'
        }],
        'instructors': ['Stepp']
      }, {
        'section': 'S',
        'meetings': [{
          'end': '12:20PM',
          'begin': '11:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'BH 235A',
          'days': 'F'
        }],
        'instructors': ['Kittner']
      }, {
        'section': 'T',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 4211',
          'days': 'F'
        }],
        'instructors': ['McGrath']
      }, {
        'section': 'U',
        'meetings': [{
          'end': '02:20PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'BH 235B',
          'days': 'F'
        }],
        'instructors': ['Roszman']
      }, {
        'section': 'W',
        'meetings': [{
          'end': '02:20PM',
          'begin': '01:30PM',
          'location': 'Doha, Qatar',
          'room': 'CMB 1190',
          'days': 'UTR'
        }],
        'instructors': ['Reilly']
      }],
      'meetings': [{
        'end': '02:20PM',
        'begin': '01:30PM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'BH 235B',
        'days': 'MW'
      }],
      'instructors': ['Roszman'],
      'lecture': 'Lec 3'
    }],
    'semester': ['F', 'S'],
    'desc': 'Human activity transcends political, geographical, and cultural boundaries. From wars to social movements, technological innovations to environmental changes, our world has long been an interconnected one. Acquiring the ability to understand such transnational and even worldwide processes is an indispensable part of any college education. This course provides students with an opportunity to develop the skills and perspectives needed to understand the contemporary world through investigating its global history. A variety of sections are offered in order to give students the opportunity to choose between different themes and approaches. All sections are comparable in their composition of lectures and recitations, required amounts of reading, and emphasis on written assignments as the central medium of assessment. The sections all aim to help students: (1) master knowledge through interaction with the instructors, reading material, and other students, (2) think critically about the context and purpose of any given information, (3) craft effective verbal and written arguments by combining evidence, logic, and creativity, and (4) appreciate the relevance of the past in the present and future. For descriptions of specific sections, see "First Year Experience" at the Dietrich College General Education Website: http://www.hss.cmu.edu/gened/.',
    'coreqs': ''
  },
  '15251': {
    'name': 'Great Theoretical Ideas in Computer Science',
    'department': 'Computer Science',
    'prereqs': '15-112 and (15-151 or 21-127)',
    'units': 12.0,
    'lectures': [{
      'sections': [{
        'section': 'A',
        'meetings': [{
          'end': '10:20AM',
          'begin': '09:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'DH 1209',
          'days': 'F'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'B',
        'meetings': [{
          'end': '11:20AM',
          'begin': '10:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 4211',
          'days': 'F'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'C',
        'meetings': [{
          'end': '12:20PM',
          'begin': '11:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'DH 1217',
          'days': 'F'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'D',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 4102',
          'days': 'F'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'E',
        'meetings': [{
          'end': '02:20PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'DH 1217',
          'days': 'F'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'F',
        'meetings': [{
          'end': '03:20PM',
          'begin': '02:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 5222',
          'days': 'F'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'G',
        'meetings': [{
          'end': '04:20PM',
          'begin': '03:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'DH 1217',
          'days': 'F'
        }],
        'instructors': ['Instructor TBA']
      }, {
        'section': 'W',
        'meetings': [{
          'end': '11:50AM',
          'begin': '10:30AM',
          'location': 'Doha, Qatar',
          'room': 'CMB 2147',
          'days': 'MW'
        }, {
          'end': '11:20AM',
          'begin': '10:30AM',
          'location': 'Doha, Qatar',
          'room': 'CMB 2147',
          'days': 'UTR'
        }],
        'instructors': ['Kapoutsis']
      }],
      'meetings': [{
        'end': '10:20AM',
        'begin': '09:00AM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'GHC 4401',
        'days': 'TR'
      }, {
        'end': '07:50PM',
        'begin': '06:30PM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'DH 2210',
        'days': 'W'
      }],
      'instructors': ["O'Donnell", 'Haeupler'],
      'lecture': 'Lec'
    }],
    'semester': ['F', 'S'],
    'desc': 'This course is about how to use theoretical ideas to formulate and solve problems in computer science. It integrates mathematical material with general problem solving techniques and computer science applications. Examples are drawn from algorithms, complexity theory, game theory, probability theory, graph theory, automata theory, algebra, cryptography, and combinatorics. Assignments involve both mathematical proofs and programming. NOTE: students must achieve a C or better in order to use this course to satisfy the pre-requisite for any subsequent Computer Science course. Course Website: http://www.cs.cmu.edu/~15251',
    'coreqs': ''
  },
  '80180': {
    'name': 'Nature of Language',
    'department': 'Philosophy',
    'prereqs': '',
    'units': 9.0,
    'lectures': [{
      'sections': [{
        'section': 'A',
        'meetings': [{
          'end': '12:20PM',
          'begin': '11:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'GHC 4215',
          'days': 'F'
        }],
        'instructors': ['Werner']
      }, {
        'section': 'B',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'PH 126A',
          'days': 'F'
        }],
        'instructors': ['Werner']
      }, {
        'section': 'C',
        'meetings': [{
          'end': '12:20PM',
          'begin': '11:30AM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 5328',
          'days': 'F'
        }],
        'instructors': ['Werner']
      }, {
        'section': 'D',
        'meetings': [{
          'end': '01:20PM',
          'begin': '12:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 5328',
          'days': 'F'
        }],
        'instructors': ['Werner']
      }, {
        'section': 'E',
        'meetings': [{
          'end': '02:20PM',
          'begin': '01:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 5302',
          'days': 'F'
        }],
        'instructors': ['Werner']
      }, {
        'section': 'F',
        'meetings': [{
          'end': '03:20PM',
          'begin': '02:30PM',
          'location': 'Pittsburgh, Pennsylvania',
          'room': 'WEH 5310',
          'days': 'F'
        }],
        'instructors': ['Werner']
      }],
      'meetings': [{
        'end': '01:20PM',
        'begin': '12:30PM',
        'location': 'Pittsburgh, Pennsylvania',
        'room': 'BH 136A',
        'days': 'MW'
      }],
      'instructors': ['Werner'],
      'lecture': 'Lec'
    }],
    'semester': ['F', 'S'],
    'desc': 'Language is used to talk about the world or to describe it, but how do we go about describing language itself? Linguistics is the name given to the science of language, whose task it is to give such a description. The discipline of linguistics has developed novel tools for describing and analyzing language over the last two hundred years and in this course we learn what these tools are and practice applying them. Sub-areas of linguistics which we study include phonetics (the study of speech sounds), phonology (the study of sound systems), morphology (the study of parts of words), and syntax (the study of combinations of words). Beyond this, we look at changes in language over time, and we consider the puzzle of linguistic meaning. The methods of linguistics are useful in the study of particular languages and in the study of language generally, so this course is useful for students of foreign languages as well as those interested in going on to study language acquisition, psycholinguistics, sociolinguistics, philosophy of language, and computer modeling of language.',
    'coreqs': ''
  }
},
'schedule': [
{
  'end': '2016-01-12T13:20:00',
  'location': 'DH- 2315',
  'duration': '1:20:00',
  'section': '1',
  'start': '2016-01-12T12:00:00',
  'title': '15150: Principles of Functional Programming',
  'instructors': ['Erdmann'],
  'course': '15150'
}, {
  'end': '2016-01-14T13:20:00',
  'location': 'DH- 2315',
  'duration': '1:20:00',
  'section': '1',
  'start': '2016-01-14T12:00:00',
  'title': '15150: Principles of Functional Programming',
  'instructors': ['Erdmann'],
  'course': '15150'
}, {
  'end': '2016-01-13T11:50:00',
  'location': 'GHC- 5208',
  'duration': '1:20:00',
  'section': 'D',
  'start': '2016-01-13T10:30:00',
  'title': '15150: Principles of Functional Programming',
  'instructors': ['TBA'],
  'course': '15150'
}, {
  'end': '2016-01-12T10:20:00',
  'location': 'GHC- 4401',
  'duration': '1:20:00',
  'section': '1',
  'start': '2016-01-12T09:00:00',
  'title': '15251: Great Theoretical Ideas in Computer Science',
  'instructors': ['Haeupler', "O'Donnell"],
  'course': '15251'
}, {
  'end': '2016-01-14T10:20:00',
  'location': 'GHC- 4401',
  'duration': '1:20:00',
  'section': '1',
  'start': '2016-01-14T09:00:00',
  'title': '15251: Great Theoretical Ideas in Computer Science',
  'instructors': ['Haeupler', "O'Donnell"],
  'course': '15251'
}, {
  'end': '2016-01-13T19:50:00',
  'location': 'DH- 2210',
  'duration': '1:20:00',
  'section': '1',
  'start': '2016-01-13T18:30:00',
  'title': '15251: Great Theoretical Ideas in Computer Science',
  'instructors': ['Haeupler', "O'Donnell"],
  'course': '15251'
}, {
  'end': '2016-01-15T14:20:00',
  'location': 'DH- 1217',
  'duration': '0:50:00',
  'section': 'E',
  'start': '2016-01-15T13:30:00',
  'title': '15251: Great Theoretical Ideas in Computer Science',
  'instructors': ['TBA'],
  'course': '15251'
}, {
  'end': '2016-01-12T16:20:00',
  'location': 'PH- 100',
  'duration': '1:20:00',
  'section': 'A',
  'start': '2016-01-12T15:00:00',
  'title': '36217: Probability Theory and Random Processes',
  'instructors': ["O'Connell"],
  'course': '36217'
}, {
  'end': '2016-01-14T16:20:00',
  'location': 'PH- 100',
  'duration': '1:20:00',
  'section': 'A',
  'start': '2016-01-14T15:00:00',
  'title': '36217: Probability Theory and Random Processes',
  'instructors': ["O'Connell"],
  'course': '36217'
}, {
  'end': '2016-01-11T14:20:00',
  'location': 'PH- 100',
  'duration': '0:50:00',
  'section': '2',
  'start': '2016-01-11T13:30:00',
  'title': '79104: The Modern Nation-state through Film',
  'instructors': ['Law'],
  'course': '79104'
}, {
  'end': '2016-01-13T14:20:00',
  'location': 'PH- 100',
  'duration': '0:50:00',
  'section': '2',
  'start': '2016-01-13T13:30:00',
  'title': '79104: The Modern Nation-state through Film',
  'instructors': ['Law'],
  'course': '79104'
}, {
  'end': '2016-01-15T13:20:00',
  'location': 'GHC- 4211',
  'duration': '0:50:00',
  'section': 'T',
  'start': '2016-01-15T12:30:00',
  'title': '79104: Global Histories',
  'instructors': ['McGrath'],
  'course': '79104'
}, {
  'end': '2016-01-11T10:20:00',
  'location': 'PH- 125C',
  'duration': '0:50:00',
  'section': '1',
  'start': '2016-01-11T09:30:00',
  'title': '79305: Moneyball Nation: Data in American Life',
  'instructors': ['Phillips'],
  'course': '79305'
}, {
  'end': '2016-01-13T10:20:00',
  'location': 'PH- 125C',
  'duration': '0:50:00',
  'section': '1',
  'start': '2016-01-13T09:30:00',
  'title': '79305: Moneyball Nation: Data in American Life',
  'instructors': ['Phillips'],
  'course': '79305'
}, {
  'end': '2016-01-15T12:20:00',
  'location': 'PH- A20',
  'duration': '0:50:00',
  'section': 'B',
  'start': '2016-01-15T11:30:00',
  'title': '79305: Moneyball Nation: Data in American Life',
  'instructors': ['Phillips'],
  'course': '79305'
}, {
  'end': '2016-01-11T13:20:00',
  'location': 'BH- 136A',
  'duration': '0:50:00',
  'section': '1',
  'start': '2016-01-11T12:30:00',
  'title': '80180: Nature of Language',
  'instructors': ['Werner'],
  'course': '80180'
}, {
  'end': '2016-01-13T13:20:00',
  'location': 'BH- 136A',
  'duration': '0:50:00',
  'section': '1',
  'start': '2016-01-13T12:30:00',
  'title': '80180: Nature of Language',
  'instructors': ['Werner'],
  'course': '80180'
}, {
  'end': '2016-01-15T15:20:00',
  'location': 'WEH- 5310',
  'duration': '0:50:00',
  'section': 'F',
  'start': '2016-01-15T14:30:00',
  'title': '80180: Nature of Language',
  'instructors': ['Werner'],
  'course': '80180'
}]
}
}

# the one user's json, which you are comparing. This is taken from Varuns's data.
my_data = { "courses": { "15251": { "coreqs": "", "department": "Computer Science", "units": 12.0, "desc": "This course is about how to use theoretical ideas to formulate and solve problems in computer science. It integrates mathematical material with general problem solving techniques and computer science applications. Examples are drawn from algorithms, complexity theory, game theory, probability theory, graph theory, automata theory, algebra, cryptography, and combinatorics. Assignments involve both mathematical proofs and programming. NOTE: students must achieve a C or better in order to use this course to satisfy the pre-requisite for any subsequent Computer Science course. Course Website: http://www.cs.cmu.edu/~15251", "name": "Great Theoretical Ideas in Computer Science", "semester": [ "F", "S" ], "lectures": [ { "instructors": [ "O'Donnell", "Haeupler" ], "lecture": "Lec", "sections": [ { "instructors": [ "Instructor TBA" ], "section": "A", "meetings": [ { "room": "DH 1209", "end": "10:20AM", "location": "Pittsburgh, Pennsylvania", "begin": "09:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "B", "meetings": [ { "room": "GHC 4211", "end": "11:20AM", "location": "Pittsburgh, Pennsylvania", "begin": "10:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "C", "meetings": [ { "room": "DH 1217", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "D", "meetings": [ { "room": "GHC 4102", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "E", "meetings": [ { "room": "DH 1217", "end": "02:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "01:30PM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "F", "meetings": [ { "room": "GHC 5222", "end": "03:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "02:30PM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "G", "meetings": [ { "room": "DH 1217", "end": "04:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "03:30PM", "days": "F" } ] }, { "instructors": [ "Kapoutsis" ], "section": "W", "meetings": [ { "room": "CMB 2147", "end": "11:50AM", "location": "Doha, Qatar", "begin": "10:30AM", "days": "MW" }, { "room": "CMB 2147", "end": "11:20AM", "location": "Doha, Qatar", "begin": "10:30AM", "days": "UTR" } ] } ], "meetings": [ { "room": "GHC 4401", "end": "10:20AM", "location": "Pittsburgh, Pennsylvania", "begin": "09:00AM", "days": "TR" }, { "room": "DH 2210", "end": "07:50PM", "location": "Pittsburgh, Pennsylvania", "begin": "06:30PM", "days": "W" } ] } ], "prereqs": "15-112 and (15-151 or 21-127)" }, "73100": { "coreqs": "", "department": "Economics", "units": 9.0, "desc": "Literally, an introduction to economic principles, the goal of this course is to give students an understanding as to what constitutes good \"economic thinking\". This thought process is grounded in the construction and use of economics models. Drawing on issues in both microeconomics and macroeconomics, fundamental principles are shown to transcend particular examples and allow the field to be seen as a coherent, unified whole. (Lecture, 2 hours; Recitation, 1 hour). Course Website: http://tepper.cmu.edu/prospective-students/course-page/73100/principles-of-economics", "name": "Principles of Economics", "semester": [ "F", "S" ], "lectures": [ { "instructors": [ "Kushnir", "Sleet" ], "lecture": "Lec 1", "sections": [], "meetings": [ { "room": "DH 2315", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "MW" } ] }, { "instructors": [ "Sleet", "Kushnir" ], "lecture": "Lec 2", "sections": [ { "instructors": [ "Instructor TBA" ], "section": "A", "meetings": [ { "room": "PH 100", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "B", "meetings": [ { "room": "PH 226C", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "C", "meetings": [ { "room": "HH B103", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "D", "meetings": [ { "room": "GHC 5222", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "E", "meetings": [ { "room": "PH A18C", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "F", "meetings": [ { "room": "PH A19", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "H", "meetings": [ { "room": "CFA 102", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "I", "meetings": [ { "room": "HH B103", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "J", "meetings": [ { "room": "PH A19", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "K", "meetings": [ { "room": "DH 1112", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "L", "meetings": [ { "room": "PH 125C", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] }, { "instructors": [ "Instructor TBA" ], "section": "M", "meetings": [ { "room": "WEH 5415", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] } ], "meetings": [ { "room": "DH 2315", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "MW" } ] } ], "prereqs": "" }, "80180": { "coreqs": "", "department": "Philosophy", "units": 9.0, "desc": "Language is used to talk about the world or to describe it, but how do we go about describing language itself? Linguistics is the name given to the science of language, whose task it is to give such a description. The discipline of linguistics has developed novel tools for describing and analyzing language over the last two hundred years and in this course we learn what these tools are and practice applying them. Sub-areas of linguistics which we study include phonetics (the study of speech sounds), phonology (the study of sound systems), morphology (the study of parts of words), and syntax (the study of combinations of words). Beyond this, we look at changes in language over time, and we consider the puzzle of linguistic meaning. The methods of linguistics are useful in the study of particular languages and in the study of language generally, so this course is useful for students of foreign languages as well as those interested in going on to study language acquisition, psycholinguistics, sociolinguistics, philosophy of language, and computer modeling of language.", "name": "Nature of Language", "semester": [ "F", "S" ], "lectures": [ { "instructors": [ "Werner" ], "lecture": "Lec", "sections": [ { "instructors": [ "Werner" ], "section": "A", "meetings": [ { "room": "GHC 4215", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Werner" ], "section": "B", "meetings": [ { "room": "PH 126A", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] }, { "instructors": [ "Werner" ], "section": "C", "meetings": [ { "room": "WEH 5328", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "F" } ] }, { "instructors": [ "Werner" ], "section": "D", "meetings": [ { "room": "WEH 5328", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "F" } ] }, { "instructors": [ "Werner" ], "section": "E", "meetings": [ { "room": "WEH 5302", "end": "02:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "01:30PM", "days": "F" } ] }, { "instructors": [ "Werner" ], "section": "F", "meetings": [ { "room": "WEH 5310", "end": "03:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "02:30PM", "days": "F" } ] } ], "meetings": [ { "room": "BH 136A", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "MW" } ] } ], "prereqs": "" }, "85241": { "coreqs": "", "department": "Psychology", "units": 9.0, "desc": "The focus of this course will be on how peoples behavior, feelings and thoughts are influenced or determined by their social environment. The course will begin with lectures and readings on how social psychologists go about studying social behavior. Next, various topics on which social psychologists have done research will be covered. These topics will include: person perception, prejudice and discrimination, the nature of attitudes and how attitudes are formed and changed, interpersonal attraction, conformity, compliance, altruism, aggression, group behavior, and applications of psychology to problems in health care, law, politics, and the environment. Through readings and lectures on these topics, students will also be exposed to social psychological theories.", "name": "Social Psychology", "semester": [ "F", "S" ], "lectures": [ { "instructors": [ "Boyd" ], "lecture": "A", "sections": [], "meetings": [ { "room": "PH 100", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:00PM", "days": "TR" } ] }, { "instructors": [ "Helgeson" ], "lecture": "B", "sections": [], "meetings": [ { "room": "BH A51", "end": "02:50PM", "location": "Pittsburgh, Pennsylvania", "begin": "01:30PM", "days": "TR" } ] } ], "prereqs": "" }, "15214": { "coreqs": "", "department": "Computer Science", "units": 12.0, "desc": "Software engineers today are less likely to design data structures and algorithms from scratch and more likely to build systems from library and framework components. In this course, students engage with concepts related to the construction of software systems at scale, building on their understanding of the basic building blocks of data structures, algorithms, program structures, and computer structures. The course covers technical topics in four areas: (1) concepts of design for complex systems, (2) object oriented programming, (3) static and dynamic analysis for programs, and (4) concurrent and distributed software. Student assignments involve engagement with complex software such as distributed massively multi-player game systems and frameworks for graphical user interaction.", "name": "Principles of Software Construction: Objects, Design, and Concurrency", "semester": [ "F", "S" ], "lectures": [ { "instructors": [ "Garrod", "Bloch" ], "lecture": "Lec", "sections": [ { "instructors": [ "Garrod" ], "section": "A", "meetings": [ { "room": "WEH 5310", "end": "10:20AM", "location": "Pittsburgh, Pennsylvania", "begin": "09:30AM", "days": "W" } ] }, { "instructors": [ "Garrod" ], "section": "B", "meetings": [ { "room": "GHC 4101", "end": "11:20AM", "location": "Pittsburgh, Pennsylvania", "begin": "10:30AM", "days": "W" } ] }, { "instructors": [ "Garrod" ], "section": "C", "meetings": [ { "room": "WEH 5310", "end": "12:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "11:30AM", "days": "W" } ] }, { "instructors": [ "Garrod" ], "section": "D", "meetings": [ { "room": "WEH 5310", "end": "01:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "12:30PM", "days": "W" } ] }, { "instructors": [ "Garrod" ], "section": "E", "meetings": [ { "room": "WEH 5310", "end": "02:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "01:30PM", "days": "W" } ] } ], "meetings": [ { "room": "WEH 7500", "end": "04:20PM", "location": "Pittsburgh, Pennsylvania", "begin": "03:00PM", "days": "TR" } ] } ], "prereqs": "(15-121 or 15-122) and (15-151 or 21-127)" } }, "schedule": [ { "instructors": [ "Bloch", "Garrod" ], "end": "2016-01-12T16:20:00", "duration": "1:20:00", "location": "WEH- 7500", "title": "15214: Principles of Software Construction: Objects, Design, and Concurrency", "course": "15214", "section": "1", "start": "2016-01-12T15:00:00" }, { "instructors": [ "Bloch", "Garrod" ], "end": "2016-01-14T16:20:00", "duration": "1:20:00", "location": "WEH- 7500", "title": "15214: Principles of Software Construction: Objects, Design, and Concurrency", "course": "15214", "section": "1", "start": "2016-01-14T15:00:00" }, { "instructors": [ "Garrod" ], "end": "2016-01-13T11:20:00", "duration": "0:50:00", "location": "GHC- 4101", "title": "15214: Principles of Software Construction: Objects, Design, and Concurrency", "course": "15214", "section": "B", "start": "2016-01-13T10:30:00" }, { "instructors": [ "Haeupler", "O'Donnell" ], "end": "2016-01-12T10:20:00", "duration": "1:20:00", "location": "GHC- 4401", "title": "15251: Great Theoretical Ideas in Computer Science", "course": "15251", "section": "1", "start": "2016-01-12T09:00:00" }, { "instructors": [ "Haeupler", "O'Donnell" ], "end": "2016-01-14T10:20:00", "duration": "1:20:00", "location": "GHC- 4401", "title": "15251: Great Theoretical Ideas in Computer Science", "course": "15251", "section": "1", "start": "2016-01-14T09:00:00" }, { "instructors": [ "Haeupler", "O'Donnell" ], "end": "2016-01-13T19:50:00", "duration": "1:20:00", "location": "DH- 2210", "title": "15251: Great Theoretical Ideas in Computer Science", "course": "15251", "section": "1", "start": "2016-01-13T18:30:00" }, { "instructors": [ "TBA" ], "end": "2016-01-15T11:20:00", "duration": "0:50:00", "location": "GHC- 4211", "title": "15251: Great Theoretical Ideas in Computer Science", "course": "15251", "section": "B", "start": "2016-01-15T10:30:00" }, { "instructors": [ "Kushnir", "Sleet" ], "end": "2016-01-11T12:20:00", "duration": "0:50:00", "location": "DH- 2315", "title": "73100: Principles of Economics", "course": "73100", "section": "1", "start": "2016-01-11T11:30:00" }, { "instructors": [ "Kushnir", "Sleet" ], "end": "2016-01-13T12:20:00", "duration": "0:50:00", "location": "DH- 2315", "title": "73100: Principles of Economics", "course": "73100", "section": "1", "start": "2016-01-13T11:30:00" }, { "instructors": [ "TBA" ], "end": "2016-01-15T12:20:00", "duration": "0:50:00", "location": "PH- A18C", "title": "73100: Principles of Economics", "course": "73100", "section": "E", "start": "2016-01-15T11:30:00" }, { "instructors": [ "Werner" ], "end": "2016-01-11T13:20:00", "duration": "0:50:00", "location": "BH- 136A", "title": "80180: Nature of Language", "course": "80180", "section": "1", "start": "2016-01-11T12:30:00" }, { "instructors": [ "Werner" ], "end": "2016-01-13T13:20:00", "duration": "0:50:00", "location": "BH- 136A", "title": "80180: Nature of Language", "course": "80180", "section": "1", "start": "2016-01-13T12:30:00" }, { "instructors": [ "Werner" ], "end": "2016-01-15T14:20:00", "duration": "0:50:00", "location": "WEH- 5302", "title": "80180: Nature of Language", "course": "80180", "section": "E", "start": "2016-01-15T13:30:00" }, { "instructors": [ "Helgeson" ], "end": "2016-01-12T14:50:00", "duration": "1:20:00", "location": "BH- A51", "title": "85241: Social Psychology", "course": "85241", "section": "B", "start": "2016-01-12T13:30:00" }, { "instructors": [ "Helgeson" ], "end": "2016-01-14T14:50:00", "duration": "1:20:00", "location": "BH- A51", "title": "85241: Social Psychology", "course": "85241", "section": "B", "start": "2016-01-14T13:30:00" } ] }

# my_data = get_courses("rishubj", "password")

def sameclasses(users, my_data):


    # datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
    # begin = dateutil.parser.parse("2016-01-11T08:00:00-05:00")

    for course in my_data["schedule"]:
    	course["friends"] = []
    	for name in users:
    		for ucourse in users[name]["schedule"]:

    			if (course["course"] == ucourse["course"] and course["section"] == ucourse["section"]  and
    				course["start"] == ucourse["start"] and course["end"] == ucourse["end"] ):
    				course["friends"].append(name)
    				break

    with open('static/my_data.json', 'w') as outfile:
      json.dump(my_data, outfile, indent=4)

    return my_data

print (sameclasses(users, my_data))

# print (freetime(users, my_data))