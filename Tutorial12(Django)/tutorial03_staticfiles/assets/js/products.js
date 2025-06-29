document.addEventListener('DOMContentLoaded', function() {
    // Initialize products
    loadProducts();

    // Filter and sort functionality
    document.getElementById('category-filter').addEventListener('change', filterProducts);
    document.getElementById('sort-by').addEventListener('change', filterProducts);

    // Pagination
    document.getElementById('prev-page').addEventListener('click', goToPrevPage);
    document.getElementById('next-page').addEventListener('click', goToNextPage);

    // Update cart count
    updateCartCount();
});

let currentPage = 1;
const productsPerPage = 8;
let allProducts = [];
let filteredProducts = [];

function loadProducts() {
    // In a real app, this would come from an API
    const allProducts = [
  {
    id: 1,
    name: 'Bamboo Toothbrush Set',
    price: 12.99,
    oldPrice: 15.99,
    image: 'https://images.unsplash.com/photo-1606813905981-01e7b1a94b78?w=600&auto=format&fit=crop&q=60',
    rating: 4.5,
    category: 'beauty',
    isNew: true,
    isSale: false,
  },
  {
    id: 2,
    name: 'Organic Cotton Tote Bag',
    price: 15.99,
    image: 'https://images.unsplash.com/photo-1600814886202-9740347f4095?w=600&auto=format&fit=crop&q=60',
    rating: 5,
    category: 'fashion',
    isNew: false,
    isSale: false,
  },
  {
    id: 3,
    name: 'Reusable Stainless Steel Straws',
    price: 9.99,
    oldPrice: 12.99,
    image: 'https://images.unsplash.com/photo-1628855171941-bb7728e26e46?w=600&auto=format&fit=crop&q=60',
    rating: 4,
    category: 'kitchen',
    isNew: false,
    isSale: true,
  },
  {
    id: 4,
    name: 'Natural Loofah Sponge',
    price: 7.99,
    image: 'https://images.unsplash.com/photo-1599747860985-40a937ddfe2f?w=600&auto=format&fit=crop&q=60',
    rating: 4.5,
    category: 'beauty',
    isNew: false,
    isSale: false,
  },
  {
    id: 5,
    name: 'Bamboo Cutting Board',
    price: 24.99,
    image: 'https://images.unsplash.com/photo-1606770340045-54a27e84c1d7?w=600&auto=format&fit=crop&q=60',
    rating: 4,
    category: 'kitchen',
    isNew: true,
    isSale: false,
  },
  {
    id: 6,
    name: 'Hemp Face Towels',
    price: 18.99,
    oldPrice: 22.99,
    image: 'https://images.unsplash.com/photo-1601379334600-7b2027a90e10?w=600&auto=format&fit=crop&q=60',
    rating: 4.5,
    category: 'beauty',
    isNew: false,
    isSale: true,
  },
  {
    id: 7,
    name: 'Cork Yoga Mat',
    price: 49.99,
    image: 'https://images.unsplash.com/photo-1570059033352-5e1f2557da1e?w=600&auto=format&fit=crop&q=60',
    rating: 5,
    category: 'home',
    isNew: false,
    isSale: false,
  },
  {
    id: 8,
    name: 'Organic Linen Sheets',
    price: 89.99,
    image: 'https://images.unsplash.com/photo-1615177264827-9c4e7d8672e6?w=600&auto=format&fit=crop&q=60',
    rating: 4,
    category: 'home',
    isNew: true,
    isSale: false,
  },
  {
    id: 9,
    name: 'Beeswax Food Wraps',
    price: 14.99,
    oldPrice: 19.99,
    image: 'https://images.unsplash.com/photo-1571468183921-2120992aa79a?w=600&auto=format&fit=crop&q=60',
    rating: 4.5,
    category: 'kitchen',
    isNew: false,
    isSale: true,
  },
  {
    id: 10,
    name: 'Reusable Coffee Cup',
    price: 16.99,
    image: 'https://images.unsplash.com/photo-1598390748671-8e34c2c5cc69?w=600&auto=format&fit=crop&q=60',
    rating: 4,
    category: 'kitchen',
    isNew: false,
    isSale: false,
  },
  {
    id: 11,
    name: 'Organic Cotton Socks',
    price: 12.99,
    image: 'https://images.unsplash.com/photo-1591318199801-705b74f26684?w=600&auto=format&fit=crop&q=60',
    rating: 4,
    category: 'fashion',
    isNew: false,
    isSale: false,
  },
  {
    id: 12,
    name: 'Bamboo Hairbrush',
    price: 19.99,
    oldPrice: 24.99,
    image: 'https://images.unsplash.com/photo-1599762565737-c1f83c9c1e78?w=600&auto=format&fit=crop&q=60',
    rating: 5,
    category: 'beauty',
    isNew: false,
    isSale: true,
  }
];


    filteredProducts = [...allProducts];
    displayProducts();
}

function filterProducts() {
    const categoryFilter = document.getElementById('category-filter').value;
    const sortBy = document.getElementById('sort-by').value;

    // Filter by category
    if (categoryFilter === 'all') {
        filteredProducts = [...allProducts];
    } else {
        filteredProducts = allProducts.filter(product => product.category === categoryFilter);
    }

    // Sort products
    switch(sortBy) {
        case 'price-low':
            filteredProducts.sort((a, b) => a.price - b.price);
            break;
        case 'price-high':
            filteredProducts.sort((a, b) => b.price - a.price);
            break;
        case 'rating':
            filteredProducts.sort((a, b) => b.rating - a.rating);
            break;
        case 'newest':
            // In a real app, this would use actual dates
            filteredProducts.sort((a, b) => b.isNew - a.isNew);
            break;
        default:
            // Default is featured (original order)
            filteredProducts = [...filteredProducts];
    }

    currentPage = 1;
    displayProducts();
}

function displayProducts() {
    const productsGrid = document.querySelector('.products-grid');
    const pagination = document.querySelector('.pagination');

    // Calculate pagination
    const totalPages = Math.ceil(filteredProducts.length / productsPerPage);
    const startIndex = (currentPage - 1) * productsPerPage;
    const endIndex = startIndex + productsPerPage;
    const productsToDisplay = filteredProducts.slice(startIndex, endIndex);

    // Display products
    productsGrid.innerHTML = productsToDisplay.map(product => `
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
            const product = allProducts.find(p => p.id == productId);
            addToCart(product);
        });
    });

    // Update pagination
    updatePagination(totalPages);
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

function updatePagination(totalPages) {
    const pageNumbers = document.getElementById('page-numbers');
    pageNumbers.innerHTML = '';

    for (let i = 1; i <= totalPages; i++) {
        const button = document.createElement('button');
        button.textContent = i;
        if (i === currentPage) {
            button.classList.add('active');
        }
        button.addEventListener('click', () => {
            currentPage = i;
            displayProducts();
        });
        pageNumbers.appendChild(button);
    }

    // Enable/disable prev/next buttons
    document.getElementById('prev-page').disabled = currentPage === 1;
    document.getElementById('next-page').disabled = currentPage === totalPages || totalPages === 0;
}

function goToPrevPage() {
    if (currentPage > 1) {
        currentPage--;
        displayProducts();
    }
}

function goToNextPage() {
    const totalPages = Math.ceil(filteredProducts.length / productsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        displayProducts();
    }
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