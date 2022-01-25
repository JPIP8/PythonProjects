###########################################################################
###COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###                Assignment 5: Iris Dataset and Dictionaries         ###
###                    Juan Pablo Idrovo - Z23501186                   ###
###########################################################################

import csv
############################ "Pretty" Printing ##############################


def pprint(a):

    # "a" is the averages
    print("###################################################################")
    # Printing the header for better comprehension of output
    print(f"{'Species':<25} {'Setosa':<12} {'Versicolor':<13} {'Virginica':<13}")
    print('-------------------------------------------------------------------')
    print("AVERAGES in cm:")
    print("-------------------------------------------------------------------")
    # Printing the data in a organized manner
    print(
        f"{'Petal Length: ':<25} {a['setosa'][0]:<12.2f} {a['versicolor'][0]:<13.2f} {a['virginica'][0]:<13.2f}")
    print(
        f"{'Petal Width: ':<25} {a['setosa'][1]:<12.2f} {a['versicolor'][1]:<13.2f} {a['virginica'][1]:<13.2f}")
    print(
        f"{'Sepal Length: ':<25} {a['setosa'][2]:<12.2f} {a['versicolor'][2]:<13.2f} {a['virginica'][2]:<13.2f}")
    print(
        f"{'Sepal Width: ':<25} {a['setosa'][3]:<12.2f} {a['versicolor'][3]:<13.2f} {a['virginica'][3]:<13.2f}")
    print('###################################################################')


############################   Compute Avg   ################################
# This function is in charge of computing the average of the data from the set.


def compAvg(dataset):
    # Creating a dict for storage of the sum
    attrb = {
        "setosa": [0, 0, 0, 0],
        "versicolor": [0, 0, 0, 0],
        "virginica": [0, 0, 0, 0]
    }
    # Creating a dict for storage of the count
    counts = {
        "setosa": 0,
        "versicolor": 0,
        "virginica": 0
    }

    # Loop for reading every line from the data
    for line in dataset:
        species = line[-1]

        # Adding the values to the columns
        # Petal Length line
        attrb[species][0] += float(line[2])
        # Petal Width line
        attrb[species][1] += float(line[3])
        # Sepal Length line
        attrb[species][2] += float(line[0])
        # Sepal Width line
        attrb[species][3] += float(line[1])

        # Increasing the counter
        counts[species] += 1

    # Calculating the statistics and storing in a dict.
    avgs = {
        species: [x / counts[species] for x in attrb[species]] for species in attrb
    }
    return avgs

############################ Main Function ##################################


print("\n################################################################")
print("################### Welcome to Assignment #5!###################")
print("################################################################\n")

print('''Assignment 5 is a program that will increase our knowledge  in the use of 
dictionaries, how to process a dataset, and producing a summary of statistics. 
We will read from a CSV file and process the information inside that file and
give the user a result.''')

# Opening the CSV file with the "with" statement
with open('iris.csv', newline='') as File:
    # Return the object iterated line over line
    reader = csv.reader(File)
    # Skipping the header
    next(reader)
    # Creating the data list
    dataL = []
    # Loop for data addition
    for row in reader:
        dataL.append(row)

# Calling the function for computing the average
AVGs = compAvg(dataL)
# Pretty printing all the data
pprint(AVGs)
