# Imports and Classes
import openpyxl, json
from datetime import datetime

# Opening JSON file
# f = open('data.json')
# data = json.load(f)
# f.close()
# print(data)

AllGovernmentResponseRecords = None
governmentResponseWB = None
governmentResponseSheet = None

class GovernmentResponseRecord():
    def __init__(self, CountryName, CountryCode, Date, C1_SchoolClosing, C1_Flag, C2_WorkplaceClosing,
                 C2_Flag, C3_CancelPublicEvents, C3_Flag, C4_RestrictionsOnGatherings, C4_Flag,
                 C5_ClosePublicTransport, C5_Flag, C6_StayAtHomeRequirements, C6_Flag, C7_RestrictionsOnInternalMovement,
                 C7_Flag, C8_InternationalTravelControls, E1_IncomeSupport, E1_Flag, E2_DebtAndContractRelief,
                 E3_FiscalMeasures, E4_InternationalSupport, H1_PublicInformationCampaigns, H1_Flag, H2_TestingPolicy,
                 H3_ContactTracing, H4_EmergencyInvestmentInHealthcare, H5_InvestmentInVaccines, H6_FacialCoverings,
                 H6_Flag, H7_VaccinationPolicy, H7_Flag, H8_ProtectionOfElderlyPeople, H8_Flag, M1_Wildcard,
                 V1_VaccinePrioritisationSummary, V2A_VaccineAvailabilitySummary,
                 V2B_VaccineAgeEligibilityGeneralPopulationSummary, V2C_VaccineAgeEligibilityAtRiskSummary,
                 V2D_MedicallyVulnerableNonElderly, V2E_Education, V2F_FrontlineWorkersNonHealthcare,
                 V2G_FrontlineWorkersHealthcare, V3_VaccineFinancialSupportSummary, ConfirmedCases, ConfirmedDeaths,
                 StringencyIndex, StringencyIndexForDisplay, StringencyLegacyIndex, StringencyLegacyIndexForDisplay,
                 GovernmentResponseIndex, GovernmentResponseIndexForDisplay, ContainmentHealthIndex,
                 ContainmentHealthIndexForDisplay, EconomicSupportIndex, EconomicSupportIndexForDisplay):
        self.EconomicSupportIndexForDisplay = EconomicSupportIndexForDisplay
        self.EconomicSupportIndex = EconomicSupportIndex
        self.ContainmentHealthIndexForDisplay = ContainmentHealthIndexForDisplay
        self.ContainmentHealthIndex = ContainmentHealthIndex
        self.GovernmentResponseIndexForDisplay = GovernmentResponseIndexForDisplay
        self.GovernmentResponseIndex = GovernmentResponseIndex
        self.StringencyLegacyIndexForDisplay = StringencyLegacyIndexForDisplay
        self.StringencyLegacyIndex = StringencyLegacyIndex
        self.StringencyIndexForDisplay = StringencyIndexForDisplay
        self.StringencyIndex = StringencyIndex
        if ConfirmedDeaths is None:
            self.ConfirmedDeaths = 0
        else:
            self.ConfirmedDeaths = ConfirmedDeaths
        if ConfirmedCases is None:
            self.ConfirmedCases = 0
        else:
            self.ConfirmedCases = ConfirmedCases
        self.V3_VaccineFinancialSupportSummary = V3_VaccineFinancialSupportSummary
        self.V2G_FrontlineWorkersHealthcare = V2G_FrontlineWorkersHealthcare
        self.V2F_FrontlineWorkersNonHealthcare = V2F_FrontlineWorkersNonHealthcare
        self.V2E_Education = V2E_Education
        self.V2D_MedicallyVulnerableNonElderly = V2D_MedicallyVulnerableNonElderly
        self.V2C_VaccineAgeEligibilityAtRiskSummary = V2C_VaccineAgeEligibilityAtRiskSummary
        self.V2B_VaccineAgeEligibilityGeneralPopulationSummary = V2B_VaccineAgeEligibilityGeneralPopulationSummary
        self.V2A_VaccineAvailabilitySummary = V2A_VaccineAvailabilitySummary
        self.V1_VaccinePrioritisationSummary = V1_VaccinePrioritisationSummary
        self.M1_Wildcard = M1_Wildcard
        self.H8_Flag = H8_Flag
        self.H8_ProtectionOfElderlyPeople = H8_ProtectionOfElderlyPeople
        self.H7_Flag = H7_Flag
        self.H7_VaccinationPolicy = H7_VaccinationPolicy
        self.H6_Flag = H6_Flag
        self.H6_FacialCoverings = H6_FacialCoverings
        self.H5_InvestmentInVaccines = H5_InvestmentInVaccines
        self.H4_EmergencyInvestmentInHealthcare = H4_EmergencyInvestmentInHealthcare
        self.H3_ContactTracing = H3_ContactTracing
        self.H2_TestingPolicy = H2_TestingPolicy
        self.H1_Flag = H1_Flag
        self.H1_PublicInformationCampaigns = H1_PublicInformationCampaigns
        self.E4_InternationalSupport = E4_InternationalSupport
        if E3_FiscalMeasures is None:
            self.E3_FiscalMeasures = None
        else:
            self.E3_FiscalMeasures = E3_FiscalMeasures
        self.E2_DebtAndContractRelief = E2_DebtAndContractRelief
        self.E1_Flag = E1_Flag
        if E1_IncomeSupport is None:
            self.E1_IncomeSupport = 0
        else:
            self.E1_IncomeSupport = E1_IncomeSupport
        self.C8_InternationalTravelControls = C8_InternationalTravelControls
        self.C7_Flag = C7_Flag
        self.C7_RestrictionsOnInternalMovement = C7_RestrictionsOnInternalMovement
        self.C6_Flag = C6_Flag
        self.C6_StayAtHomeRequirements = C6_StayAtHomeRequirements
        self.C5_Flag = C5_Flag
        self.C5_ClosePublicTransport = C5_ClosePublicTransport
        self.C4_Flag = C4_Flag
        self.C4_RestrictionsOnGatherings = C4_RestrictionsOnGatherings
        self.C3_Flag = C3_Flag
        if C3_CancelPublicEvents is None:
            self.C3_CancelPublicEvents = 0
        else:
            self.C3_CancelPublicEvents = C3_CancelPublicEvents
        if C2_Flag is None:
            self.C2_Flag = 0
        else:
            self.C2_Flag = C2_Flag
        if C2_WorkplaceClosing is None:
            self.C2_WorkplaceClosing = None
        else:
            self.C2_WorkplaceClosing = C2_WorkplaceClosing
        self.C1_Flag = C1_Flag
        if C1_SchoolClosing is None:
            self.C1_SchoolClosing = None
        else:
            self.C1_SchoolClosing = C1_SchoolClosing
        self.Date = self.convertDate(Date)
        self.CountryCode = CountryCode
        self.CountryName = CountryName
    def convertDate(self, rawDate):
        s = str(rawDate)
        dateForm = f"{s[4]+s[5]}/{s[6]+s[7]}/{s[0]+s[1]+s[2]+s[3]}"
        return datetime.strptime(dateForm, "%m/%d/%Y")

