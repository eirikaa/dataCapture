# -*- coding: utf-8 -*-

from prepareData import PrepareData
import matplotlib.pyplot as plt
from classification import Classification

__author__ = 'eirikaa'

class Plot:
    def __init__(self):
        pass

    @staticmethod
    def plot(x, y, z, xyz, time, diff_class, speed, geo_time):
        """

        :param x:
        :param y:
        :param z:
        :param xyz:
        :param time:
        :param diff_class:
        :return:
        """

        # Plot XYZ data
        # plt.ion()
        plt.plot(time, xyz, "r", label="xyz")
        plt.plot(time, diff_class, "bo", label="movement")
        plt.gcf().autofmt_xdate()
        plt.axis([min(time), max(time), min(diff_class)-5, max(diff_class)+5])
        plt.show()


        # TODO: få med speed i plottet
    @staticmethod
    def plot2(x, y, z, xyz, time, diff_class, speed, geo_time):
        fig, ax1 = plt.subplots()
        ax1.plot(time, xyz)

        ax2 = ax1.twinx()
        ax2.plot(geo_time, speed, "r")
        # plt.plot(geo_time, speed, "r", label="speed")
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    prep = PrepareData(geo_file='data/log/02_18_geo.csv', accelero_file='data/log/02_18_accelero.csv')
    classification = Classification(diff_range=10)
    x, y, z, xyz, time, readable_time_acclero, activity, activity2, data = prep.read_accelerometer_data()
    lat, lon, speed, accuracy, altitude, heading, time_geo, readable_time_geo, activity, activity2, data_geo = prep.read_geodata()

    # diff_xyz = ana.diff_maxmin(x, y, z, xyz)
    diff_xyz = classification.diff_avg(x, y, z, xyz)
    diff_class = classification.differentiate(diff_xyz, xyz, time)

    print(prep.calibration(xyz))

    # Plot.plot(x, y, z, xyz, time, diff_class)
    clean_diff_class = []
    for i in diff_class:
       clean_diff_class.append(i[0])
    print (clean_diff_class)
    Plot.plot(x, y, z, xyz, readable_time_acclero, clean_diff_class, speed, time_geo)


    # classification.classify_geo_data(diff_class,time_geo,data,data_geo)
    # Plot.plot(x, y, z, xyz, time, data_geo['Diff class'], speed, time_geo)