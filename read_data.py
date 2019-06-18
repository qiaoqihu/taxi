import os
import main as ma
import pandas as pd

# ==========================判断数据文件路径是否存在================

"""
linux下的路径
精简数据路径：path1 
源数据路径：path0 
windows下的路径
精简数据路径：path3 
源数据路径：path2 
"""


path_a = ma.path0  # 选择源数据路径
path_b = ma.path1  # 选择精简数据路径

isExists = os.path.exists(path_a)
if not isExists:
    print("源数据文件不存在")
    exit()


# ==========================读取数据的函数=============================


def txt_name(day, hour, minute):
    """
    根据表的时间生成表名
    :param day:
    :param hour:
    :param minute:
    :return:
    """
    name = '1603%02d%02d%02d.txt' % (day, hour, minute)
    return name


def txt_path(day, hour, types):
    """
    根据要求生成数据文件路径
    :param day:
    :param hour:
    :param types: 0表示源文件路径，其他表示精简的文件路径
    :return:
    """
    if types == 0:
        path = '%s/%02d/%02d/' % (path_a, day, hour)
    else:
        path = '%s/%02d/%02d/' % (path_b, day, hour)
    return path


def path_name(day, hour, minute, types=0):
    """
    生成完整的文件路径与名称
    :param day:
    :param hour:
    :param minute:
    :param types:
    :return:
    """
    name = txt_name(day, hour, minute)
    path = txt_path(day, hour, types)
    pt_name = '%s/%s' % (path, name)
    return pt_name


def view_one_txt(day, hour, minute, types=0):
    """
    查看单个txt文件的原数据
    :param day:
    :param hour:
    :param minute:
    :param types:
    :return:
    """
    path = path_name(day, hour, minute, types)
    data = pd.read_csv(path, delimiter='|', names=['id', 'control', 'police', 'empty',
                                                   'state', 'Viaduct', 'brake', 'P1',
                                                   'receipt_time', 'gps_time', 'lon', 'lat',
                                                   'speed', 'direction', 'numS', 'P2'],
                       encoding='iso-8859-1')

    print(data)


def read_txt(day, hour, minute, types=0):
    """
    读取单个文件数据
    :param day:
    :param hour:
    :param minute:
    :param types:
    :return:
    """
    pt_name0 = path_name(day, hour, minute, types)
    if types == 0:

        pt_name0 = path_name(day, hour, minute, types)
        data = pd.read_csv(pt_name0, delimiter='|',
                           names=['id', 'control', 'police', 'empty',
                                  'state', 'Viaduct', 'brake', 'P1',
                                  'receipt_time', 'gps_time', 'lon', 'lat',
                                  'speed', 'direction', 'numS', 'P2'], encoding='iso-8859-1', low_memory=False)
    else:
        data = pd.read_csv(pt_name0,
                           names=['id', 'control', 'empty', 'state', 'receipt_time',
                                  'gps_time', 'lon', 'lat', 'speed'], encoding='iso-8859-1', low_memory=False)
    return data


if __name__ == '__main__':
    pass
