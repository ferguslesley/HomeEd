#Formats a string
x = "There are %d types of people." % 10
#sets up some variables to be strings
binary = "binary"
do_not = "don't"
#uses formatting to print strings
y = "Those who know %s and those who %s" % (binary, do_not)
#prints two strings with strings inside of them
print x
print y
#prints some more variables and strings using formatting
print "I said %r." % x
print "I also said: '%s'." %y
#sets up some variables
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"
#Prints the two strings "joke_evaluation" and "hilarious"
print joke_evaluation % hilarious
#sets up variables that go on the same line
w = "This is the left side of..."
e = "a string with a right side."
#prints the two strings
print w + e


