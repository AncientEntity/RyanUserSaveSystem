import os, json
folderLocation = "userSaves"
cache = {}

def CreateNewUser(userID):
    if(os.path.isfile(folderLocation+"\\"+userID+".dat") == False):
        f = open(folderLocation+"\\"+userID+".dat","w")
        f.write("{}")
        f.close()
        print("New User Created: "+userID)
def SaveKey(userID, key, value):
    jsonDictionary = None
    if(userID not in cache):
        CreateNewUser(userID)
        userFile = open(folderLocation+"\\"+userID+".dat","r")
        raw = userFile.read()
        if(raw == ""):
            raw = "{}"
        jsonDictionary = json.loads(raw)
        userFile.close()
    else:
        jsonDictionary = cache[userID]
    jsonDictionary[key] = value
    try:
        jsonSave = json.dumps(jsonDictionary,sort_keys=True, indent=4)
    except Exception as e:
        raise(e)
        return
    userFile = open(folderLocation+"\\"+userID+".dat","w")
    userFile.truncate(0)
    userFile.write(jsonSave)
    userFile.close()
    cache[userID] = jsonDictionary

def GetKey(userID,key):
    if(os.path.isfile(folderLocation+"\\"+userID+".dat") == True):
        userFile = open(folderLocation+"\\"+userID+".dat","r")
        cache[userID] = json.loads(userFile.read())
    else:
        CreateNewUser(userID)

    if(userID in cache and key in cache[userID]):
        return cache[userID][key]
    
    return None


SaveKey("34234234","T","yolo")
print(GetKey("34234234","Balance"))
print(GetKey("34234234","T"))
SaveKey("34234234","Name","joe")
SaveKey("34234234","Balance",454)
SaveKey("34234234","NotBalance",{"Test":"T"})
print(GetKey("34234234","Name"))

print(GetKey("3243","Name"))


