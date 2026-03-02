window.HELP_IMPROVE_VIDEOJS = false;

// More Works Dropdown Functionality
function toggleMoreWorks() {
    const dropdown = document.getElementById('moreWorksDropdown');
    const button = document.querySelector('.more-works-btn');

    if (dropdown.classList.contains('show')) {
        dropdown.classList.remove('show');
        button.classList.remove('active');
    } else {
        dropdown.classList.add('show');
        button.classList.add('active');
    }
}

// Close dropdown when clicking outside
document.addEventListener('click', function (event) {
    const container = document.querySelector('.more-works-container');
    const dropdown = document.getElementById('moreWorksDropdown');
    const button = document.querySelector('.more-works-btn');

    if (container && !container.contains(event.target)) {
        dropdown.classList.remove('show');
        button.classList.remove('active');
    }
});

// Close dropdown on escape key
document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        const dropdown = document.getElementById('moreWorksDropdown');
        const button = document.querySelector('.more-works-btn');
        dropdown.classList.remove('show');
        button.classList.remove('active');
    }
});

// Copy BibTeX to clipboard
function copyBibTeX() {
    const bibtexElement = document.getElementById('bibtex-code');
    const button = document.querySelector('.copy-bibtex-btn');
    const copyText = button.querySelector('.copy-text');

    if (bibtexElement) {
        navigator.clipboard.writeText(bibtexElement.textContent).then(function () {
            // Success feedback
            button.classList.add('copied');
            copyText.textContent = 'Cop';

            setTimeout(function () {
                button.classList.remove('copied');
                copyText.textContent = 'Copy';
            }, 2000);
        }).catch(function (err) {
            console.error('Failed to copy: ', err);
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = bibtexElement.textContent;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);

            button.classList.add('copied');
            copyText.textContent = 'Cop';
            setTimeout(function () {
                button.classList.remove('copied');
                copyText.textContent = 'Copy';
            }, 2000);
        });
    }
}

// Scroll to top functionality
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Show/hide scroll to top button
window.addEventListener('scroll', function () {
    const scrollButton = document.querySelector('.scroll-to-top');
    if (window.pageYOffset > 300) {
        scrollButton.classList.add('visible');
    } else {
        scrollButton.classList.remove('visible');
    }
});

// Video carousel autoplay when in view
function setupVideoCarouselAutoplay() {
    const carouselVideos = document.querySelectorAll('.results-carousel video');

    if (carouselVideos.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const video = entry.target;
            if (entry.isIntersecting) {
                // Video is in view, play it
                video.play().catch(e => {
                    // Autoplay failed, probably due to browser policy
                    console.log('Autoplay prevented:', e);
                });
            } else {
                // Video is out of view, pause it
                video.pause();
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% of the video is visible
    });

    carouselVideos.forEach(video => {
        observer.observe(video);
    });
}

$(document).ready(function () {
    // Check for click events on the navbar burger icon

    var options = {
        slidesToScroll: 1,
        slidesToShow: 1,
        loop: true,
        infinite: true,
        autoplay: true,
        autoplaySpeed: 5000,
    }

    // Initialize all div with carousel class
    var carousels = bulmaCarousel.attach('.carousel', options);

    bulmaSlider.attach();

    // Setup video autoplay for carousel
    setupVideoCarouselAutoplay();

    // Initialize Scroll Animations
    setupScrollReveal();

    // Initialize Stat Counter
    setupStatCountUp();

    // Smooth scroll for nav links
    setupSmoothScroll();
})

// Smooth Scroll for Navigation
function setupSmoothScroll() {
    document.querySelectorAll('.hl-nav-links a, .hl-nav-logo').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Offset for fixed header (approx 80px)
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });
}

// Stat Count-Up Animation
function setupStatCountUp() {
    var statItems = document.querySelectorAll('.stat-animate');
    if (!statItems.length) return;

    var animated = false;

    var observer = new IntersectionObserver(function (entries) {
        if (animated) return;
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                animated = true;
                observer.disconnect();
                triggerCountUp(statItems);
            }
        });
    }, { threshold: 0.3 });

    observer.observe(document.querySelector('.stat-bar'));
}

function triggerCountUp(items) {
    var duration = 1800; // ms

    items.forEach(function (item, index) {
        // Stagger the reveal
        item.classList.add('is-counting');

        var valueEl = item.querySelector('.stat-value');
        var target = parseFloat(valueEl.dataset.target);
        var suffix = valueEl.dataset.suffix || '';
        var decimals = parseInt(valueEl.dataset.decimals) || 0;

        // Delay counting to match the CSS stagger
        var delay = index * 120;
        var startTime = null;

        setTimeout(function () {
            function step(timestamp) {
                if (!startTime) startTime = timestamp;
                var progress = Math.min((timestamp - startTime) / duration, 1);

                // Ease-out cubic
                var eased = 1 - Math.pow(1 - progress, 3);
                var current = eased * target;

                valueEl.textContent = current.toFixed(decimals) + suffix;

                if (progress < 1) {
                    requestAnimationFrame(step);
                } else {
                    valueEl.textContent = target.toFixed(decimals) + suffix;
                }
            }
            requestAnimationFrame(step);
        }, delay);
    });
}

// Scroll Reveal Animation System
function setupScrollReveal() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                // Optional: Stop observing once revealed
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15, // Trigger when 15% visible
        rootMargin: "0px 0px -50px 0px"
    });

    document.querySelectorAll('.reveal').forEach(el => {
        el.classList.add('will-animate'); // Enable animation state
        observer.observe(el);
    });
}

/* ── Mobile / Desktop video source swap ────────────────── */
(function () {
    var isMobile = window.matchMedia('(max-width: 768px)').matches;
    var src = isMobile ? 'plots/hierloc_ad_mobile.mp4' : 'plots/hierloc_ad.mp4';
    ['showcase-video-fs', 'showcase-video-inline'].forEach(function (id) {
        var v = document.getElementById(id);
        if (v) {
            v.src = src;
            v.load();
            // Re-trigger autoplay after programmatic load (only for fullscreen)
            if (id === 'showcase-video-fs') {
                v.play().catch(function () {});
            }
        }
    });
})();

/* ── Fullscreen Video Overlay ───────────────────────────── */
(function () {
    var overlay = document.getElementById('video-fullscreen-overlay');
    var fsVideo = document.getElementById('showcase-video-fs');
    var content = document.getElementById('post-video-content');
    var skipBtn = document.getElementById('skip-video-btn');

    if (!overlay || !fsVideo || !content) return;

    document.documentElement.classList.add('video-playing');

    function dismiss() {
        fsVideo.pause();
        document.documentElement.classList.remove('video-playing');
        overlay.classList.add('dismissed');
        skipBtn.classList.add('hidden');
        // Remove overlay from DOM after transition
        setTimeout(function () { overlay.remove(); }, 700);
        // Reveal the rest of the page
        content.classList.remove('post-video-hidden');
        content.classList.add('post-video-visible');
        // Scroll to top of page (hero section)
        setTimeout(function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }, 100);
    }

    fsVideo.addEventListener('ended', dismiss);
    skipBtn.addEventListener('click', dismiss);
})();
