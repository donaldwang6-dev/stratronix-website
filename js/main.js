// Stratronix / 鼎图 双语网站主脚本

document.addEventListener('DOMContentLoaded', function() {
    // ====================
    // 1. 移动端导航菜单切换
    // ====================
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            const icon = this.querySelector('i');
            if (navMenu.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
        
        // 点击菜单项后关闭菜单（移动端）
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 768) {
                    navMenu.classList.remove('active');
                    const icon = navToggle.querySelector('i');
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            });
        });
        
        // 点击页面其他区域关闭菜单
        document.addEventListener('click', function(event) {
            if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
                const icon = navToggle.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }
    
    // ====================
    // 2. 平滑滚动
    // ====================
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // 如果是页面内锚点链接
            if (href !== '#' && href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    // 如果是移动端，先关闭导航菜单
                    if (window.innerWidth <= 768 && navMenu) {
                        navMenu.classList.remove('active');
                        const icon = navToggle.querySelector('i');
                        if (icon) {
                            icon.classList.remove('fa-times');
                            icon.classList.add('fa-bars');
                        }
                    }
                    
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // ====================
    // 3. 导航栏滚动效果
    // ====================
    let lastScrollTop = 0;
    const navbar = document.querySelector('.navbar');
    
    if (navbar) {
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            // 向下滚动时隐藏导航栏，向上滚动时显示
            if (scrollTop > lastScrollTop && scrollTop > 100) {
                navbar.style.transform = 'translateY(-100%)';
            } else {
                navbar.style.transform = 'translateY(0)';
            }
            
            // 添加滚动阴影
            if (scrollTop > 10) {
                navbar.style.boxShadow = 'var(--shadow-md)';
            } else {
                navbar.style.boxShadow = 'none';
            }
            
            lastScrollTop = scrollTop;
        });
    }
    
    // ====================
    // 4. 当前页面高亮
    // ====================
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const linkHref = link.getAttribute('href');
        if (linkHref === currentPage || 
            (currentPage === '' && linkHref === 'index.html') ||
            (currentPage === '/' && linkHref === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
    
    // ====================
    // 5. 表单验证
    // ====================
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 简单的表单验证
            const name = this.querySelector('input[name="name"]');
            const email = this.querySelector('input[name="email"]');
            const message = this.querySelector('textarea[name="message"]');
            
            let isValid = true;
            
            // 重置错误状态
            [name, email, message].forEach(input => {
                input.classList.remove('error');
                const errorMsg = input.nextElementSibling;
                if (errorMsg && errorMsg.classList.contains('error-message')) {
                    errorMsg.remove();
                }
            });
            
            // 验证姓名
            if (!name.value.trim()) {
                showError(name, getText('nameRequired'));
                isValid = false;
            }
            
            // 验证邮箱
            if (!email.value.trim()) {
                showError(email, getText('emailRequired'));
                isValid = false;
            } else if (!isValidEmail(email.value)) {
                showError(email, getText('emailInvalid'));
                isValid = false;
            }
            
            // 验证消息
            if (!message.value.trim()) {
                showError(message, getText('messageRequired'));
                isValid = false;
            } else if (message.value.trim().length < 10) {
                showError(message, getText('messageMinLength'));
                isValid = false;
            }
            
            if (isValid) {
                // 这里可以添加表单提交逻辑
                alert(getText('formSuccess'));
                this.reset();
            }
        });
    }
    
    // 显示错误信息
    function showError(input, message) {
        input.classList.add('error');
        const errorElement = document.createElement('div');
        errorElement.className = 'error-message';
        errorElement.textContent = message;
        errorElement.style.color = 'var(--accent-color)';
        errorElement.style.fontSize = '0.85rem';
        errorElement.style.marginTop = '0.25rem';
        input.parentNode.insertBefore(errorElement, input.nextSibling);
    }
    
    // 验证邮箱格式
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    // ====================
    // 6. 懒加载图片
    // ====================
    const lazyImages = document.querySelectorAll('img[data-src]');
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => imageObserver.observe(img));
    } else {
        // 回退方案
        lazyImages.forEach(img => {
            img.src = img.dataset.src;
        });
    }
    
    // ====================
    // 7. 回到顶部按钮
    // ====================
    const backToTopButton = document.createElement('button');
    backToTopButton.innerHTML = '<i class="fas fa-chevron-up"></i>';
    backToTopButton.className = 'back-to-top';
    backToTopButton.setAttribute('aria-label', getText('backToTop'));
    backToTopButton.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        box-shadow: var(--shadow-lg);
        transition: all var(--transition-normal);
        z-index: 999;
        opacity: 0.9;
    `;
    
    document.body.appendChild(backToTopButton);
    
    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'flex';
        } else {
            backToTopButton.style.display = 'none';
        }
    });
    
    // 添加悬停效果
    backToTopButton.addEventListener('mouseenter', function() {
        this.style.backgroundColor = 'var(--primary-dark)';
        this.style.transform = 'translateY(-3px)';
        this.style.opacity = '1';
    });
    
    backToTopButton.addEventListener('mouseleave', function() {
        this.style.backgroundColor = 'var(--primary-color)';
        this.style.transform = 'translateY(0)';
        this.style.opacity = '0.9';
    });
    
    // ====================
    // 8. 卡片悬停效果增强
    // ====================
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // ====================
    // 9. 响应式图片处理
    // ====================
    function handleResponsiveImages() {
        const images = document.querySelectorAll('img');
        images.forEach(img => {
            if (!img.hasAttribute('loading')) {
                img.setAttribute('loading', 'lazy');
            }
        });
    }
    
    handleResponsiveImages();
    
    // ====================
    // 10. 键盘导航支持
    // ====================
    document.addEventListener('keydown', function(e) {
        // ESC键关闭导航菜单
        if (e.key === 'Escape' && navMenu && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            const icon = navToggle.querySelector('i');
            if (icon) {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        }
        
        // 空格键滚动
        if (e.key === ' ' && !(e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) {
            e.preventDefault();
            window.scrollBy(0, window.innerHeight * 0.8);
        }
    });
    
    // ====================
    // 11. 性能优化：减少重绘
    // ====================
    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                // 这里可以添加需要优化的滚动相关代码
                ticking = false;
            });
            ticking = true;
        }
    });
    
    // ====================
    // 12. 多语言文本函数
    // ====================
    function getText(key) {
        const texts = {
            // 英文文本
            'en': {
                'nameRequired': 'Please enter your name',
                'emailRequired': 'Please enter your email',
                'emailInvalid': 'Please enter a valid email address',
                'messageRequired': 'Please enter your message',
                'messageMinLength': 'Message must be at least 10 characters',
                'formSuccess': 'Thank you for your message! We will contact you soon.',
                'backToTop': 'Back to top'
            },
            // 中文文本
            'zh': {
                'nameRequired': '请输入您的姓名',
                'emailRequired': '请输入您的邮箱',
                'emailInvalid': '请输入有效的邮箱地址',
                'messageRequired': '请输入您的消息',
                'messageMinLength': '消息内容至少需要10个字符',
                'formSuccess': '感谢您的留言！我们会尽快与您联系。',
                'backToTop': '回到顶部'
            }
        };
        
        // 检测当前语言
        const currentLang = document.documentElement.lang || 'en';
        return texts[currentLang][key] || key;
    }
    
    // ====================
    // 13. 语言切换功能
    // ====================
    function initLanguageSwitcher() {
        // 获取所有语言切换按钮
        const langButtons = document.querySelectorAll('.lang-btn');
        
        langButtons.forEach(button => {
            button.addEventListener('click', function(e) {
                // 防止默认链接行为（我们将用JavaScript处理）
                e.preventDefault();
                
                // 获取当前页面路径
                const currentPath = window.location.pathname;
                
                // 确定目标语言（使用data-lang属性）
                let targetLang = this.getAttribute('data-lang') || 'en'; // 默认英语
                
                // 如果没有data-lang属性，回退到文本检测
                if (!targetLang) {
                    const buttonText = this.textContent.trim();
                    if (buttonText.includes('中文') || buttonText === '中文') {
                        targetLang = 'zh';
                    } else if (buttonText.includes('English') || buttonText === 'English') {
                        targetLang = 'en';
                    }
                }
                
                // 获取当前文件名
                let currentFile = 'index.html';
                if (currentPath.includes('/en/')) {
                    currentFile = currentPath.split('/en/')[1] || 'index.html';
                } else if (currentPath.includes('/zh/')) {
                    currentFile = currentPath.split('/zh/')[1] || 'index.html';
                } else {
                    // 如果在根目录
                    currentFile = currentPath.substring(1) || 'index.html';
                }
                
                // 构建目标URL
                let targetUrl = '';
                if (targetLang === 'zh') {
                    targetUrl = `/zh/${currentFile}`;
                } else {
                    targetUrl = `/en/${currentFile}`;
                }
                
                // 跳转到目标页面
                console.log(`Switching language to ${targetLang}, navigating to: ${targetUrl}`);
                window.location.href = targetUrl;
            });
        });
        
        // 更新活动按钮状态
        updateActiveLanguageButton();
    }
    
    function updateActiveLanguageButton() {
        const currentPath = window.location.pathname;
        const langButtons = document.querySelectorAll('.lang-btn');
        
        // 移除所有active类
        langButtons.forEach(button => {
            button.classList.remove('active');
        });
        
        // 根据当前URL添加active类
        langButtons.forEach(button => {
            const buttonLang = button.getAttribute('data-lang');
            
            if (!buttonLang) return;
            
            if (currentPath.includes('/zh/') && buttonLang === 'zh') {
                button.classList.add('active');
            } else if (currentPath.includes('/en/') && buttonLang === 'en') {
                button.classList.add('active');
            } else if (!currentPath.includes('/zh/') && !currentPath.includes('/en/')) {
                // 根目录，默认英语
                if (buttonLang === 'en') {
                    button.classList.add('active');
                }
            }
        });
    }
    
    // ====================
    // 14. 设备检测
    // ====================
    function detectDevice() {
        const userAgent = navigator.userAgent;
        const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(userAgent);
        const isTablet = /iPad|Android(?!.*Mobile)/i.test(userAgent);
        
        if (isMobile) {
            document.body.classList.add('is-mobile');
        } else if (isTablet) {
            document.body.classList.add('is-tablet');
        } else {
            document.body.classList.add('is-desktop');
        }
    }
    
    detectDevice();
    
    // ====================
    // 15. 初始化语言切换
    // ====================
    initLanguageSwitcher();
    
    // ====================
    // 16. 初始化完成
    // ====================
    console.log('Stratronix / 鼎图 website initialized successfully');
});

// 页面加载完成后的额外初始化
window.addEventListener('load', function() {
    // 添加加载完成类
    document.body.classList.add('loaded');
    
    // 移除加载动画（如果有）
    const loadingElement = document.querySelector('.loading');
    if (loadingElement) {
        loadingElement.style.display = 'none';
    }
    
    // 性能监控
    if ('performance' in window) {
        const perfData = window.performance.timing;
        const loadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log(`Page loaded in ${loadTime}ms`);
    }
});

// 错误处理
window.addEventListener('error', function(e) {
    console.error('Website error:', e.error);
    // 这里可以添加错误上报逻辑
});

// 离线检测
window.addEventListener('offline', function() {
    console.log('You are now offline.');
    // 这里可以添加离线处理逻辑
});

window.addEventListener('online', function() {
    console.log('You are now online.');
    // 这里可以添加重新连接逻辑
});