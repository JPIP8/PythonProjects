###########################################################################
###COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###                Assignment 4: Vehicle fuel consumption              ###
###                    Juan Pablo Idrovo - Z23501186                   ###
###########################################################################

import pylab

print("")
print('''This is a simple app for us to practice lists, tuples, functions, and
CSV file manipulation. This simple app will give a simple solution for querying
the EPA fuel consumption data and also will give you some plots of the data. It
will have two options, one for the MPG interval and other to plot.''')

############################   Read File   ##################################


def read_f(file):

    for line in file:
        if "BMW" in line:
            print(line[:75])

############################  Mileage List ##################################


def create_mileage_list(file, Aint, Bint):
    # Creating a list of cars and mileage from the file
    mileage_list = []
    header = file.readline()    # Skipping header line
    for line in file:
        line_list = line.split(',')  # When ",", then split

        if 'Car' in line_list[70]:
            if int(line_list[10]) >= Aint and int(line_list[10]) <= Bint:

                mileage_list.append(
                    (int(line_list[10]), line_list[2], line_list[3]))

    return mileage_list

############################ Main Function ##################################


print("\n################################################################")
print("################### Welcome to Assignment #4!###################")
print("################################################################\n")


print("Choose your option: (1) Mileage or (2) Trend Plot: \n")
option = input(" ")
option = int(option)


if option == 1:

    epa15_f = open("epadata2015.csv", "r")

    print("You are in Mileage\n")
    print("Type the MPG Interval that you are interested in: \n")
    print("Starting Interval: \n")
    intA = input("")
    intA = int(intA)
    print("Ending Interval: \n")
    intB = input("")
    intB = int(intB)

    range_mil = create_mileage_list(epa15_f, intA, intB)

    print(range_mil)

elif option == 2:

    epa20_f = open("epadata2020.csv", "r")
    x, y = [], []

    for line in epa20_f:
        line_1 = line.strip().split()
        x.append(int(line_1[0][:]))  # the year
        y.append(float(line_1[6]))  # HIGHWAY MPG

    print("You are in Trend Plot\n")

    print("Input the measure: (H)ighway MPG, (C)ity MPG, and (O)verall MPG:")
    opt_measure = input("")
    opt_measure.lower()
    print("Do you want to (D)isplay or save to (F)ile? ")
    opt_plot = input("")
    opt_plot.lower()

    if opt_measure == 'h':
        print("(H)ighway MPG\n")
        for line in epa20_f:
            line_1 = line.strip().split()
            x.append(int(line_1[0][:]))  # the year
            y.append(float(line_1[6]))  # HIGHWAY MPG

        pylab.plot(x, y)
        pylab.ylabel("HIGHWAY MPG")
        pylab.xlabel("YEAR")
        pylab.title("EPA annual average data in HIGHWAY MPG")

        if opt_plot == 'd':
            pylab.show()

        elif opt_plot == 'f':
            pylab.savefig("epa_lop.png")

        else:
            print("You decided to exit the program. Thank You!\n")

    elif opt_measure == 'c':
        print("(C)ity MPG\n")
        for line in epa20_f:
            line_1 = line.strip().split()
            x.append(int(line_1[0][:]))  # the year
            y.append(float(line_1[5]))  # CITY MPG

        pylab.plot(x, y)
        pylab.ylabel("CITY MPG")
        pylab.xlabel("YEAR")
        pylab.title("EPA annual average data in CITY MPG")

        if opt_plot == 'd':
            pylab.show()

        elif opt_plot == 'f':

            pylab.savefig("epa_lop.png")

        else:
            print("You decided to exit the program. Thank You!\n")

    elif opt_measure == 'o':
        print("(O)verall MPG\n")
        for line in epa20_f:
            line_1 = line.strip().split()
            x.append(int(line_1[0]))  # the year
            y.append(float(line_1[4]))  # OVERALL MPG

        pylab.plot(x, y)
        pylab.ylabel("OVERALL MPG")
        pylab.xlabel("YEAR")
        pylab.title("EPA annual average data in OVERALL MPG")

        if opt_plot == 'd':
            pylab.show()

        elif opt_plot == 'f':
            pylab.savefig("epa_lop.png")

        else:
            print("You decided to exit the program. Thank You!\n")

    else:
        print("You decided to exit the program. Thank You!\n")


else:
    print("You decided to exit the program. Thank You!\n")
