import csv
import json
import time
import DBOperation
import IPDictionary


#if need update the city information by IP, updateIP=True; else updateIP=False
def sourceFielReader(filepath,updateIP):
    csv_reader=csv.reader(open(filepath,encoding="utf-8"))
    for row in csv_reader:
        if(row[2]=="UserLoggedIn"):
            jsonStr=row[3]
            jsonToPython=json.loads(jsonStr)
            if(jsonToPython["ResultStatus"]=="Succeeded"):
                loginDate=jsonToPython["CreationTime"]
                loginIP=jsonToPython["ClientIP"]

                timeZone = time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(loginDate,"%Y-%m-%dT%H:%M:%S"))
                
                IPCity = ""
                if(updateIP):
                    IPCity = IPDictionary.getIPCity(loginIP)
                else:
                    IPCity = DBOperation.findOneRecord({"Ip":loginIP})
                    if(not IPCity):
                        IPCity = IPDictionary.getIPCity(loginIP)
                    
                print(IPCity)

sourceFielReader("../data/IPDictionary.csv",True)



