[hadoop@ip-172-31-27-180 ~]$ vim price_predict.sc
[hadoop@ip-172-31-27-180 ~]$ vim price_predict.sc
[hadoop@ip-172-31-27-180 ~]$ cat price_predict.sc 
import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression._
import org.apache.spark.mllib.evaluation._
import org.apache.spark.mllib.tree._
import org.apache.spark.mllib.tree.model._
import org.apache.spark.rdd._

//Write code to create a decision tree based on length, width, height, stroke, city-mpg and highway-mpg. Predict the price based on these features. 

val categoricalFeatureInfo = Map[Int,Int]()

val text = sc.textFile("input")
val parseData = text.map(x => x.split(','))

val data = parseData.map{ x =>
		val feature = Vector.dense( y => (
				if (y(10) == "?") {-1} else (y(10).toDouble),		
				if (y(11) == "?") {-1} else (y(11).toDouble),
				if (y(12) == "?") {-1} else (y(12).toDouble),
				if (y(23) == "?") {-1} else (y(23).toDouble),
				if (y(24) == "?") {-1} else (y(24).toDouble)
				)) 
		val label = Vector.dense( z => (z(25).toDouble) )
		LabeledPoint(label, feature)		
			}

val model = DecisionTree.trainClassifier(data,2,categoricalFeatureInfo,"gini",7,20)
val testData = Vectors.dense(150,70,50,25,35)

val prediction = model.predict(testData)
println("Learned classification model:\n" + model.toDebugString)
