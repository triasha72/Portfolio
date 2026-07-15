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

// Staggered reveals
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

// 3D tilt + magnetic buttons (fine pointers only)
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

// Cursor spotlight + hero photo parallax
if (!reduceMotion && matchMedia('(pointer:fine)').matches) {
  const glow = document.createElement('div');
  glow.className = 'cursor-glow';
  glow.setAttribute('aria-hidden', 'true');
  document.body.appendChild(glow);
  window.addEventListener('mousemove', (e) => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
    glow.style.opacity = '1';
  }, { passive: true });
  document.documentElement.addEventListener('mouseleave', () => { glow.style.opacity = '0'; });

  const hero = document.querySelector('.hero');
  const mainPhoto = document.querySelector('.main-photo');
  const smallPhoto = document.querySelector('.small-photo');
  if (hero && mainPhoto && smallPhoto) {
    hero.addEventListener('mousemove', (e) => {
      const r = hero.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      mainPhoto.style.transform = 'rotate(2deg) translate(' + (x * -12) + 'px,' + (y * -10) + 'px)';
      smallPhoto.style.transform = 'rotate(-5deg) translate(' + (x * 16) + 'px,' + (y * 12) + 'px)';
    });
    hero.addEventListener('mouseleave', () => {
      mainPhoto.style.transform = '';
      smallPhoto.style.transform = '';
    });
  }
}

// Scrollspy
const navLinks = [...document.querySelectorAll('.nav-links a[href^="#"]')];
const spied = navLinks
  .map(a => document.getElementById(a.getAttribute('href').slice(1)))
  .filter(Boolean);
if (spied.length) {
  const spy = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + entry.target.id));
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  spied.forEach(sec => spy.observe(sec));
}

// Intro reveal (once per browser session)
if (!reduceMotion && !sessionStorage.getItem('introSeen')) {
  sessionStorage.setItem('introSeen', '1');
  const intro = document.createElement('div');
  intro.className = 'intro-overlay';
  intro.setAttribute('aria-hidden', 'true');
  intro.innerHTML = '<div class="intro-inner"><div class="intro-mark">TS</div><p>Triasha Sarkar</p></div>';
  document.body.appendChild(intro);
  intro.addEventListener('animationend', (e) => {
    if (e.target === intro) intro.remove();
  });
  setTimeout(() => { if (intro.parentNode) intro.remove(); }, 3000);
}

// Paper plane riding the scroll-progress bar
const plane = document.createElement('span');
plane.className = 'scroll-plane';
plane.setAttribute('aria-hidden', 'true');
plane.textContent = '✈︎';
document.body.appendChild(plane);
const updatePlane = () => {
  const max = document.documentElement.scrollHeight - window.innerHeight;
  plane.style.left = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%';
};
window.addEventListener('scroll', updatePlane, { passive: true });
updatePlane();

// Back-to-top rocket
const toTop = document.createElement('button');
toTop.className = 'to-top';
toTop.setAttribute('aria-label', 'Back to top');
toTop.textContent = '↑';
document.body.appendChild(toTop);
window.addEventListener('scroll', () => {
  toTop.classList.toggle('show', window.scrollY > 600);
}, { passive: true });
toTop.addEventListener('click', () => {
  toTop.classList.add('launch');
  window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
  setTimeout(() => toTop.classList.remove('launch'), 800);
});

// Constellation network in the hero
const heroDecor = document.querySelector('.hero-decor');
if (heroDecor && !reduceMotion) {
  const canvas = document.createElement('canvas');
  canvas.className = 'hero-net';
  canvas.setAttribute('aria-hidden', 'true');
  heroDecor.appendChild(canvas);
  const ctx = canvas.getContext('2d');
  let w, h, nodes = [], mouse = null, running = true;

  const resize = () => {
    w = canvas.width = heroDecor.offsetWidth;
    h = canvas.height = heroDecor.offsetHeight;
  };
  resize();
  window.addEventListener('resize', resize);

  const N = Math.min(55, Math.floor(w * h / 26000));
  for (let i = 0; i < N; i++) {
    nodes.push({
      x: Math.random() * w, y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.35, vy: (Math.random() - 0.5) * 0.35,
      r: 1 + Math.random() * 1.8,
      amber: Math.random() < 0.18
    });
  }
  document.addEventListener('mousemove', (e) => {
    const r = canvas.getBoundingClientRect();
    mouse = { x: e.clientX - r.left, y: e.clientY - r.top };
  }, { passive: true });

  const LINK = 130;
  const draw = () => {
    if (!running) return;
    ctx.clearRect(0, 0, w, h);
    nodes.forEach(n => {
      n.x += n.vx; n.y += n.vy;
      if (n.x < 0 || n.x > w) n.vx *= -1;
      if (n.y < 0 || n.y > h) n.vy *= -1;
    });
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x, dy = nodes[i].y - nodes[j].y;
        const d = Math.hypot(dx, dy);
        if (d < LINK) {
          ctx.strokeStyle = 'rgba(45,212,191,' + (0.14 * (1 - d / LINK)) + ')';
          ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(nodes[i].x, nodes[i].y); ctx.lineTo(nodes[j].x, nodes[j].y); ctx.stroke();
        }
      }
      if (mouse) {
        const dx = nodes[i].x - mouse.x, dy = nodes[i].y - mouse.y;
        const d = Math.hypot(dx, dy);
        if (d < LINK * 1.3) {
          ctx.strokeStyle = 'rgba(245,165,36,' + (0.22 * (1 - d / (LINK * 1.3))) + ')';
          ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(nodes[i].x, nodes[i].y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke();
        }
      }
    }
    nodes.forEach(n => {
      ctx.fillStyle = n.amber ? 'rgba(245,165,36,.7)' : 'rgba(45,212,191,.6)';
      ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2); ctx.fill();
    });
    requestAnimationFrame(draw);
  };
  new IntersectionObserver((entries) => {
    const visible = entries[0].isIntersecting;
    if (visible && !running) { running = true; draw(); }
    else if (!visible) running = false;
    else if (visible && running) draw();
  }, { threshold: 0 }).observe(heroDecor.parentElement);
}

// Scroll parallax on hero glow orbs
const decorEl = document.querySelector('.hero-decor');
if (decorEl && !reduceMotion) {
  window.addEventListener('scroll', () => {
    decorEl.style.transform = 'translateY(' + (window.scrollY * 0.22) + 'px)';
  }, { passive: true });
}
