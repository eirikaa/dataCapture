# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

__author__ = 'eirikaa'


class Plot:
    def __init__(self):
        pass

    @staticmethod
    def plot_xyz(x, y, z, xyz, time, diff_class, speed, geo_time):
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
        plt.plot(time, diff_class, "bo", label="Activity")
        plt.legend()
        plt.gcf().autofmt_xdate()
        plt.axis([min(time), max(time), min(diff_class)-5, max(diff_class)+5])
        plt.show()

        # TODO: få med speed i plottet

    @staticmethod
    def plot_3_axis(x, y, z, time):
        plt.plot(time, x, 'r', label='x-axis')
        plt.plot(time, y, 'b', label='y-axis')
        plt.plot(time, z, 'g', label='z-axis')

        plt.legend()

        plt.gcf().autofmt_xdate()
        plt.axis([min(time), max(time), min(x) - 5, max(y) + 20])
        plt.show()

    @staticmethod
    def plot2(x, y, z, xyz, time, diff_class, speed, geo_time):
        fig, ax1 = plt.subplots()
        ax1.plot(time, xyz)

        ax2 = ax1.twinx()
        ax2.plot(geo_time, speed, "r")
        # plt.plot(geo_time, speed, "r", label="speed")
        fig.tight_layout()
        plt.show()

    @staticmethod
    def count_steps(data_accelero):
        # TODO: findpeaks
        # https://blog.ytotech.com/2015/11/01/findpeaks-in-python/

        import numpy as np
        import peakutils
        from peakutils.plot import plot as pplot

        # cb = np.array(data_accelero["XYZ"])
        cb = data_accelero["XYZ"].as_matrix()

        indexes = peakutils.indexes(cb, thres=8 / max(cb), min_dist=3)
        print(indexes)
        plt.figure(figsize=(10, 6))
        pplot(data_accelero["Time"].as_matrix(), cb, indexes)

        # interpolatedIndexes = peakutils.interpolate(range(0, len(cb)), cb, ind=indexes)
        # interpolatedIndexes = peakutils.interpolate(data_accelero["Time"].as_matrix(), cb, ind=indexes)
        # pplot(data_accelero["Time"].as_matrix(), cb, interpolatedIndexes)

        plt.show()

if __name__ == "__main__":
    pass
