// Mobile menu
const button = document.querySelector('.menu-button');
const header = document.querySelector('.site-header');
if (button && header) {
  button.addEventListener('click', () => {
    const open = header.classList.toggle('open');
    button.setAttribute('aria-expanded', String(open));
  });
}

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Scroll progress bar
const progress = document.createElement('div');
progress.className = 'scroll-progress';
progress.setAttribute('aria-hidden', 'true');
document.body.appendChild(progress);
const updateProgress = () => {
  const max = document.documentElement.scrollHeight - window.innerHeight;
  progress.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%';
};
window.addEventListener('scroll', updateProgress, { passive: true });
updateProgress();

// Staggered reveals: promote grid cards to individual reveal targets
document.querySelectorAll('.timeline-grid, .method-grid, .beyond-grid, .feature-grid').forEach(grid => {
  [...grid.children].forEach((card, i) => {
    card.setAttribute('data-reveal', '');
    card.style.setProperty('--reveal-delay', (i * 90) + 'ms');
  });
});
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));

// 3D tilt on project cards
if (!reduceMotion && matchMedia('(pointer:fine)').matches) {
  document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      card.style.transform = 'perspective(900px) rotateY(' + (x * 4) + 'deg) rotateX(' + (y * -4) + 'deg) translateY(-4px)';
    });
    card.addEventListener('mouseleave', () => { card.style.transform = ''; });
  });

  // Magnetic buttons
  document.querySelectorAll('.button').forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const r = btn.getBoundingClientRect();
      const x = e.clientX - r.left - r.width / 2;
      const y = e.clientY - r.top - r.height / 2;
      btn.style.transform = 'translate(' + (x * 0.18) + 'px, ' + (y * 0.18) + 'px)';
    });
    btn.addEventListener('mouseleave', () => { btn.style.transform = ''; });
  });
}
