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

data = []
for line in inData:
    data.append(line.rstrip('\n'))
logger.info(f"Successfully imported {len(data)} lines of data")