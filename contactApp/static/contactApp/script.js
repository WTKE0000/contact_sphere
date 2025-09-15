document.getElementById('contactForm').addEventListener('submit', function(event) {
    // Prevent the form from submitting
    event.preventDefault();

    // Get the input values
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;

    // Validate name (only characters)
    if (!/^[a-zA-Z\s]+$/.test(name)) {
        alert('Please enter a valid name using characters only.');
        return;
    }

    // Validate phone number (only digits)
    if (!/^\d+$/.test(phone)) {
        alert('Please enter a valid phone number using digits only.');
        return;
    }

    // Validate email format
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // If all validations pass
    alert('Contact saved successfully!');

    // Optionally, reset the form
    document.getElementById('contactForm').reset();
});