def getAllGovernmentResponseRecord():
    global AllGovernmentResponseRecords
    if AllGovernmentResponseRecords is not None:
        return AllGovernmentResponseRecords
    else:
        allRecordsList = []
        for i in range(2, governmentResponseSheet.max_row):
            record = GovernmentResponseRecord(governmentResponseSheet[f"A{i}"].value,
                                                    governmentResponseSheet[f"B{i}"].value,
                                                    governmentResponseSheet[f"C{i}"].value,
                                                    governmentResponseSheet[f"D{i}"].value,
                                                    governmentResponseSheet[f"E{i}"].value,
                                                    governmentResponseSheet[f"F{i}"].value,
                                                    governmentResponseSheet[f"G{i}"].value,
                                                    governmentResponseSheet[f"H{i}"].value,
                                                    governmentResponseSheet[f"I{i}"].value,
                                                    governmentResponseSheet[f"J{i}"].value,
                                                    governmentResponseSheet[f"K{i}"].value,
                                                    governmentResponseSheet[f"L{i}"].value,
                                                    governmentResponseSheet[f"M{i}"].value,
                                                    governmentResponseSheet[f"N{i}"].value,
                                                    governmentResponseSheet[f"O{i}"].value,
                                                    governmentResponseSheet[f"P{i}"].value,
                                                    governmentResponseSheet[f"Q{i}"].value,
                                                    governmentResponseSheet[f"R{i}"].value,
                                                    governmentResponseSheet[f"S{i}"].value,
                                                    governmentResponseSheet[f"T{i}"].value,
                                                    governmentResponseSheet[f"U{i}"].value,
                                                    governmentResponseSheet[f"V{i}"].value,
                                                    governmentResponseSheet[f"W{i}"].value,
                                                    governmentResponseSheet[f"X{i}"].value,
                                                    governmentResponseSheet[f"Y{i}"].value,
                                                    governmentResponseSheet[f"Z{i}"].value,
                                                    governmentResponseSheet[f"AA{i}"].value,
                                                    governmentResponseSheet[f"AB{i}"].value,
                                                    governmentResponseSheet[f"AC{i}"].value,
                                                    governmentResponseSheet[f"AD{i}"].value,
                                                    governmentResponseSheet[f"AE{i}"].value,
                                                    governmentResponseSheet[f"AF{i}"].value,
                                                    governmentResponseSheet[f"AG{i}"].value,
                                                    governmentResponseSheet[f"AH{i}"].value,
                                                    governmentResponseSheet[f"AI{i}"].value,
                                                    governmentResponseSheet[f"AJ{i}"].value,
                                                    governmentResponseSheet[f"AK{i}"].value,
                                                    governmentResponseSheet[f"AL{i}"].value,
                                                    governmentResponseSheet[f"AM{i}"].value,
                                                    governmentResponseSheet[f"AN{i}"].value,
                                                    governmentResponseSheet[f"AO{i}"].value,
                                                    governmentResponseSheet[f"AP{i}"].value,
                                                    governmentResponseSheet[f"AQ{i}"].value,
                                                    governmentResponseSheet[f"AR{i}"].value,
                                                    governmentResponseSheet[f"AS{i}"].value,
                                                    governmentResponseSheet[f"AT{i}"].value,
                                                    governmentResponseSheet[f"AU{i}"].value,
                                                    governmentResponseSheet[f"AV{i}"].value,
                                                    governmentResponseSheet[f"AW{i}"].value,
                                                    governmentResponseSheet[f"AX{i}"].value,
                                                    governmentResponseSheet[f"AY{i}"].value,
                                                    governmentResponseSheet[f"AZ{i}"].value,
                                                    governmentResponseSheet[f"BA{i}"].value,
                                                    governmentResponseSheet[f"BB{i}"].value,
                                                    governmentResponseSheet[f"BC{i}"].value,
                                                    governmentResponseSheet[f"BD{i}"].value,
                                                    governmentResponseSheet[f"BE{i}"].value)
            allRecordsList.append(record)
        AllGovernmentResponseRecords = allRecordsList
        return allRecordsList

def getByCountry(countryName):
    global AllGovernmentResponseRecords
    if AllGovernmentResponseRecords is None:
        AllGovernmentResponseRecords = getAllGovernmentResponseRecord()
    returnList = []
    for record in AllGovernmentResponseRecords:
        if record.CountryName.lower() == countryName.lower():
            returnList.append(record)
    return returnList

def load():
    global governmentResponseWB
    global governmentResponseSheet
    """
        load function loads the sheets which can take much time.
        If you do not need to access GovernmentResponseRecords, do not load it.
    """
    governmentResponseWB = openpyxl.load_workbook("Oxford_covid_government_response_variables.xlsx")
    governmentResponseSheet = governmentResponseWB["Data"]

def getByHDI(lowerBound, upperBound):
    global AllGovernmentResponseRecords
    # Opening JSON file
    f = open('data.json')
    data = json.load(f)
    f.close()

    returnList = []
    for record in AllGovernmentResponseRecords:
        code = record.CountryCode.lower()
        if code in data.keys():
            hdi = data[code]
            if hdi is not None:
                if hdi >= lowerBound and hdi <= upperBound:
                    returnList.append(record)
    return returnList