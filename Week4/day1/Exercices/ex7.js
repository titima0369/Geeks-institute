(function(userName) {
    const navbar = document.getElementById("navbar");
    const div = document.createElement("div");
    div.innerHTML = `<span>Welcome, ${userName}!</span>
                     <img src="https://via.placeholder.com/40" alt="profile">`;
    navbar.appendChild(div);
})("John");
