import json
import requests
from contextlib import suppress

# get the ticker from the ticker list
ticker = "AAPL"

# Yahoo Finance API
def yahooFinanceApiSetup():

    # calling the API
    urlBody = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"
    moduleQ = "?modules="
    modulesList = ["assetProfile", "incomeStatementHistory", "incomeStatementHistoryQuarterly", "balanceSheetHistory", "balanceSheetHistoryQuarterly",
                               "cashFlowStatementHistory", "cashFlowStatementHistoryQuarterly", "defaultKeyStatistics", "financialData", "calendarEvents",
                               "secFilings", "recommendationTrend", "upgradeDowngradeHistory", "institutionOwnership", "fundOwnership", "majorDirectHolders",
                               "majorHoldersBreakdown", "insiderTransactions", "insiderHolders", "netSharePurchaseActivity", "earnings", "earningsHistory",
                               "earningsTrend", "industryTrend", "indexTrend", "sectorTrend", "esgScores", "summaryDetail"," summaryProfile", "price"]
                                # Modules list [0-29]
    modules = {"defaultKeyStatistics": modulesList[7], "financialData": modulesList[8], "majorHoldersBreakdown": modulesList[16],
               "netSharePurchaseActivity": modulesList[19], "esgScores": modulesList[26], "summaryDetail": modulesList[27]}

    queryBody = urlBody + ticker + moduleQ
    return modules, queryBody

#Financial Modelling Prep API
def fmpApiSetup():

    # calling the API
    urlBody = "https://financialmodelingprep.com/api/v3/"
    modulesList = ["ratios", "key-metrics-ttm", "key-executives", "analyst-estimates"] #Modules list [0-X!]
    modules = {"ratios": modulesList[0], "key-metrics-ttm": modulesList[1], "key-executives": modulesList[2], "analyst-estimates": modulesList[3]}

    key = "KEYGOESHERE"
    return urlBody, modules, key

#Getting the data from Yahoo Finance
def getYahooFinanceData():
    modules, queryBody = yahooFinanceApiSetup()

    # 'defaultKeyStatistics' data points
    try: # instead of 'try', 'except', can use 'with suppress(Exception):'
        # Converting API response to json
        response = requests.get(queryBody + modules['defaultKeyStatistics'])
        data = response.text
        parsed = json.loads(data)

        #API response directory
        responseDirectory = parsed['quoteSummary']['result'][0][modules['defaultKeyStatistics']]
    except (Exception): 
        print(modules['defaultKeyStatistics'] + " is missing")

    # Data points
    try:
        priceToBook = responseDirectory['priceToBook']['fmt']
    except (Exception):
        priceToBook = "is missing"
    finally:
        priceToBook = priceToBook
    try:
        pegRatio = responseDirectory['pegRatio']['fmt']
    except (Exception):
        pegRatio = "is missing"
    finally:
        pegRatio = pegRatio
    try:
        forwardEps = responseDirectory['forwardEps']['fmt']
    except (Exception):
        forwardEps = "is missing"
    finally:
        forwardEps = forwardEps

    # 'financialData' data points
    try:
        response = requests.get(queryBody + modules['financialData'])
        data = response.text
        parsed = json.loads(data)
        responseDirectory = parsed['quoteSummary']['result'][0][modules['financialData']]
    except (Exception):
        print(modules['financialData'] + " is missing")
    try:
        debtToEquity = responseDirectory['debtToEquity']['fmt']
    except (Exception):
        debtToEquity = "is missing"
    finally:
        debtToEquity = debtToEquity
    try:
        quickRatio = responseDirectory['quickRatio']['fmt']
    except (Exception):
        quickRatio = "is missing"
    finally:
        quickRatio = quickRatio
    try:
        returnOnEquity = responseDirectory['returnOnEquity']['fmt']
    except (Exception):
        returnOnEquity = "is missing"
    finally:
        returnOnEquity = returnOnEquity

    # 'majorHoldersBreakdown' data points
    try:
        response = requests.get(queryBody + modules['majorHoldersBreakdown'])
        data = response.text
        parsed = json.loads(data)
        responseDirectory = parsed['quoteSummary']['result'][0][modules['majorHoldersBreakdown']]
    except (Exception):
        print(modules['majorHoldersBreakdown'] + " is missing")
    try:
        institutionsPercentHeld = responseDirectory['institutionsPercentHeld']['fmt']
    except (Exception):
        institutionsPercentHeld = "is missing"
    finally:
        institutionsPercentHeld = institutionsPercentHeld
    try:
        insidersPercentHeld = responseDirectory['insidersPercentHeld']['fmt']
    except (Exception):
        insidersPercentHeld = "is missing"
    finally:
        insidersPercentHeld = insidersPercentHeld

    # 'netSharePurchaseActivity' data points
    try:
        response = requests.get(queryBody + modules['netSharePurchaseActivity'])
        data = response.text
        parsed = json.loads(data)
        responseDirectory = parsed['quoteSummary']['result'][0][modules['netSharePurchaseActivity']]
    except (Exception):
        print(modules['netSharePurchaseActivity'] + " is missing")
    try:
        buyPercentInsiderShares = responseDirectory['buyPercentInsiderShares']['raw']
    except (Exception):
        buyPercentInsiderShares = "is missing"
    finally:
        buyPercentInsiderShares = buyPercentInsiderShares
    try:
        sellPercentInsiderShares = responseDirectory['sellPercentInsiderShares']['raw']
    except (Exception):
        sellPercentInsiderShares = "is missing"
    finally:
        sellPercentInsiderShares = sellPercentInsiderShares
    try:
        insidersBuySellRatio = buyPercentInsiderShares/sellPercentInsiderShares
    except (Exception):
        insidersBuySellRatio = "is missing"
    finally:
        insidersBuySellRatio = insidersBuySellRatio

    # 'esgScores' data points
    try:
        response = requests.get(queryBody + modules['esgScores'])
        data = response.text
        parsed = json.loads(data)
        responseDirectory = parsed['quoteSummary']['result'][0][modules['esgScores']]
    except (Exception):
        print(modules['esgScores'] + " is missing")
    try:
        environmentScore = responseDirectory['environmentScore']['fmt']
    except (Exception):
        environmentScore = "is missing"
    finally:
        environmentScore = environmentScore
    try:
        socialScore = responseDirectory['socialScore']['fmt']
    except (Exception):
        socialScore = "is missing"
    finally:
        socialScore = socialScore
    try:
        governanceScore = responseDirectory['governanceScore']['fmt']
    except (Exception):
        governanceScore = "is missing"
    finally:
        governanceScore = governanceScore

    # 'summaryDetail' data points
    try:
        response = requests.get(queryBody + modules['summaryDetail'])
        data = response.text
        parsed = json.loads(data)
        responseDirectory = parsed['quoteSummary']['result'][0][modules['summaryDetail']]
    except (Exception):
        print("Houston have a problem6...")
    try:
        trailingPE = responseDirectory['trailingPE']['fmt']
    except (Exception):
        trailingPE = "is missing"
    finally:
        trailingPE = trailingPE

    # Data points dictionary
    yahooFinanceData = {"priceToBook": priceToBook, "pegRatio": pegRatio, "forwardEps": forwardEps, "debtToEquity": debtToEquity, "quickRatio": quickRatio,
                        "returnOnEquity": returnOnEquity, "institutionsPercentHeld": institutionsPercentHeld, "insidersPercentHeld": insidersPercentHeld,
                        "insidersBuySellRatio": insidersBuySellRatio, "environmentScore": environmentScore, "socialScore": socialScore,
                        "governanceScore": governanceScore, "trailingPE": trailingPE}

    return yahooFinanceData


