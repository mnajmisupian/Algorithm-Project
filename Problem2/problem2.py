from typing import List
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import matplotlib.pyplot as plt
import numpy as np
import re, string


def jnt(first, second, third):

    url0 = Request(first, headers={"User-Agent": "Mozilla/5.0"})  # scraping
    pageOpen0 = urlopen(url0)
    pageHtml0 = pageOpen0.read().decode("utf-8")
    htmlParsed0 = BeautifulSoup(pageHtml0, "html.parser")
    mainParsed0 = htmlParsed0.find("div", attrs={"class": "odd field-item"})
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
    mainParsed2 = htmlParsed2.find("div", attrs={"class": "entry-content css-19a2kph"})
    mainP2 = mainParsed2.find_all("p")

    pList = pToList(mainP0, mainP1, mainP2)

    stopWordList = stopWords()

    wordList = paraToWords(pList, stopWordList)  # filtered stop words

    wordDic = wordListToDic(wordList)

    wordKeyList = list(wordDic.keys())  # transfer word in the disctionary to list
    wordValueList = []  # transfer word values(frequency) to list
    for i in wordDic.values():
        wordValueList.append(int(i))
    # print(wordValueList)
    # print(wordKeyList)

    barChart(
        wordKeyList,
        wordValueList,
        "Word Frequency",
        "Frequency",
        "Word",
        8,
        "Problem2\J&T\wordCount",
        150,
        150,
    )

    posWordList = posWords()

    negWordList = negWords()

    positiveWord, positiveWordVal, positive = posWordsNVal(posWordList, wordDic)

    negativeWord, negativeWordVal, negative = negWordsNVal(negWordList, wordDic)

    barChart(
        positiveWord,
        positiveWordVal,
        "Positive Word Frequency",
        "Frequency",
        "Positive Word",
        10,
        "Problem2\J&T\posWord",
        20,
        20,
    )
    barChart(
        negativeWord,
        negativeWordVal,
        "Negative Word Frequency",
        "Frequency",
        "Negative Word",
        20,
        "Problem2\J&T\\negWord",
        20,
        20,
    )
    posVSnegBarChart(positive, negative, "Problem2\J&T\posNeg")
    posSent = positive / len(wordList)
    negSent = negative / len(wordList)
    overall = (posSent - negSent) / 3
    if overall > 0:
        sentiment = "positive"
    elif overall < 0:
        sentiment = "negative"
    return overall


def cityLink(first, second, third):
    url0 = Request(first, headers={"User-Agent": "Mozilla/5.0"})  # scraping
    pageOpen0 = urlopen(url0)
    pageHtml0 = pageOpen0.read().decode("utf-8")
    htmlParsed0 = BeautifulSoup(pageHtml0, "html.parser")
    mainParsed0 = htmlParsed0.find("div", attrs={"class": "td-post-text-content"})
    mainP0 = mainParsed0.find_all("p")

    url1 = Request(second, headers={"User-Agent": "Mozilla/5.0"})
    pageOpen1 = urlopen(url1)
    pageHtml1 = pageOpen1.read().decode("utf-8")
    htmlParsed1 = BeautifulSoup(pageHtml1, "html.parser")
    mainParsed1 = htmlParsed1.find(
        "div", attrs={"id": "story-body", "class": "story bot-15 relative"}
    )
    mainP1 = mainParsed1.find_all("p")

    url2 = Request(third, headers={"User-Agent": "Mozilla/5.0"})
    pageOpen2 = urlopen(url2)
    pageHtml2 = pageOpen2.read().decode("utf-8")
    htmlParsed2 = BeautifulSoup(pageHtml2, "html.parser")
    mainParsed2 = htmlParsed2.find(
        "div", attrs={"class": "paragraph", "mlnid": "idcon=270416;order=3.0"}
    )
    mainP2 = mainParsed2.find_all("p")

    pList = pToList(mainP0, mainP1, mainP2)

    stopWordList = stopWords()

    wordList = paraToWords(pList, stopWordList)

    wordDic = wordListToDic(wordList)

    wordKeyList = list(wordDic.keys())  # transfer word in the disctionary to list
    wordValueList = []  # transfer word values(frequency) to list
    for i in wordDic.values():
        wordValueList.append(int(i))
    # print(wordValueList)
    # print(wordKeyList)

    barChart(
        wordKeyList,
        wordValueList,
        "Word Frequency",
        "Frequency",
        "Word",
        8,
        "Problem2\CityLink\wordCount",
        100,
        100,
    )

    posWordList = posWords()

    negWordList = negWords()

    positiveWord, positiveWordVal, positive = posWordsNVal(posWordList, wordDic)

    negativeWord, negativeWordVal, negative = negWordsNVal(negWordList, wordDic)

    barChart(
        positiveWord,
        positiveWordVal,
        "Positive Word Frequency",
        "Frequency",
        "Positive Word",
        10,
        "Problem2\CityLink\posWord",
        20,
        20,
    )
    barChart(
        negativeWord,
        negativeWordVal,
        "Negative Word Frequency",
        "Frequency",
        "Negative Word",
        20,
        "Problem2\CityLink\\negWord",
        20,
        20,
    )
    posVSnegBarChart(positive, negative, "Problem2\CityLink\posNeg")
    posSent = positive / len(wordList)
    negSent = negative / len(wordList)
    overall = (posSent - negSent) / 3
    if overall > 0:
        sentiment = "positive"
    elif overall < 0:
        sentiment = "negative"
    return overall


