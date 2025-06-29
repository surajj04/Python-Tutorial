document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const menuBtn = document.getElementById('menu-btn');
    const nav = document.querySelector('.nav');
    
    menuBtn.addEventListener('click', function() {
        nav.classList.toggle('active');
        menuBtn.classList.toggle('fa-times');
    });

    // Search Toggle
    const searchBtn = document.getElementById('search-btn');
    const searchForm = document.querySelector('.search-form');
    
    searchBtn.addEventListener('click', function(e) {
        e.preventDefault();
        searchForm.classList.toggle('active');
    });

    // Close search when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.search-form') && !e.target.closest('#search-btn')) {
            searchForm.classList.remove('active');
        }
    });


    // Animate impact numbers
    animateImpactNumbers();

    // Update cart count
    updateCartCount();
});


function getStarRating(rating) {
    const fullStars = Math.floor(rating);
    const halfStar = rating % 1 >= 0.5 ? 1 : 0;
    const emptyStars = 5 - fullStars - halfStar;
    
    return `
        ${'<i class="fas fa-star"></i>'.repeat(fullStars)}
        ${halfStar ? '<i class="fas fa-star-half-alt"></i>' : ''}
        ${'<i class="far fa-star"></i>'.repeat(emptyStars)}
    `;
}

// Cart Functions
function addToCart(product) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    
    // Check if product already in cart
    const existingItem = cart.find(item => item.id === product.id);
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            ...product,
            quantity: 1
        });
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    
    // Show notification
    showNotification(`${product.name} added to cart!`);
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const totalItems = cart.reduce((total, item) => total + item.quantity, 0);
    document.querySelector('.cart-count').textContent = totalItems;
}

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Animate impact numbers
function animateImpactNumbers() {
    const counters = document.querySelectorAll('.count');
    const speed = 200;
    
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const increment = target / speed;
        
        if (count < target) {
            counter.innerText = Math.ceil(count + increment);
            setTimeout(animateImpactNumbers, 1);
        } else {
            counter.innerText = target.toLocaleString();
        }
    });
}

// Add notification styles dynamically
const notificationStyles = document.createElement('style');
notificationStyles.textContent = `
    .notification {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: var(--primary-color);
        color: white;
        padding: 15px 25px;
        border-radius: 5px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        transform: translateY(100px);
        opacity: 0;
        transition: all 0.3s ease;
        z-index: 1000;
    }
    
    .notification.show {
        transform: translateY(0);
        opacity: 1;
    }
`;
document.head.appendChild(notificationStyles);