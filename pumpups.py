import gspread
import random



gc = gspread.service_account(filename='credentials.json')

sh = gc.open("pump-up-buddies-2025")

worksheet = sh.sheet1

names = worksheet.col_values(1)

playerData = []

x = 1

for i in names: 
    if i != "Name":
        data = {'name': i, 'partners': [], 'number': x}
        playerData.append(data)
        x += 1

number_range = range(1, len(playerData) + 1)

playerNumbers = random.sample(population=number_range, k=len(playerData))



try:

    for i, player in enumerate(playerData):

        index = 0

        while player['number'] == playerNumbers[index] or playerNumbers[index] in player['partners']:
            index += 1

        player['partners'].append(playerNumbers[index])
        del playerNumbers[index]

except: 
     
     print("Failure")





dataToUpload = []



for i, player in enumerate(playerData):
    dataToUpload.append(player['partners'][-1])

for i, player in enumerate(playerData):
    num = player['number']
    numIndex = dataToUpload.index(num)
    dataToUpload[numIndex]=[player['name']]
 

worksheet.update(dataToUpload, 'B2:B25', )

