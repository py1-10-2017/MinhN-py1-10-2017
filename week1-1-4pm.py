# Intro Python -> closer to the metal, a more strict than javascript
# Numbers
# Data types
	# Booleans
# print type(False)
# print type(True)

# 	Doubles, Ints, Strings
# print type(5.5)
# print type(5)
# print (5.0 == "5")
# name = "Travis"
# name += "10"
# print name[0]
# name[0] = "z"
# print "jldsa;fkdsawerasdfs" + str(5)
# 	Objects
# 		Dictionaries, Lists, Tuples
tree = {
	"trunk_color":"brown",
	"number_of_leaves": 300,
	"height":50
}
# print dir(tree)
# print tree.keys()
# if "type" in tree.keys():
# 	print tree["type"]
favorite_numbers = [5,7,3,2,3,4,6,4,3,2,7,9,0,7,6,6,4,3]
my_tuple = ("Minh", "Nguyen", "glasses", "asian", "blue")
print my_tuple[0]
(favorite_numbers[0], favorite_numbers[1]) = (favorite_numbers[1], favorite_numbers[0])
print favorite_numbers
# favorite_numbers[1] = 15
# # print favorite_numbers
# # range(start, end, increment)
# for key in tree:
# 	print tree[key]
# 	# favorite_numbers[i] = 20
# 	# number = 20
# # print favorite_numbers
# # print tree["type"]
# # Control/Code Flow
# if "true" == "true":
# 	print "true"
# 	print "asdfasd"
# else:
# 	print "not true"