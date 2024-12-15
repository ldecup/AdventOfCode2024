import os
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

targetInput = "testinput.txt"

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
        try:orderingRules[int(line.split('|')[1])].append(int(line.split('|')[0]))
        except:orderingRules[int(line.split('|')[1])] = [(int(line.split('|')[0]))]
    elif inputMode == "update_list":
        updateList.append(line.rstrip('\n'))

logger.info(f"Successfully imported {len(orderingRules)} lines of data")