def posLaju(first, second, third):
    url0 = Request(first, headers={"User-Agent": "Mozilla/5.0"})  # scraping
    pageOpen0 = urlopen(url0)
    pageHtml0 = pageOpen0.read().decode("utf-8")
    htmlParsed0 = BeautifulSoup(pageHtml0, "html.parser")
    mainParsed0 = htmlParsed0.find(
        "div", attrs={"id": "story-body", "class": "story bot-15 relative"}
    )
    mainP0 = mainParsed0.find_all("p")

    url1 = Request(second, headers={"User-Agent": "Mozilla/5.0"})
    pageOpen1 = urlopen(url1)
    pageHtml1 = pageOpen1.read().decode("utf-8")
    htmlParsed1 = BeautifulSoup(pageHtml1, "html.parser")
    mainParsed1 = htmlParsed1.find("div", attrs={"class": "entry-content"})
    mainP1 = mainParsed1.find_all("p")

    url2 = Request(third, headers={"User-Agent": "Mozilla/5.0"})
    pageOpen2 = urlopen(url2)
    pageHtml2 = pageOpen2.read().decode("utf-8")
    htmlParsed2 = BeautifulSoup(pageHtml2, "html.parser")
    mainParsed2 = htmlParsed2.find("div", attrs={"class": "post-content description"})
    mainP2 = mainParsed2.find_all("p")

    pList = pToList(mainP0, mainP1, mainP2)

    stopWordList = stopWords()

    wordList = paraToWords(pList, stopWordList)

    wordDic = wordListToDic(wordList)

    wordKeyList = list(wordDic.keys())  # transfer word in the disctionary to list
    wordValueList = []  # transfer word values(frequency) to list
    for i in wordDic.values():
        wordValueList.append(int(i))
    # print(wordValueList)
    # print(wordKeyList)

    barChart(
        wordKeyList,
        wordValueList,
        "Word Frequency",
        "Frequency",
        "Word",
        8,
        "Problem2\PosLaju\wordCount",
        100,
        100,
    )

    posWordList = posWords()

    negWordList = negWords()

    positiveWord, positiveWordVal, positive = posWordsNVal(posWordList, wordDic)

    negativeWord, negativeWordVal, negative = negWordsNVal(negWordList, wordDic)

    barChart(
        positiveWord,
        positiveWordVal,
        "Positive Word Frequency",
        "Frequency",
        "Positive Word",
        10,
        "Problem2\PosLaju\posWord",
        20,
        20,
    )
    barChart(
        negativeWord,
        negativeWordVal,
        "Negative Word Frequency",
        "Frequency",
        "Negative Word",
        20,
        "Problem2\PosLaju\\negWord",
        20,
        20,
    )
    posVSnegBarChart(positive, negative, "Problem2\PosLaju\posNeg")
    posSent = positive / len(wordList)
    negSent = negative / len(wordList)
    overall = (posSent - negSent) / 3
    if overall > 0:
        sentiment = "positive"
    elif overall < 0:
        sentiment = "negative"
    return overall


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

    pList = pToList(mainP0, mainP1, mainP2)

    stopWordList = stopWords()

    wordList = paraToWords(pList, stopWordList)

    wordDic = wordListToDic(wordList)

    wordKeyList = list(wordDic.keys())  # transfer word in the disctionary to list
    wordValueList = []  # transfer word values(frequency) to list
    for i in wordDic.values():
        wordValueList.append(int(i))
    # print(wordValueList)
    # print(wordKeyList)

    barChart(
        wordKeyList,
        wordValueList,
        "Word Frequency",
        "Frequency",
        "Word",
        8,
        "Problem2\GDEX\wordCount",
        100,
        100,
    )

    posWordList = posWords()

    negWordList = negWords()

    positiveWord, positiveWordVal, positive = posWordsNVal(posWordList, wordDic)

    negativeWord, negativeWordVal, negative = negWordsNVal(negWordList, wordDic)

    barChart(
        positiveWord,
        positiveWordVal,
        "Positive Word Frequency",
        "Frequency",
        "Positive Word",
        10,
        "Problem2\GDEX\posWord",
        20,
        20,
    )
    barChart(
        negativeWord,
        negativeWordVal,
        "Negative Word Frequency",
        "Frequency",
        "Negative Word",
        20,
        "Problem2\GDEX\\negWord",
        20,
        20,
    )
    posVSnegBarChart(positive, negative, "Problem2\GDEX\posNeg")
    posSent = positive / len(wordList)
    negSent = negative / len(wordList)
    overall = (posSent - negSent) / 3
    if overall > 0:
        sentiment = "positive"
    elif overall < 0:
        sentiment = "negative"
    return overall


