import sys

from pyspark import SparkConf, SparkContext

"""
Purpose: Find most spoken language (by country) for each landmass
"""

if __name__ ==  "__main__":

    sc = SparkContext('local', 'Finding most spoken language')
    vals = sc.textFile('input').map(lambda line: line.split(",")  )
    vals = vals.map(lambda x: ( (x[1], x[5]), (1) )  )
    red = vals.reduceByKey(lambda x,y: x+y  )

    vals = red.map(lambda x: ( (x[0][0]),(x[0][1],x[1]) )  )
    red = vals.reduceByKey(lambda x,y: (x[0],x[1]) if (x[1]>y[1]) else (y[0],y[1])  )

    red.saveAsTextFile("output")