#Getting the data from Financial Modelling Prep
def getFMPData():
    urlBody, modules, key = fmpApiSetup()

    # 'ratios' data points
    # Converting API response to json
    response = requests.get(urlBody + modules['ratios'] + "/" + ticker + key)
    data = response.text
    parsed = json.loads(data)

    # API response
    try:
        dividendYield = parsed[0]['dividendYield']  #0 is the most recent period, 1 is the previous period etc.... (check if periods are in quarter or year)
    except(Exception):
        dividendYield = "is missing"
    finally:
        dividendYield = dividendYield
    try:
        returnOnCapitalEmployed = parsed[0]['returnOnCapitalEmployed']
    except(Exception):
        returnOnCapitalEmployed = "is missing"
    finally:
        returnOnCapitalEmployed = returnOnCapitalEmployed

    # 'key-executives' data points
    response = requests.get(urlBody + modules['key-executives'] + "/" + ticker + key)
    data = response.text
    parsed = json.loads(data)
    try:
        titleSince = parsed[0]['titleSince'] #need to pay for this datapoint, make sure to add into return and import
    except(Exception):
        titleSince = "is missing"
    finally:
        titleSince = titleSince

    # 'analyst-estimates' data points
    response = requests.get(urlBody + modules['analyst-estimates'] + "/" + ticker + key)
    data = response.text
    parsed = json.loads(data)
    try:
        estimatedEpsAvg = parsed[0]['estimatedEpsAvg'] #need to pay for this datapoint, make sure to add into return and import
    except(Exception):
        estimatedEpsAvg = "is missing"
    finally:
        estimatedEpsAvg = estimatedEpsAvg

    # Data points dictionary
    fmpData = {"dividendYield": dividendYield, "returnOnCapitalEmployed": returnOnCapitalEmployed, "titleSince": titleSince, "estimatedEpsAvg": estimatedEpsAvg}

    return fmpData

def modelScores():
    yahooFinanceData = getYahooFinanceData()
    fmpData = getFMPData()

    #Value Score:
    valueScore = yahooFinanceData, fmpData

    #Growth Score:


    #Health Score:


    #Management Score:

    return valueScore

#Output
valueScore = modelScores()
print(valueScore)