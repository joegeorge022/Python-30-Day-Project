document.addEventListener('DOMContentLoaded', () => {
    initializeDayOrder();
    initializeMemberOrder();
    initializeIntersectionObserver();
    initializeBackToTop();
});

function initializeDayOrder() {
    const days = document.querySelectorAll('.day');
    days.forEach((day, index) => {
        day.style.setProperty('--order', index + 1);
    });
}

function initializeMemberOrder() {
    const members = document.querySelectorAll('.members span');
    members.forEach((member, index) => {
        member.style.setProperty('--order', index + 1);
    });
}

function initializeIntersectionObserver() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.day, .members span').forEach(el => {
        observer.observe(el);
    });
}

function initializeBackToTop() {
    const backToTop = document.querySelector('.back-to-top');
    
    const toggleBackToTop = () => {
        if (window.scrollY > window.innerHeight / 2) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    };

    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };

    window.addEventListener('scroll', toggleBackToTop);
    backToTop.addEventListener('click', scrollToTop);
}
