// Simple Core Values Cards Animation
document.addEventListener('DOMContentLoaded', function() {
    const simpleCards = document.querySelectorAll('.simple-card');
    
    if (simpleCards.length === 0) return;
    
    // 初始化卡片状态
    simpleCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    });
    
    // 滚动动画
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const index = Array.from(simpleCards).indexOf(entry.target);
                
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 150);
                
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '50px'
    });
    
    simpleCards.forEach(card => {
        observer.observe(card);
    });
    
    // 鼠标悬停效果
    simpleCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            // 轻微放大和上浮
            this.style.transform = 'translateY(-8px) scale(1.02)';
            
            // 添加光晕效果
            const glow = document.createElement('div');
            glow.className = 'simple-card-glow';
            glow.style.position = 'absolute';
            glow.style.top = '0';
            glow.style.left = '0';
            glow.style.right = '0';
            glow.style.bottom = '0';
            glow.style.background = 'radial-gradient(circle at center, rgba(26, 115, 232, 0.1), transparent 70%)';
            glow.style.opacity = '0';
            glow.style.transition = 'opacity 0.3s ease';
            glow.style.pointerEvents = 'none';
            
            this.appendChild(glow);
            
            setTimeout(() => {
                glow.style.opacity = '1';
            }, 10);
        });
        
        card.addEventListener('mouseleave', function() {
            // 恢复原始状态
            this.style.transform = 'translateY(0) scale(1)';
            
            // 移除光晕效果
            const glow = this.querySelector('.simple-card-glow');
            if (glow) {
                glow.style.opacity = '0';
                setTimeout(() => {
                    if (glow.parentNode === this) {
                        this.removeChild(glow);
                    }
                }, 300);
            }
        });
        
        card.addEventListener('mousemove', function(e) {
            // 动态光晕跟随鼠标
            const glow = this.querySelector('.simple-card-glow');
            if (glow) {
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                glow.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(26, 115, 232, 0.15), transparent 70%)`;
            }
            
            // 轻微3D倾斜效果
            const cardWidth = this.offsetWidth;
            const cardHeight = this.offsetHeight;
            const centerX = cardWidth / 2;
            const centerY = cardHeight / 2;
            const mouseX = e.offsetX;
            const mouseY = e.offsetY;
            
            const rotateY = ((mouseX - centerX) / centerX) * 1;
            const rotateX = ((centerY - mouseY) / centerY) * 1;
            
            this.style.transform = `translateY(-8px) scale(1.02) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });
        
        // 点击效果
        card.addEventListener('click', function() {
            this.style.transform = 'translateY(-4px) scale(0.98)';
            
            setTimeout(() => {
                this.style.transform = 'translateY(-8px) scale(1.02)';
            }, 150);
        });
    });
    
    // 初始动画
    setTimeout(() => {
        simpleCards.forEach((card, index) => {
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 200);
        });
    }, 300);
});