const toggleButton = document.getElementById('toggleButton');
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('overlay');
        
        toggleButton.addEventListener('click', function() {
            sidebar.classList.toggle('sidebar-visible');
            overlay.classList.toggle('overlay-visible');
            toggleButton.textContent = sidebar.classList.contains('sidebar-visible') ? '✕' : '☰';
            toggleButton.style.left = sidebar.classList.contains('sidebar-visible') ? '270px' : '20px';
        });
        
        overlay.addEventListener('click', function() {
            sidebar.classList.remove('sidebar-visible');
            overlay.classList.remove('overlay-visible');
            toggleButton.textContent = '☰';
            toggleButton.style.left = '20px';
        });