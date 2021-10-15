import sys

from pyspark import SparkContext, SparkConf

"""
Input: movie-input.txt - Values: Col 1 - UserID Col 2 - MovieID Col 3 - Rating
Purpose: Find the maximum rating for each movie
"""


if __name__ == "__main__":

    sc = SparkContext('local', 'Movie Ratings')
    val = sc.textFile('input').map(lambda line: line.split(','))
    res = val.map(lambda x: ( x[1], float(x[2]) )  )                # x[1] = MovieID (our key) x[2] = Rating (float value) 

    res = res.reduceByKey(lambda x,y: (x) if (x>y) else (y))

    res.saveAsTextFile('output')
