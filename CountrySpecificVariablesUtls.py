# Imports and Classes
import openpyxl

countrySpecificVariablesWB = None
countrySpecificVariablesSheet = None
AllCountrySpecificVariablesRecords = None

class CountrySpecificVariablesRecord():
    def __init__(self, iso_code, continent, location, date, total_cases,
                 new_cases, new_cases_smoothed, total_deaths, new_deaths, new_deaths_smoothed,
                 total_cases_per_million, new_cases_per_million, new_cases_smoothed_per_million,
                 total_deaths_per_million, new_deaths_per_million, new_deaths_smoothed_per_million,
                 reproduction_rate, icu_patients, icu_patients_per_million, hosp_patients,
                 hosp_patients_per_million, weekly_icu_admissions, weekly_icu_admissions_per_million,
                 weekly_hosp_admissions, weekly_hosp_admissions_per_million, new_tests, total_tests,
                 total_tests_per_thousand, new_tests_per_thousand, new_tests_smoothed,
                 new_tests_smoothed_per_thousand, positive_rate, tests_per_case, tests_units,
                 total_vaccinations, people_vaccinated, people_fully_vaccinated, total_boosters,
                 new_vaccinations, new_vaccinations_smoothed, total_vaccinations_per_hundred,
                 people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred,
                 total_boosters_per_hundred, new_vaccinations_smoothed_per_million,
                 new_people_vaccinated_smoothed, new_people_vaccinated_smoothed_per_hundred,
                 stringency_index, population, population_density, median_age, aged_65_older,
                 aged_70_older, gdp_per_capita, extreme_poverty, cardiovasc_death_rate, diabetes_prevalence,
                 female_smokers, male_smokers, handwashing_facilities, hospital_beds_per_thousand,
                 life_expectancy, human_development_index, excess_mortality_cumulative_absolute,
                 excess_mortality_cumulative, excess_mortality, excess_mortality_cumulative_per_million
                 ):
        self.excess_mortality_cumulative_per_million = excess_mortality_cumulative_per_million
        self.excess_mortality = excess_mortality
        self.excess_mortality_cumulative = excess_mortality_cumulative
        self.excess_mortality_cumulative_absolute = excess_mortality_cumulative_absolute
        self.human_development_index = human_development_index
        self.life_expectancy = life_expectancy
        self.hospital_beds_per_thousand = hospital_beds_per_thousand
        self.handwashing_facilities = handwashing_facilities
        self.male_smokers = male_smokers
        self.female_smokers = female_smokers
        self.diabetes_prevalence = diabetes_prevalence
        self.cardiovasc_death_rate = cardiovasc_death_rate
        self.extreme_poverty = extreme_poverty
        self.gdp_per_capita = gdp_per_capita
        self.aged_70_older = aged_70_older
        self.aged_65_older = aged_65_older
        self.median_age = median_age
        self.population_density = population_density
        self.population = population
        self.stringency_index = stringency_index
        self.new_people_vaccinated_smoothed_per_hundred = new_people_vaccinated_smoothed_per_hundred
        self.new_people_vaccinated_smoothed = new_people_vaccinated_smoothed
        self.new_vaccinations_smoothed_per_million = new_vaccinations_smoothed_per_million
        self.total_boosters_per_hundred = total_boosters_per_hundred
        self.people_fully_vaccinated_per_hundred = people_fully_vaccinated_per_hundred
        self.people_vaccinated_per_hundred = people_vaccinated_per_hundred
        self.total_vaccinations_per_hundred = total_vaccinations_per_hundred
        self.new_vaccinations_smoothed = new_vaccinations_smoothed
        self.new_vaccinations = new_vaccinations
        self.total_boosters = total_boosters
        self.people_fully_vaccinated = people_fully_vaccinated
        if people_vaccinated is None:
            self.people_vaccinated = 0
        else:
            self.people_vaccinated = people_vaccinated
        self.total_vaccinations = total_vaccinations
        self.tests_units = tests_units
        self.tests_per_case = tests_per_case
        self.positive_rate = positive_rate
        self.new_tests_smoothed_per_thousand = new_tests_smoothed_per_thousand
        self.new_tests_smoothed = new_tests_smoothed
        self.new_tests_per_thousand = new_tests_per_thousand
        self.total_tests_per_thousand = total_tests_per_thousand
        self.total_tests = total_tests
        self.new_tests = new_tests
        self.weekly_hosp_admissions_per_million = weekly_hosp_admissions_per_million
        if weekly_hosp_admissions is None:
            self.weekly_hosp_admissions = 0
        else:
            self.weekly_hosp_admissions = weekly_hosp_admissions
        self.weekly_icu_admissions_per_million = weekly_icu_admissions_per_million
        self.weekly_icu_admissions = weekly_icu_admissions
        self.hosp_patients_per_million = hosp_patients_per_million
        if hosp_patients is None:
            self.hosp_patients = 0
        else:
            self.hosp_patients = hosp_patients
        self.icu_patients_per_million = icu_patients_per_million
        self.icu_patients = icu_patients
        self.reproduction_rate = reproduction_rate
        self.new_deaths_smoothed_per_million = new_deaths_smoothed_per_million
        self.new_deaths_per_million = new_deaths_per_million
        self.total_deaths_per_million = total_deaths_per_million
        self.new_cases_smoothed_per_million = new_cases_smoothed_per_million
        self.new_cases_per_million = new_cases_per_million
        self.total_cases_per_million = total_cases_per_million
        if new_deaths_smoothed is None:
            self.new_deaths_smoothed = 0
        else:
            self.new_deaths_smoothed = new_deaths_smoothed
        self.new_deaths = new_deaths
        if total_deaths is None:
            self.total_deaths = 0
        else:
            self.total_deaths = total_deaths
        if new_cases_smoothed is None:
            self.new_cases_smoothed = 0
        else:
            self.new_cases_smoothed = new_cases_smoothed
        if new_cases is None:
            self.new_cases = 0
        else:
            self.new_cases = new_cases
        if total_cases is None:
            self.total_cases = 0
        else:
            self.total_cases = total_cases
        self.date = date
        self.location = location
        self.continent = continent
        self.iso_code = iso_code

    def toString(self):
        string = f"""excess_mortality_cumulative_per_million={self.excess_mortality_cumulative_per_million}\n
        excess_mortality={self.excess_mortality}\n
        excess_mortality_cumulative={self.excess_mortality_cumulative}\n
        excess_mortality_cumulative_absolute={self.excess_mortality_cumulative_absolute}\n
        human_development_index={self.human_development_index}\n
        life_expectancy={self.life_expectancy}\n
        hospital_beds_per_thousand={self.hospital_beds_per_thousand}\n
        handwashing_facilities={self.handwashing_facilities}\n
        male_smokers={self.male_smokers}\n
        female_smokers={self.female_smokers}\n
        diabetes_prevalence={self.diabetes_prevalence}\n
        cardiovasc_death_rate={self.cardiovasc_death_rate}\n
        extreme_poverty={self.extreme_poverty}\n
        gdp_per_capita={self.gdp_per_capita}\n
        aged_70_older={self.aged_70_older}\n
        aged_65_older={self.aged_65_older}\n
        median_age={self.median_age}\n
        population_density={self.population_density}\n
        population={self.population}\n
        stringency_index={self.stringency_index}\n
        new_people_vaccinated_smoothed_per_hundred={self.new_people_vaccinated_smoothed_per_hundred}\n
        new_people_vaccinated_smoothed={self.new_people_vaccinated_smoothed}\n
        new_vaccinations_smoothed_per_million={self.new_vaccinations_smoothed_per_million}\n
        total_boosters_per_hundred={self.total_boosters_per_hundred}\n
        people_fully_vaccinated_per_hundred={self.people_fully_vaccinated_per_hundred}\n
        people_vaccinated_per_hundred={self.people_vaccinated_per_hundred}\n
        total_vaccinations_per_hundred={self.total_vaccinations_per_hundred}\n
        new_vaccinations_smoothed={self.new_vaccinations_smoothed}\n
        new_vaccinations={self.new_vaccinations}\n
        total_boosters={self.total_boosters}\n
        people_fully_vaccinated={self.people_fully_vaccinated}\n
        people_vaccinated={self.people_vaccinated}\n
        total_vaccinations={self.total_vaccinations}\n
        tests_units={self.tests_units}\n
        tests_per_case={self.tests_per_case}\n
        positive_rate={self.positive_rate}\n
        new_tests_smoothed_per_thousand={self.new_tests_smoothed_per_thousand}\n
        new_tests_smoothed={self.new_tests_smoothed}\n
        new_tests_per_thousand={self.new_tests_per_thousand}\n
        total_tests_per_thousand={self.total_tests_per_thousand}\n
        total_tests={self.total_tests}\n
        new_tests={self.new_tests}\n
        weekly_hosp_admissions_per_million={self.weekly_hosp_admissions_per_million}\n
        weekly_hosp_admissions={self.weekly_hosp_admissions}\n
        weekly_icu_admissions_per_million={self.weekly_icu_admissions_per_million}\n
        weekly_icu_admissions={self.weekly_icu_admissions}\n
        hosp_patients_per_million={self.hosp_patients_per_million}\n
        hosp_patients={self.hosp_patients}\n
        icu_patients_per_million={self.icu_patients_per_million}\n
        icu_patients={self.icu_patients}\n
        reproduction_rate={self.reproduction_rate}\n
        new_deaths_smoothed_per_million={self.new_deaths_smoothed_per_million}\n
        new_deaths_per_million={self.new_deaths_per_million}\n
        total_deaths_per_million={self.total_deaths_per_million}\n
        new_cases_smoothed_per_million={self.new_cases_smoothed_per_million}\n
        new_cases_per_million={self.new_cases_per_million}\n
        total_cases_per_million={self.total_cases_per_million}\n
        new_deaths_smoothed={self.new_deaths_smoothed}\n
        new_deaths={self.new_deaths}\n
        total_deaths={self.total_deaths}\n
        new_cases_smoothed={self.new_cases_smoothed}\n
        new_cases={self.new_cases}\n
        total_cases={self.total_cases}\n
        date={self.date}\n
        location={self.location}\n
        continent={self.continent}\n
        iso_code={self.iso_code}\n"""
        return string

