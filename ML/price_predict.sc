import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression._
import org.apache.spark.mllib.evaluation._
import org.apache.spark.mllib.tree._
import org.apache.spark.mllib.tree.model._
import org.apache.spark.rdd._

//Write code to create a decision tree based on length, width, height, stroke, city-mpg and highway-mpg. Predict the price based on these features. 

val test = sc.textFile("input")
val splitData = text.map(x => x.split(","))

val parseData = splitData.map(x =>
                    (if(x(10) == "?") {-1} else {x(10).toDouble},
                    if(x(11) == "?") {-1} else {x(11).toDouble},
                    if(x(12) == "?") {-1} else {x(12).toDouble},
                    if(x(19) == "?") {-1} else {x(19).toDouble},
                    if(x(23) == "?") {-1} else {x(23).toDouble},
                    if(x(24) == "?") {-1} else {x(24).toDouble},
                    if(x(25) == "?") {-1} else if {x(25).toDouble > 10000} {2} else {1}))

val data = parseData.map( x =>
            val featureVector = Vectors.dense(x._1, x._2, x._3, x._4, x._5, x._6)
            val label = x._7
            LabeledPoint(label, featureVector)
                        )

val categoricalFeatureInfo = Map[Int,Int]()
val model = DecisionTree.trainClassifier(data,3,categoricalFeatureInfo,"gini",5,100)

val testData = Vectors.dense(150,65,50,3,34,45)
val prediction = model.predict(testData)
println("Prediction: " + prediction)
