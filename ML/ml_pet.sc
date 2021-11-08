import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression._
import org.apache.spark.mllib.evaluation._
import org.apache.spark.mllib.tree._
import org.apache.spark.mllib.tree.model._
import org.apache.spark.rdd._

val text = sc.textFile("input") // "input" is a directory which contains input.txt
val header = text.first()
val splitData = text.filter(x => x != header) //lambda line: line = line.split(",")

val parseData = splitData.map(x => (if x(1) == "?")) {-1} else {x(1).toDouble},
                                    if(x(2) == "?") {-1} else {x(2).toDouble},
        if(x(3) == "?") {-1} else if (x(3) == "Brown") {1} else if (x(3) == "Green") {2} else if (x(3) == "Tan") {3} else if (x(3) == "Gray") {4} else {5},
        if(x(4) == "?") {-1} else if (x(4) == "yes") {1} else {0}   ))

val data = parseData.map( x =>
            val featureVector = Vectors.dense(x._1, x._2, x._3)
            val label = x._4
            LabeledPoint(label, featureVector)
                        )

//training

val categoricalFeatureInfo = Map[Int,Int]()
val model = DecisionTree.trainClassifier(data,2,categoricalFeatureInfo,"gini",5,100)

//predict

val testData = Vectors.dense(0.2,2,4)
val prediction = model.predict(testData)
println(prediction)
