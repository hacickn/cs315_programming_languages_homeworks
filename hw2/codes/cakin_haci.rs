

fn main() {
// 1. Iteration statements provided
// Iterations are provided in rust by using while, for and loop 
println!("1. Iteration statements provided \n");
let mut num = 0;
while num < 5 {
    if num != 4{
        println!("{} is the current value in while", num);
    }else{
        println!("while reached to 4\n");
        break;
    }
    num = num + 1;
}
let mut num1 = 0;
loop{
    if num1 == 4 {
        println!("loop reached to 4\n");
        break;
    }
    println!("{} is the current value in loop",num1);
    num1 = num1 + 1;
}

for num2 in 0..4{
    println!("{} is the current value in for",num2);
}
println!("for reached to 4");
// 2. Data structures suitable for iteration
// Built in data structures are in rust array
println!("\n2. Data structures suitable for iteration\n");
let array2 = [1907,24,02,2000];
for num4 in array2.iter(){
    println!("Element is: {}", num4 );
}

// 3. The way the next item is accessed
println!("\n3. The way the next item is accessed\n");
let mut num5 = 0;
   while num5 < 11 {
      if num5 == 6 {
        println!("num5 Reached to 6");
        break
    }
    println!("num5 =  {}", num5);
    num5 = num5 + 2;
  }

}
