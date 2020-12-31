import json
import requests

# get the ticker from the ticker list
ticker = "AAPL"  # this can be done programmatically from an array of all stock tickers but for now just set to AAPL.

# Yahoo Finance API
def yahooFinanceApi():

    # calling the API
    urlBody = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"
    moduleQ = "?modules="
    modules = ["assetProfile", "incomeStatementHistory", "incomeStatementHistoryQuarterly", "balanceSheetHistory", "balanceSheetHistoryQuarterly",
                               "cashFlowStatementHistory", "cashFlowStatementHistoryQuarterly", "defaultKeyStatistics", "financialData", "calendarEvents",
                               "secFilings", "recommendationTrend", "upgradeDowngradeHistory", "institutionOwnership", "fundOwnership", "majorDirectHolders",
                               "majorHoldersBreakdown", "insiderTransactions", "insiderHolders", "netSharePurchaseActivity", "earnings", "earningsHistory",
                               "earningsTrend", "industryTrend", "indexTrend", "sectorTrend", "esgScores", "summaryDetail"," summaryProfile", "price"]
                                # Modules list [0-29]
    return urlBody, moduleQ, modules

#Financial Modelling Prep API
def fmpApi():

    # calling the API
    urlBody = "https://financialmodelingprep.com/api/v3/"
    modules = ["ratios", "key-metrics-ttm", "key-executives", "analyst-estimates"] #Modules list [0-X!]
    key = "?apikey=89500f3f3a2a64cf74c3147add5f8021"
    return urlBody, modules, key

#Getting the data from Yahoo Finance
def yahooFinanceData():
    urlBody, moduleQ, modules = yahooFinanceApi()

    # Module 7 'defaultKeyStatistics' data points
    # Converting API response to json
    response = requests.get(urlBody + ticker + moduleQ + modules[7])
    data = response.text
    parsed = json.loads(data)

    #API response directory
    responseDirectory = parsed['quoteSummary']['result'][0][modules[7]]

    # Data points
    priceToBook = responseDirectory['priceToBook']['fmt']
    pegRatio = responseDirectory['pegRatio']['fmt']
    forwardEps = responseDirectory['forwardEps']['fmt']

    # Module 8 'financialData' data points
    # Converting API response to json
    response = requests.get(urlBody + ticker + moduleQ + modules[8])
    data = response.text
    parsed = json.loads(data)

    # API response directory
    responseDirectory = parsed['quoteSummary']['result'][0][modules[8]]

    # Data points
    debtToEquity = responseDirectory['debtToEquity']['fmt']
    quickRatio = responseDirectory['quickRatio']['fmt']
    returnOnEquity = responseDirectory['returnOnEquity']['fmt']

    # Module 16 'majorHoldersBreakdown' data points
    # Converting API response to json
    response = requests.get(urlBody + ticker + moduleQ + modules[16])
    data = response.text
    parsed = json.loads(data)

    # API response directory
    responseDirectory = parsed['quoteSummary']['result'][0][modules[16]]

    # Data points
    institutionsPercentHeld = responseDirectory['institutionsPercentHeld']['fmt']
    insidersPercentHeld = responseDirectory['insidersPercentHeld']['fmt']

    # Module 19 'netSharePurchaseActivity' data points
    # Converting API response to json
    response = requests.get(urlBody + ticker + moduleQ + modules[19])
    data = response.text
    parsed = json.loads(data)

    # API response directory
    responseDirectory = parsed['quoteSummary']['result'][0][modules[19]]

    # Data points
    buyPercentInsiderShares = responseDirectory['buyPercentInsiderShares']['raw']
    sellPercentInsiderShares = responseDirectory['sellPercentInsiderShares']['raw']
    insidersBuySellRatio = buyPercentInsiderShares/sellPercentInsiderShares

    # Module 26 'esgScores' data points
    # Converting API response to json
    response = requests.get(urlBody + ticker + moduleQ + modules[26])
    data = response.text
    parsed = json.loads(data)

    # API response directory
    responseDirectory = parsed['quoteSummary']['result'][0][modules[26]]

    # Data points
    environmentScore = responseDirectory['environmentScore']['fmt']
    socialScore = responseDirectory['socialScore']['fmt']
    governanceScore = responseDirectory['governanceScore']['fmt']

    # Module 27 'summaryDetail' data points
    # Converting API response to json
    response = requests.get(urlBody + ticker + moduleQ + modules[27])
    data = response.text
    parsed = json.loads(data)

    # API response directory
    responseDirectory = parsed['quoteSummary']['result'][0][modules[27]]

    # Data points
    trailingPE = responseDirectory['trailingPE']['fmt']

    return priceToBook, pegRatio, forwardEps, debtToEquity, quickRatio, returnOnEquity, institutionsPercentHeld, insidersPercentHeld, \
           insidersBuySellRatio, environmentScore, socialScore, governanceScore, trailingPE

#Getting the data from Financial Modelling Prep
def fmpData():
    urlBody, modules, key = fmpApi()

    # Module 0 'ratios' data points
    # Converting API response to json
    response = requests.get(urlBody + modules[0] + "/" + ticker + key)
    data = response.text
    parsed = json.loads(data)

    # API response
    dividendYield = parsed[0]['dividendYield']  #0 is the most recent period, 1 is the previous period etc.... (check if periods are in quarter or year)
    returnOnCapitalEmployed = parsed[0]['returnOnCapitalEmployed']

    # Module 2 'key-executives' data points
    # Converting API response to json
    response = requests.get(urlBody + modules[2] + "/" + ticker + key)
    data = response.text
    parsed = json.loads(data)

    # API response
    #titleSince = parsed[0]['titleSince'] #need to pay for this datapoint, make sure to add into return and import

    # Module 3 'analyst-estimates' data points
    # Converting API response to json
    response = requests.get(urlBody + modules[3] + "/" + ticker + key)
    data = response.text
    parsed = json.loads(data)

    # API response
    #estimatedEpsAvg = parsed[0]['estimatedEpsAvg'] #need to pay for this datapoint, make sure to add into return and import

    return dividendYield, returnOnCapitalEmployed

def modelScores():
    priceToBook, pegRatio, forwardEps, debtToEquity, quickRatio, returnOnEquity, institutionsPercentHeld, insidersPercentHeld, \
    insidersBuySellRatio, environmentScore, socialScore, governanceScore, trailingPE = yahooFinanceData()
    dividendYield, returnOnCapitalEmployed = fmpData()

    #Value Score:
    valueScore = insidersBuySellRatio


    #Growth Score:


    #Health Score:


    #Management Score:

    return valueScore,

#Output
valueScore, = modelScores()
print(valueScore)
