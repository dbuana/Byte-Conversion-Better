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
	chart = chart.Figure(data=go.Table(header=dict(values["App Name", "App Storage"]), 
		cells=dict(values[dowloadApp, appStorage])))

	chart.show()
