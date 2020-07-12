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