def dhl(first, second, third):
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

    pList = pToList(mainP0, mainP1, mainP2)

    stopWordList = stopWords()

    wordList = paraToWords(pList, stopWordList)

    wordDic = wordListToDic(wordList)

    wordKeyList = list(wordDic.keys())  # transfer word in the disctionary to list
    wordValueList = []  # transfer word values(frequency) to list
    for i in wordDic.values():
        wordValueList.append(int(i))
    # print(wordValueList)
    # print(wordKeyList)

    barChart(
        wordKeyList,
        wordValueList,
        "Word Frequency",
        "Frequency",
        "Word",
        7,
        "Problem2\DHL\wordCount",
        150,
        150,
    )

    posWordList = posWords()

    negWordList = negWords()

    positiveWord, positiveWordVal, positive = posWordsNVal(posWordList, wordDic)

    negativeWord, negativeWordVal, negative = negWordsNVal(negWordList, wordDic)

    barChart(
        positiveWord,
        positiveWordVal,
        "Positive Word Frequency",
        "Frequency",
        "Positive Word",
        10,
        "Problem2\DHL\posWord",
        20,
        20,
    )
    barChart(
        negativeWord,
        negativeWordVal,
        "Negative Word Frequency",
        "Frequency",
        "Negative Word",
        20,
        "Problem2\DHL\\negWord",
        20,
        20,
    )
    posVSnegBarChart(positive, negative, "Problem2\DHL\posNeg")
    posSent = positive / len(wordList)
    negSent = negative / len(wordList)
    overall = (posSent - negSent) / 3
    if overall > 0:
        sentiment = "positive"
    elif overall < 0:
        sentiment = "negative"
    return overall


