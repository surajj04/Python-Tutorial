document.addEventListener('DOMContentLoaded', function() {
    // Load cart items
    loadCartItems();

    // Update cart count
    updateCartCount();

    // Load cross-sell products
    loadCrossSellProducts();

    // Event listeners
    document.querySelector('.update-cart').addEventListener('click', updateCart);
    document.querySelector('.apply-coupon').addEventListener('click', applyCoupon);
});

function loadCartItems() {
    const cartBody = document.querySelector('.cart-body');
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    if (cart.length === 0) {
        cartBody.innerHTML = `
            <div class="empty-cart">
                <i class="fas fa-shopping-cart"></i>
                <p>Your cart is empty</p>
                <a href="products.html" class="btn">Continue Shopping</a>
            </div>
        `;
        document.querySelector('.checkout-btn').style.display = 'none';
        updateCartSummary([]);
        return;
    }

    cartBody.innerHTML = cart.map(item => `
        <div class="cart-item" data-id="${item.id}">
            <div class="product-info">
                <div class="product-image">
                    <img src="${item.image}" alt="${item.name}">
                </div>
                <div class="product-details">
                    <h3>${item.name}</h3>
                    <div class="variant">One Size</div>
                </div>
            </div>
            <div class="price">$${item.price.toFixed(2)}</div>
            <div class="quantity-control">
                <button class="quantity-btn minus"><i class="fas fa-minus"></i></button>
                <input type="number" class="quantity-input" value="${item.quantity}" min="1">
                <button class="quantity-btn plus"><i class="fas fa-plus"></i></button>
            </div>
            <div class="item-total">$${(item.price * item.quantity).toFixed(2)}</div>
            <div class="remove-item"><i class="fas fa-times"></i></div>
        </div>
    `).join('');

    // Add event listeners to quantity buttons
    document.querySelectorAll('.quantity-btn.minus').forEach(button => {
        button.addEventListener('click', function() {
            const input = this.nextElementSibling;
            if (parseInt(input.value) > 1) {
                input.value = parseInt(input.value) - 1;
                updateItemTotal(this.closest('.cart-item'));
            }
        });
    });

    document.querySelectorAll('.quantity-btn.plus').forEach(button => {
        button.addEventListener('click', function() {
            const input = this.previousElementSibling;
            input.value = parseInt(input.value) + 1;
            updateItemTotal(this.closest('.cart-item'));
        });
    });

    document.querySelectorAll('.quantity-input').forEach(input => {
        input.addEventListener('change', function() {
            if (parseInt(this.value) < 1) {
                this.value = 1;
            }
            updateItemTotal(this.closest('.cart-item'));
        });
    });

    // Add event listeners to remove buttons
    document.querySelectorAll('.remove-item').forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.closest('.cart-item').getAttribute('data-id');
            removeFromCart(itemId);
        });
    });

    // Update cart summary
    updateCartSummary(cart);
}

function updateItemTotal(itemElement) {
    const price = parseFloat(itemElement.querySelector('.price').textContent.replace('$', ''));
    const quantity = parseInt(itemElement.querySelector('.quantity-input').value);
    const total = (price * quantity).toFixed(2);
    itemElement.querySelector('.item-total').textContent = `$${total}`;
}

function updateCart() {
    const cartItems = document.querySelectorAll('.cart-item');
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    cartItems.forEach(itemElement => {
        const itemId = itemElement.getAttribute('data-id');
        const quantity = parseInt(itemElement.querySelector('.quantity-input').value);

        const cartItem = cart.find(item => item.id == itemId);
        if (cartItem) {
            cartItem.quantity = quantity;
        }
    });

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    updateCartSummary(cart);
    showNotification('Cart updated successfully!');
}

function removeFromCart(itemId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(item => item.id != itemId);
    localStorage.setItem('cart', JSON.stringify(cart));

    loadCartItems();
    updateCartCount();
    showNotification('Item removed from cart');
}

function updateCartSummary(cart) {
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const tax = subtotal * 0.08; // 8% tax
    const total = subtotal + tax;

    document.querySelector('.subtotal').textContent = `$${subtotal.toFixed(2)}`;
    document.querySelector('.tax').textContent = `$${tax.toFixed(2)}`;
    document.querySelector('.cart-total').textContent = `$${total.toFixed(2)}`;
}

function applyCoupon() {
    const couponCode = document.querySelector('.coupon input').value.trim();

    if (couponCode === 'ECOTREND10') {
        showNotification('Coupon applied: 10% discount');
    } else if (couponCode) {
        showNotification('Invalid coupon code');
    } else {
        showNotification('Please enter a coupon code');
    }
}

function loadCrossSellProducts() {
    const crossSellGrid = document.querySelector('.cross-sell-grid');

    // In a real app, this would come from an API
    const crossSellProducts = [
        {
            id: 9,
            name: 'Beeswax Food Wraps',
            price: 14.99,
            oldPrice: 19.99,
            image: 'images/product9.jpg',
            rating: 4.5,
            isSale: true
        },
        {
            id: 10,
            name: 'Reusable Coffee Cup',
            price: 16.99,
            image: 'images/product10.jpg',
            rating: 4,
            isNew: true
        },
        {
            id: 11,
            name: 'Organic Cotton Socks',
            price: 12.99,
            image: 'images/product11.jpg',
            rating: 4
        },
        {
            id: 12,
            name: 'Bamboo Hairbrush',
            price: 19.99,
            oldPrice: 24.99,
            image: 'images/product12.jpg',
            rating: 5,
            isSale: true
        }
    ];

    crossSellGrid.innerHTML = crossSellProducts.map(product => `
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
            const product = crossSellProducts.find(p => p.id == productId);
            addToCart(product);
        });
    });
}

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
    loadCartItems();
    updateCartCount();
    showNotification(`${product.name} added to cart!`);
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