// 完整的一体化后台管理系统
document.addEventListener('DOMContentLoaded', function() {
    console.log('Full Admin System loaded');
    
    // 数据存储键 - 统一命名，网站可以访问
    const STORAGE_KEYS = {
        PRODUCTS: 'stratronix_products',           // 产品数据 - 网站可访问
        TEAM: 'stratronix_team',                   // 团队数据 - 网站可访问
        CONTENT: 'stratronix_content',             // 内容数据 - 网站可访问
        SETTINGS: 'stratronix_settings',           // 设置数据 - 网站可访问
        USER: 'stratronix_admin_user'              // 用户数据 - 仅后台使用
    };
    
    // 当前状态
    let currentUser = null;
    let currentPage = 'dashboard';
    let editingId = null;
    let editingType = null;
    
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
            team: 'Team Management',
            content: 'Content Management',
            system: 'System Information'
        };
        return titles[page] || 'Admin';
    }
    
    // 加载页面数据
    function loadPageData(page) {
        switch(page) {
            case 'dashboard':
                updateDashboardStats();
                break;
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
    
    // 更新仪表板统计
    function updateDashboardStats() {
        const products = loadProductsData();
        const team = loadTeamData();
        const content = loadContentData();
        
        document.getElementById('productsCount').textContent = products.length;
        document.getElementById('teamCount').textContent = team.length;
        document.getElementById('visitorsCount').textContent = '1,234'; // 示例数据
        document.getElementById('contentCount').textContent = Object.keys(content).length;
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
                    <td>
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
    
    function editProduct(productId) {
        const products = loadProductsData();
        const product = products.find(p => p.id === productId);
        
        if (!product) {
            showMessage('Product not found', 'error');
            return;
        }
        
        editingId = productId;
        editingType = 'product';
        
        // 显示表单
        showForm('product');
        
        // 填充表单
        document.getElementById('productName').value = product.name;
        document.getElementById('productCategory').value = product.category;
        document.getElementById('productPrice').value = product.price;
        document.getElementById('productStock').value = product.stock;
        document.getElementById('productDescription').value = product.description || '';
        document.getElementById('productSpecs').value = product.specs || '';
        
        document.getElementById('formTitle').textContent = 'Edit Product';
    }
    
    function deleteProduct(productId) {
        if (!confirm('Are you sure you want to delete this product?')) {
            return;
        }
        
        const products = loadProductsData();
        const filteredProducts = products.filter(p => p.id !== productId);
        
        if (saveProductsData(filteredProducts)) {
            loadProducts();
            updateDashboardStats();
            showMessage('Product deleted successfully', 'success');
        }
    }
    
    function saveProduct(e) {
        e.preventDefault();
        
        const product = {
            id: editingId || Date.now().toString(),
            name: document.getElementById('productName').value.trim(),
            category: document.getElementById('productCategory').value,
            price: parseFloat(document.getElementById('productPrice').value) || 0,
            stock: parseInt(document.getElementById('productStock').value) || 0,
            description: document.getElementById('productDescription').value.trim(),
            specs: document.getElementById('productSpecs').value.trim(),
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
            updateDashboardStats();
            hideForm();
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
                    <td>
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
    
    function editTeamMember(memberId) {
        const team = loadTeamData();
        const member = team.find(m => m.id === memberId);
        
        if (!member) {
            showMessage('Team member not found', 'error');
            return;
        }
        
        editingId = memberId;
        editingType = 'team';
        
        // 显示表单
        showForm('team');
        
        // 填充表单
        document.getElementById('memberName').value = member.name;
        document.getElementById('memberPosition').value = member.position;
        document.getElementById('memberEmail').value = member.email;
        document.getElementById('memberPhone').value = member.phone || '';
        document.getElementById('memberRole').value = member.role;
        document.getElementById('memberBio').value = member.bio || '';
        
        document.getElementById('formTitle').textContent = 'Edit Team Member';
    }
    
    function deleteTeamMember(memberId) {
        if (!confirm('Are you sure you want to delete this team member?')) {
            return;
        }
        
        const team = loadTeamData();
        const filteredTeam = team.filter(m => m.id !== memberId);
        
        if (saveTeamData(filteredTeam)) {
            loadTeam();
            updateDashboardStats();
            showMessage('Team member deleted successfully', 'success');
        }
    }
    
    function saveTeamMember(e) {
        e.preventDefault();
        
        const member = {
            id: editingId || Date.now().toString(),
            name: document.getElementById('memberName').value.trim(),
            position: document.getElementById('memberPosition').value.trim(),
            email: document.getElementById('memberEmail').value.trim(),
            phone: document.getElementById('memberPhone').value.trim(),
            role: document.getElementById('memberRole').value,
            bio: document.getElementById('memberBio').value.trim(),
            createdAt: editingId ? undefined : new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        
        // 验证
        if (!member.name || !member.position || !member.email) {
            showMessage('Please fill in all required fields', 'error');
            return;
        }
        
        const team = loadTeamData();
        
        if (editingId) {
            // 更新
            const index = team.findIndex(m => m.id === editingId);
            if (index !== -1) {
                team[index] = { ...team[index], ...member };
                showMessage('Team member updated successfully', 'success');
            }
        } else {
            // 添加
            team.push(member);
            showMessage('Team member added successfully', 'success');
        }
        
        if (saveTeamData(team)) {
            loadTeam();
            updateDashboardStats();
            hideForm();
        }
    }
    
    // ==================== 内容管理功能 ====================
    
    function loadContentData() {
        try {
            const data = localStorage.getItem(STORAGE_KEYS.CONTENT);
            return data ? JSON.parse(data) : {
                homepage: {
                    title: 'Welcome to Stratronix',
                    subtitle: 'Professional Photography & Audio Equipment',
                    description: 'High-quality equipment for professionals and enthusiasts. Experience the difference with Stratronix.',
                    heroButton: 'View Products'
                },
                about: {
                    title: 'About Stratronix',
                    content: 'We provide professional photography, audio, and video equipment for creators worldwide.',
                    mission: 'Our mission is to empower creators with the best tools for their craft.',
                    vision: 'To be the leading provider of professional creative equipment.'
                },
                contact: {
                    email: 'info@stratronix.ai',
                    phone: '+1 (555) 123-4567',
                    address: '123 Creative Street, San Francisco, CA 94107'
                }
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
    
    function loadContent() {
        const content = loadContentData();
        
        // 填充表单
        document.getElementById('homepageTitle').value = content.homepage?.title || '';
        document.getElementById('homepageSubtitle').value = content.homepage?.subtitle || '';
        document.getElementById('homepageDescription').value = content.homepage?.description || '';
        document.getElementById('homepageButton').value = content.homepage?.heroButton || '';
        
        document.getElementById('aboutTitle').value = content.about?.title || '';
        document.getElementById('aboutContent').value = content.about?.content || '';
        document.getElementById('aboutMission').value = content.about?.mission || '';
        document.getElementById('aboutVision').value = content.about?.vision || '';
        
        document.getElementById('contactEmail').value = content.contact?.email || '';
        document.getElementById('contactPhone').value = content.contact?.phone || '';
        document.getElementById('contactAddress').value = content.contact?.address || '';
    }
    
    function saveContent(e) {
        e.preventDefault();
        
        const content = {
            homepage: {
                title: document.getElementById('homepageTitle').value,
                subtitle: document.getElementById('homepageSubtitle').value,
                description: document.getElementById('homepageDescription').value,
                heroButton: document.getElementById('homepageButton').value
            },
            about: {
                title: document.getElementById('aboutTitle').value,
                content: document.getElementById('aboutContent').value,
                mission: document.getElementById('aboutMission').value,
                vision: document.getElementById('aboutVision').value
            },
            contact: {
                email: document.getElementById('contactEmail').value,
                phone: document.getElementById('contactPhone').value,
                address: