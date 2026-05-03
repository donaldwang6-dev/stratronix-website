// 产品管理页面JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Product management page loaded');
    
    // 显示/隐藏添加产品表单
    const addProductBtn = document.getElementById('addProductBtn');
    const addProductForm = document.getElementById('addProductForm');
    const cancelBtn = document.getElementById('cancelBtn');
    const saveProductBtn = document.getElementById('saveProductBtn');
    
    if (addProductBtn && addProductForm) {
        addProductBtn.addEventListener('click', function() {
            addProductForm.style.display = 'block';
            this.style.display = 'none';
            document.getElementById('productName').focus();
        });
    }
    
    if (cancelBtn && addProductForm && addProductBtn) {
        cancelBtn.addEventListener('click', function() {
            addProductForm.style.display = 'none';
            addProductBtn.style.display = 'inline-flex';
        });
    }
    
    // 保存产品
    if (saveProductBtn) {
        saveProductBtn.addEventListener('click', function() {
            const name = document.getElementById('productName').value;
            const category = document.getElementById('productCategory').value;
            const price = document.getElementById('productPrice').value;
            const stock = document.getElementById('productStock').value;
            
            if (!name || !category || !price || !stock) {
                alert('Please fill in all required fields');
                return;
            }
            
            console.log('Saving product:', { name, category, price, stock });
            alert('Product saved successfully! (This is a demo)');
            
            // 重置表单
            if (addProductForm && addProductBtn) {
                addProductForm.style.display = 'none';
                addProductBtn.style.display = 'inline-flex';
            }
            
            // 清空表单
            document.getElementById('productName').value = '';
            document.getElementById('productCategory').value = '';
            document.getElementById('productPrice').value = '';
            document.getElementById('productStock').value = '';
            document.getElementById('productDescription').value = '';
            document.getElementById('productSpecs').value = '';
            document.getElementById('productImage').value = '';
        });
    }
    
    // 编辑产品按钮
    document.querySelectorAll('.btn-secondary').forEach(btn => {
        if (btn.textContent.includes('Edit')) {
            btn.addEventListener('click', function() {
                const row = this.closest('tr');
                const productName = row.querySelector('td:nth-child(2)').textContent;
                alert(`Editing product: ${productName}\n\nEdit functionality will be implemented in the next version.`);
            });
        }
    });
    
    // 删除产品按钮
    document.querySelectorAll('.btn-danger').forEach(btn => {
        if (btn.textContent.includes('Delete')) {
            btn.addEventListener('click', function() {
                const row = this.closest('tr');
                const productName = row.querySelector('td:nth-child(2)').textContent;
                
                if (confirm(`Are you sure you want to delete "${productName}"?`)) {
                    row.style.display = 'none';
                    alert(`Product "${productName}" deleted (demo only)`);
                }
            });
        }
    });
    
    // 搜索功能
    const searchInput = document.querySelector('.search-box input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const rows = document.querySelectorAll('tbody tr');
            
            rows.forEach(row => {
                const productName = row.querySelector('td:nth-child(2)').textContent.toLowerCase();
                const category = row.querySelector('td:nth-child(3)').textContent.toLowerCase();
                
                if (productName.includes(searchTerm) || category.includes(searchTerm)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    }
    
    // 导航菜单
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', function(e) {
            if (this.getAttribute('href') === '#') {
                e.preventDefault();
                const page = this.querySelector('span').textContent;
                console.log('Navigating to:', page);
                alert(`Navigating to ${page} page (under development)`);
            }
        });
    });
    
    console.log('Product management page ready');
});