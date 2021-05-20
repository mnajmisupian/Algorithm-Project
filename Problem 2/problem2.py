from typing import List
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import matplotlib.pyplot as plt
import numpy as np
import re


url = Request("https://www.straitstimes.com/asia/se-asia/pandemic-fuelled-e-shopping-boom-spurs-courier-firms-growth", headers={"User-Agent" : "Mozilla/5.0"})
pageOpen = urlopen(url)
pageHtml = pageOpen.read().decode("utf-8")
htmlParsed = BeautifulSoup(pageHtml,"html.parser")
mainParsed = htmlParsed.find("div", attrs={"class" : "odd field-item"})
mainP = mainParsed.find_all("p")

pList = []
for i in mainP:
    holdText = i.text
    holdText = re.sub("[-,.\"():]", "", holdText)
    pList.append(holdText.lower())
# print(pList[0])

stopWordList = []
sW = open("Problem 2\stopWord.txt")
for line in sW:
    line = line.replace("\n", "")
    stopWordList.append(line)
sW.close()
# print(stopWordList)
# print(len(stopWordList))
# print(stopWordList)

wordList = []
for i in pList:
    holdSplit = i.split()
    for j in holdSplit:
        if j not in stopWordList:
            wordList.append(j)
        # wordList.append(j)
# print(wordList)
# print(len(wordList))
wordDic = {}
for i in wordList:
    wordDic.update({i : "{}".format(wordList.count(i))})
# print(wordDic)
wordKeyList = list(wordDic.keys())
wordValueList = []
for i in wordDic.values():
    wordValueList.append(int(i))
# print(wordValueList)
# print(wordKeyList)

xKey = np.array(wordKeyList)
yVal = np.array(wordValueList)
plt.bar(xKey,yVal)
plt.savefig("Problem 2\wordCount.png")
plt.show()

posWordList = []
pW = open("Problem 2\positiveWord.txt")
for line in pW:
    line = line.replace("\n", "")
    posWordList.append(line)
pW.close()
negWordList = []
nW = open("Problem 2\\negativeWord.txt")
for line in nW:
    line = line.replace("\n", "")
    negWordList.append(line)
nW.close()

positiveWord = []
positiveWordVal = []
positive = 0
for i in posWordList:
    if i in wordDic.keys():
        positive += int(wordDic.get(i))
        positiveWord.append(i)
        positiveWordVal.append(int(wordDic.get(i)))

negativeWord = []
negativeWordVal = []
negative = 0
for i in negWordList:
    if i in wordDic.keys():
        negative += int(wordDic.get(i))
        negativeWord.append(i)
        negativeWordVal.append(int(wordDic.get(i)))

xPW = np.array(positiveWord)
yPWV = np.array(positiveWordVal)
plt.bar(xPW,yPWV)
plt.savefig("Problem 2\posWord.png")
plt.show()

xNW = np.array(negativeWord)
yNWV = np.array(negativeWordVal)
plt.bar(xNW,yNWV)
plt.savefig("Problem 2\\negWord.png")
plt.show()

xPN = np.array(["Positive", "Negative"])
yPNval = np.array([positive, negative])
plt.bar(xPN,yPNval)
plt.savefig("Problem 2\posNeg.png")
plt.show()


