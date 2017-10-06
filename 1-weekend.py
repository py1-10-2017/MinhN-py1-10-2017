# 1. basic python
# 	functions
#	
# 2. github 
# 3. flask
# 4. virtualenv

# students = [#array/list
#      {'first_name':  'Michael', 'last_name' : 'Jordan'}, #object/dictionary
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for i in range(0, len(students)): #for(var i = 0 ; i < students.length; i++)
# 	# print i
# 	# print students[i]
# 	print "{} {}".format(students[i]["first_name"], students[i]["last_name"])

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}


# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13
for group in users:
	print group
	print users[group]
	group_of_users = users[group]
	for i in range(0, len(group_of_users)):
		# print i
		full_name = group_of_users[i]["first_name"] + group_of_users[i]["last_name"]
		print "{} - {} {} - {}".format(i+1, group_of_users[i]["first_name"], group_of_users[i]["last_name"], len(full_name))



