// dashboard.js

// Example: Dashboard navigation toggle
const dashboardNavLinks = document.querySelectorAll('.dashboard-nav-link');

dashboardNavLinks.forEach(link => {
    link.addEventListener('click', (event) => {
        // Handle active link highlighting
        dashboardNavLinks.forEach(l => l.classList.remove('active'));
        event.currentTarget.classList.add('active');
        
        // Load corresponding content dynamically if needed
        const sectionId = event.currentTarget.getAttribute('data-section');
        document.querySelectorAll('.dashboard-section').forEach(section => {
            section.style.display = 'none';
        });
        document.querySelector(`#${sectionId}`).style.display = 'block';
    });
});

// Example: Display notifications
const notificationButton = document.querySelector('#showNotifications');
const notificationBox = document.querySelector('.notification-box');

notificationButton.addEventListener('click', () => {
    notificationBox.classList.toggle('hidden');
});
