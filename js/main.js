/* =========================================
   MAIN JAVASCRIPT (PREMIUM ENHANCEMENTS)
   ========================================= */

document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation Toggle
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');
    const body = document.body;

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent immediate close
            navMenu.classList.toggle('active');

            // Accessibility & Icon toggle
            const isActive = navMenu.classList.contains('active');
            mobileToggle.setAttribute('aria-expanded', isActive);
            mobileToggle.textContent = isActive ? '✕' : '☰';

            // Prevent background scrolling when menu is open
            body.style.overflow = isActive ? 'hidden' : '';
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && e.target !== mobileToggle) {
                navMenu.classList.remove('active');
                mobileToggle.textContent = '☰';
                mobileToggle.setAttribute('aria-expanded', 'false');
                body.style.overflow = '';
            }
        });
    }

    // Close menu smoothly when clicking a link
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (mobileToggle) {
                mobileToggle.textContent = '☰';
                mobileToggle.setAttribute('aria-expanded', 'false');
            }
            if (navMenu) navMenu.classList.remove('active');
            body.style.overflow = '';
        });
    });

    // Active Link Highlighting & Premium ScrollSpy
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';

    const setActiveNav = (targetHref) => {
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === targetHref || (targetHref === '' && href === 'index.html') || (targetHref === '/' && href === 'index.html')) {
                link.classList.add('active');
            }
        });
    };

    // 1. Initial Load State
    setActiveNav(currentPath);

    // 2. ScrollSpy (Home Page Dynamic Highlighting)
    if (currentPath === 'index.html' || currentPath === '') {
        const sections = document.querySelectorAll('header.hero, section');
        let sectionMap = [];

        sections.forEach(sec => {
            let target = 'index.html'; 
            if (sec.id === 'about' || sec.classList.contains('hero') || sec.id === 'journey') {
                target = 'index.html';
            } else if (sec.id === 'powerbi-portfolio' || sec.querySelector('.project-card')) {
                target = 'projects.html';
            } else if (sec.id === 'thesis-vault') {
                target = 'sop.html';
            } else if (sec.querySelector('a[href="experience.html"]')) {
                target = 'experience.html';
            } else if (sec.querySelector('a[href="education.html"]')) {
                target = 'education.html';
            } else if (sec.id === 'contact') {
                target = 'contact.html';
            }
            sectionMap.push({ element: sec, targetHref: target });
        });

        const scrollSpyOptions = { root: null, rootMargin: '-40% 0px -60% 0px', threshold: 0 };
        const scrollSpyObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const mapped = sectionMap.find(s => s.element === entry.target);
                    if (mapped) setActiveNav(mapped.targetHref);
                }
            });
        }, scrollSpyOptions);

        sectionMap.forEach(sec => scrollSpyObserver.observe(sec.element));
    }

    // Premium Scroll Animations (Optimized Intersection Observer)
    // Add scroll observer for zigzag timeline rows
    const storyObserverOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2
    };

    const storyObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, storyObserverOptions);

    const storyRows = document.querySelectorAll('.zigzag-row');
    storyRows.forEach(row => {
        storyObserver.observe(row);
    });

    const observerOptions = {
        threshold: 0.15, // Trigger slightly later for better effect
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add a class to trigger CSS transition
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                // Unobserve after animation (performance)
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Select elements to animate
    const animateElements = document.querySelectorAll(
        '.card, .timeline-item, .hero-text, .hero-visual, .section-title, .project-card, .btn, .zigzag-row'
    );

    // Initial state setup (if JS fails, CSS should have defaults, but here we enforce starting state for animation)
    animateElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        // Stagger animations slightly for a premium feel
        // We use inline styles for the transition to ensure it overrides specific class styles if needed
        el.style.transition = `opacity 0.8s cubic-bezier(0.25, 0.8, 0.25, 1) ${index * 0.05}s, transform 0.8s cubic-bezier(0.25, 0.8, 0.25, 1) ${index * 0.05}s`;
        observer.observe(el);
    });

    // Generic Language Toggle Logic
    const langToggle = document.getElementById('langToggle');
    // Set initial state based on toggle
    if (langToggle) {
        
        const updateLanguage = (isEnglish) => {
            const deElements = document.querySelectorAll('.lang-de');
            const enElements = document.querySelectorAll('.lang-en');
            const deLabel = document.querySelector('.toggle-label.de');
            const enLabel = document.querySelector('.toggle-label.en');

            if (isEnglish) {
                // Switch to English
                deElements.forEach(el => el.style.display = 'none');
                enElements.forEach(el => el.style.display = '');
                if(deLabel) { deLabel.classList.remove('active'); deLabel.style.color = 'var(--text-light)'; deLabel.style.fontWeight = 'normal'; }
                if(enLabel) { enLabel.classList.add('active'); enLabel.style.color = 'var(--primary-color)'; enLabel.style.fontWeight = 'bold'; }
                localStorage.setItem('preferredLang', 'en');
            } else {
                // Switch to German (Default)
                enElements.forEach(el => el.style.display = 'none');
                deElements.forEach(el => el.style.display = '');
                if(enLabel) { enLabel.classList.remove('active'); enLabel.style.color = 'var(--text-light)'; enLabel.style.fontWeight = 'normal'; }
                if(deLabel) { deLabel.classList.add('active'); deLabel.style.color = 'var(--primary-color)'; deLabel.style.fontWeight = 'bold'; }
                localStorage.setItem('preferredLang', 'de');
            }
        };

        // Check if there's a saved language preference across pages
        const savedLang = localStorage.getItem('preferredLang');
        if (savedLang === 'en') {
            langToggle.checked = true;
            updateLanguage(true);
        } else {
            langToggle.checked = false;
            updateLanguage(false);
        }

        langToggle.addEventListener('change', function() {
            updateLanguage(this.checked);
        });
    } else {
        // Enforce language on pages without toggle but still having translatable elements
        const savedLang = localStorage.getItem('preferredLang');
        const deElements = document.querySelectorAll('.lang-de');
        const enElements = document.querySelectorAll('.lang-en');
        if (savedLang === 'en') {
            deElements.forEach(el => el.style.display = 'none');
            enElements.forEach(el => el.style.display = '');
        } else {
            enElements.forEach(el => el.style.display = 'none');
            deElements.forEach(el => el.style.display = '');
        }
    }
});

// Image Modal Functions (Global Scope for inline onclicks)
window.openImageModal = function(src) {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    if(modal && modalImg) {
        modalImg.src = src;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent scrolling in background
    }
};

window.closeImageModal = function() {
    const modal = document.getElementById('imageModal');
    if(modal) {
        modal.classList.remove('active');
        document.body.style.overflow = ''; // Restore scrolling
    }
};

// Also close on ESC
document.addEventListener('keydown', (e) => {
    if(e.key === 'Escape') closeImageModal();
});
