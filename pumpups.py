import gspread
import random
from Queue import Queue


#gc = gspread.service_account(filename='credentials.json')
#sh = gc.open("pump-up-buddies-2025")
#worksheet = sh.sheet1
letters = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
names = ['CS', 'KN', 'LK', 'MB', 'DW']


#RETRIEVES DATA -> NAMES, PARTNERS 

#names = worksheet.col_values(1)

partners = [['KN', 'LK', 'CS', 'DW', 'MB']]

i = 2

"""
while worksheet.col_values(i): 
    partnerList = worksheet.col_values(i)[1:]
    partners.append(partnerList)
    i+=1
"""

#CREATES LIST CONTAINING DICTIONARIES WITH PLAYER DATA

playerData = []

x = 1

for i in names: 
    index_list = x - 1  
    if i != "Name":
        data = {'name': i, 'partners': [], 'number': x}
        for i in partners: 
            data['partners'].append(i[index_list])
        playerData.append(data)
        x += 1

#CREATES LIST OF RANDOMIZED NUMBERS

number_range = range(1, len(playerData) + 1)
playerNumbers = random.sample(population=number_range, k=len(playerData))

#ASSIGNS NAMES TO NUMBERS 

for i, player in enumerate(playerData):
    num = player['number']
    numIndex = playerNumbers.index(num)
    playerNumbers[numIndex]=[player['name']]

#CREATE QUEUE 

playerQueue = Queue()

for i in playerNumbers:
    playerQueue.enqueue(i[0])

#GO THROUGH QUEUE 

def partnerAssignment(player):
    tries = 0
    queue_size = playerQueue.size()
    
    while tries < queue_size:    
        possiblePartner = playerQueue.first()
        if possiblePartner != player['name'] and possiblePartner not in player['partners']:
            partner = playerQueue.dequeue()
            player['partners'].append(partner)
            return partner
        else: 
            notPartner = playerQueue.dequeue()
            playerQueue.enqueue(notPartner)
            tries += 1

    print("Retry")
    return None


partnersList = []

for i, player in enumerate(playerData):
    partner = partnerAssignment(player)
    partnersList.append(partner)


print(partnersList)

"""

try:

    for i, player in enumerate(playerData):

        index = 0

        while player['number'] == playerNumbers[index] or playerNumbers[index] in player['partners']:
            index += 1

        player['partners'].append(playerNumbers[index])
        del playerNumbers[index]

except: 
     
     print("Failure")

"""

dataToUpload = []



for i, player in enumerate(playerData):
    dataToUpload.append(player['partners'][-1])
"""
for i, player in enumerate(playerData):
    num = player['number']
    numIndex = dataToUpload.index(num)
    dataToUpload[numIndex]=[player['name']]
 """

#worksheet.update(dataToUpload, 'C2:C25', )

