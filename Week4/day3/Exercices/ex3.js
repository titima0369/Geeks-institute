const users = { user1: 18273, user2: 92833, user3: 90315 };

const usersArray = Object.entries(users);
console.log(usersArray);

const doubledIDs = usersArray.map(([user, id]) => [user, id * 2]);
console.log(doubledIDs);