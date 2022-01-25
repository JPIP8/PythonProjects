###########################################################################
###COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###                Assignment 6: EDA for the Iris Dataset              ###
###                    Juan Pablo Idrovo - Z23501186                   ###
###########################################################################
import statistics
import csv
############################ "Pretty" Printing ##############################


def pprint(a, b, _min_, _std_, _count_):

    print("###################################################################")
    # Printing the header for better comprehension of output
    print(f"{'Species':<25} {'Setosa':<12} {'Versicolor':<13} {'Virginica':<13}")
    print('-------------------------------------------------------------------')
    # Printing the data in a organized manner
    print(
        f"{'MEAN Petal Length: ':<25} {a['setosa'][0]:<12.2f} {a['versicolor'][0]:<13.2f} {a['virginica'][0]:<13.2f}")
    print(
        f"{'MEAN Petal Width: ':<25} {a['setosa'][1]:<12.2f} {a['versicolor'][1]:<13.2f} {a['virginica'][1]:<13.2f}")
    print(
        f"{'MEAN Sepal Length: ':<25} {a['setosa'][2]:<12.2f} {a['versicolor'][2]:<13.2f} {a['virginica'][2]:<13.2f}")
    print(
        f"{'MEAN Sepal Width: ':<25} {a['setosa'][3]:<12.2f} {a['versicolor'][3]:<13.2f} {a['virginica'][3]:<13.2f}")
    print('-------------------------------------------------------------------')

    print(
        f"{'MAX Petal Length: ':<25} {b['setosa']['max_sepal_length']:<12.2f} {b['versicolor']['max_sepal_length']:<13.2f} {b['virginica']['max_sepal_length']:<13.2f}")
    print(
        f"{'MAX Petal Width: ':<25} {b['setosa']['max_sepal_width']:<12.2f} {b['versicolor']['max_sepal_width']:<13.2f} {b['virginica']['max_sepal_width']:<13.2f}")
    print(
        f"{'MAX Sepal Length: ':<25} {b['setosa']['max_petal_length']:<12.2f} {b['versicolor']['max_petal_length']:<13.2f} {b['virginica']['max_petal_length']:<13.2f}")
    print(
        f"{'MAX Sepal Width: ':<25} {b['setosa']['max_petal_width']:<12.2f} {b['versicolor']['max_petal_width']:<13.2f} {b['virginica']['max_petal_width']:<13.2f}")
    print('-------------------------------------------------------------------')

    print(
        f"{'MIN Petal Length: ':<25} {_min_['setosa']['max_sepal_length']:<12.2f} {_min_['versicolor']['max_sepal_length']:<13.2f} {_min_['virginica']['max_sepal_length']:<13.2f}")
    print(
        f"{'MIN Petal Width: ':<25} {_min_['setosa']['max_sepal_width']:<12.2f} {_min_['versicolor']['max_sepal_width']:<13.2f} {_min_['virginica']['max_sepal_width']:<13.2f}")
    print(
        f"{'MIN Sepal Length: ':<25} {_min_['setosa']['max_petal_length']:<12.2f} {_min_['versicolor']['max_petal_length']:<13.2f} {_min_['virginica']['max_petal_length']:<13.2f}")
    print(
        f"{'MIN Sepal Width: ':<25} {_min_['setosa']['max_petal_width']:<12.2f} {_min_['versicolor']['max_petal_width']:<13.2f} {_min_['virginica']['max_petal_width']:<13.2f}")
    print('-------------------------------------------------------------------')

    print(
        f"{'Std Dev Petal Length: ':<25} {_std_['setosa']['max_sepal_length']:<12.2f} {_std_['versicolor']['max_sepal_length']:<13.2f} {_std_['virginica']['max_sepal_length']:<13.2f}")
    print(
        f"{'Std Dev Petal Width: ':<25} {_std_['setosa']['max_sepal_width']:<12.2f} {_std_['versicolor']['max_sepal_width']:<13.2f} {_std_['virginica']['max_sepal_width']:<13.2f}")
    print(
        f"{'Std Dev Sepal Length: ':<25} {_std_['setosa']['max_petal_length']:<12.2f} {_std_['versicolor']['max_petal_length']:<13.2f} {_std_['virginica']['max_petal_length']:<13.2f}")
    print(
        f"{'Std Dev Sepal Width: ':<25} {_std_['setosa']['max_petal_width']:<12.2f} {_std_['versicolor']['max_petal_width']:<13.2f} {_std_['virginica']['max_petal_width']:<13.2f}")
    print('-------------------------------------------------------------------')

    print(
        f"{'Count: ':<25} {_count_['setosa']:<12} {_count_['versicolor']:<13} {_count_['virginica']:<13}")
    print('-------------------------------------------------------------------')

    print('###################################################################')

