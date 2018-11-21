from math import log
import operator


def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFetVec = featVec[:axis]
            reducedFetVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFetVec)
    return retDataSet


def calcShannonEnt(dataSet):
    num = len(dataSet)
    labelCount = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCount:
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCount:
        prob = float(labelCount[key]) / num
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def chooseBestFeatureToSplit(dataSet):
    numFetures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeture = -1
    for i in range(numFetures):
        # 使用列表推导来创建新的列表，将第i个特征值数据都写入list
        featList = [example[i] for example in dataSet]
        uniqueValues = set(featList)
        newEntropy = 0.0
        for value in uniqueValues:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        print("feature index:{}, infoGain:{}".format(i, infoGain))
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeture = i
    return bestFeture


# 投票表决节点属于哪个分类
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount)
    return sortedClassCount[0][0]


# 递归函数的第一个停止条件是所有的类标签完全相同，则返回该类标签
# 第二个停止条件是使用完了所有特征，仍然不能将数据集划分成仅包含唯一类别的分组。此时无法简单地返回唯一的类标签，需要挑选出次数最多的类别作为返回值
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    print(classList)
    # 类别完全相同，停止划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 遍历完成所有特征，返回次数最多的特征值
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel = labels[bestFeature]
    myTree = {bestFeatureLabel: {}}
    # del 删除的是变量，将labels中bestFeature对应的label删除
    del (labels[bestFeature])
    # 得到列表包含的所有值
    featValues = [example[bestFeature] for example in dataSet]
    uniqueValues = set(featValues)
    for value in uniqueValues:
        subLabels = labels[:]
        myTree[bestFeatureLabel][value] = createTree(splitDataSet(dataSet, bestFeature, value), subLabels)

    return myTree


if __name__ == "__main__":
    dataSet, labels = createDataSet()
    print(dataSet[0])
    featList = [example[0] for example in dataSet]
    print(featList)
    shannonEnt = calcShannonEnt(dataSet)
    print(shannonEnt)

    bestFeature = chooseBestFeatureToSplit(dataSet)
    print(bestFeature)
    print("====create tree====")
    myTree = createTree(dataSet, labels)
    print(myTree)
