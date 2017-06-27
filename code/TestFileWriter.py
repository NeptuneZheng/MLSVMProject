import time

from code import IPDictionary


def testFileWriter(filePath,override):
    if(override):
        testFile = open("data/test.txt","w")
    else:
        testFile = open("data/test.txt","a")
    dict={}
    cityCount = 0
    with open(filePath) as ifile:
        for line in ifile:
            arrs = line.strip().split("*")
            if(len(arrs[0])>3):
                timeZone = time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(arrs[0],"%Y-%m-%dT%H:%M:%S"))
                IPCity = IPDictionary.getIPCity(arrs[1])

                #convert City name to number for analysis
                if(dict[IPCity]):
                    cityNum = dict[IPCity]
                else:
                    cityCount+=1
                    cityNum = cityCount
                    dict[IPCity]=cityCount

                string = str(timeZone)+"*"+cityNum+"*"+arrs[2]+"\n"
                testFile.write(string)
        testFile.close()

# testFileWriter("data/source.txt",False)