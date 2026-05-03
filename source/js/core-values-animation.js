// Core Values Dynamic Cards Animation
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.dynamic-card');
    
    // 检查是否支持Intersection Observer
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('card-visible');
                    
                    // 为每个卡片添加延迟动画
                    const index = Array.from(cards).indexOf(entry.target);
                    entry.target.style.animationDelay = `${index * 0.2}s`;
                    
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '50px'
        });
        
        cards.forEach(card => {
            observer.observe(card);
        });
    }
    
    // 鼠标悬停效果增强
    cards.forEach(card => {
        card.addEventListener('mouseenter', function(e) {
            // 创建光晕效果
            const glow = this.querySelector('.card-glow');
            if (glow) {
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                glow.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(26, 115, 232, 0.2), transparent 70%)`;
            }
            
            // 轻微震动效果
            this.style.transform = 'translateY(-10px) scale(1.02) rotateX(2deg)';
            
            // 图标旋转
            const icon = this.querySelector('.card-icon');
            if (icon) {
                icon.style.transform = 'scale(1.2) rotate(5deg)';
            }
        });
        
        card.addEventListener('mousemove', function(e) {
            // 动态光晕跟随鼠标
            const glow = this.querySelector('.card-glow');
            if (glow) {
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                glow.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(26, 115, 232, 0.2), transparent 70%)`;
            }
            
            // 3D倾斜效果
            const cardWidth = this.offsetWidth;
            const cardHeight = this.offsetHeight;
            const centerX = cardWidth / 2;
            const centerY = cardHeight / 2;
            const mouseX = e.offsetX;
            const mouseY = e.offsetY;
            
            const rotateY = ((mouseX - centerX) / centerX) * 2;
            const rotateX = ((centerY - mouseY) / centerY) * 2;
            
            this.style.transform = `translateY(-10px) scale(1.02) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });
        
        card.addEventListener('mouseleave', function() {
            // 恢复原始状态
            this.style.transform = 'translateY(0) scale(1) rotateX(0) rotateY(0)';
            
            // 恢复图标
            const icon = this.querySelector('.card-icon');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0)';
            }
            
            // 重置光晕
            const glow = this.querySelector('.card-glow');
            if (glow) {
                glow.style.background = 'radial-gradient(circle at center, rgba(26, 115, 232, 0.1), transparent 70%)';
            }
        });
        
        // 点击效果
        card.addEventListener('click', function() {
            this.style.transform = 'translateY(-5px) scale(0.98)';
            setTimeout(() => {
                this.style.transform = 'translateY(-10px) scale(1.02)';
            }, 150);
        });
    });
    
    // 添加滚动动画
    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY;
        const windowHeight = window.innerHeight;
        
        cards.forEach((card, index) => {
            const cardPosition = card.getBoundingClientRect().top + scrollPosition;
            const cardCenter = cardPosition - windowHeight / 2;
            
            if (scrollPosition > cardCenter - windowHeight && scrollPosition < cardCenter + windowHeight) {
                const progress = (scrollPosition - (cardCenter - windowHeight)) / (windowHeight * 2);
                const opacity = Math.min(1, progress * 2);
                const translateY = (1 - progress) * 20;
                
                card.style.opacity = opacity;
                card.style.transform = `translateY(${translateY}px)`;
            }
        });
    });
    
    // 初始化卡片状态
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });
    
    // 触发初始动画
    setTimeout(() => {
        cards.forEach((card, index) => {
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 200);
        });
    }, 500);
});