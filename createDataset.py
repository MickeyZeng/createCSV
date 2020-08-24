import pandas

"""
TODO: 生成数据集包含 Train Test Validate (比例 6：2：2)
1. 首先把timed_png文件夹和trimed_png_list和label.csv读取下来
2. CSV上面得到postive & negative 的集合 然后就按照比例分
3. 根据病人的ID去trimed_png_list找图片的路径
4. 把图片路径 & 标签结果 放入新建的CSV中
"""


# Read files function
def readFile(path, index):
    # index 1 -- Read CSV File
    if index == 1:
        csv_file = pandas.read_csv(path)
        return csv_file
    elif index == 2:
        image_file = pandas.read_fwf(path)
        return image_file
    pass


def dividedIntoThreeGroups(target_list):
    portion_index = int(len(target_list) / 10)
    positive_set_portion1 = target_list[: 6 * portion_index]
    positive_set_portion2 = target_list[6 * portion_index: 8 * portion_index]
    positive_set_portion3 = target_list[8 * portion_index:]
    return [positive_set_portion1, positive_set_portion2, positive_set_portion3]


def getList(devided_set, path_file, type):
    """
    :param devided_set: 训练集的patientID
    :param path_file: 图片文件的路径
    :param type: Positive & Negative
    :return:
    """
    resultList = []
    # For trained
    for i in devided_set:
        for j in path_file.get('image_path'):
            if str(i) == str(j).split("/")[1]:
                tempList = {'patient_id': i, 'label': type, 'image_path': j}
                resultList.append(tempList)

    return resultList


def writeCSV(list, name):
    """
    TODO: Transfer the list into CSV
    :param list:
    :return:
    """
    dataframe = pandas.DataFrame(list)
    dataframe.to_csv("output/" + name + ".csv", index=False, sep=',')
    pass

"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image_path', type=str, required=True)
    parser.add_argument('-c', '--csv_file_path', type=str, required=True)
    args = parser.parse_args()
    image_path = args.image_path
    csv_file_path = args.csv_file_path
    # image_path = '/Users/mickey/document/Master of computer science/Project/data/orthopedics/trimed_png_list.txt'
    # csv_file_path = '/Users/mickey/document/Master of computer science/Project/data/orthopedics/label.csv'
    for i in tqdm(range(1)):
        path_file = readFile(image_path, 2)
        csv_file = readFile(csv_file_path, 1)
        positive_set = list()
        negative_set = list()
        labelSet = csv_file.get('label')
        for i, v in labelSet.items():
            if v == 1:
                positive_set.append(csv_file.get('patient_id')[i])
            else:
                negative_set.append(csv_file.get('patient_id')[i])
        # 6 : 2 : 2 random shuffle
        random.seed(2)
        random.shuffle(positive_set)
        random.shuffle(negative_set)
        divided_positive_set = dividedIntoThreeGroups(positive_set)
        divided_negative_set = dividedIntoThreeGroups(negative_set)

        trainedList = getList(divided_positive_set[0], path_file, 1) + getList(divided_negative_set[0], path_file, 0)
        testList = getList(divided_positive_set[1], path_file, 1) + getList(divided_negative_set[1], path_file, 0)
        validateList = getList(divided_positive_set[2], path_file, 1) + getList(divided_negative_set[2], path_file, 0)

        writeCSV(trainedList, "trainedList")
        writeCSV(testList, "testList")
        writeCSV(validateList, "validateList")

        for i in trainedList:
            i.update({'set': 'train'})
        for i in testList:
            i.update({'set': 'test'})
        for i in validateList:
            i.update({'set': 'validate'})

        wholeList = trainedList + testList + validateList
        writeCSV(wholeList, "wholeList")
"""

if __name__ == '__main__':
    path = "/Users/mickey/document/Master of computer science/Project/cifar10/master_with_prediction_1.0.csv"
    master = pandas.read_csv(path)

    # print(len(master))

    resultList = []

    da = master.to_dict(orient='records')

    for i in da:
        if i['to_label'] == 'Yes':
            resultList.append(i)

    writeCSV(resultList, 'yes_csv')
