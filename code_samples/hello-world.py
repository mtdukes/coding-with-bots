#import a python library to help us work with dates and times
#import datetime

# define a FUNCTION to run a specified task
def main():
	print 'Hello World!'
	print 'I am some prepackaged code.'
	print "I don't do much, but I'm still special!"

# another function, but we won't run this at first
# this function accepts two arguments it will use to perform its task
def add_two_things(x, y):
	print '\nIt looks like you want to add '+str(x)+' and '+str(y)+'!'
	print 'I can do that!'
	print 'The sum is:'
	print x + y

# Use the datetime library to get the current date
def get_date():
	print '\nThe current date and time is: '
	print datetime.datetime.now()
	if datetime.datetime.now() > datetime.datetime(2016, 3, 30, 10, 0, 0, 0):
		print "It looks like Tyler is behind schedule. Tell him to hurry up!"
	else:
		print "Tyler's on schedule. He must be well caffeinated."

# it's good practice to use this bit of code
# when you're writing scripts you plan to run
if __name__ == '__main__':

	#run the function we defined earlier
	main()
	#add_two_things(20,17)
	#get_date()