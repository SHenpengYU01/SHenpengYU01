// js/custom.js

document.addEventListener('DOMContentLoaded', (event) => {
    // Select all copy buttons
    const copyButtons = document.querySelectorAll('.md-clipboard');

    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Change button text to "Copied!" for 2 seconds
            button.textContent = 'Copied!';
            setTimeout(() => {
                button.textContent = '';
            }, 2000);
        });
    });
});
