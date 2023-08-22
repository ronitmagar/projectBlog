const slider = document.querySelector('.slider-container');
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', (e) => {
  isDown = true;
  slider.classList.add('active');
  startX = e.pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;
});
slider.addEventListener('mouseleave', () => {
  isDown = false;
  slider.classList.remove('active');
});
slider.addEventListener('mouseup', () => {
  isDown = false;
  slider.classList.remove('active');
});
slider.addEventListener('mousemove', (e) => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - slider.offsetLeft;
  const walk = (x - startX) * 3; // adjust scrolling speed
  slider.scrollLeft = scrollLeft - walk;
});

const blogLinks = document.querySelectorAll('.blog-link');
blogLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    // open the whole blog
    window.location.href = link.href;
  });
});
