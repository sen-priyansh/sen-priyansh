document.addEventListener('DOMContentLoaded', () => {
    const button1 = document.querySelector('.glow-button:nth-of-type(1)');
    const button2 = document.querySelector('#random-button'); // Target Button 2 by ID
    const maxOffset = 50; // Adjust this value to control the maximum movement

    // Add click event listener to Button 1
    if (button1) {
        button1.addEventListener('click', () => {
            window.location.href = 'congratulations.html'; // Redirect to new page
        });
    }

    // Add random position functionality to Button 2
    if (button2) {
        button2.addEventListener('click', () => {
            const tile = button2.closest('.tile'); // Find the closest tile
            const tileRect = tile.getBoundingClientRect();
            const buttonRect = button2.getBoundingClientRect();

            const maxX = tileRect.width - buttonRect.width - maxOffset;
            const maxY = tileRect.height - buttonRect.height - maxOffset;

            const randomX = Math.floor(Math.random() * (maxX - maxOffset)) + maxOffset;
            const randomY = Math.floor(Math.random() * (maxY - maxOffset)) + maxOffset;

            button2.style.left = `${randomX}px`;
            button2.style.top = `${randomY}px`;
            button2.style.position = 'absolute'; // Ensure button is positioned absolutely
        });
    } else {
        console.error('Element with ID "random-button" not found.');
    }
});
