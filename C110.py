import pandas as pd
import csv
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("temp.csv")
data = df["temp"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df =  mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print(mean)
setup()



# population_mean = statistics.mean(data)
# print("Population_mean: ", population_mean)
# mean = statistics.mean(mean_list)
# print(mean)
# std_deviation = statistics.stdev(dataset)
# print(mean)
# print(std_deviation)

def standerd_deviation():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    # show_fig(mean_list)
    std_deviation = statistics.stdev(mean_list)
    print(std_deviation)
standerd_deviation()
