import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    sc = SparkContext('local', 'Movie Ratings')
    val = sc.textFile('input').map(lambda line: line.split(','))
    res = val.map(lambda x: ( x[1], float(x[2]) )  )

    res = res.reduceByKey(lambda x,y: (x) if (x>y) else (y))

    res.saveAsTextFile('output')
