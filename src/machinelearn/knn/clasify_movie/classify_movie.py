# k-NN方法，电影分类
# 参考：http://cuijiahua.com/blog/2017/11/ml_1_knn.html

import numpy as np
import operator


def create_data_set():
    # 四组二维特征
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    # 四组特征的标签
    labels = ['爱情片', '爱情片', '动作片', '动作片']
    return group, labels


"""
函数说明:kNN算法,分类器

Parameters:
    inX - 用于分类的数据(测试集)
    dataSet - 用于训练的数据(训练集)
    labes - 分类标签
    k - kNN算法参数,选择距离最小的k个点
Returns:
    sortedClassCount[0][0] - 分类结果

"""


def classify0(idX, dataSet, labels, k):
    # 数据集的大小，shape
    dataSetSize = dataSet.shape[0]
    # 计算用于分类的数据与测试数据集之间的距离
    diffMat = np.tile(idX, [dataSetSize, 1]) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances ** 0.5

    # 返回distance从小到大排序的索引值，选出距离最近的k个索引以及对于的标签
    sortedDistanceIndices = distance.argsort()
    print("sortedDistanceIndex:")
    print(sortedDistanceIndices)
    # 定义一个记录类别的字典
    classCount = {}
    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDistanceIndices[i]]
        # 计算类别次数
        # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    print(classCount)
    # 对每个类别的个数从大到小排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount)
    # 返回类别技术次数最大的类别
    return sortedClassCount[0][0]


if __name__ == '__main__':
    group, labels = create_data_set()
    # 测试集
    test = [101, 20]
    # kNN分类结果
    test_class = classify0(test, group, labels, 3)
    print(test_class)
