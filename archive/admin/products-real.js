// 产品管理系统核心逻辑
document.addEventListener('DOMContentLoaded', function() {
    console.log('Product Management System loaded');
    
    // 产品数据存储键
    const STORAGE_KEY = 'stratronix_products_v2';
    let products = [];
    let currentProductId = null;
    
    // 初始化
    function init() {
        loadProducts();
        renderProducts();
        setupEventListeners();
        updateProductsCount();
        showMessage('Product management system ready', 'info');
    }
    
    // 加载产品数据
    function loadProducts() {
        try {
            const data = localStorage.getItem(STORAGE_KEY);
            products = data ? JSON.parse(data) : [];
            console.log(`Loaded ${products.length} products`);
        } catch (error) {
            console.error('Error loading products:', error);
            products = [];
            showMessage('Error loading product data', 'error');
        }
    }
    
    // 保存产品数据
    function saveProducts() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(products));
            updateProductsCount();
            return true;
        } catch (error) {
            console.error('Error saving products:', error);
            showMessage('Error saving product data', 'error');
            return false;
        }
    }
    
    // 渲染产品列表
    function renderProducts() {
        const tbody = document.getElementById('productsBody');
        const noProducts = document.getElementById('noProducts');
        
        if (products.length === 0) {
            tbody.innerHTML = '';
            noProducts.style.display = 'block';
            return;
        }
        
        noProducts.style.display = 'none';
        
        let html = '';
        products.forEach(product => {
            const statusClass = product.stock > 0 ? 'status-active' : 'status-inactive';
            const statusText = product.stock > 0 ? 'In Stock' : 'Out of Stock';
            
            // 处理图片显示
            let imageHtml = '<div style="width: 60px; height: 60px; background: #f0f0f0; border-radius: 5px; display: flex; align-items: center; justify-content: center; color: #999;"><i class="fas fa-image"></i></div>';
            if (product.imageData) {
                imageHtml = `<img src="${product.imageData}" class="product-image" alt="${product.name}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 5px;">`;
            }
            
            html += `
                <tr data-id="${product.id}">
                    <td>${imageHtml}</td>
                    <td><strong>${product.name}</strong></td>
                    <td>${product.category}</td>
                    <td>$${parseFloat(product.price).toFixed(2)}</td>
                    <td>${product.stock}</td>
                    <td class="${statusClass}">${statusText}</td>
                    <td class="actions">
                        <button class="btn btn-secondary btn-small edit-btn" data-id="${product.id}">
                            <i class="fas fa-edit"></i> Edit
                        </button>
                        <button class="btn btn-danger btn-small delete-btn" data-id="${product.id}">
                            <i class="fas fa-trash"></i> Delete
                        </button>
                    </td>
                </tr>
            `;
        });
        
        tbody.innerHTML = html;
        
        // 重新绑定编辑和删除按钮事件
        document.querySelectorAll('.edit-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const productId = this.getAttribute('data-id');
                editProduct(productId);
            });
        });
        
        document.querySelectorAll('.delete-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const productId = this.getAttribute('data-id');
                deleteProduct(productId);
            });
        });
    }
    
    // 添加新产品
    function addProduct(productData) {
        const newProduct = {
            id: Date.now().toString(), // 简单ID生成
            ...productData,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        
        products.push(newProduct);
        if (saveProducts()) {
            renderProducts();
            showMessage('Product added successfully', 'success');
            return true;
        }
        return false;
    }
    
    // 更新产品
    function updateProduct(productId, productData) {
        const index = products.findIndex(p => p.id === productId);
        if (index !== -1) {
            products[index] = {
                ...products[index],
                ...productData,
                updatedAt: new Date().toISOString()
            };
            
            if (saveProducts()) {
                renderProducts();
                showMessage('Product updated successfully', 'success');
                return true;
            }
        }
        return false;
    }
    
    // 删除产品
    function deleteProduct(productId) {
        if (!confirm('Are you sure you want to delete this product?')) {
            return false;
        }
        
        const index = products.findIndex(p => p.id === productId);
        if (index !== -1) {
            products.splice(index, 1);
            if (saveProducts()) {
                renderProducts();
                showMessage('Product deleted successfully', 'success');
                return true;
            }
        }
        return false;
    }
    
    // 编辑产品
    function editProduct(productId) {
        const product = products.find(p => p.id === productId);
        if (!product) {
            showMessage('Product not found', 'error');
            return;
        }
        
        currentProductId = productId;
        
        // 填充表单
        document.getElementById('productId').value = product.id;
        document.getElementById('name').value = product.name || '';
        document.getElementById('category').value = product.category || '';
        document.getElementById('price').value = product.price || '';
        document.getElementById('stock').value = product.stock || '';
        document.getElementById('description').value = product.description || '';
        document.getElementById('specifications').value = product.specifications || '';
        
        // 处理图片
        if (product.imageData) {
            document.getElementById('previewImage').src = product.imageData;
            document.getElementById('imagePreview').style.display = 'block';
            document.getElementById('imageData').value = product.imageData;
        } else {
            document.getElementById('imagePreview').style.display = 'none';
            document.getElementById('imageData').value = '';
        }
        
        // 更新表单标题
        document.getElementById('formTitle').innerHTML = '<i class="fas fa-edit"></i> Edit Product';
        
        // 显示表单
        document.getElementById('productForm').classList.add('active');
        document.getElementById('addProductBtn').style.display = 'none';
        
        // 滚动到表单
        document.getElementById('productForm').scrollIntoView({ behavior: 'smooth' });
    }
    
    // 重置表单
    function resetForm() {
        document.getElementById('productFormElement').reset();
        document.getElementById('productId').value = '';
        document.getElementById('imagePreview').style.display = 'none';
        document.getElementById('previewImage').src = '';
        document.getElementById('imageData').value = '';
        document.getElementById('formTitle').innerHTML = '<i class="fas fa-plus-circle"></i> Add New Product';
        currentProductId = null;
    }
    
    // 显示消息
    function showMessage(text, type = 'info') {
        const messageEl = document.getElementById('message');
        messageEl.textContent = text;
        messageEl.className = `message ${type}`;
        messageEl.style.display = 'block';
        
        // 自动隐藏消息
        setTimeout(() => {
            messageEl.style.display = 'none';
        }, 5000);
    }
    
    // 更新产品计数
    function updateProductsCount() {
        document.getElementById('productsCount').textContent = products.length;
    }
    
    // 设置事件监听器
    function setupEventListeners() {
        // 添加产品按钮
        document.getElementById('addProductBtn').addEventListener('click', function() {
            resetForm();
            document.getElementById('productForm').classList.add('active');
            this.style.display = 'none';
            document.getElementById('name').focus();
        });
        
        // 取消按钮
        document.getElementById('cancelBtn').addEventListener('click', function() {
            document.getElementById('productForm').classList.remove('active');
            document.getElementById('addProductBtn').style.display = 'inline-flex';
            resetForm();
        });
        
        // 表单提交
        document.getElementById('productFormElement').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 收集表单数据
            const productData = {
                name: document.getElementById('name').value.trim(),
                category: document.getElementById('category').value,
                price: parseFloat(document.getElementById('price').value) || 0,
                stock: parseInt(document.getElementById('stock').value) || 0,
                description: document.getElementById('description').value.trim(),
                specifications: document.getElementById('specifications').value.trim(),
                imageData: document.getElementById('imageData').value
            };
            
            // 验证必填字段
            if (!productData.name || !productData.category || productData.price <= 0) {
                showMessage('Please fill in all required fields correctly', 'error');
                return;
            }
            
            // 保存或更新产品
            let success = false;
            if (currentProductId) {
                success = updateProduct(currentProductId, productData);
            } else {
                success = addProduct(productData);
            }
            
            if (success) {
                // 重置表单并隐藏
                document.getElementById('productForm').classList.remove('active');
                document.getElementById('addProductBtn').style.display = 'inline-flex';
                resetForm();
            }
        });
        
        // 图片上传
        const imageUploadArea = document.getElementById('imageUploadArea');
        const imageFileInput = document.getElementById('imageFile');
        const imagePreview = document.getElementById('imagePreview');
        const previewImage = document.getElementById('previewImage');
        const imageDataInput = document.getElementById('imageData');
        
        imageUploadArea.addEventListener('click', function() {
            imageFileInput.click();
        });
        
        imageFileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            // 验证文件类型和大小
            if (!file.type.startsWith('image/')) {
                showMessage('Please select an image file', 'error');
                return;
            }
            
            if (file.size > 5 * 1024 * 1024) { // 5MB限制
                showMessage('Image size should be less than 5MB', 'error');
                return;
            }
            
            // 读取文件为Base64
            const reader = new FileReader();
            reader.onload = function(event) {
                const base64Data = event.target.result;
                previewImage.src = base64Data;
                imagePreview.style.display = 'block';
                imageDataInput.value = base64Data;
                showMessage('Image uploaded successfully', 'success');
            };
            reader.readAsDataURL(file);
        });
        
        // 数据导出
        document.getElementById('exportBtn').addEventListener('click', function() {
            const dataStr = JSON.stringify(products, null, 2);
            const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
            
            const exportFileDefaultName = `stratronix-products-${new Date().toISOString().split('T')[0]}.json`;
            
            const linkElement = document.createElement('a');
            linkElement.setAttribute('href', dataUri);
            linkElement.setAttribute('download', exportFileDefaultName);
            linkElement.click();
            
            showMessage('Data exported successfully', 'success');
        });
        
        // 数据导入
        document.getElementById('importBtn').addEventListener('click', function() {
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = '.json';
            
            input.addEventListener('change', function(e) {
                const file = e.target.files[0];
                if (!file) return;
                
                const reader = new FileReader();
                reader.onload = function(event) {
                    try {
                        const importedData = JSON.parse(event.target.result);
                        if (Array.isArray(importedData)) {
                            // 合并数据，避免重复ID
                            const existingIds = new Set(products.map(p => p.id));
                            importedData.forEach(product => {
                                if (!existingIds.has(product.id)) {
                                    products.push(product);
                                }
                            });
                            
                            if (saveProducts()) {
                                renderProducts();
                                showMessage(`Imported ${importedData.length} products`, 'success');
                            }
                        } else {
                            showMessage('Invalid data format', 'error');
                        }
                    } catch (error) {
                        showMessage('Error parsing JSON file', 'error');
                    }
                };
                reader.readAsText(file);
            });
            
            input.click();
        });
        
        // 清空数据
        document.getElementById('clearBtn').addEventListener('click', function() {
            if (confirm('Are you sure you want to clear ALL product data? This cannot be undone!')) {
                products = [];
                if (saveProducts()) {
                    renderProducts();
                    showMessage('All product data cleared', 'success');
                }
            }
        });
        
        // 导航链接
        document.querySelectorAll('.nav-links a').forEach(link => {
            if (link.getAttribute('href') === '#') {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    const page = this.textContent;
                    showMessage(`${page} page is under development`, 'info');
                });
            }
        });
    }
    
    // 初始化系统
    init();
    
    console.log('Product Management System initialized successfully');
});