import sys

from pyspark import SparkConf, SparkContext

if __name__ == "__main__":

    sc = SparkContext('local', 'Average rating for each movie')
    lines = sc.textFile('input').map(lambda line: line.split(','))
    vals = lines.map(lambda x: (x[1], (float(x[2]),1 ) )  )

    vals = vals.reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1])  )
    vals = vals.mapValues(lambda x: (x[0]/x[1])  )

    vals.saveAsTextFile('output')