############################   Compute MEAN   ################################
# This function is in charge of computing the MEAN of the data from the set.


def compMean(dataset):
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

    # Calculating mean

    # Creating a new empty dictionary for the mean
    d_mean = {}

    # For loop for traversar the species in attrb
    for species in attrb:

        # Filling the s_mean dictionary with the mean of the different species
        d_mean[species] = [sum_attr / counts[species]
                           for sum_attr in attrb[species]]

    return d_mean

############################   Compute MAX   ################################
# This function is in charge of computing the MAX of the data from the set.


def compMax(dataset):

    dict_att = {'setosa': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []}, 'versicolor': {'sepal_length': [], 'sepal_width': [
    ], 'petal_length': [], 'petal_width': []}, 'virginica': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []}}

    # Read every line of the dataset
    for line in dataset:
        species = line[-1]

        dict_att[species]['sepal_length'].append(float(line[0]))
        dict_att[species]['sepal_width'].append(float(line[1]))
        dict_att[species]['petal_length'].append(float(line[2]))
        dict_att[species]['petal_width'].append(float(line[3]))

    # Dictionary of dictionaries for storing all the max values
    max_att = {'setosa': {'max_sepal_length': 0, 'max_sepal_width': 0, 'max_petal_length': 0, 'max_petal_width': 0}, 'versicolor': {'max_sepal_length': 0, 'max_sepal_width': 0,
                                                                                                                                    'max_petal_length': 0, 'max_petal_width': 0}, 'virginica': {'max_sepal_length': 0, 'max_sepal_width': 0, 'max_petal_length': 0, 'max_petal_width': 0}}

    # Getting max values for all the attributes of the SETOSA type
    max_att['setosa']['max_sepal_length'], max_att['setosa']['max_sepal_width'], max_att['setosa']['max_petal_length'], max_att['setosa']['max_petal_width'] = max(
        dict_att['setosa']['sepal_length']), max(dict_att['setosa']['sepal_width']), max(dict_att['setosa']['petal_length']), max(dict_att['setosa']['petal_width'])

    # Getting max values for all the attributes of the VERSICOLOR type
    max_att['versicolor']['max_sepal_length'], max_att['versicolor']['max_sepal_width'], max_att['versicolor']['max_petal_length'], max_att['versicolor']['max_petal_width'] = max(
        dict_att['versicolor']['sepal_length']), max(dict_att['versicolor']['sepal_width']), max(dict_att['versicolor']['petal_length']), max(dict_att['versicolor']['petal_width'])

    # Getting max values for all the attributes of the VIRGINICA type
    max_att['virginica']['max_sepal_length'], max_att['virginica']['max_sepal_width'], max_att['virginica']['max_petal_length'], max_att['virginica']['max_petal_width'] = max(
        dict_att['virginica']['sepal_length']), max(dict_att['virginica']['sepal_width']), max(dict_att['virginica']['petal_length']), max(dict_att['virginica']['petal_width'])

    return max_att


############################   Compute MIN   ################################
# This function is in charge of computing the MIN of the data from the set.


def compMin(dataset):

    dict_att = {'setosa': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []}, 'versicolor': {'sepal_length': [], 'sepal_width': [
    ], 'petal_length': [], 'petal_width': []}, 'virginica': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []}}

    # Read every line of the dataset
    for line in dataset:
        species = line[-1]

        dict_att[species]['sepal_length'].append(float(line[0]))
        dict_att[species]['sepal_width'].append(float(line[1]))
        dict_att[species]['petal_length'].append(float(line[2]))
        dict_att[species]['petal_width'].append(float(line[3]))

    # Dictionary of dictionaries for storing all the MIN values
    min_att = {'setosa': {'max_sepal_length': 0, 'max_sepal_width': 0, 'max_petal_length': 0, 'max_petal_width': 0}, 'versicolor': {'max_sepal_length': 0, 'max_sepal_width': 0,
                                                                                                                                    'max_petal_length': 0, 'max_petal_width': 0}, 'virginica': {'max_sepal_length': 0, 'max_sepal_width': 0, 'max_petal_length': 0, 'max_petal_width': 0}}

    # Getting MIN values for all the attributes of the SETOSA type
    min_att['setosa']['max_sepal_length'], min_att['setosa']['max_sepal_width'], min_att['setosa']['max_petal_length'], min_att['setosa']['max_petal_width'] = min(
        dict_att['setosa']['sepal_length']), min(dict_att['setosa']['sepal_width']), min(dict_att['setosa']['petal_length']), min(dict_att['setosa']['petal_width'])

    # Getting MIN values for all the attributes of the VERSICOLOR type
    min_att['versicolor']['max_sepal_length'], min_att['versicolor']['max_sepal_width'], min_att['versicolor']['max_petal_length'], min_att['versicolor']['max_petal_width'] = min(
        dict_att['versicolor']['sepal_length']), min(dict_att['versicolor']['sepal_width']), min(dict_att['versicolor']['petal_length']), min(dict_att['versicolor']['petal_width'])

    # Getting MIN values for all the attributes of the VIRGINICA type
    min_att['virginica']['max_sepal_length'], min_att['virginica']['max_sepal_width'], min_att['virginica']['max_petal_length'], min_att['virginica']['max_petal_width'] = min(
        dict_att['virginica']['sepal_length']), min(dict_att['virginica']['sepal_width']), min(dict_att['virginica']['petal_length']), min(dict_att['virginica']['petal_width'])

    return min_att

