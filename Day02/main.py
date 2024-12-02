import os
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append([int(num) for num in line.split()])
logger.info(f"Successfully imported {len(data)} lines of data")

def isReportSafe(report):
    isValid = True
    for index in range(0,len(report)-1):
        if (abs(report[index]-report[index+1]) < 1) or (abs(report[index]-report[index+1]) > 3):
            isValid = False
            break
    if ((report == sorted(report)) or (report == sorted(report, reverse=True))) and isValid:
        return True
    return False


numberOfSafeReports = 0
numberOfSafeReportsWithDampener = 0
for report in data:
    if isReportSafe(report):
        numberOfSafeReports+=1
        logger.debug(f"Report {report} is safe")
    else:
        for index,level in enumerate(report):
            tempReport = list(report)
            tempReport.pop(index)
            if isReportSafe(tempReport):
                numberOfSafeReportsWithDampener+=1
                logger.debug(f"Report {report} is safe (dampener used, safe as {tempReport})")
                break

logger.info(f"Number of safe reports: {numberOfSafeReports}")
logger.info(f"Number of safe reports (with dampener): {numberOfSafeReports+numberOfSafeReportsWithDampener}")