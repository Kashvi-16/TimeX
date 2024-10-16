// login.js

// Form validation for login
const loginForm = document.querySelector('#loginForm');

loginForm.addEventListener('submit', (event) => {
    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;
    
    if (username === '' || password === '') {
        event.preventDefault();
        alert('Username and Password are required!');
    }
});

// Toggle password visibility
const passwordField = document.querySelector('#password');
const togglePassword = document.querySelector('#togglePassword');

togglePassword.addEventListener('click', () => {
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    togglePassword.classList.toggle('fa-eye-slash');
});
