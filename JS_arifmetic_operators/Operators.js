let a = 2, b = 3;

function restoreOfValue() {
    a = 2, b = 3;
}


function assingmentOperators() {
    console.log(a = b); // simple assigment
    restoreOfValue();
    
    console.log(a += b); // assigment with summ 
    restoreOfValue();

    console.log(a -= b); // assingment with difference
    restoreOfValue();

    console.log(a *= b); // assingment with multiplication
    restoreOfValue();

    console.log(a /= b); // assingment with division
    restoreOfValue(); 

    console.log(a %= b); // assingment by module
    restoreOfValue(); 

    console.log(a << b); // assingment with shift to left
    restoreOfValue(); 

    console.log(a >> b); // assingment with shift to right
    restoreOfValue(); 

    console.log(a >>> b); // assingment with unsigned shift to right
    restoreOfValue(); 
}

function comparisonOperators() {
    console.log(a == b); // equality 
    console.log(a != b); // inequality
    console.log(a === b); // strict equality
    console.log(a !== b); // strict inequality 
    console.log(a > b); // more
    console.log(a < b); // less
    console.log(a >= b); // more or equality
    console.log(a <= b); // less of equality
}

function arifmeticOperators() {
    
}

// assingmentOperators();
// comparisonOperators();