############################   Compute Standard Dev   ################################
# This function is in charge of computing the Standard Dev  of the data from the set.


def compStd(dataset):

    dict_att = {'setosa': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []}, 'versicolor': {'sepal_length': [], 'sepal_width': [
    ], 'petal_length': [], 'petal_width': []}, 'virginica': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []}}

    # Read every line of the dataset
    for line in dataset:
        species = line[-1]

        dict_att[species]['sepal_length'].append(float(line[0]))
        dict_att[species]['sepal_width'].append(float(line[1]))
        dict_att[species]['petal_length'].append(float(line[2]))
        dict_att[species]['petal_width'].append(float(line[3]))

    # Dictionary of dictionaries for storing all the max values
    std_att = {'setosa': {'max_sepal_length': 0, 'max_sepal_width': 0, 'max_petal_length': 0, 'max_petal_width': 0}, 'versicolor': {'max_sepal_length': 0, 'max_sepal_width': 0,
                                                                                                                                    'max_petal_length': 0, 'max_petal_width': 0}, 'virginica': {'max_sepal_length': 0, 'max_sepal_width': 0, 'max_petal_length': 0, 'max_petal_width': 0}}

    # Getting Standard Dev values for all the attributes of the SETOSA type
    std_att['setosa']['max_sepal_length'], std_att['setosa']['max_sepal_width'], std_att['setosa']['max_petal_length'], std_att['setosa']['max_petal_width'] = statistics.stdev(
        dict_att['setosa']['sepal_length']), statistics.stdev(dict_att['setosa']['sepal_width']), statistics.stdev(dict_att['setosa']['petal_length']), statistics.stdev(dict_att['setosa']['petal_width'])

    # Getting Standard Dev values for all the attributes of the VERSICOLOR type
    std_att['versicolor']['max_sepal_length'], std_att['versicolor']['max_sepal_width'], std_att['versicolor']['max_petal_length'], std_att['versicolor']['max_petal_width'] = statistics.stdev(
        dict_att['versicolor']['sepal_length']), statistics.stdev(dict_att['versicolor']['sepal_width']), statistics.stdev(dict_att['versicolor']['petal_length']), statistics.stdev(dict_att['versicolor']['petal_width'])

    # Getting Standard Dev values for all the attributes of the VIRGINICA type
    std_att['virginica']['max_sepal_length'], std_att['virginica']['max_sepal_width'], std_att['virginica']['max_petal_length'], std_att['virginica']['max_petal_width'] = statistics.stdev(
        dict_att['virginica']['sepal_length']), statistics.stdev(dict_att['virginica']['sepal_width']), statistics.stdev(dict_att['virginica']['petal_length']), statistics.stdev(dict_att['virginica']['petal_width'])

    return std_att


############################   Compute COUNT   ################################
# This function is in charge of computing the COUNT of the data from the set.


def compCount(dataset):

    # Creating a dict for storage of the count
    count_att = {
        "setosa": 0,
        "versicolor": 0,
        "virginica": 0
    }

    # Loop for reading every line from the data
    for line in dataset:
        species = line[-1]

        # Increasing the counter
        count_att[species] += 1

    return count_att
############################ Main Function ##################################


print("\n################################################################")
print("################### Welcome to Assignment #6!###################")
print("################################################################\n")

print('''Assignment 6 is a program that will increase our knowledge  in the use of 
dictionaries, how to process a dataset, producing a summary of statistics, and creation
of graphs by plotting.  We will read from a CSV file and process the information inside
that file and give the user a result.''')

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
mean = compMean(dataL)
max_ = compMax(dataL)
min_ = compMin(dataL)
std_ = compStd(dataL)
count_ = compCount(dataL)
# Pretty printing all the data
pprint(mean, max_, min_, std_, count_)
