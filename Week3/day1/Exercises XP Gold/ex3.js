let age = [20,5,12,43,98,55];
let sum = 0;
for ( let i = 0 ; age.length > i ; i++)
{
    sum = sum + age[i];
}
 console.log(`the sum of all the numbers is ${sum}`);
 let highest  = age[0];
 for ( let i = 1 ; age.length > i ; i++) {

 if (age[i] > highest) {
    highest = age[i]; 
 }
 }
 console.log(`the highest of all the numbers is ${highest}`);