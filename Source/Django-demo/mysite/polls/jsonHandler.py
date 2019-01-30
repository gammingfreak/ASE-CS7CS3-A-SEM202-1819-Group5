import requests

dublinbike_data = requests.get('https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=29374861957fe56e1b065c24f9cf06f84ae8dce2').json()

def getBikeStandData():
    details_list=[]
    for stands in dublinbike_data:
        details_list.append(stands["name"]+str(stands["available_bikes"])+str(stands["available_bike_stands"])+str(stands['last_update']))
    return details_list

def getAllData():
    return dublinbike_data

print(getBikeStandData())



li =[]
for l in dublinbike_data:
    #li.append(l["number"])
    #li.sort()
    print(l)

#print(getBikeStandData(89))

