# Coded by: Jacob Jewitt
# Last Updated: 04/09/2022
# Description:
#   This program intends to find pi via the monte carlo algorithm. Stores x and y coords in pd dataframe along with
#   number of points in the circle and the current estimation of pi.

import random
import pandas as pd
import numpy as np


# This def calculates the estimate of pi by generating two random coords, and then applying the appropriate formulas for
# the calculation.
def calculate_pi(total_points):
    points_in_circle = 0
    data = []
    variance = []

    for numbers in range(0, total_points):
        x = random.random()
        y = random.random()

        if (x * x + y * y) <= 1:
            points_in_circle += 1
        else:
            points_in_circle = points_in_circle

        pi = 4 * (points_in_circle / total_points)

        variance.append([x, y])
        var = np.var(variance)

        data.append([x, y, points_in_circle, pi, var])

    return data


# This def writes all data to a pd df for easy viewing and further manipulation if needed
def write_to_df(data):

    df = pd.DataFrame(data, columns=['X Coordinate', 'Y Coordinate', 'Point in Circle', 'Estimation of Pi', 'Variance'])
    print(df)

    return df


if __name__ == "__main__":
    calculate_pi = calculate_pi(10000)
    write_to_df(calculate_pi)
