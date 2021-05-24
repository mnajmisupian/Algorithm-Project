from typing import List
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import matplotlib.pyplot as plt
import numpy as np
import re


def gdex(first, second, third):

    url0 = Request(first, headers={"User-Agent": "Mozilla/5.0"})  # scraping
    pageOpen0 = urlopen(url0)
    pageHtml0 = pageOpen0.read().decode("utf-8")
    htmlParsed0 = BeautifulSoup(pageHtml0, "html.parser")
    mainParsed0 = htmlParsed0.find(
        "div", attrs={"class": "field-item even", "property": "content:encoded"}
    )
    mainP0 = mainParsed0.find_all("p")

    url1 = Request(second, headers={"User-Agent": "Mozilla/5.0"})
    pageOpen1 = urlopen(url1)
    pageHtml1 = pageOpen1.read().decode("utf-8")
    htmlParsed1 = BeautifulSoup(pageHtml1, "html.parser")
    mainParsed1 = htmlParsed1.find(
        "div", attrs={"class": "field-item even", "property": "content:encoded"}
    )
    mainP1 = mainParsed1.find_all("p")

    url2 = Request(third, headers={"User-Agent": "Mozilla/5.0"})
    pageOpen2 = urlopen(url2)
    pageHtml2 = pageOpen2.read().decode("utf-8")
    htmlParsed2 = BeautifulSoup(pageHtml2, "html.parser")
    mainParsed2 = htmlParsed2.find(
        "div", attrs={"class": "field-item even", "property": "content:encoded"}
    )
    mainP2 = mainParsed2.find_all("p")

    pList = []  # change all <p> tag to string and replace all unwanted characters
    for i in mainP0:
        holdText = i.text
        holdText = re.sub('[-,."():]', "", holdText)
        pList.append(holdText.lower())
    print(pList[0])
    for i in mainP1:
        holdText = i.text
        holdText = re.sub('[-,."():]', "", holdText)
        pList.append(holdText.lower())
    print(pList[0])
    for i in mainP2:
        holdText = i.text
        holdText = re.sub('[-,."():]', "", holdText)
        pList.append(holdText.lower())
    print(pList[0])

    stopWordList = []  # get stop words list
    sW = open("Problem2\stopWord.txt")
    for line in sW:
        line = line.replace("\n", "")
        stopWordList.append(line)
    sW.close()
    # print(stopWordList)
    # print(len(stopWordList))

    wordList = []  # filter stop word from the extracted paragraph
    for i in pList:
        holdSplit = i.split()
        for j in holdSplit:
            if j not in stopWordList:
                wordList.append(j)
            # wordList.append(j)
    # print(wordList)
    # print(len(wordList))

    wordDic = {}  # word frequency
    for i in wordList:
        wordDic.update({i: "{}".format(wordList.count(i))})
    # print(wordDic)

    wordKeyList = list(wordDic.keys())  # transfer word in the disctionary to list
    wordValueList = []  # transfer word values(frequency) to list
    for i in wordDic.values():
        wordValueList.append(int(i))
    # print(wordValueList)
    # print(wordKeyList)

    xKey = np.array(wordKeyList)  # create word frequency bar chart
    yVal = np.array(wordValueList)
    plt.figure(figsize=(50, 50))
    plt.title("Word Frequency")
    plt.ylabel("Frequency")
    plt.xlabel("Word")
    plt.xticks(rotation=90)
    plt.tick_params(axis="x", labelsize=2)
    plt.bar(xKey, yVal)
    plt.savefig("Problem2\GDEX\wordCount.svgz")
    plt.savefig("Problem2\GDEX\wordCount.png")
    # plt.show()

    posWordList = []  # get positive word from txt file
    pW = open("Problem2\positiveWord.txt")
    for line in pW:
        line = line.replace("\n", "")
        posWordList.append(line)
    pW.close()

    negWordList = []  # get negative word from txt file
    nW = open("Problem2\\negativeWord.txt")
    for line in nW:
        line = line.replace("\n", "")
        negWordList.append(line)
    nW.close()

    positiveWord = []
    positiveWordVal = []
    positive = 0
    for i in posWordList:  # count positive word
        if i in wordDic.keys():
            positive += int(wordDic.get(i))
            positiveWord.append(i)
            positiveWordVal.append(int(wordDic.get(i)))

    negativeWord = []
    negativeWordVal = []
    negative = 0
    for i in negWordList:  # count negative word
        if i in wordDic.keys():
            negative += int(wordDic.get(i))
            negativeWord.append(i)
            negativeWordVal.append(int(wordDic.get(i)))
    # print(negativeWordVal)

    xPW = np.array(positiveWord)  # create positive word bar chart
    yPWV = np.array(positiveWordVal)
    plt.figure(figsize=(20, 20))
    plt.title("Positive Word Frequency")
    plt.ylabel("Frequency")
    plt.xlabel("Positive Word")
    plt.xticks(rotation=90)
    plt.tick_params(axis="x", labelsize=5)
    plt.bar(xPW, yPWV)
    plt.savefig("Problem2\GDEX\posWord.svgz")
    plt.savefig("Problem2\GDEX\posWord.png")
    # plt.show()

    xNW = np.array(negativeWord)  # create negative word bar chart
    yNWV = np.array(negativeWordVal)
    plt.figure(figsize=(20, 20))
    plt.title("Negative Word Frequency")
    plt.ylabel("Frequency")
    plt.xlabel("Negative Word")
    plt.xticks(rotation=90)
    plt.tick_params(axis="x", labelsize=5)
    plt.bar(xNW, yNWV)
    plt.savefig("Problem2\GDEX\\negWord.svgz")
    plt.savefig("Problem2\GDEX\\negWord.png")
    # plt.show()

    xPN = np.array(
        ["Positive", "Negative"]
    )  # positive vs negative word total bar chart
    yPNval = np.array([positive, negative])
    plt.title("Positive vs Negative")
    plt.ylabel("Frequency")
    plt.xlabel("Sentiment")
    plt.bar(xPN, yPNval)
    plt.savefig("Problem2\GDEX\posNeg.png")
    # plt.show()
