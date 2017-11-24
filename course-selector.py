# Author: Jonathan Zwiebel
# Version: 24 November 2017

day_ids = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}

class Course:
	def __init__(self, code, name, units, instructor, times, intensity):
		self.code = code
		self.name = name
		self.units = units
		self.instructor = instructor
		self.times = times
		self.intensity = intensity

	def __repr__(self):
		return self.code + " - " + self.name + " | " + str(self.units) + " units | " + self.instructor + " | Meets " + " | " + str(self.intensity) + " hrs/week"

class Times:
	# Times must be in comma separated format of DAY HOUR-HOUR with hours in military time
	def __init__(self, times):
		individual_times = times.split(", ")
		self.times_tuples = []
		for individual_time in individual_times:
			day,hours = individual_time.split(" ")
			start_hour,end_hour = hours.split("-")
			start_time = day_ids[day] * 1440 + int(start_hour[0:2]) * 60 + int(start_hour[2:4])
			end_time = day_ids[day] * 1440 + int(end_hour[0:2]) * 60 + int(end_hour[2:4])
			self.times_tuples.append((start_time, end_time))

	def __repr__(self):
		return str(self.times_tuples)

def check_overlap(time1, time2):
	for time_tuple_outer in time1.times_tuples:
		for time_tuple_inner in time2.times_tuples:
			if time_tuple_inner[0] > time_tuple_outer[0] and time_tuple_inner[0] < time_tuple_outer[1]:
				return True
			if time_tuple_inner[1] > time_tuple_outer[0] and time_tuple_inner[1] < time_tuple_outer[1]:
				return True
	return False


def get_possible_courseloads(courses):
	current_courseloads = []
	current_courses = []
	get_possible_courseloads_recursive(courses, current_courses, current_courseloads)
	return current_courseloads

def get_possible_courseloads_recursive(courses_left, current_courses, current_courseloads):
	if len(courses_left) == 0:
		course_ids = []
		for course in current_courses:
			course_ids.append(course.code)
		# TODO: Static constraings
		current_courseloads.append(course_ids)
	else:
		# TODO: Live constraints
		first_course = courses_left[0]
		new_courses_left = courses_left[1:]
		get_possible_courseloads_recursive(new_courses_left, current_courses, current_courseloads)
		current_courses.append(first_course)
		get_possible_courseloads_recursive(new_courses_left, current_courses, current_courseloads)
		current_courses.pop(len(current_courses) - 1)



_CS107E = Course("CS 107E", "Computer Systems from the Ground Up", 5, "Pat Hanrahan", Times("Mon 1130-1250, Fri 1130-1250"), 17.5)
_CS103 = Course("CS 103", "Mathematical Foundations of Computing", 5, "Keith Schwarz", Times("Mon 1500-1620, Wed 1500-1620, Fri 1500-1620"), 12.5)
_HISTORY101 = Course("HISTORY 101", "The Greeks", 5, "Ian Morris", Times("Mon 1130-1220, Wed 1130-1220"), 7.5)

courses = []
courses.append(_CS107E)
courses.append(_CS103)
courses.append(_HISTORY101)
print(courses)

print(get_possible_courseloads(courses)) 