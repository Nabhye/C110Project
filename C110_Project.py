import pandas as pd
import random
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("C110Project_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()

population_mean = statistics.mean(data)
print("Population Mean: ", population_mean)
population_std_deviation = statistics.stdev(data)
print("Satnderd Deviation: ", population_std_deviation)

dataset = []
for i in range(0, 1000):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)
print("Mean of 100 values: ", mean)
print("Standerd deviation of 1000 values: ", std_deviation)