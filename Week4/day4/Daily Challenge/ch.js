const form = document.getElementById('userForm');
const output = document.getElementById('output');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the page from reloading

    // Step 3: Get input values
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;

    // Step 4: Create JSON object
    const userData = {
        firstName: firstName,
        lastName: lastName
    };

    output.textContent = JSON.stringify(userData, null, 2);
});
