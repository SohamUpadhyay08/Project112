import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv

df = pd.read_csv("MediumArticleP.csv")
data = df["reading_time"].tolist()
graph = ff.create_distplot([data],["temp"],show_hist=False)
graph.show()
Pmean = statistics.mean(data)
pstd = statistics.stdev(data)
##print("mean of the population is ",Pmean)
##print("standard deviation of the population is ",pstd)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    samplemean = statistics.mean(dataset)
    return samplemean

mean_list = []
for i in range(0,100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

sd_std = statistics.stdev(mean_list)
sd_mean = statistics.mean(mean_list)
print("mean of sample distribution is :",sd_mean)
print("standard deviation of sample distribution is :",sd_std)
first_std_deviation_start,first_std_deviation_end = sd_mean-sd_std,sd_mean+sd_std
second_std_deviation_start,second_std_deviation_end = sd_mean-(2*sd_std),sd_mean+(2*sd_std)
third_std_deviation_start,third_std_deviation_end = sd_mean-(3*sd_std),sd_mean+(3*sd_std)
graph = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
graph.add_trace(go.Scatter(x=[sd_mean,sd_mean],y=[0,0.20],mode="lines",name="MEAN"))
graph.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.20],mode="lines",name="1st SD start"))
graph.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.20],mode="lines",name="1st SD end"))
graph.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.20],mode="lines",name="2nd SD start"))
graph.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.20],mode="lines",name="2nd SD end"))
graph.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.20],mode="lines",name="3rd SD start"))
graph.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.20],mode="lines",name="3rd SD end"))
graph.show()
df1 = pd.read_csv("SampleP.csv")
data1 = df1["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data1)
print("mean of sample 1 is ",mean_of_sample1)
z_score = (mean_of_sample1 - sd_mean)/sd_std
print("the z score is ",z_score)

