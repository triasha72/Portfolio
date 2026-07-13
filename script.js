const button = document.querySelector('.menu-button');
const header = document.querySelector('.site-header');
if (button && header) {
  button.addEventListener('click', () => {
    const open = header.classList.toggle('open');
    button.setAttribute('aria-expanded', String(open));
  });
}
const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();
const observer = new IntersectionObserver((entries)=>{
  entries.forEach(entry=>{ if(entry.isIntersecting){ entry.target.classList.add('is-visible'); observer.unobserve(entry.target); } });
},{threshold:.12});
document.querySelectorAll('[data-reveal]').forEach(el=>observer.observe(el));
