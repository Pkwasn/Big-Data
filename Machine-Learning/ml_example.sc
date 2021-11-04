import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression._
import org.apache.spark.mllib.evaluation._
import org.apache.spark.mllib.tree._
import org.apache.spark.mllib.tree.model._
import org.apache.spark.rdd._

val text = sc.textFile("input") // Directory containing input.txt
val header = text.first() //this is out header
val data = text.filter(x => x != header)
val categoricalFeatureInfo = Map[Int,Int]((1,2),(3,4),(4,2),(5,2) )
val categoricalFeatureInfo = Map[Int,Int]()

val data = rawdata.map{ line =>
    val values = line.split(',').map(line => line.toDouble)
    val featurevector = Vectors.dense(values.init)
    val label = values.last
    LabeledPoint(label, featurevector)
    }

val mode = DecisionTree.trainClassifier(data,2,categoricalFeatureInfo,"gini",7,20)
val testData = Vectors.dense(10,1,3,1,0,0)

val prediction = model.predict(testData)
println("Learned classification model:\n" + model.toDebugString)
