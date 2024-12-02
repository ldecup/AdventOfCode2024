import os
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

leftList = []
rightList = []
for line in inData:
    leftList.append(int(line.split()[0]))
    rightList.append(int(line.split()[1]))
logger.info(f"Successfully imported {len(leftList)} lines of data")

leftList.sort()
rightList.sort()

totalDistance = 0
similarityScore = 0
for leftNum, rightNum in zip(leftList, rightList):
    totalDistance += abs(rightNum - leftNum)
    similarityScore += leftNum * rightList.count(leftNum)

logger.info(f"Final distance for part 1: {totalDistance}")
logger.info(f"Similarity score for part 2: {similarityScore}")