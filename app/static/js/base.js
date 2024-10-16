// base.js

// Example: Toggle Navbar on smaller screens
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');

navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('is-active');
});

// Example: Common alert message close
const alertCloseButtons = document.querySelectorAll('.alert-close');
alertCloseButtons.forEach(button => {
    button.addEventListener('click', () => {
        button.parentElement.style.display = 'none';
    });
});
