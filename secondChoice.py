# Creating a second choice function, gives an opportunity for the user; if they have the desire, at least.
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
