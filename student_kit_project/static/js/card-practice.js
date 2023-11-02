let currentSlide = 0;
const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');
const slideWidth = slides[0].offsetWidth;

function showSlide(n) {
    currentSlide = (currentSlide + n + slides.length) % slides.length;
    const transformValue = -currentSlide * slideWidth;
    slider.style.transform = `translateX(${transformValue}px)`;
    updateSlideCount(currentSlide + 1, slides.length); // Update slide count
}

function changeSlide(n) {
    showSlide(n);
}

function updateSlideCount(current, total) {
    const slideCountElement = document.getElementById('slide-count');
    slideCountElement.textContent = `${current} of ${total}`;
}

showSlide(0);
