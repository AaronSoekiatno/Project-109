import csv
import statistics
import pandas as pd

df = pd.read_csv(r"SP.csv")
mathScores = df["math score"].tolist()
scoresMedian = statistics.median(mathScores)
scoresMean = statistics.mean(mathScores)
scoresMode = statistics.mode(mathScores)
scoresStdev = statistics.stdev(mathScores)

first_stdev_start, first_stdev_end = scoresMean-mathScores, scoresMean+mathScores
second_stdev_start, second_stdev_end = scoresMean-(2*mathScores), scoresMean+(2*mathScores)
third_stdev_start, third_stdev_end = scoresMean-(3*mathScores), scoresMean+(3*mathScores)

first_stdev = [result for result in mathScores if result>first_stdev_start and result< first_stdev_end]
print("{}% of data in first deviation".format(len(first_stdev)*100/len(mathScores)))

second_stdev = [result for result in mathScores if result>second_stdev_start and result< second_stdev_end]
print("{}% of data in second deviation".format(len(second_stdev)*100/len(mathScores)))

third_stdev = [result for result in mathScores if result>third_stdev_start and result< third_stdev_end]
print("{}% of data in third deviation".format(len(third_stdev)*100/len(mathScores)))
