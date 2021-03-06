import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# function, range, 'dx' values, derivative point
function = lambda x : -np.power(x, 2)
dx_values = [1, 0.1, 0.01]
point = 0.1
xmin, xmax = point - 1, point + np.max(dx_values)

fig, axs = plt.subplots(figsize=(15, 8), nrows=len(dx_values))
# [ax.grid(True) for ax in axs]

for idx, dx in enumerate(dx_values):
    # plot function
    x = np.arange(xmin, xmax, 0.01)
    y = function(x)
    axs[idx].plot(x, y)

    # plot points (x, f(x)) and (x+dx, f(x+dx))
    xpoint = np.array([point, point + dx])
    ypoint = function(xpoint)
    axs[idx].scatter(xpoint, ypoint, s=7, color=(1, 0, 0))
    
    # add labels
    arrow = dict(facecolor='black', shrink=0.01, width=1, headwidth=5, headlength=5)
    axs[idx].annotate('f(x)', xy=(xpoint[0], ypoint[0]), xytext=(-1, 0), arrowprops=arrow)
    axs[idx].annotate('f(x + dx), dx=%.2f' % dx, xy=(xpoint[1], ypoint[1]), xytext=(1, 0), arrowprops=arrow)

    # plot line going through points
    line_eq = lambda x : ((ypoint[1]-ypoint[0])/(xpoint[1]-xpoint[0])) * (x - xpoint[0]) + ypoint[0]
    xline_min, xline_max = axs[idx].get_xlim()
    xline = np.arange(xline_min, xline_max, 0.01)
    axs[idx].plot(xline, line_eq(xline), clip_on=False, color=(0.8, 0, 0.8, 0.7))

plt.suptitle('df/dx = lim dx->0 [f(x + dx) - f(x)] / dx')
plt.show()