def getAllCountrySpecificVariablesRecords():
    global AllCountrySpecificVariablesRecords
    if AllCountrySpecificVariablesRecords is not None:
        return AllCountrySpecificVariablesRecords
    else:
        allRecordsList = []
        for i in range(2, countrySpecificVariablesSheet.max_row):
            record = CountrySpecificVariablesRecord(countrySpecificVariablesSheet[f"A{i}"].value,
                                                    countrySpecificVariablesSheet[f"B{i}"].value,
                                                    countrySpecificVariablesSheet[f"C{i}"].value,
                                                    countrySpecificVariablesSheet[f"D{i}"].value,
                                                    countrySpecificVariablesSheet[f"E{i}"].value,
                                                    countrySpecificVariablesSheet[f"F{i}"].value,
                                                    countrySpecificVariablesSheet[f"G{i}"].value,
                                                    countrySpecificVariablesSheet[f"H{i}"].value,
                                                    countrySpecificVariablesSheet[f"I{i}"].value,
                                                    countrySpecificVariablesSheet[f"J{i}"].value,
                                                    countrySpecificVariablesSheet[f"K{i}"].value,
                                                    countrySpecificVariablesSheet[f"L{i}"].value,
                                                    countrySpecificVariablesSheet[f"M{i}"].value,
                                                    countrySpecificVariablesSheet[f"N{i}"].value,
                                                    countrySpecificVariablesSheet[f"O{i}"].value,
                                                    countrySpecificVariablesSheet[f"P{i}"].value,
                                                    countrySpecificVariablesSheet[f"Q{i}"].value,
                                                    countrySpecificVariablesSheet[f"R{i}"].value,
                                                    countrySpecificVariablesSheet[f"S{i}"].value,
                                                    countrySpecificVariablesSheet[f"T{i}"].value,
                                                    countrySpecificVariablesSheet[f"U{i}"].value,
                                                    countrySpecificVariablesSheet[f"V{i}"].value,
                                                    countrySpecificVariablesSheet[f"W{i}"].value,
                                                    countrySpecificVariablesSheet[f"X{i}"].value,
                                                    countrySpecificVariablesSheet[f"Y{i}"].value,
                                                    countrySpecificVariablesSheet[f"Z{i}"].value,
                                                    countrySpecificVariablesSheet[f"AA{i}"].value,
                                                    countrySpecificVariablesSheet[f"AB{i}"].value,
                                                    countrySpecificVariablesSheet[f"AC{i}"].value,
                                                    countrySpecificVariablesSheet[f"AD{i}"].value,
                                                    countrySpecificVariablesSheet[f"AE{i}"].value,
                                                    countrySpecificVariablesSheet[f"AF{i}"].value,
                                                    countrySpecificVariablesSheet[f"AG{i}"].value,
                                                    countrySpecificVariablesSheet[f"AH{i}"].value,
                                                    countrySpecificVariablesSheet[f"AI{i}"].value,
                                                    countrySpecificVariablesSheet[f"AJ{i}"].value,
                                                    countrySpecificVariablesSheet[f"AK{i}"].value,
                                                    countrySpecificVariablesSheet[f"AL{i}"].value,
                                                    countrySpecificVariablesSheet[f"AM{i}"].value,
                                                    countrySpecificVariablesSheet[f"AN{i}"].value,
                                                    countrySpecificVariablesSheet[f"AO{i}"].value,
                                                    countrySpecificVariablesSheet[f"AP{i}"].value,
                                                    countrySpecificVariablesSheet[f"AQ{i}"].value,
                                                    countrySpecificVariablesSheet[f"AR{i}"].value,
                                                    countrySpecificVariablesSheet[f"AS{i}"].value,
                                                    countrySpecificVariablesSheet[f"AT{i}"].value,
                                                    countrySpecificVariablesSheet[f"AU{i}"].value,
                                                    countrySpecificVariablesSheet[f"AV{i}"].value,
                                                    countrySpecificVariablesSheet[f"AW{i}"].value,
                                                    countrySpecificVariablesSheet[f"AX{i}"].value,
                                                    countrySpecificVariablesSheet[f"AY{i}"].value,
                                                    countrySpecificVariablesSheet[f"AZ{i}"].value,
                                                    countrySpecificVariablesSheet[f"BA{i}"].value,
                                                    countrySpecificVariablesSheet[f"BB{i}"].value,
                                                    countrySpecificVariablesSheet[f"BC{i}"].value,
                                                    countrySpecificVariablesSheet[f"BD{i}"].value,
                                                    countrySpecificVariablesSheet[f"BE{i}"].value,
                                                    countrySpecificVariablesSheet[f"BF{i}"].value,
                                                    countrySpecificVariablesSheet[f"BG{i}"].value,
                                                    countrySpecificVariablesSheet[f"BH{i}"].value,
                                                    countrySpecificVariablesSheet[f"BI{i}"].value,
                                                    countrySpecificVariablesSheet[f"BJ{i}"].value,
                                                    countrySpecificVariablesSheet[f"BK{i}"].value,
                                                    countrySpecificVariablesSheet[f"BL{i}"].value,
                                                    countrySpecificVariablesSheet[f"BM{i}"].value,
                                                    countrySpecificVariablesSheet[f"BN{i}"].value,
                                                    countrySpecificVariablesSheet[f"BO{i}"].value)
            allRecordsList.append(record)
        AllCountrySpecificVariablesRecords = allRecordsList
        return allRecordsList