def pToList(mainP0, mainP1, mainP2):
    pList = []  # change all <p> tag to string and replace all unwanted characters
    for i in mainP0:
        holdText = i.text
        # holdText = re.sub("^\W+", "", holdText)
        holdText = re.sub("[\\%,–.\"-():;“”‘’'—’?\[\]-]", "", holdText)
        pList.append(holdText.lower())
    # print(pList[0])
    for i in mainP1:
        holdText = i.text
        # holdText = re.sub("^\W+", "", holdText)
        holdText = re.sub("[\\%,–.\"():;“”‘’'—’?\[\]-]", "", holdText)
        pList.append(holdText.lower())
    # print(pList[0])
    for i in mainP2:
        holdText = i.text
        # holdText = re.sub("^\W+", "", holdText)
        holdText = re.sub("[\\%,–.\"():;“”‘’'—’?\[\]-]", "", holdText)
        pList.append(holdText.lower())
    # print(pList[0])
    return pList


def stopWords():
    stopWordList = []  # get stop words list
    sW = open("Problem2\stopWord.txt")
    for line in sW:
        line = line.replace("\n", "")
        stopWordList.append(line)
    sW.close()
    # print(stopWordList)
    # print(len(stopWordList))
    return stopWordList


def paraToWords(pList, stopWordList):
    wordList = []  # filter stop word from the extracted paragraph
    for i in pList:
        holdSplit = i.split()
        for j in holdSplit:
            if j not in stopWordList:
                wordList.append(j)
            # wordList.append(j)
    # print(wordList)
    # print(len(wordList))
    return wordList


def wordListToDic(wordList):
    wordDic = {}  # word frequency
    for i in wordList:
        wordDic.update({i: "{}".format(wordList.count(i))})
    # print(wordDic)
    return wordDic


def barChart(xList, yList, barTitle, yAxis, xAxis, sizeLabel, location, figX, figY):
    x = np.array(xList)  # create word frequency bar chart
    y = np.array(yList)
    plt.figure(figsize=(figX, figY))
    plt.title(barTitle)
    plt.ylabel(yAxis)
    plt.xlabel(xAxis)
    plt.xticks(rotation=90)
    plt.tick_params(axis="x", labelsize=sizeLabel)
    plt.bar(x, y)
    plt.savefig("{}.svgz".format(location))
    plt.savefig("{}.png".format(location))
    # plt.show()
    plt.clf()


def posWords():
    posWordList = []  # get positive word from txt file
    pW = open("Problem2\positiveWord.txt")
    for line in pW:
        line = line.replace("\n", "")
        posWordList.append(line)
    pW.close()
    return posWordList


def negWords():
    negWordList = []  # get negative word from txt file
    nW = open("Problem2\\negativeWord.txt")
    for line in nW:
        line = line.replace("\n", "")
        negWordList.append(line)
    nW.close()
    return negWordList


def posWordsNVal(posWordList, wordDic):
    positiveWord = []
    positiveWordVal = []
    positive = 0
    for i in posWordList:  # count positive word
        if i in wordDic.keys():
            positive += int(wordDic.get(i))
            positiveWord.append(i)
            positiveWordVal.append(int(wordDic.get(i)))
    return positiveWord, positiveWordVal, positive


def negWordsNVal(negWordList, wordDic):
    negativeWord = []
    negativeWordVal = []
    negative = 0
    for i in negWordList:  # count negative word
        if i in wordDic.keys():
            negative += int(wordDic.get(i))
            negativeWord.append(i)
            negativeWordVal.append(int(wordDic.get(i)))
    return negativeWord, negativeWordVal, negative


def posVSnegBarChart(positive, negative, location):
    xPN = np.array(
        ["Positive", "Negative"]
    )  # positive vs negative word total bar chart
    yPNval = np.array([positive, negative])
    plt.title("Positive vs Negative")
    plt.ylabel("Frequency")
    plt.xlabel("Sentiment")
    plt.bar(xPN, yPNval)
    plt.savefig("{}.svgz".format(location))
    plt.savefig("{}.png".format(location))
    # plt.show()
    plt.clf()
