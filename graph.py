from math import sqrt
from string import split
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from matplotlib.mlab import stineman_interp


__author__ = 'Jervis'

# Returns a Random point in a Unit Square
def get_random_point():
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    return [x, y]

def get_random_points(n):
    points = []
    for _ in xrange(n):
        point = get_random_point()
        points.append(point)
    return points

def plot_random_points():
    n  = 512
    points = get_random_points(n)
    x_points = []
    y_points = []
    for point in points:
        x_points.append(point[0])
        y_points.append(point[1])

    fig = figure()
    fig.suptitle('Visualizing Output of a Random Number Generator', fontsize=14, fontweight='bold')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x_points, y_points, 'ro')
    plt.show()
    fig.savefig('test3.png')

def func(n):
    return 1 / np.sqrt(n)

def func2(x):
    return 1 / np.square(x)

def plot_file(file):
    f = open(file)

    line = f.readline()
    x = []
    y = []
    while line:
        row = split(line, ',')
        sample_size = long(row[0])
        y.append(sample_size)

        err = float(row[1])
        x.append(err)
        line = f.readline()


    fig = figure()
    plt.xlabel('Error')
    plt.ylabel('No Samples')

    print x
    print y


    plt.plot(x, y, 'r--', x,y, 'bo')

    plt.show()
    fig.savefig('graph.png')


def test():
    plot_file('data.csv')


plot_random_points()