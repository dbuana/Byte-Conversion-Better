# Python; Introduction to Data Structures and Algorithms
import random

# Arranging Array Algorithm
# Goal: Using "user-input", they have the opportunity on crating their own number arrays and function has to organize the numbers
data = []

def userInput():
	# The user input is heliocentric to this code
	n1 = int(input(""))
	n2 = int(input(""))
	n3 = int(input(""))
	n4 = int(input(""))
	# Calling the interface
	print(n1)
	print(n2)
	print(n3)
	print(n4)
	# Implementing the interface 
	data = [n1, n2, n3, n4]
	return dataI

def organize_data():
	data = [n1, n2, n3, n4]

	for i in dataI:
		if n[int(-1)] > n[int(1)]:
			print(n)
	return n

print(userInput())
print(organize_data())

# The algorithm is considerably simple, in terms of concept. The concept is a user creates their
# own number array and then the program tries to arrange the numbers. 

# Inside/Analyzing: I have included the user-interface by simply using the input method, in addition
# I added a "for loop". For the purpose of validating each numbers present in the array. 
# With that; the result should be the numbers listed, in order. 

# Algorithms; Arrays and Memories
# A tutorial session with resources from the internet
# Goal: Have a decent comprehension on this concept.

# Array - In data science, array is usually depicted as the list of elements to data structures. - [2,3,5,2,5,3,1] <-- An example
# Memory - Where the computer stores data, or programs. Represented as bytes, megabytes and kilobytes! 

# Goal: Create an algortihm to convert bytes and, create a user interface for user to store their data
# Also, help the user by asking "the amount of storage in their device, then the conversion function; maybe used to help them calculate their app"

# Conversion method
bytes = 8 #bits

def byteConversion():
	deviceStorage = int(input("Type in the amount GB in your device, (Iphone, Ipad): "))
	print(deviceStorage + "GigaBytes")

	# Making sure the user downloads an app with the ideal amount of storage
	appDownload = int(input("Type in the recent app you downloaded: "))
	appStorage = int(input("Type in the amount of storage does your app need(In MB): "))

	GB = appStorage * 8
	if GB > deviceStorage:
		print("Too much for your device, buddy!")
		print("Download an app with smaller app storage")
		pass
	elif GB < deviceStorage:
		print("Just fine!")

	# Creating the converter list
	KB = appStorage * 8
	MB = appStorage
	TB = appStorage * 1100
	EB = appStorage * 1153

	KBstring = f"Your app is {KB} kilobytes"
	MBstring = f"Your app is {MB} megabytes"
	TBstring = f"Your app is {TB} terebytes"
	EBstring = f"Your app is {EB} exabytes"

	listStorage = [KBstring, MBstring, TBstring, EBstring]

	# A loop 
	for i in appDownload:
		if n[deviceStorage] > n[appStorage]:
			result -= 1
			print("Your app is ideal for the device")
			print(result)
			print(n)
		elif n[deviceStorage] < n[appStorage]:
			print("Your app was not ideal for the device")
			resultStorage = appStorage
			# Creating the statement
			result = listStorage
			print(n)

	return KBstring, MBstring, TBstring, EBstring

print(byteConversion())

# Storing and Saving Algorithm: A continuation of the previous code, though, this code will not be as sophisticated. 
# I can promise that this code will execute smoothly. 

# The program keeps track of the users downloading habit, in a table chart
import plotply.graphs_object as go

# This function will store the users app, in a table chart. It is very efficient; yet comprehensible
def storing(byteConversion):
	downloadApp = input("Type in the app you wish to download: ")
	appStorage = int(input("Type in the storage(MB): "))

	# The validation statement. Simple, but executes perfectly
	if int(appStorage) > int(deviceStorage):
		print("Action may not be permitted")
		pass
	elif int(appStorage) == int(deviceStorage) or int(appStorage) < int(deviceStorage):
			pass

	# Creating the chart
	chart = chart.Figure(data=go.Table(header=dict(values["App Name", "App Storage"]), # The first line tells the heading title for the table char
		cells=dict(values[downloadApp, appStorage]))) # Shows the value of the charts, as "downloadApp" and "appStorage"

	chart.show() # Calling the chart program and making sure it runs smoothly

# Creating a second choice function, starting with a user-interface. 
second = input("Would you like to download another application: ")

def secondChoice(second):
	# Answer: If yes; answer with yes or y, If no anwer with 
	if second == "yes" or second == "y":
		print("The process awaits :-)")
	elif second == "no" or second == "n":
		pass 

	while second == "yes":
		downloadApp = input("Type in the app you wish to download: ")
		appStorage = int(input("Type in the storage(MB): "))

		# The validation statement
		if int(appStorage) > int(deviceStorage):
			print("Action may not be permitted")
			pass
		elif int(appStorage) == int(deviceStorage) or int(appStorage) < int(deviceStorage):
			break

		# Creating the chart
		chart = chart.Figure(data=go.Table(header=dict(values["Name of application", "Application Storage"]),
			cells=dict(values[downloadApp, appStorage])))

		chart.show()

# Dynamic Prgramming and Recurssive; Basically a style of programming
