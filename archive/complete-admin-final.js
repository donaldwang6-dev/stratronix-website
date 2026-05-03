// 完整的一体化后台管理系统 - Final Solution
document.addEventListener('DOMContentLoaded', function() {
    console.log('Complete Admin Final Solution loaded');
    
    // 数据存储键 - 统一命名，网站可以访问
    const STORAGE_KEYS = {
        PRODUCTS: 'stratronix_complete_products',
        TEAM: 'stratronix_complete_team',
        CONTENT: 'stratronix_complete_content',
        SETTINGS: 'stratronix_complete_settings',
        IMAGES: 'stratronix_complete_images'
    };
    
    // 当前状态
    let currentSection = 'products';
    let editingId = null;
    let editingType = null;
    
    // 初始化
    function init() {
        setupEventListeners();
        showSection('products');
        updateStats();
    }
    
    // 设置事件监听器
    function setupEventListeners() {
        // 侧边栏导航
        document.querySelectorAll('.nav-item[data-section]').forEach(item => {
            item.addEventListener('click', function() {
                const section = this.getAttribute('data-section');
                showSection(section);
            });
        });
        
        // 功能操作
        document.querySelectorAll('.nav-item[data-action], .action-item[data-action], button[data-action]').forEach(item => {
            item.addEventListener('click', function() {
                const action = this.getAttribute('data-action');
                handleAction(action);
            });
        });
        
        // 产品表单
        const productForm = document.getElementById('productForm');
        if (productForm) {
            productForm.addEventListener('submit', function(e) {
                e.preventDefault();
                saveProduct();
            });
        }
        
        // 团队成员表单
        const memberForm = document.getElementById('memberForm');
        if (memberForm) {
            memberForm.addEventListener('submit', function(e) {
                e.preventDefault();
                saveTeamMember();
            });
        }
        
        // 内容保存
        document.querySelectorAll('#contentForm input, #contentForm textarea').forEach(input => {
            input.addEventListener('change', saveContent);
        });
        
        // 图片上传
        const imageUpload = document.getElementById('imageUpload');
        if (imageUpload) {
            imageUpload.addEventListener('change', handleImageUpload);
        }
        
        // 数据导出导入
        document.getElementById('exportData')?.addEventListener('click', exportData);
        document.getElementById('importData')?.addEventListener('click', importData);
    }
    
    // 显示区域
    function showSection(section) {
        currentSection = section;
        
        // 更新导航激活状态
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
        });
        
        // 激活当前区域导航
        const activeNav = document.querySelector(`.nav-item[data-section="${section}"]`);
        if (activeNav) {
            activeNav.classList.add('active');
        }
        
        // 隐藏所有区域
        document.querySelectorAll('.form-section').forEach(section => {
            section.classList.remove('active');
        });
        
        // 显示当前区域
        const sectionElement = document.getElementById(`${section}Section`);
        if (sectionElement) {
            sectionElement.classList.add('active');
            updatePageTitle(section);
            
            // 加载区域数据
            loadSectionData(section);
        }
    }
    
    // 更新页面标题
    function updatePageTitle(section) {
        const titles = {
            products: 'Product Management Dashboard',
            team: 'Team Management Dashboard',
            content: 'Content Management Dashboard',
            system: 'System Information Dashboard'
        };
        
        document.getElementById('pageTitle').textContent = titles[section] || 'Admin Dashboard';
    }
    
    // 加载区域数据
    function loadSectionData(section) {
        switch(section) {
            case 'products':
                loadProducts();
                break;
            case 'team':
                loadTeam();
                break;
            case 'content':
                loadContent();
                break;
            case 'system':
                loadSystemInfo();
                break;
        }
    }
    
    // 处理操作
    function handleAction(action) {
        console.log('Action:', action);
        
        switch(action) {
            // 产品管理操作
            case 'add-product':
                showProductForm();
                break;
            case 'edit-products':
                loadProducts();
                break;
            case 'upload-images':
                showImageUpload();
                break;
            case 'manage-specs':
                showSpecifications();
                break;
                
            // 团队管理操作
            case 'add-member':
                showMemberForm();
                break;
            case 'edit-members':
                loadTeam();
                break;
            case 'manage-roles':
                showRolesManagement();
                break;
            case 'view-members':
                loadTeam();
                break;
                
            // 内容管理操作
            case 'edit-homepage':
                showHomepageEditor();
                break;
            case 'update-about':
                showAboutEditor();
                break;
            case 'manage-blog':
                showBlogManagement();
                break;
            case 'edit-contact':
                showContactEditor();
                break;
                
            // 通用操作
            case 'cancel-form':
                hideForm();
                break;
        }
    }
    
    // ==================== 产品管理功能 ====================
    
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
        const container = document.getElementById('productsList');
        
        if (!container) return;
        
        if (products.length === 0) {
            container.innerHTML = '<div style="text-align: center; padding: 40px; color: #666;">No products yet. Click "Add New Product" to add your first product.</div>';
            return;
        }
        
        let html = '<table class="data-table"><thead><tr><th>Name</th><th>Category</th><th>Price</th><th>Stock</th><th>Status</th><th>Actions</th></tr></thead><tbody>';
        
        products.forEach(product => {
            const status = product.stock > 0 ? 'In Stock' : 'Out of Stock';
            const statusColor = product.stock > 0 ? '#34a853' : '#ea4335';
            
            html += `
                <tr data-id="${product.id}" data-type="product">
                    <td><strong>${product.name}</strong></td>
                    <td>${product.category}</td>
                    <td>$${product.price.toFixed(2)}</td>
                    <td>${product.stock}</td>
                    <td><span style="color: ${statusColor}">${status}</span></td>
                    <td class="table-actions">
                        <button class="btn btn-warning btn-small edit-btn" data-id="${product.id}" data-type="product">Edit</button>
                        <button class="btn btn-danger btn-small delete-btn" data-id="${product.id}" data-type="product">Delete</button>
                    </td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        container.innerHTML = html;
        
        // 重新绑定事件
        document.querySelectorAll('.edit-btn[data-type="product"]').forEach(btn => {
            btn.addEventListener('click', function() {
                const id = this.getAttribute('data-id');
                editProduct(id);
            });
        });
        
        document.querySelectorAll('.delete-btn[data-type="product"]').forEach(btn => {
            btn.addEventListener('click', function() {
                const id = this.getAttribute('data-id');
                deleteProduct(id);
            });
        });
    }
    
    function showProductForm() {
        // 创建或显示产品表单
        const formHtml = `
            <div class="form-header">
                <h3>${editingId ? 'Edit Product' : 'Add New Product'}</h3>
                <button class="btn" data-action="cancel-form">Cancel</button>
            </div>
            
            <form id="productForm">
                <input type="hidden" id="productId" value="${editingId || ''}">
                
                <div class="form-grid">
                    <div class="form-group">
                        <label for="productName">Product Name *</label>
                        <input type="text" id="productName" required>
                    </div>
                    <div class="form-group">
                        <label for="productCategory">Category *</label>
                        <select id="productCategory" required>
                            <option value="">Select Category</option>
                            <option value="photography">Photography</option>
                            <option value="audio">Audio</option>
                            <option value="video">Video</option>
                            <option value="lighting">Lighting</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="productPrice">Price ($) *</label>
                        <input type="number" id="productPrice" step="0.01" required>
                    </div>
                    <div class="form-group">
                        <label for="productStock">Stock *</label>
                        <input type="number" id="productStock" required>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="productDescription">Description</label>
                    <textarea id="productDescription" rows="3"></textarea>
                </div>
                
                <div class="form-group">
                    <label for="productSpecs">Specifications (JSON format)</label>
                    <textarea id="productSpecs" rows="4" placeholder='{"weight": "2kg", "dimensions": "10x20x30cm", "features": ["Feature 1", "Feature 2"]}'></textarea>
                </div>
                
                <div class="form-actions">
                    <button type="submit" class="btn btn-success">${editingId ? 'Update Product' : 'Save Product'}</button>
                    <button type="button" class="btn" data-action="cancel-form">Cancel</button>
                </div>
            </form>
        `;
        
        showForm('productFormContainer', formHtml);
        
        // 如果是编辑模式，填充数据
        if (editingId) {
            const products = loadProductsData();
            const product = products.find(p => p.id === editingId);
            
            if (product) {
                document.getElementById('productName').value = product.name;
                document.getElementById('productCategory').value = product.category;
                document.getElementById('productPrice').value = product.price;
                document.getElementById('productStock').value = product.stock;
                document.getElementById('productDescription').value = product.description || '';
                document.getElementById('productSpecs').value = product.specs ? JSON.stringify(product.specs, null, 2) : '';
            }
        }
        
        // 重新绑定表单事件
        document.getElementById('productForm')?.addEventListener('submit', function(e) {
            e.preventDefault();
            saveProduct();
        });
    }
    
    function editProduct(productId) {
        editingId = productId;
        editingType = 'product';
        showProductForm();
    }
    
    function saveProduct() {
        const product = {
            id: editingId || Date.now().toString(),
            name: document.getElementById('productName').value.trim(),
            category: document.getElementById('productCategory').value,
            price: parseFloat(document.getElementById('productPrice').value) || 0,
            stock: parseInt(document.getElementById('productStock').value) || 0,
            description: document.getElementById('productDescription').value.trim(),
            specs: parseSpecs(document.getElementById('productSpecs').value),
            createdAt: editingId ? undefined : new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        
        // 验证
        if (!product.name || !product.category || product.price <= 0) {
            showMessage('Please fill in all required fields correctly', 'error');
            return;
        }
        
        const products = loadProductsData();
        
        if (editingId) {
            // 更新
            const index = products.findIndex(p => p.id === editingId);
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
            hideForm();
        }
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
    
    function parseSpecs(specsText) {
        try {
            return specsText ? JSON.parse(specsText) : {};
        } catch (error) {
            console.error('Error parsing specs:', error);
            return {};
        }
    }
    
    // ==================== 团队管理功能 ====================
    
    function loadTeamData() {
        try {
            const data = localStorage.getItem(STORAGE_KEYS.TEAM);
            return data ? JSON.parse(data) : [];
        } catch (error) {
            console.error('Error loading team:', error);
            return [];
        }
    }
    
    function saveTeamData(team) {
        try {
            localStorage.setItem(STORAGE_KEYS.TEAM, JSON.stringify(team));
            return true;
        } catch (error) {
            console.error('Error saving team:', error);
            return false;
        }
    }
    
    function loadTeam() {
        const team = loadTeamData();
        const container = document.getElementById('teamList');
        
        if (!container) return;
        
        if (team.length === 0) {
            container.innerHTML = '<div style="text-align: center; padding: 40px; color: #666;">No team members yet. Click "Add Team Member" to add your first member.</div>';
            return;
        }
        
        let html = '<table class="data-table"><thead><tr><th>Name</th><th>Position</th><th>Email</th><th>Role</th><th>Actions</th></tr></thead><tbody>';
        
        team.forEach(member => {
            html += `
                <tr data-id="${member.id}" data-type="team">
                    <td><strong>${member.name}</strong></td>
                    <td>${member.position}</td>
                    <td>${member.email}</td>
                    <td>${member.role}</td>
                    <td class="table-actions">
                        <button class="btn btn-warning btn-small edit-btn" data-id="${member.id}" data-type="team">Edit</button>
                        <button class="btn btn-danger btn-small delete-btn" data-id="${member.id}" data-type="team">Delete</button>
                    </td>
                </tr>
            `;
        });
        
        html += '</tbody></table>';
        container.innerHTML = html;
        
        // 重新绑定事件
        document.querySelectorAll('.edit-btn[data-type="team"]').forEach(btn => {
            btn.addEventListener('click', function() {
                const id = this.getAttribute('data-id');
                editTeamMember(id);
            });
        });
        
        document.querySelectorAll('.delete-btn[data-type="team"]').forEach(btn => {
            btn.addEventListener('click', function() {
                const id = this.getAttribute('data-id');
                deleteTeamMember(id);
            });
        });
    }
    
    function showMemberForm() {
        // 创建或显示成员表单
        const formHtml = `
            <div class="form-header">
                <h3>${editingId ? 'Edit Team Member' : 'Add Team Member'}</h3>
                <button class="btn" data-action="cancel-form">Cancel</button>
            </div>
            
            <form id="memberForm">
                <input type="hidden" id="memberId" value="${editingId || ''}">
                
                <div class="form-grid">
                    <div class="form-group">
                        <label for="memberName">Full Name *</label>
                        <input type="text" id="memberName" required>
                    </div>
                    <div class="form-group">
                        <label for="memberPosition">Position *</label>
                        <input type="text" id="memberPosition" required>
                    </div>
                    <div class="form-group">
                        <label for="memberEmail">Email *</label>
                        <input type="email" id="memberEmail" required>
                    </div>
                    <div class="form-group">
                        <label for="memberPhone">Phone</label>
                        <input type="tel" id="memberPhone">
                    </div>
                    <div class="form-group">
                        <label for="memberRole">Role *</label>
                        <select id="memberRole" required>
                            <option value="">Select Role</option>
                            <option value="admin">Administrator</option>
                            <option value="manager">Manager</option>
                            <option value="staff">Staff</option>
                            <option value="support">Support</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="memberDepartment">Department</label>
                        <input type="text" id="memberDepartment">
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="memberBio">Bio/Description</label>
                    <textarea id="memberBio" rows="4"></textarea>
                </div>
                
                <div class="form-actions">
                    <button type="submit" class="btn btn-success">${editingId ? 'Update Member' : 'Save Member'}</button>
                    <button type="button" class="btn" data-action="cancel-form">Cancel</button>
                </div>
            </form>
        `;
        
        showForm