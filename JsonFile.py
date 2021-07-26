import json
import os
import glob
from os import path
from pandas import json_normalize
sourceJson = "/Users/satchidanandatripathy/Desktop/STUDY/Python/Python/input/sample.json" # give the source file path and the name
targetCSV = "/Users/satchidanandatripathy/Desktop/STUDY/Python/Python/input/tgt_" #give the intended target file path and names, it will create sub files with this name

#This function first check if the target file has already created if yes it will append data in to it else create new target with normalized data
#first arguement is a dictionary (source data will be converted to a dictionary) and second arguement is blank in the first iteration
def normalize(normInput, name):
    normOutput = json_normalize(normInput)
    #normOutput is a dataframe which will keep normalized data from the source file in tabular format. 
    if path.exists(f"{targetCSV}{name}.csv"):
        normOutput.to_csv(f"{targetCSV}{name}.csv", mode='a', header=False)
    else:
        normOutput.to_csv(f"{targetCSV}{name}.csv")
    checkData(normOutput)

def checkData(checkItem):
    for rows in range(len(checkItem)):
        for itemctr in range(len(checkItem[checkItem.columns].to_numpy()[rows])):
            if isinstance(checkItem[checkItem.columns].to_numpy()[rows][itemctr], (list, tuple)):
                for each in checkItem[checkItem.columns].to_numpy()[rows][itemctr]:
                    if isinstance(each, dict):
                        normalize(each, checkItem.columns[itemctr])
# glob function will fetch all the files with matching name pattern and put in a list
fileList = glob.glob(f"{targetCSV}*.csv")
for file in fileList:
    try:
        os.remove(file)
    except:
        print('')
f = open(sourceJson,'r')
#the load() function convert the json into python dictionary object with key and value pair.
#json object will become dict  array will become list
#string	str number (int)	int number (real)	float
#true	True false	False null	None
data = json.load(f)
normalize(data,"")
f.close()