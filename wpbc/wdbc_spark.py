import sys

from pyspark import SparkConf, SparkContext

"""
Date: Monday, November 1, 2021
Purpose: Find the average radius of maligant tumor cells
"""

if __name__ == "__main__":
    sc = SparkContext('local', 'Finding the average radius of malignant tumor cells')
    line = sc.textFile('input').map(lambda line: line.split(',')  )
    keyv = line.map(lambda x: ((x[1]), (float(x[2]), 1) )  )
    val = keyv.reduceByKey(lambda x,y: ((x[0] + y[0]), (x[1] + y[1]))  )
    val = val.mapValues(lambda x: (x[0]/x[1])  )
    val = val.filter(lambda x: x[0] == 'M')
    val.saveAsTextFile('output')
