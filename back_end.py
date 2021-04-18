# testing importing data using a CSV file
import pandas as pd
import numpy as np

CSVfile = pd.read_csv('https://docs.google.com/spreadsheets/d/1LFbQ4c64YoRfpRhSXPihPnMzPJ4v3SjFUB-tx5XgRjs/export?gid=1898114679&format=csv')

#value = CSVfile._get_value(14, 'Purdue')
#value += 1
#print(value)

# end of testing for CSV file

#data should be a 2 row matrix
#Converts 2 row matrix to dictionary
def TwoLineCSVtoDict(data):
  dataT = np.transpose(data)
  cases_dict = {}
  for i in range(len(dataT)):
    for j in range(2):
      cases_dict[dataT[i][0]] = dataT[i][j]
  return cases_dict

class School:
    def __init__(self, name, totalTests, totalCases):
        self.name = name
        self.totalTests = totalTests
        self.totalCases = totalCases
        self.fallStudentCases = 0
        self.fallFacultyCases = 0
        self.springTotalTests = 0
        self.springStudentCases = 0
        self.springFacultyCases = 0
        self.totalStudentTests = 0
        self.totalStudentCases = 0
        self.totalFacultyTests = 0
        self.positivityRate = 0
        self.totalFacultyCases = 0
        self.dateOfReopening = ""
        self.universityVaccinationRate = 0
        self.hybridLearningAvailability = None
        self.quarantineAvailability = None
        self.surveillanceTestingPercent = 0
        self.universityPopulation = 0
        self.classEventCapacity = 0
        self.countyName = ""
        self.countyPopulation = 0
        self.countyTotal = 0
        self.countyDeaths = 0
        self.countyTotalPositiveCases = 0
        self.state = ""
        self.statePopulation = ""
        self.stateDeaths = ""
        self.stateTotalPositiveCases = ""
        self.statePositivityRate = ""
        self.stateDeathRate = ""
        self.stateDeathToPositiveCases = ""
        self.fullyVaccinatedRate = 0


# list that holds the names of each Big 10 school
nameList = ["Purdue", "Northwestern", "UIUC", "IU", "Wisconsin", "Michigan", "Michigan State", "Penn State", "OSU",
            "Nebraska", "Minnesota", "Rutgers", "Maryland", "Iowa"]

# list that will hold the school objects for each Big 10 School
schoolList = []


#make sure the numbers are using the general style without commas
#change range for both loops back to 14 when all the school data has been entered

for i in range(14):
    #to get CSV row subtract two from row number in sheets
    tempSchool = School(nameList[i], int(CSVfile._get_value(1, nameList[i])), int(CSVfile._get_value(2, nameList[i])))

    for j in range(15):
        index = j + 3
        if index == 3:
            tempSchool.positivityRate = CSVfile._get_value(index, nameList[i])
        if index == 4:
            tempSchool.dateOfReopening = CSVfile._get_value(index, nameList[i])
        if index == 5:
            tempSchool.universityPopulation = CSVfile._get_value(index, nameList[i])
        if index == 6:
            tempSchool.countyName = CSVfile._get_value(index, nameList[i])
        if index == 7:
            tempSchool.countyPopulation = CSVfile._get_value(index, nameList[i])
        if index == 8:
            tempSchool.countyDeaths = CSVfile._get_value(index, nameList[i])
        if index == 9:
            tempSchool.countyTotalPositiveCases = CSVfile._get_value(index, nameList[i])
        if index == 10:
            tempSchool.state = CSVfile._get_value(index, nameList[i])
        if index == 11:
            tempSchool.fullyVaccinatedRate = CSVfile._get_value(index, nameList[i])
        if index == 12:
            tempSchool.statePopulation = CSVfile._get_value(index, nameList[i])
        if index == 13:
            tempSchool.stateDeaths = CSVfile._get_value(index, nameList[i])
        if index == 14:
            tempSchool.stateTotalPositiveCases = CSVfile._get_value(index, nameList[i])
        if index == 15:
            tempSchool.statePositivityRate = CSVfile._get_value(index, nameList[i])
        if index == 16:
            tempSchool.stateDeathRate = CSVfile._get_value(index, nameList[i])
        if index == 17:
            tempSchool.stateDeathToPositiveCases = CSVfile._get_value(index, nameList[i])

    schoolList.append(tempSchool)


for i in range(14):
    print(schoolList[i].name)
    print(schoolList[i].totalTests)
    print(schoolList[i].totalCases)
    print(schoolList[i].positivityRate)
    print(schoolList[i].stateDeathToPositiveCases)
