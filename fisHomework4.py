"gg6549@rit.edu"
"Author - Geeta Madhav Gali"
import math


def findAccuracy(values):
	"""
		findAccuracy will find the accuracies of the values:
		@param: values : contains all the attribute values including the classes
	"""
	correctClassification = 0
	wrongClassification = 0
	#built the model that is obtained from the building Tree
	for temp in range(len(values)):
		if(values[temp][4] > 2.85):
			if(values[temp][3] >3.99):
				if(values[temp][5] > 4.13):
					if(values[temp][6] == "A"):
						correctClassification += 1
					else:
						wrongClassification += 1
				else:
					if(values[temp][6] == "B"):
						correctClassification += 1
					else:
						wrongClassification += 1
			else:
				if(values[temp][6] == "A"):
					correctClassification += 1
				else:
					wrongClassification += 1
		else:
			if(values[temp][6] == "B"):
				correctClassification += 1
			else:
				wrongClassification += 1
	#printing the accuracy of the model for the training data	
	accuracy = correctClassification/(correctClassification+wrongClassification)		
	print("accuracy =  "+ str(accuracy))


def sortValues(values, attributeNumber):
	"""
		sortValues will sort the data according to the attribute number mentioned. Bubble sort is used.
	@param values: contains all the attribute values including the classes
	@param attributeNumber : the attribute number on which sorting has to be occured
	
	@return values: sorted list
	"""
	templist = []#templist is used to store the values temporarily 
	for pointer1 in range(len(values)):
		for pointer2 in range(pointer1, len(values)):
			if(values[pointer1][attributeNumber] > values[pointer2][attributeNumber]):
				templist = values[pointer1]
				values[pointer1] = values[pointer2]
				values[pointer2] = templist
	return values

def buildingTree(values, attributes):
	"""
		buildingTree will build the classification model for one of the best attributes available.
		
	@param values: contains all the attribute values including the classes
	@param attributes : list of attributes present in the data model
	
	@return returns when it reaches the threshold limit value
	"""
	#print(len(attributes))
	#print(attributes)
	#counts of the different classes available
	GreyhoundCount = 0
	WhippetCount = 0
	for temp in range(len(values)):
		if(values[temp][len(attributes)-1] == "A"):
			GreyhoundCount += 1
		else:
			WhippetCount += 1
	#print(GreyhoundCount)
	#print(WhippetCount)
	#If the class contains 60 percent or more similar instances then returning 
	if((GreyhoundCount/len(values)) >= 0.65):
		print("leafnode" + " A")
		return
	elif((WhippetCount/len(values)) >= 0.65):
		print("leafnode" + " B")
		return
	#Initializing the best attribute, best splot Attribute, best Impurity	
	bestAtrribute = 0
	bestSplitAttribute = 0
	bestImpurity = math.inf
	#for each value in the attributes except the class name running a loop
	for temp in range(len(attributes)-1):
		#sorting the data according to the selected attribute
		values = sortValues(values, temp)
		#print(values)
		#initializing best gini, best split value
		bestGini = math.inf
		bestSplitValue = 0
		#for each value in the attribute running a loop
		for index in range(len(values)):
			#assigning the splitvalue
			splitValue = values[index][temp]
			#print(values[index])
			countGreyhoundLeft = 0
			countWhippetLeft = 0
			countGreyhoundRight = 0
			countWhippetRight = 0
			countInstanceLeft = 0
			countInstanceRight = 0
			giniRight = 0
			giniLeft = 0
			probabilityGreyhoundRight = 0
			probabilityGreyhoundLeft = 0
			probabilityWhippetRight = 0
			probabilityWhippetLeft = 0
			# for each value in the range of values present in the attribute counting the left and the right
			for index1 in range(len(values)):
				if values[index1][temp] <= splitValue:
					if values[index1][len(attributes)-1] == "A":
						countGreyhoundLeft += 1
					else:
						countWhippetLeft += 1
					countInstanceLeft += 1
				else:
					if values[index1][len(attributes)-1] == "A":
						countGreyhoundRight += 1
					else:
						countWhippetRight += 1
					countInstanceRight += 1
			#calculating the probabilities of the left and the right
			if countInstanceRight != 0:
				probabilityGreyhoundRight = countGreyhoundRight/ countInstanceRight
				probabilityWhippetRight = countWhippetRight/ countInstanceRight
			#calculating the gini index for right
			giniRight = 1 - (probabilityGreyhoundRight**2 + probabilityWhippetRight**2)
			#print(giniRight)
			if countInstanceLeft != 0:
				probabilityGreyhoundLeft = countGreyhoundLeft/ countInstanceLeft
				probabilityWhippetLeft = countWhippetLeft/ countInstanceLeft
			#calculating the gini index for left
			giniLeft = 1 - (probabilityGreyhoundLeft**2 + probabilityWhippetLeft**2)
			#print(giniLeft)
			#calculating the mixed gini index
			mixedGini = (((countInstanceRight/(countInstanceRight+countInstanceLeft))*giniRight) + ((countInstanceLeft/(countInstanceRight+countInstanceLeft))*giniLeft))
			#print(mixedGini)
			#updating the best Gini index if mixed Gini is better than the bestGini
			if mixedGini < bestGini:
				bestGini = mixedGini
				bestSplitValue = splitValue
		#print(bestGini)
		#print(bestSplitValue)
		#updating the best Impurity index if best Gini is better than the bestImpurity
		if bestGini < bestImpurity:
			bestImpurity = bestGini
			bestAtrribute = temp
			bestSplitAttribute = bestSplitValue
	print("attribute =" +str(bestAtrribute))
	print("best split = " + str(bestSplitAttribute))
	#initializing two list left and right
	valueLeft = []
	valueRight = []
	#assigning the values to the left and right lists based on the split value
	for temp in range(len(values)):
		if values[temp][bestAtrribute] <= bestSplitAttribute:
			valueLeft.append(values[temp])
		else:
			valueRight.append(values[temp])
	#recursively calling the buildingTree function with left and right values
	buildingTree(valueLeft,attributes)
	buildingTree(valueRight,attributes)
	
		
	
	
def main():
	#opening the input file
	datafile = "fisHw4.csv"
	with open(datafile) as data:
		attributes = data.readline().strip().split(",")
		#print(attributes)
		#calculating the length of the attributes alone
		length = len(attributes) - 1
		values = []
		#storing all the values in the list
		for instance in data:
			tempList = []
			instance = instance.strip().split(",")
			for temp in range(len(instance)):
				if(temp != length):
					val = float(instance[temp])
					tempList.append(val)
				else:
					tempList.append(instance[temp])
			values.append(tempList)
	#calling the building tree function
	buildingTree(values,attributes)
	#finding the accuracy of the training data
	"""
	findAccuracy(values)
	buildingProgram()
	classifyTestdata("HW_05C_DecTree_TESTING__FOR_STUDENTS__v540.csv")
	"""
			
	
main()