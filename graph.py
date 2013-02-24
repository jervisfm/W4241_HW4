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
    fig.savefig('graph.png')


if __name__ == '__main__':
    print "Random Number Generator Visualizer"
    plot_random_points()
    print "Graph Plotted"