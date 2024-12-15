import os
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

targetInput = "input.txt"

logger.info(f"Running on {targetInput}")
inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      targetInput)
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

orderingRules = {}
updateList = []
inputMode = "ordering_rules"
for line in inData:
    if line == "\n":
        inputMode = "update_list"
        continue
    if inputMode == "ordering_rules":
        line = line.rstrip('\n')
        try:orderingRules[line.split('|')[1]].append(line.split('|')[0])
        except:orderingRules[line.split('|')[1]] = [(line.split('|')[0])]
    elif inputMode == "update_list":
        updateList.append(line.rstrip('\n'))

logger.info(f"Successfully imported rules for {len(orderingRules)} values and {len(updateList)} updates to print.")

validUpdates = []
score = 0
for line in updateList:
    line = line.split(',')
    updateIsValid = True
    for pageIndex,pageToPrint in enumerate(line):
        for pageAfter in line[pageIndex:]:
            try:
                if pageAfter in orderingRules[pageToPrint]:
                    updateIsValid = False
                    logger.debug(f"Failure in {line}: {pageAfter} appears after {pageToPrint}")
                    break
            except: pass #No update rule for that page number
        if not updateIsValid:
            break
    if updateIsValid:
        validUpdates.append(line)
        score += int(line[int(len(line)/2-0.5)])

logger.debug(f"Found {len(validUpdates)} valid updates: {validUpdates}")
logger.info(f"Final score: {score}")