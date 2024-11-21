document.addEventListener('DOMContentLoaded', function () {
    const scrollWrapper = document.querySelector('.scroll-wrapper');
    const scrollContent = document.querySelector('.scroll-content');
    const btnLeft = document.getElementById('scroll-left');
    const btnRight = document.getElementById('scroll-right');

    // Desplazamiento en píxeles
    const scrollAmount = 300;

    btnLeft.addEventListener('click', () => {
        scrollWrapper.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });

    btnRight.addEventListener('click', () => {
        scrollWrapper.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });
});
