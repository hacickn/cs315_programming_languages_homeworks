fn myfunction1 ()-> bool {
    println!(" * 1st function * ");
    return false;
}
fn myfunction2 ()-> bool {
    println!(" * 2nd function * ");
    return true;
}

fn myfunction3 ()-> bool {
    println!(" * 3rd function * ");
    return false;
}

fn main() {
	let _bool1 = false;
	let _bool2 = true;

    /*
        1. Boolean operators provided &,|,!,^
        2.  Data types for operands of boolean operators[  &,|,!,^] - bool
    */
	println!("1. Boolean operators provided &&,||,! \n");
	println!(
	  "2. Data types for operands of boolean operators [ &&,||,!] \n"
	);

    println!("false and true =  {} \n" , _bool1 && _bool2);
    println!("false or true =  {} \n" ,  _bool1 || _bool2);
    println!("not false and true =  {} \n" ,  !_bool1 && _bool2);
    println!("\n\n");
	
    /*
    3. Operator precedence rules in descending order
    1 --> ()     
    2 --> !     
    3 --> &
    4 --> ^ 
    4 --> |  
    */

    println!("3. Operator precedence rules in descending order \n");
    println!("    1 --> ()     2 --> !     3 --> &4 --> ^ 4 --> |  \n\n");
    
    println!("True and True or False = {} \n", _bool2 && _bool2 || _bool1);
    println!("True or True and False = {} \n", _bool2 ||  _bool2 && _bool1);
    println!("False or True and False = {} \n", _bool1 ||  _bool2 && _bool1);
    println!("False or True and False = {} \n", _bool1 ||  _bool2 && _bool1);
    println!("True and True and (True or True) and False = {} \n", _bool2 && _bool2 && (_bool2 || _bool2) && _bool1);
    println!("True and True and not (True or True) and False = {} \n", _bool2 && _bool2 && !(_bool2 ||  _bool2) && _bool1);
    println!("True and True and True or True and False = {} \n", _bool2 && _bool2 && _bool2 ||  _bool2 && _bool1);
    println!("True and not True and True or True and False = {} \n", _bool2 && ! _bool2 && _bool2 ||  _bool2 && _bool1);
    println!("True xor not True and True or True and False = {} \n", _bool2 ^ ! _bool2 && _bool2 ||  _bool2 && _bool1);
    println!("\n\n");

    /*
    4 Operator associativity rules for bool operators
    all operators are left associativity.
    */

    println!("4. Operator associativity rules for bool operator \n\n");
    println!("True and True and False => {} \n", _bool2 && _bool2 && _bool1);
    println!("True or True or False => {} \n",    _bool2 || _bool2 || _bool1);
    println!("\n\n");

    /*
    5. Operand evaluation order
    LEFT -> RIGHT in rust
    */
    println!("5. Operand evaluation order \n\n");
    println!("myfunction1() and myfunction2() and myfunction3() = {} \n", myfunction1() && myfunction2() && myfunction3());
    println!("myfunction1() or myfunction2() or myfunction3() =  {}  \n", myfunction1() || myfunction2() || myfunction3());
    println!("myfunction1() == myfunction2() ^ myfunction3() = {}  \n", (myfunction1() == myfunction2()) ^ myfunction3());
    println!("\n\n");

    /*
    6. short-circuit evoluation
    LEFT -> RIGHT in c
    */
    println!("6. short-circuit evoluation \n\n");
    println!("These exapmles shows that rust has short circuit \n");
    println!("myfunction1() and myfunction2() and myfunction3() = {} \n", myfunction1() && myfunction2() && myfunction3());
    println!("myfunction1() or myfunction2() or myfunction3() =  {}  \n", myfunction1() || myfunction2() || myfunction3());
    println!("myfunction1() == myfunction2() ^ myfunction3() = {}  \n", (myfunction1() == myfunction2()) ^ myfunction3());
    println!("\n\n");
}