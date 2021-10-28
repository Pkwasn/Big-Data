import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    sc = SparkContext('local', '2-key (2 reducer) Map Reduce to find lowest temp per City')
    lines = sc.textFile('input').map(lambda line: line.split(","))
    val = lines.map(lambda x: ((x[0], x[1]),(float(x[2]) )  )   )
    val = val.reduceByKey(lambda x,y: (x) if (x<y) else (y)  )
    val = val.map(lambda x: ((x[0][0]), (x[0][1], x[1]) )  )
    res = val.reduceByKey(lambda x,y: (x[0],x[1]) if (x[1] < y[1]) else (y[0],y[1])  )

    res.saveAsTextFile('output')
