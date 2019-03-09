import scala.collection.mutable.ArrayBuffer

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val indicesByValue = (nums.indices zip nums).toMap
	    var ret = ArrayBuffer[Int]()
	    indicesByValue.foreach{ 	
		case(key,value) => 
			var el: Int = target - value
			val elKey = indicesByValue.filter(_._2 == el).map(_._1)
			if(indicesByValue.values.exists(_ == el) && elKey.last > key){
				ret += (key,elKey.last)
				//println(ret)
			}
		}
		ret.toArray
}
}