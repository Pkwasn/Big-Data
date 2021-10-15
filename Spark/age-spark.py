import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    sc = SparkContext('local', 'Gender count for certain ages')
    val = sc.textFile("input").map(lambda line: line.split(','))
    val = val.map(lambda x: ( int(x[0]), int(x[1])) )

    res = val.map(lambda x: (1, (x[1], 1)) (if x[1]==1 and x[0]>30 and x[0]<60)
                  else ( (2, (x[1], 1)) if (x[1]==0 and x[0]>40 and x[0]<71)
                  else (0, (0,0)) ) )

    res = res.reduceByKey(lambda x,y: (x[0], x[1]+y[1]) )
    res = res.mapValues(lambda x: x[1])                         #mapValues only operates on values, not key/value pairs
    res = res.filter(lambda x: x[0]>0)                          #filter operates on key/value pairs, so x[0] is the gender,
                                                                # so if gender is female or male, those values will be included
    res.saveAsTextFile('output')
