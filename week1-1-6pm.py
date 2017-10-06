# print type(5)
# print type(5.5) 
# print ("5.0" == 5) # Type and value not equal
# print "sadf;kawerjasdfasd	"
name = "cassie"
# print name[0] # can access just like array
# name[0] = "x" #cant do this
name += "34" # name = name + "34"
# print name
# name += 34 #cant do this
danny = {
	"first_name":"danny",
	"last_name":"hua",
	"hair_color":"black",
	"height": 6,
	"head_shot": "google.com/dannyhuaheadshot",
	"favorite_numbers": [1,4,6,7]
}
# print danny["hair_color"]
# print danny["favorite_numbers"]
# danny["favorite_color"] = "red"
# print danny

favorite_numbers = [9,117,5,7,0]
# print favorite_numbers[0]
# 
# range(start, end, increment)
# for index in range(0, len(favorite_numbers), 2):
# 	print "start"
# 	favorite_numbers[index] = 15
# 	print "end"
# print favorite_numbers

# if 5 < 10:
# 	print True
# else:
# 	print False

my_tuple = ("Minh", "Nguyen", "glasses", "6ft", True)
(favorite_numbers[0], favorite_numbers[1]) = (favorite_numbers[1], favorite_numbers[0])
print favorite_numbers