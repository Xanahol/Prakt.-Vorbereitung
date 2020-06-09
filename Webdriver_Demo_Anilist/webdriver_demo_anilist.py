#################################
#      Created by Noël B.       #
#    in preparation for the     #
#     1 year of internship      #
#           09.06.2020          #
#################################


import readnames as ReadNames
import driverconnection as DC


def startProcedure():
    userInput = input(
        "For randomly generated names, type 'r':\nFor getting your names in order, type 'o'\n(r/o): ")

    if userInput == "r":
        ReadNames.getRandomNames()
    elif userInput == "o":
        ReadNames.getNamesInOrder()
    else:
        print("\nInvalid Input,\nPlease type 'r' or 'o' and hit enter!\n")
        startProcedure()


DC.connectToAnilist()
startProcedure()
