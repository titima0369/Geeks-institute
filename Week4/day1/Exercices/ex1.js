function funcOne() {
    let a = 5;
    if (a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}
funcOne(); 

let a = 0;
function funcTwo() {
    a = 5;
}
function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

funcThree();
funcTwo();
funcThree();
function funcFour() {
    window.a = "hello"; 
}
function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

funcFour();
funcFive(); 

let a2 = 1;
function funcSix() {
    let a2 = "test"; 
    alert(`inside the funcSix function ${a2}`);
}

funcSix();

let a3 = 2;
if (true) {
    let a3 = 5;
    alert(`in the if block ${a3}`);
}
alert(`outside of the if block ${a3}`);
