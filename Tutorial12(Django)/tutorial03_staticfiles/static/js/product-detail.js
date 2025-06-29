document.addEventListener('DOMContentLoaded', function() {
    // Thumbnail image switcher
    const thumbnails = document.querySelectorAll('.thumbnail');
    const mainImage = document.getElementById('main-image');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            // Remove active class from all thumbnails
            thumbnails.forEach(t => t.classList.remove('active'));

            // Add active class to clicked thumbnail
            this.classList.add('active');

            // Change main image
            const newImageSrc = this.getAttribute('data-image');
            mainImage.src = newImageSrc;
        });
    });

    // Product tabs
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanels = document.querySelectorAll('.tab-panel');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons and panels
            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanels.forEach(p => p.classList.remove('active'));

            // Add active class to clicked button
            this.classList.add('active');

            // Show corresponding panel
            const tabId = this.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });

    // Quantity selector
    const minusBtn = document.querySelector('.quantity-btn.minus');
    const plusBtn = document.querySelector('.quantity-btn.plus');
    const quantityInput = document.getElementById('quantity');

    minusBtn.addEventListener('click', function() {
        let value = parseInt(quantityInput.value);
        if (value > 1) {
            quantityInput.value = value - 1;
        }
    });

    plusBtn.addEventListener('click', function() {
        let value = parseInt(quantityInput.value);
        quantityInput.value = value + 1;
    });

    // Add to cart
    const addToCartBtn = document.querySelector('.add-to-cart');
    addToCartBtn.addEventListener('click', function() {
        // In a real app, this would get the actual product data
        const product = {
            id: 1,
            name: 'Bamboo Toothbrush Set',
            price: 12.99,
            image: 'images/product1.jpg'
        };

        const quantity = parseInt(quantityInput.value);
        addToCart(product, quantity);
    });

    // Load related products
    loadRelatedProducts();

    // Update cart count
    updateCartCount();
});

function addToCart(product, quantity = 1) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Check if product already in cart
    const existingItem = cart.find(item => item.id === product.id);

    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        cart.push({
            ...product,
            quantity: quantity
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

function loadRelatedProducts() {
    const relatedProductsGrid = document.querySelector('.related-products-grid');

    // In a real app, this would come from an API
    const relatedProducts = [
        {
            id: 5,
            name: 'Bamboo Hairbrush',
            price: 19.99,
            oldPrice: 24.99,
            image: 'images/product12.jpg',
            rating: 5,
            isSale: true
        },
        {
            id: 6,
            name: 'Hemp Face Towels',
            price: 18.99,
            oldPrice: 22.99,
            image: 'images/product6.jpg',
            rating: 4.5,
            isSale: true
        },
        {
            id: 7,
            name: 'Bamboo Cotton Swabs',
            price: 8.99,
            image: 'images/product13.jpg',
            rating: 4,
            isNew: true
        },
        {
            id: 8,
            name: 'Natural Deodorant',
            price: 14.99,
            image: 'images/product14.jpg',
            rating: 4.5
        }
    ];

    relatedProductsGrid.innerHTML = relatedProducts.map(product => `
        <div class="product-card" data-id="${product.id}">
            ${product.isNew ? '<span class="product-badge new">New</span>' : ''}
            ${product.isSale ? '<span class="product-badge sale">Sale</span>' : ''}
            <div class="product-img">
                <img src="${product.image}" alt="${product.name}">
                <div class="product-actions">
                    <button class="quick-view" title="Quick View"><i class="fas fa-eye"></i></button>
                    <button class="add-to-wishlist" title="Add to Wishlist"><i class="far fa-heart"></i></button>
                </div>
            </div>
            <div class="product-info">
                <h3>${product.name}</h3>
                <div class="price">
                    <span class="current-price">$${product.price.toFixed(2)}</span>
                    ${product.oldPrice ? `<span class="old-price">$${product.oldPrice.toFixed(2)}</span>` : ''}
                </div>
                <div class="rating">
                    ${getStarRating(product.rating)}
                    <span>(${product.rating})</span>
                </div>
                <button class="btn add-to-cart">Add to Cart</button>
            </div>
        </div>
    `).join('');

    // Add event listeners to add to cart buttons
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.closest('.product-card').getAttribute('data-id');
            const product = relatedProducts.find(p => p.id == productId);
            addToCart(product);
        });
    });
}

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