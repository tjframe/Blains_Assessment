# Coding assignment
# Tylar Frame

from datetime import datetime, timedelta

# object definition for the CSV string.
class transaction:
    def __init__(self, firstName, middleName, lastName, transactionNumber, transactionAmount, transactionDate):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.transactionNumber = transactionNumber
        self.transactionAmount = transactionAmount
        self.transactionDate = transactionDate

# function to convert the number representing the date in the CSV string into a date mm/dd/yyyy format.
def convertDate(date):
    returnDate = datetime(2018, 2, 1) - timedelta(days=float(date)) # calculates the date
    returnDate = datetime.strftime(returnDate, "%m/%d/%Y") # this formats the date to mm/dd/yyyy
    return returnDate

# function that calculates the total of all transactions given.
def totalTransaction(transaction):
    total = 0
    i = 0
    for x in transaction:
        total = total + float(transaction[i].transactionAmount)
        i = i + 1

    if total<0: # this is needed to return the number with parentheses representing a negative number.
        total = abs(total)
        parenthesesReturn = "("
        parenthesesReturn = parenthesesReturn + str(total)
        parenthesesReturn = parenthesesReturn + ")"
        print(parenthesesReturn)
        return parenthesesReturn

    print(total)
    print("------------------------------------------------------")
    return total

# function that will return the total of the transactions of names that match the search
def searchFilter(filter):
    filter = filter.upper() # all names use upper case so if search is lower case change.
    if filter == "":
        totalTransaction(transactions)

    transactionsToSend = []
    i = 0
    for x in transactions:
        if filter in transactions[i].firstName or filter in transactions[i].middleName or filter in transactions[i].lastName:
            transactionsToSend.append(transactions[i])
        i = i + 1

    print(totalTransaction(transactionsToSend))
    print("------------------------------------------------------")

# function that returns all object data for dates matching or before the search date
def searchDate(date):
    newdate = datetime.strptime(date, "%m/%d/%Y") # convert the given date to datetime
    i = 0
    for x in transactions:
        check = transactions[i].transactionDate # convert date in object to datetime
        newcheck = datetime.strptime(check, "%m/%d/%Y")
        if(newdate>=newcheck):
            print(transactions[i].firstName, transactions[i].middleName, transactions[i].lastName,
                  transactions[i].transactionNumber, transactions[i].transactionAmount, transactions[i].transactionDate)
            i = i +1
        else:
            i = i + 1

    print("------------------------------------------------------")


#  Start main code here.
transactions = []  # transactions list that will hold all the transaction objects.
# transactions.append(transaction("", "", "", 0, 0, 0))
# transactions.append(transaction("", "", "", 0, 0, 0))
# transactions.append(transaction("", "", "", 0, 0, 0))
# transactions.append(transaction("", "", "", 0, 0, 0))
# transactions.append(transaction("", "", "", 0, 0, 0))

CSV = "greg R hopper,0123654,24.25,255\n  Sam Smith,000126,(24.25),421\n maximus WHITE  ,000025,(12),\n Bill Masters,000526,6.5,11\n Frank   Berg,000527,6.75,1"

toSearch = "M"  # hard coded string to be used in the search function for task 3
toSearchDate = "05/22/2017"  # hard coded string to be used in the search function for task 4

newLineSplitCSV = CSV.split("\n") #splits up data by newline

i = 0 #loop control
j = 0 #loop control
for x in newLineSplitCSV: # this loop is going through each of the transactions as each \n is a different transaction
    transactions.append(transaction("", "", "", 0, 0, 0))
    commaSplitCSV = newLineSplitCSV[i].split(",") # split up the new line data into data for each object

    # transaction number needs to be converted from int to str to fix extra leading zeros.
    transactionNum = int(commaSplitCSV[1])
    transactionNum = str(transactionNum).zfill(6) # if number is not 6 characters add zeros to fix.
    transactions[i].transactionNumber = transactionNum # adds transaction Number to object

    # This is needed to take a negative number in parentheses and put a negative value in the object.
    k = 0
    negativeNum = ""
    if commaSplitCSV[2][0] == "(":
        for y in commaSplitCSV[2]:
            if commaSplitCSV[2][k] == "(":
                negativeNum = negativeNum + "-"
            elif commaSplitCSV[2][k] == ")":
                negativeNum = negativeNum
            else:
                negativeNum = negativeNum + commaSplitCSV[2][k]
            k = k + 1

        transactions[i].transactionAmount = float(negativeNum) # adds transaction Amount to object
    else:
        transactions[i].transactionAmount = commaSplitCSV[2]  # adds transaction Amount to object

    # Check if the transactionDate spot is left blank in the string. make 0 if none, convert date if not blank.
    if commaSplitCSV[3] == "":
        transactions[i].transactionDate = convertDate(0)
    else:
        transactions[i].transactionDate = convertDate(commaSplitCSV[3])


    spaceSplitCSV = commaSplitCSV[0].split(" ")  # last split to separate first middle and last names

    j=0
    nameLoop = 0
    for y in spaceSplitCSV:  # This loop is needed to assign the first middle and last names as some names do not have a middle name.
        if spaceSplitCSV[j] != "":
            if nameLoop == 0:
                transactions[i].firstName = y.upper()
                nameLoop = nameLoop + 1
            elif nameLoop == 1:
                transactions[i].lastName = y.upper()
                nameLoop = nameLoop + 1
            elif nameLoop == 2: # if this elif is reached that means the user has a middle name and needs to be swapped with current last name value.
                temp = transactions[i].lastName
                transactions[i].middleName = temp
                transactions[i].lastName = y.upper()
        j = j+1

    i = i + 1

# here begins the code for showing that each of the 4 tasks work.
# prints out converted CSV string into objects for Task 1.
print("------------------------------------------------------")
i=0
for x in transactions:
    print(transactions[i].firstName, transactions[i].middleName, transactions[i].lastName, transactions[i].transactionNumber, transactions[i].transactionAmount, transactions[i].transactionDate)
    i = i+1
print("------------------------------------------------------")

# function used in task 2
totalTransaction(transactions)

# function used in task 3
searchFilter(toSearch)

# function used in task 4
searchDate(toSearchDate)
