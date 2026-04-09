// 完整的管理系统JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Complete Admin System loaded');
    
    // 数据存储键 - 使用共享键名，让网站可以访问
    const STORAGE_KEYS = {
        PRODUCTS: 'stratronix_products',           // 共享键名，网站可以访问
        CONTENT: 'stratronix_content',             // 共享键名
        USER: 'stratronix_admin_user'              // 仅后台使用
    };
    
    // 当前状态
    let currentUser = null;
    let currentPage = 'dashboard';
    let editingProductId = null;
    
    // 初始化
    function init() {
        loadUser();
        setupEventListeners();
        
        if (currentUser) {
            showAdminPage();
        } else {
            showLoginPage();
        }
    }
    
    // 加载用户
    function loadUser() {
        try {
            const userData = localStorage.getItem(STORAGE_KEYS.USER);
            currentUser = userData ? JSON.parse(userData) : null;
        } catch (error) {
            console.error('Error loading user:', error);
            currentUser = null;
        }
    }
    
    // 保存用户
    function saveUser(user) {
        try {
            localStorage.setItem(STORAGE_KEYS.USER, JSON.stringify(user));
            currentUser = user;
            return true;
        } catch (error) {
            console.error('Error saving user:', error);
            return false;
        }
    }
    
    // 显示消息
    function showMessage(text, type = 'info', elementId = 'adminMessage') {
        const el = document.getElementById(elementId);
        if (!el) return;
        
        el.textContent = text;
        el.className = `message ${type}`;
        el.style.display = 'block';
        
        setTimeout(() => {
            el.style.display = 'none';
        }, 3000);
    }
    
    // 显示登录页面
    function showLoginPage() {
        document.getElementById('loginPage').style.display = 'flex';
        document.getElementById('adminPage').style.display = 'none';
    }
    
    // 显示管理页面
    function showAdminPage() {
        document.getElementById('loginPage').style.display = 'none';
        document.getElementById('adminPage').style.display = 'block';
        showPage(currentPage);
    }
    
    // 显示页面
    function showPage(page) {
        currentPage = page;
        
        // 隐藏所有页面
        document.querySelectorAll('.page').forEach(p => {
            p.classList.remove('active');
        });
        
        // 更新导航激活状态
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
        });
        
        // 激活当前页面导航
        const activeNav = document.querySelector(`.nav-item[data-page="${page}"]`);
        if (activeNav) {
            activeNav.classList.add('active');
        }
        
        // 显示当前页面
        const pageElement = document.getElementById(`${page}Page`);
        if (pageElement) {
            pageElement.classList.add('active');
            document.getElementById('pageTitle').textContent = getPageTitle(page);
            
            // 加载页面数据
            loadPageData(page);
        }
    }
    
    // 获取页面标题
    function getPageTitle(page) {
        const titles = {
            dashboard: 'Dashboard',
            products: 'Product Management',
            members: 'Team Members',
            content: 'Content Management',
            settings: 'Settings'
        };
        return titles[page] || 'Admin';
    }
    
    // 加载页面数据
    function loadPageData(page) {
        switch(page) {
            case 'dashboard':
                updateStats();
                break;
            case 'products':
                loadProducts();
                break;
            case 'content':
                loadContent();
                break;
        }
    }
    
    // 更新统计
    function updateStats() {
        const products = loadProductsData();
        
        document.getElementById('productsCount').textContent = products.length;
        
        // 计算总收入
        const totalRevenue = products.reduce((sum, product) => {
            return sum + (product.price * product.sold || 0);
        }, 0);
        
        document.getElementById('revenueCount').textContent = `$${totalRevenue.toLocaleString()}`;
    }
    
    // 产品管理功能
    function loadProductsData() {
        try {
            const data = localStorage.getItem(STORAGE_KEYS.PRODUCTS);
            return data ? JSON.parse(data) : [];
        } catch (error) {
            console.error('Error loading products:', error);
            return [];
        }
    }
    
    function saveProductsData(products) {
        try {
            localStorage.setItem(STORAGE_KEYS.PRODUCTS, JSON.stringify(products));
            return true;
        } catch (error) {
            console.error('Error saving products:', error);
            return false;
        }
    }
    
    function loadProducts() {
        const products = loadProductsData();
        const tbody = document.getElementById('productsTableBody');
        
        if (!tbody) return;
        
        if (products.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; padding: 30px; color: #666;">No products yet. Click "Add New Product" to add your first product.</td></tr>';
            return;
        }
        
        let html = '';
        products.forEach(product => {
            const status = product.stock > 0 ? 'In Stock' : 'Out of Stock';
            const statusColor = product.stock > 0 ? '#34a853' : '#ea4335';
            
            html += `
                <tr data-id="${product.id}">
                    <td><strong>${product.name}</strong></td>
                    <td>${product.category}</td>
                    <td>$${product.price.toFixed(2)}</td>
                    <td><span style="color: ${statusColor}">${product.stock} (${status})</span></td>
                    <td class="actions">
                        <button class="btn btn-warning btn-small edit-product-btn" data-id="${product.id}">Edit</button>
                        <button class="btn btn-danger btn-small delete-product-btn" data-id="${product.id}">Delete</button>
                    </td>
                </tr>
            `;
        });
        
        tbody.innerHTML = html;
        
        // 重新绑定事件
        document.querySelectorAll('.edit-product-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const productId = this.getAttribute('data-id');
                editProduct(productId);
            });
        });
        
        document.querySelectorAll('.delete-product-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const productId = this.getAttribute('data-id');
                deleteProduct(productId);
            });
        });
    }
    
    function editProduct(productId) {
        const products = loadProductsData();
        const product = products.find(p => p.id === productId);
        
        if (!product) {
            showMessage('Product not found', 'error');
            return;
        }
        
        editingProductId = productId;
        
        // 填充表单
        document.getElementById('productId').value = product.id;
        document.getElementById('productName').value = product.name;
        document.getElementById('productCategory').value = product.category;
        document.getElementById('productPrice').value = product.price;
        document.getElementById('productStock').value = product.stock;
        document.getElementById('productDescription').value = product.description || '';
        
        document.getElementById('formTitle').textContent = 'Edit Product';
        document.getElementById('productForm').classList.add('active');
        document.getElementById('addProductBtn').style.display = 'none';
    }
    
    function deleteProduct(productId) {
        if (!confirm('Are you sure you want to delete this product?')) {
            return;
        }
        
        const products = loadProductsData();
        const filteredProducts = products.filter(p => p.id !== productId);
        
        if (saveProductsData(filteredProducts)) {
            loadProducts();
            updateStats();
            showMessage('Product deleted successfully', 'success');
        }
    }
    
    function saveProduct(e) {
        e.preventDefault();
        
        const product = {
            id: editingProductId || Date.now().toString(),
            name: document.getElementById('productName').value.trim(),
            category: document.getElementById('productCategory').value,
            price: parseFloat(document.getElementById('productPrice').value) || 0,
            stock: parseInt(document.getElementById('productStock').value) || 0,
            description: document.getElementById('productDescription').value.trim(),
            createdAt: editingProductId ? undefined : new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        
        // 验证
        if (!product.name || !product.category || product.price <= 0) {
            showMessage('Please fill in all required fields correctly', 'error');
            return;
        }
        
        const products = loadProductsData();
        
        if (editingProductId) {
            // 更新
            const index = products.findIndex(p => p.id === editingProductId);
            if (index !== -1) {
                products[index] = { ...products[index], ...product };
                showMessage('Product updated successfully', 'success');
            }
        } else {
            // 添加
            products.push(product);
            showMessage('Product added successfully', 'success');
        }
        
        if (saveProductsData(products)) {
            loadProducts();
            updateStats();
            cancelProductForm();
        }
    }
    
    function cancelProductForm() {
        document.getElementById('productForm').classList.remove('active');
        document.getElementById('addProductBtn').style.display = 'block';
        document.getElementById('productFormElement').reset();
        document.getElementById('productId').value = '';
        document.getElementById('formTitle').textContent = 'Add New Product';
        editingProductId = null;
    }
    
    // 内容管理功能
    function loadContent() {
        const content = loadContentData();
        
        // 填充内容编辑器
        document.getElementById('homepageTitle').value = content.homepage?.title || '';
        document.getElementById('homepageContent').value = content.homepage?.content || '';
    }
    
    function loadContentData() {
        try {
            const data = localStorage.getItem(STORAGE_KEYS.CONTENT);
            return data ? JSON.parse(data) : {
                homepage: { title: 'Welcome to Stratronix', content: 'Default homepage content' }
            };
        } catch (error) {
            console.error('Error loading content:', error);
            return {};
        }
    }
    
    function saveContentData(content) {
        try {
            localStorage.setItem(STORAGE_KEYS.CONTENT, JSON.stringify(content));
            return true;
        } catch (error) {
            console.error('Error saving content:', error);
            return false;
        }
    }
    
    function saveContent() {
        const content = {
            homepage: {
                title: document.getElementById('homepageTitle').value,
                content: document.getElementById('homepageContent').value
            }
        };
        
        if (saveContentData(content)) {
            showMessage('Content saved successfully', 'success');
        }
    }
    
    // 设置事件监听器
    function setupEventListeners() {
        // 登录表单
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            // 简单验证
            if (username === 'admin' && password === 'stratronix2024') {
                const user = {
                    username: 'admin',
                    name: 'Administrator',
                    role: 'superadmin',
                    loggedInAt: new Date().toISOString()
                };
                
                if (saveUser(user)) {
                    showAdminPage();
                    showMessage('Login successful', 'success', 'adminMessage');
                }
            } else {
                showMessage('Invalid username or password', 'error', 'loginMessage');
            }
        });
        
        // 导航菜单
        document.querySelectorAll('.nav-item[data-page]').forEach(item => {
            item.addEventListener('click', function() {
                const page = this.getAttribute('data-page');
                showPage(page);
            });
        });
        
        // 退出登录
        document.getElementById('logoutBtn').addEventListener('click', function() {
            if (confirm('Are you sure you want to logout?')) {
                localStorage.removeItem(STORAGE_KEYS.USER);
                currentUser = null;
                showLoginPage();
            }
        });
        
        // 快速操作按钮
        document.querySelectorAll('button[data-page]').forEach(btn => {
            btn.addEventListener('click', function() {
                const page = this.getAttribute('data-page');
                showPage(page);
            });
        });
        
        // 产品管理
        const addProductBtn = document.getElementById('addProductBtn');
        if (addProductBtn) {
            addProductBtn.addEventListener('click', function() {
                document.getElementById('productForm').classList.add('active');
                this.style.display = 'none';
                document.getElementById('productName').focus();
            });
        }
        
        const productFormElement = document.getElementById('productFormElement');
        if (productFormElement) {
            productFormElement.addEventListener('submit', saveProduct);
        }
        
        const cancelProductBtn = document.getElementById('cancelProductBtn');
        if (cancelProductBtn) {
            cancelProductBtn.addEventListener('click', cancelProductForm);
        }
        
        // 内容保存
        const saveContentBtn = document.getElementById('saveContentBtn');
        if (saveContentBtn) {
            saveContentBtn.addEventListener('click', saveContent);
        }
    }
    
    // 初始化系统
    init();
    
    console.log('Complete Admin System initialized');
});