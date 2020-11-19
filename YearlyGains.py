import csv
import time
from datetime import datetime
import operator
import json

csv_file = "/Users/valverde/Dev/Finances/Transactions.csv"

orders = {} 
name_isin = {}

year_to_check = 2019

#Read CSV
with open(csv_file) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    #Remove Header
    iterspamreader = iter(spamreader)
    next(iterspamreader)

    
    #itemDict = {time.strptime(item[0], "%d-%m-%Y").tm_year: item[:] for item in iterspamreader}
    #print(itemDict)

    #Sort By date
    sortedlist = sorted(iterspamreader,  key = lambda row: datetime.strptime(row[0], "%d-%m-%Y"))

    #Parse info
    for row in sortedlist:
        name_isin[row[3]] = row[2]
        orders.setdefault(row[3],{}).setdefault(time.strptime(row[0], "%d-%m-%Y").tm_year,[]).append(
            [ time.strptime(row[0]+" "+row[1],"%d-%m-%Y %H:%M"), #Date
            float(row[5]), #N shares
            float(row[11]), # Price
            float(row[14] or 0), # comission
            float(row[16])]) # Total

print(json.dumps(orders, sort_keys=True, indent=1))


#Get sells
shares = {}
for row in orders:
    shares[row] = {
        "number" : 0.0, 
        "price" : 0.0 , 
        "comission": 0.0, 
        "total":0.0, 
        "last_sell":0
    }
    print(name_isin[row])
    for order in orders[row]:
        #Get Price per share
        if order[0].tm_year > year_to_check:
            break
        try:
            print(order)
            shares[row]["number"] += abs(order[1])/order[1] 
            shares[row]["price"] += order[2]
            shares[row]["comission"] += order[3]
            shares[row]["total"] += order[4]
            shares[row]["last_sell"] = order[0]
        except:
            print("Execption")
            print(order)
#        #Get Sell
#        if order[0].tm_year == year_to_check or shares[row]["number"] != 0 :
#            if not (order[0].tm_year != year_to_check and order[1] < 0): #Sell on another year
#                #if (name_isin[row] == "CHINA MOBILE LIMITED C"):
#                #    print(name_isin[row])
#                #print(order)
#
#                for n in range(0,abs(int(order[1]))):
#                    shares[row]["number"] += abs(order[1])/order[1]
#                    #print(shares[row]["number"])
#                    itershare = iter(shares[row])
#                    next(itershare)
#                    for i, value in enumerate(itershare, start=2):
#                        #print(i)
#                        shares[row][value] += order[i]/abs(order[1])
#                        #print(shares[row]["number"] , value, shares[row][value])
#                    if shares[row]["number"] == 0:
#                        break


            

print("\nTotal Calculation")
total = 0.0
value = 0.0
comission = 0.0
for share in shares:
    if shares[share]["price"] != 0 and shares[share]["last_sell"].tm_year == year_to_check:
        print(name_isin[share])
        print(shares[share])
        if shares[share]["number"] < 1.0:
            total +=shares[share]["total"]
            value +=shares[share]["price"]
            comission +=shares[share]["comission"]

print(value)         
print(comission)
print(total)
