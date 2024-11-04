import sys
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
matplotlib.use('Agg')

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myFunc(x):
    return slope * x + intercept

mymodel = list(map(myFunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_pulse")
plt.ylabel("Calorie_Burnage")
plt.show()

plt.savefig("output_plot.png")


