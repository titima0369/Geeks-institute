const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
};  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}; 


const shoppingList = ["banana", "orange", "apple"];


function myBill() {
    let total = 0;

    for (let i = 0; i < shoppingList.length; i++) {
        let item = shoppingList[i];

        if (item in stock && stock[item] > 0) {
            total += prices[item];   
            stock[item] -= 1;      
        }
    }

    return total;
}

console.log("Total bill:", myBill());
console.log("Updated stock:", stock); // to see stock changes

