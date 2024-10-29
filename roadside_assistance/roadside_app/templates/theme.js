// Theme management
function initializeTheme() {
    const themeSwitch = document.getElementById('themeSwitch');
    const themeSwitchIcon = themeSwitch.querySelector('i');
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    themeSwitch.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        // Update theme
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        // Update icon
        updateThemeIcon(newTheme);
    });
}

function updateThemeIcon(theme) {
    const themeSwitchIcon = document.querySelector('#themeSwitch i');
    if (theme === 'dark') {
        themeSwitchIcon.classList.remove('fa-moon');
        themeSwitchIcon.classList.add('fa-sun');
    } else {
        themeSwitchIcon.classList.remove('fa-sun');
        themeSwitchIcon.classList.add('fa-moon');
    }
}

// Initialize theme when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeTheme();
    
    // Apply saved theme immediately
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
});