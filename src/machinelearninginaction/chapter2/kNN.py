from numpy import *
from os import listdir
import operator
import datetime
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inx, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistanceIndex = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistanceIndex[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayAllLines = fr.readlines()
    numberOfLines = len(arrayAllLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayAllLines:
        # 去掉回车换行符
        line = line.strip()
        # print(line)
        listFromLine = line.split("\t")
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(StringLabel2Num(listFromLine[-1])))
        index += 1
    return returnMat, classLabelVector


def StringLabel2Num(x):
    if x == 'largeDoses':
        return 3
    if x == 'smallDoses':
        return 2
    if x == 'didntLike':
        return 1


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.1
    returnMat, classLabelVector = file2matrix("datingTestSet.txt")
    # print(returnMat)
    # print(classLabelVector[0:20])
    # plot1(returnMat[:, 1], returnMat[:, 2], classLabelVector)
    normDataSet, ranges, minVals = autoNorm(returnMat)
    m = normDataSet.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify0(normDataSet[i, :], normDataSet[numTestVecs:m, :],
                                     classLabelVector[numTestVecs:m], 3)
        print("the classifier came back with: %d, "
              "the real answer is: %d" % (classifierResult, int(classLabelVector[i])))
        if (classifierResult != classLabelVector[i]):
            errorCount += 1
    print("the total error is: %f" % ((errorCount / float(numTestVecs))))


def plot1(mat1, mat2, mat3):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(mat1, mat2, 15 * array(mat3), 15 * array(mat3))
    plt.show()


def img2Vector(filename):
    returnVector = zeros((1, 1024))
    file = open(filename)
    allLines = file.readlines()
    i = 0
    for line in allLines:
        for j in range(32):
            returnVector[0, j + 32 * i] = int(line[j])
        i += 1
    return returnVector


def handWriteClassTest():
    hwLabels = []
    trainingFileList = listdir("trainingDigits")
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileName = trainingFileList[i]
        fileNamePrefix = fileName.split(".")[0]
        fileLabel = fileNamePrefix.split("_")[0]
        trainingMat[i, :] = img2Vector("trainingDigits/%s" % fileName)
        hwLabels.append(fileLabel)
    print(trainingMat.shape)
    print(set(hwLabels))

    errorCount = 0
    testLabels = []
    testFileList = listdir("testDigits")
    n = len(testFileList)
    testMat = zeros((n, 1024))
    for j in range(n):
        fileName = testFileList[j]
        fileNamePrefix = fileName.split(".")[0]
        fileLabel = fileNamePrefix.split("_")[0]
        testVector = img2Vector("testDigits/%s" % fileName)
        testMat[j, :] = testVector
        testLabels.append(fileLabel)
        # classifier
        testResult = classify0(testVector, trainingMat, hwLabels, 7)
        # print("classifier call back with: %d, the real answer is: %d" % (int(testResult), int(fileLabel)))
        if testResult != fileLabel:
            errorCount += 1
    print("the totel error numbers is: {}".format(errorCount))
    print("the total error is: %f" % (errorCount / float(n)))


if __name__ == '__main__':
    # 简单的KNN分类
    group, labels = createDataSet()
    test = [0, 0]
    test_class = classify0(test, group, labels, 3)
    print(test_class)
    # date分类
    # datingClassTest()
    # 手写字分类
    start_time = datetime.datetime.now()
    handWriteClassTest()
    end_time = datetime.datetime.now()
    print("time cost: %f" % float((end_time - start_time).seconds))
