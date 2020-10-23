/**
 * You can edit, run, and share this code. 
 * play.kotlinlang.org 
 */
fun main(){

	//You can change this Int Array
    val arr:IntArray = intArrayOf(10, 20,33,1, 42, 4,2,23, 99,75)
    bubbleSortWithSteps(arr)
}


fun bubbleSortWithSteps(numbers: IntArray) {
    println("Initial numbers: [%s]".format(numbers.joinToString(separator = ", ")))
    for (pass in 0 until (numbers.size - 1)) {
        // A single pass of bubble sort
        for (currentPosition in 0 until (numbers.size - pass - 1)) {
            // This is a single step
            print("Pass-%d-Step-%d: Comparing elements at position %d(%d) and %d(%d). ".format(pass, currentPosition,
                    currentPosition, numbers[currentPosition], (currentPosition + 1), numbers[currentPosition + 1]))
            if (numbers[currentPosition] > numbers[currentPosition + 1]) {
                println("They are in wrong order, swap them")
                val tmp = numbers[currentPosition]
                numbers[currentPosition] = numbers[currentPosition + 1]
                numbers[currentPosition + 1] = tmp
            } else {
                println("They are in correct order, do not swap them")
            }
            println("Numbers after Pass-%d-Step-%d: [%s]".format(pass, currentPosition, numbers.joinToString(separator =
            ", ")))
        }
    }
    println("Sorted numbers: [%s]".format(numbers.joinToString(separator = ", ")))
}