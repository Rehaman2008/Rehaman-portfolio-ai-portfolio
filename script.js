/* =========================================================
   PORTFOLIO INTERACTIVITY SCRIPT
   Author: Shaik Rehaman Shareef
   Reg No: 2026BTAI076
========================================================= */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Typewriter Effect
  const typewriterElement = document.getElementById('typewriter');
  const typewriterPrefix = document.querySelector('.typewriter-prefix');
  if (typewriterElement) {
    const items = [
      { prefix: 'I am an ', text: 'AI & Machine Learning Enthusiast' },
      { prefix: 'I am a ', text: 'B.Tech CSE (AI) Student' }
    ];
    let itemIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const typeSpeed = 100;
    const backSpeed = 50;
    const delayBetweenWords = 2200;

    function type() {
      const current = items[itemIndex];
      if (typewriterPrefix) {
        typewriterPrefix.textContent = current.prefix;
      }
      if (isDeleting) {
        typewriterElement.textContent = current.text.substring(0, charIndex - 1);
        charIndex--;
      } else {
        typewriterElement.textContent = current.text.substring(0, charIndex + 1);
        charIndex++;
      }

      let currentSpeed = isDeleting ? backSpeed : typeSpeed;

      if (!isDeleting && charIndex === current.text.length) {
        currentSpeed = delayBetweenWords;
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        itemIndex = (itemIndex + 1) % items.length;
        currentSpeed = 500;
      }

      setTimeout(type, currentSpeed);
    }

    type();
  }

  // 2. Theme Toggle (Dark / Light)
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = themeToggle.querySelector('i');
  const savedTheme = localStorage.getItem('sr_portfolio_theme') || 'dark';

  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('sr_portfolio_theme', newTheme);
    updateThemeIcon(newTheme);
  });

  function updateThemeIcon(theme) {
    if (theme === 'light') {
      themeIcon.className = 'fa-solid fa-sun';
    } else {
      themeIcon.className = 'fa-solid fa-moon';
    }
  }

  // 3. Mobile Navigation Menu Toggle
  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  menuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('open');
    const icon = menuToggle.querySelector('i');
    if (navMenu.classList.contains('open')) {
      icon.className = 'fa-solid fa-xmark';
    } else {
      icon.className = 'fa-solid fa-bars';
    }
  });

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('open');
      menuToggle.querySelector('i').className = 'fa-solid fa-bars';
    });
  });

  // 4. Active Navigation Link on Scroll
  const sections = document.querySelectorAll('section[id]');
  
  function highlightActiveNav() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');
      const targetNavLink = document.querySelector(`.nav-list a[href*='${sectionId}']`);

      if (targetNavLink) {
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
          targetNavLink.classList.add('active');
        } else {
          targetNavLink.classList.remove('active');
        }
      }
    });
  }

  window.addEventListener('scroll', highlightActiveNav);

  // 5. Back to Top Button
  const backToTopBtn = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    if (window.pageYOffset > 400) {
      backToTopBtn.classList.add('show');
    } else {
      backToTopBtn.classList.remove('show');
    }
  });

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  // 6. Contact Form Submission Handler
  window.handleFormSubmit = function(event) {
    event.preventDefault();
    const submitBtn = document.getElementById('submit-btn');
    const feedback = document.getElementById('form-feedback');
    const form = document.getElementById('contact-form');

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const subject = document.getElementById('subject').value.trim();
    const message = document.getElementById('message').value.trim();

    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending message...';

    setTimeout(() => {
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="fa-solid fa-check"></i> Message Sent!';

      feedback.style.display = 'block';
      feedback.className = 'form-feedback success';
      feedback.innerHTML = `
        <div style="display: flex; align-items: flex-start; gap: 12px;">
          <i class="fa-solid fa-circle-check" style="font-size: 1.5rem; margin-top: 2px;"></i>
          <div>
            <h4 style="margin: 0 0 4px; font-size: 1.05rem; color: #10b981;">Message Sent Successfully!</h4>
            <p style="margin: 0 0 8px; font-size: 0.9rem; color: var(--text-primary);">
              Thank you, <strong>${name}</strong>! Your inquiry about <em>"${subject}"</em> has been received. I will reply to you at <strong>${email}</strong> shortly.
            </p>
            <a href="mailto:shaikrehamanshareef2008@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent('From: ' + name + ' (' + email + ')\n\n' + message)}" 
               class="btn btn-secondary" 
               style="display: inline-flex; padding: 6px 14px; font-size: 0.82rem; margin-top: 4px;"
               target="_blank">
              <i class="fa-solid fa-envelope-open-text"></i> Open in Your Email App
            </a>
          </div>
        </div>
      `;

      form.reset();

      setTimeout(() => {
        submitBtn.innerHTML = '<i class="fa-solid fa-paper-plane"></i> Send Message';
      }, 4000);
    }, 600);
  };
});
