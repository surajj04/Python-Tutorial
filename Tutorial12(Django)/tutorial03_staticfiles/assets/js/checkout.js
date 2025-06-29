document.addEventListener('DOMContentLoaded', function() {
    // Load order summary
    loadOrderSummary();

    // Update cart count
    updateCartCount();

    // Initialize checkout steps
    initCheckoutSteps();

    // Payment tabs
    initPaymentTabs();

    // Apply coupon button
    document.querySelector('.apply-coupon').addEventListener('click', applyCoupon);
});

function loadOrderSummary() {
    const summaryItems = document.querySelector('.summary-items');
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    if (cart.length === 0) {
        window.location.href = 'products.html';
        return;
    }

    // Calculate totals
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const tax = subtotal * 0.08; // 8% tax
    const total = subtotal + tax;

    // Update summary items
    summaryItems.innerHTML = cart.map(item => `
        <div class="summary-item">
            <div class="summary-item-img">
                <img src="${item.image}" alt="${item.name}">
            </div>
            <div class="summary-item-details">
                <div class="summary-item-name">${item.name}</div>
                <div class="summary-item-price">$${item.price.toFixed(2)}</div>
                <div class="summary-item-qty">Qty: ${item.quantity}</div>
            </div>
        </div>
    `).join('');

    // Update totals
    document.querySelector('.subtotal').textContent = `$${subtotal.toFixed(2)}`;
    document.querySelector('.tax').textContent = `$${tax.toFixed(2)}`;
    document.querySelector('.order-total').textContent = `$${total.toFixed(2)}`;
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const totalItems = cart.reduce((total, item) => total + item.quantity, 0);
    document.querySelector('.cart-count').textContent = totalItems;
}

function initCheckoutSteps() {
    const steps = document.querySelectorAll('.checkout-step');
    const nextBtn = document.querySelector('.next-btn');
    let currentStep = 0;

    // Show first step
    steps[currentStep].classList.add('active');
    updateNextButton(currentStep);

    // Next button click handler
    nextBtn.addEventListener('click', function() {
        // Validate current step
        if (!validateStep(currentStep)) {
            return;
        }

        // Hide current step
        steps[currentStep].classList.remove('active');

        // Move to next step
        currentStep++;

        // If last step, change button text
        if (currentStep === steps.length - 1) {
            nextBtn.textContent = 'Complete Order';
            nextBtn.addEventListener('click', completeOrder);
        }

        // If completed all steps
        if (currentStep >= steps.length) {
            currentStep = steps.length - 1;
            return;
        }

        // Show next step
        steps[currentStep].classList.add('active');
        updateNextButton(currentStep);
    });

    function validateStep(stepIndex) {
        const step = steps[stepIndex];
        const inputs = step.querySelectorAll('input[required], select[required]');
        let isValid = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.style.borderColor = '#f44336';
                isValid = false;

                // Remove error style after 2 seconds
                setTimeout(() => {
                    input.style.borderColor = '';
                }, 2000);
            }
        });

        if (!isValid) {
            showNotification('Please fill in all required fields');
        }

        return isValid;
    }

    function updateNextButton(stepIndex) {
        switch(stepIndex) {
            case 0:
                nextBtn.textContent = 'Continue to Shipping';
                break;
            case 1:
                nextBtn.textContent = 'Continue to Payment';
                break;
            case 2:
                nextBtn.textContent = 'Continue to Review';
                break;
        }
    }

    function completeOrder() {
        // In a real app, this would process the payment
        showNotification('Order placed successfully!');

        // Clear cart
        localStorage.removeItem('cart');

        // Redirect to thank you page
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 2000);
    }
}

function initPaymentTabs() {
    const tabs = document.querySelectorAll('.payment-tab');
    const panels = document.querySelectorAll('.payment-panel');

    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Remove active class from all tabs and panels
            tabs.forEach(t => t.classList.remove('active'));
            panels.forEach(p => p.classList.remove('active'));

            // Add active class to clicked tab
            this.classList.add('active');

            // Show corresponding panel
            const tabId = this.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });
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