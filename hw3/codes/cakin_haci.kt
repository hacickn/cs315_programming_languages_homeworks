fun main() {
    
    println("1) Nested subprogram definitions")
    var numForNestedSubprogram = 5
    fun sumOfSubractionMultiplication(x: Int): Int{
		val sum = x + 10
    	fun multiply(y: Int): Int{
        	return sum * y
    	}
        fun substract(y: Int): Int{
        	return sum - y
    	}
    	return multiply(10) + substract(10)
	}
  
    println("Result is : ${sumOfSubractionMultiplication(numForNestedSubprogram)} \n\n")

    println("2) Scope of local variables")
    var numberForScope1 = 0
    var numberForScope2 = 1
    var numberForScope3 = 5

    fun scopeOfSubProgram(value : Int){
        var numberForScope1 = 2
        numberForScope2 = 7
        var numberForScope4 = value
        numberForScope1 = 6;
        println("NumberForScope1 i is defined and called in function ${numberForScope1} in the function")
        println("NumberForScope2 i is defined and called in function ${numberForScope2} in the function")
        println("NumberForScope3 i is defined and called in function ${numberForScope3} in the function")
    }
     
    println("NumberForScope1 i is called in outside of function ${numberForScope1} before function called")
    println("NumberForScope2 i is called in outside of function ${numberForScope2} before function called")
    println("NumberForScope3 i is called in outside of function ${numberForScope3} before function called")
    scopeOfSubProgram(10)
    //println("NumberForScope3 i is defined and called in function ${numberForScope4}") // unreachable
    println("NumberForScope1 i is called in outside of function ${numberForScope1} after function called")
    println("NumberForScope2 i is called in outside of function ${numberForScope2} after function called")
    println("NumberForScope3 i is called in outside of function ${numberForScope3} after function called \n\n")

    println("3) Parameter passing methods")
    fun calculateProduct():Int{
        return 4 * 3
    }

    fun parameterPassingMethod(func:()->Int):Int{
        return func()
    }
    println("Parameter passing method's result is ${parameterPassingMethod(::calculateProduct)} \n\n");

    println("4) Keyword and default parameters")
    fun keywordAndDefaultParameter(temp: Int = 0, trace: Int =2, number : Int=3){
        println("In the method parameter temp is ${temp}")
        println("In the method parameter trace is ${trace}")
        println("In the method parameter number is ${number}")
    }

    fun sayMyName(name: String = "Empty",surname:String = "Empty"){
        println("My name is ${name} ${surname}")
    }

    println("With 0 parameter ---- \n")
    sayMyName()
    keywordAndDefaultParameter()
    println("With 1 parameter ---- \n")
    sayMyName("Hacı")
    keywordAndDefaultParameter(15)
    println("With 2 parameter ---- \n")
    keywordAndDefaultParameter(30)
    println("With keywords \n")
    sayMyName(name= "Hacı",surname="Çakın" )
    keywordAndDefaultParameter(number= 3333)


    println("5) Closures")

    var total = 0
    var studentNumber = 0
    var studentGrades = listOf(90,80,85,30,90,90,20,10)
    studentGrades.forEach(){ 
        total = total + it
        studentNumber++
    }
    println("Average scor is ${total/studentNumber}")
}
