import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression._
import org.apache.spark.mllib.evaluation._
import org.apache.spark.rdd._
import org.apache.spark.mllib.clustering._
import org.apache.spark.mllib.tree._
import org.apache.spark.mllib.tree.model._

//Write code to create 100 cluster using Kmeans clustering considering the following numerical features - landmass, language, area, population

val text = sc.textFile("input")
val splitData = text.map(x => x.split(","))
val parseData = splitData.map(x => Vectors.dense(
                if (x(1) == "?") {-1} else {x(1).toDouble},
                if (x(5) == "?") {-1} else {x(5).toDouble},
                if (x(3) == "?") {-1} else {x(3).toDouble},
                if (x(4) == "?") {-1} else {x(4).toDouble}
                             ))

val kmeans = new KMeans()
kmeans.setK(10)
val model = kmeans.run(parseData)
model.predict(parseData)
model.predict(parseData).foreach(println)

val testData = Vectors.dense(1, 1, 2000, 100)
val pred = model.predict(testData)

val testData2 = Vectors.dense(1, 2, 1750, 80)
val pred2 = model.predict(testData2)

println("Prediction: " + pred)
println("Prediction2: " + pred2)