def getByCountry(iso_code):
    global AllCountrySpecificVariablesRecords
    if AllCountrySpecificVariablesRecords is None:
        AllCountrySpecificVariablesRecords = getAllCountrySpecificVariablesRecords()
    returnList = []
    for record in AllCountrySpecificVariablesRecords:
        if record.iso_code.lower() == iso_code.lower():
            returnList.append(record)
    return returnList

def getByHumanDevelopmentIndex(lowerBound, upperBound):
    """
    The smallest Niger with .394 and largest Norway .957

    Gets all records of a certain HDI, doesn't include records with Null
    :param lowerBound: The lower bound of which the % will be used, inclusive, must be 0 <= lowerBound <= 1
    :param upperBound: The uppder bound of which the % will be used, inclusive, must be 0 <= upperBound <= 1
    :return: All the records >= to the lowerbound, but <= to the upperbound
    """
    global AllCountrySpecificVariablesRecords
    if AllCountrySpecificVariablesRecords is None:
        AllCountrySpecificVariablesRecords = getAllCountrySpecificVariablesRecords()
    returnList = []
    for record in AllCountrySpecificVariablesRecords:
        if record.human_development_index is not None:
            if record.human_development_index >= lowerBound and record.human_development_index <= upperBound:
                returnList.append(record)
    return returnList

def load():
    global countrySpecificVariablesWB
    global countrySpecificVariablesSheet
    """
        load function loads the sheets which can take much time.
        If you do not need to access CountrySpecificVariablesRecords, do not load it.
    """
    countrySpecificVariablesWB = openpyxl.load_workbook("Covid_variables_and_country_specific_variables.xlsx")
    countrySpecificVariablesSheet = countrySpecificVariablesWB["data"]
