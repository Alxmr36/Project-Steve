import csv

fName = "Order.csv"

#initializing the container variables
field = []
row = []

with open(fName, "r") as csvfile:
    fReader = csv.reader(csvfile)
    
    #get field names
    fields = next(fReader)

    #remove the header row
    lines = csvfile.readlines()

    #Initializie the dictionary to store the items 
    items = {"Hardware": 0, "Lumber": 0, "Paint": 0}

field = next(fReader)

#get data row
for nRow in fReader:
    row.append(nRow)
    

