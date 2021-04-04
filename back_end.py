# testing importing data using a CSV file
import pandas as pd

CSVfile = pd.read_csv(r'C:\Users\isaac\Desktop\testMultiples.csv')

#value = CSVfile._get_value(14, 'Purdue')
#value += 1
#print(value)

# end of testing for CSV file


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
        self.totalFacultyCases = 0
        self.dateOfReopening = ""
        self.universityVaccinationRate = 0
        self.hybridLearningAvailability = None
        self.quarantineAvailability = None
        self.surveillanceTestingPercent = 0
        self.universityPopulation = 0
        self.classEventCapacity = 0
        self.county = ""
        self.countyPopulation = 0
        self.countyTotal = 0
        self.countyDeaths = 0
        self.countyTotalPositiveCases = 0
        self.state = ""
        self.fullyVaccinatedRate = 0


# list that holds the names of each Big 10 school
nameList = ["Purdue", "Northwestern", "UIUC", "IU", "Wisconsin", "Michigan", "Michigan State", "Penn State", "OSU",
            "Nebraska", "Minnesota", "Rutgers", "Maryland", "Iowa"]

# list that will hold the school objects for each Big 10 School
schoolList = []


#make sure the numbers are using the general style without commas

for i in range(14):
    #to get CSV row subtract three from row number in sheets
    tempSchool = School(nameList[i], int(CSVfile._get_value(13, nameList[i])), int(CSVfile._get_value(14, nameList[i])))
    schoolList.append(tempSchool)

for i in range(14):
    print(schoolList[i].name)
    print(schoolList[i].totalTests)
    print(schoolList[i].totalCases)


