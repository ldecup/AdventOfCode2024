import os
import logging
import re

regexp1 = r"(?:mul\()(\d+),(\d+)(?:\))|(do\(\))|(don't\(\))"

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

targetInput = "input.txt"

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

instructions = re.findall(regexp1,data[0])
logger.info(f"Found {len(instructions)} instructions")

result = 0
currentlyEnabled = True
part2Enabled = False
for x,y,do,dont in instructions:
    if do and part2Enabled:
        currentlyEnabled = True
        logger.debug("Enabled")
    if dont and part2Enabled:
        currentlyEnabled = False
        logger.debug("Disabled")
    if x!='' and currentlyEnabled:
        result += int(x)*int(y)

logger.info(f"Result: {result}")