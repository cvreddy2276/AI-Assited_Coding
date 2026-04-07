const products = [
  {id:1,name:'Precision Wireless Mouse',price:29.99,desc:'Ergonomic, 1600 DPI, long battery life.',image:'https://source.unsplash.com/collection/technology/400x300?sig=11'},
  {id:2,name:'Noise-Cancelling Headphones',price:89.99,desc:'Immersive sound with comfortable over-ear fit.',image:'https://source.unsplash.com/collection/technology/400x300?sig=12'},
  {id:3,name:'Smart LED Lamp',price:39.99,desc:'App-controlled with adjustable color temperature.',image:'https://source.unsplash.com/collection/technology/400x300?sig=13'},
  {id:4,name:'Portable Charger 10000mAh',price:22.50,desc:'Lightweight and fast USB-C charging.',image:'https://source.unsplash.com/collection/technology/400x300?sig=14'},
  {id:5,name:'Wireless Keyboard',price:48.75,desc:'Compact design with responsive keys.',image:'https://source.unsplash.com/collection/technology/400x300?sig=15'},
  {id:6,name:'Bluetooth Speaker',price:54.00,desc:'360° sound and pairable stereo mode.',image:'https://source.unsplash.com/collection/technology/400x300?sig=16'}
];

const productGrid = document.getElementById('productGrid');
const cartCount = document.getElementById('cartCount');
const toast = document.getElementById('toast');

let cart = {count:0,items:{}};

function renderProducts(){
  productGrid.innerHTML = products.map(product => `
    <article class="product-card" data-id="${product.id}">
      <img class="product-image" src="${product.image}" alt="${product.name}" />
      <h3 class="product-title">${product.name}</h3>
      <p class="product-desc">${product.desc}</p>
      <div class="product-foot">
        <span class="price">$${product.price.toFixed(2)}</span>
        <button class="add-btn" data-id="${product.id}">Add to Cart</button>
      </div>
    </article>
  `).join('');
}

function updateCartUI(){
  cartCount.textContent = cart.count;
}

function showToast(message){
  toast.textContent = message;
  toast.classList.add('show');
  clearTimeout(toast.hideTimeout);
  toast.hideTimeout = setTimeout(() => toast.classList.remove('show'), 1800);
}

productGrid.addEventListener('click', e => {
  const addButton = e.target.closest('.add-btn');
  if(!addButton) return;

  const id = parseInt(addButton.dataset.id, 10);
  const product = products.find(p => p.id === id);
  if(!product) return;

  cart.count += 1;
  cart.items[id] = (cart.items[id] || 0) + 1;

  updateCartUI();
  addButton.textContent = 'Added';
  addButton.disabled = true;
  addButton.style.background = '#059669';

  setTimeout(() => {
    addButton.textContent = 'Add to Cart';
    addButton.disabled = false;
    addButton.style.background = '';
  }, 900);

  showToast(`${product.name} added to cart!`);
});

renderProducts();
updateCartUI();