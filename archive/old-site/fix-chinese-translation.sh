#!/bin/bash
echo "=== 修复中文版本中的英文内容 ==="

# 1. 修复Home页面
echo "1. 修复Home页面..."
echo "----------------------------------------"

# 翻译Core Values描述
sed -i 's|Continuously researching and developing breakthrough technologies to drive industry advancement and create sustainable competitive advantages.|持续研究和开发突破性技术，推动行业进步，创造可持续的竞争优势。|g' zh/index.html
sed -i 's|Ensuring product quality and system stability through rigorous testing, continuous optimization, and 99.99% uptime guarantee for mission-critical operations.|通过严格测试、持续优化和99.99%运行时间保证，确保产品质量和系统稳定性，满足关键任务需求。|g' zh/index.html
sed -i 's|Centered on customer needs, providing personalized solutions, professional support, and dedicated partnership to ensure your success with our technology.|以客户需求为中心，提供个性化解决方案、专业支持和专属合作伙伴关系，确保您在使用我们的技术时取得成功。|g' zh/index.html

# 翻译Featured Performance描述
sed -i 's|Pre‑installed OpenClaw ensures enterprise‑grade reliability, no compatibility issues, and immediate productivity for your small‑scale high‑performance computing.|预装OpenClaw确保企业级可靠性，无兼容性问题，为您的⼩规模高性能计算提供即时生产力。|g' zh/index.html
sed -i 's|A fully private AI assistant that processes sensitive data locally—no cloud dependencies, no data leaks, complete control over your AI workflows.|完全私有的AI助手，在本地处理敏感数据——无云依赖，无数据泄露，完全控制您的AI工作流程。|g' zh/index.html
sed -i 's|A secure, isolated cloud platform that scales with your needs while maintaining full data sovereignty and regulatory compliance.|安全、隔离的云平台，根据您的需求扩展，同时保持完全的数据主权和法规合规性。|g' zh/index.html

# 翻译按钮文字
sed -i 's|Learn More|了解更多|g' zh/index.html
sed -i 's|Request Demo|申请演示|g' zh/index.html
sed -i 's|Consult Solutions|咨询方案|g' zh/index.html

echo "Home页面修复完成"

# 2. 修复Products页面
echo ""
echo "2. 修复Products页面..."
echo "----------------------------------------"

# 翻译产品描述
sed -i 's|The A100 is our flagship Private AI‑Agent Appliance, engineered for enterprises that demand uncompromising performance, security, and autonomy.|A100是我们的旗舰私有AI代理设备，专为要求无妥协性能、安全性和自主性的企业而设计。|g' zh/products.html
sed -i 's|Pre‑installed with OpenClaw Enterprise, ready to deploy in minutes, not months.|预装OpenClaw企业版，准备在几分钟内部署，而不是几个月。|g' zh/products.html

# 翻译规格描述
sed -i 's|Stable Server-used System|稳定的服务器级系统|g' zh/products.html
sed -i 's|High-efficiency architecture|高效能架构|g' zh/products.html
sed -i 's|High-Speed Memory|高速内存|g' zh/products.html
sed -i 's|Network Interfaces|网络接口|g' zh/products.html
sed -i 's|Uptime Guarantee|运行时间保证|g' zh/products.html
sed -i 's|Power Consumption|功耗|g' zh/products.html
sed -i 's|Warranty Period|保修期|g' zh/products.html

# 翻译应用场景描述
sed -i 's|Real-time market monitoring and automated trading strategies with complete data privacy.|实时市场监控和自动化交易策略，具有完全的数据隐私。|g' zh/products.html
sed -i 's|AI‑powered diagnostic support, patient data analysis, and research acceleration while maintaining HIPAA/GDPR compliance.|AI驱动的诊断支持、患者数据分析和研究加速，同时保持HIPAA/GDPR合规性。|g' zh/products.html
sed -i 's|Predictive maintenance, quality control, and supply chain optimization for manufacturing operations.|制造业务的预测性维护、质量控制和供应链优化。|g' zh/products.html

echo "Products页面修复完成"

# 3. 修复About页面
echo ""
echo "3. 修复About页面..."
echo "----------------------------------------"

# 翻译Our Mission描述
sed -i 's|Enhance productivity across individuals, businesses, and organizations.|提升个人、企业和组织的生产力。|g' zh/about.html
sed -i 's|With our PAA device, you can rapidly transform workflows and significantly improve efficiency.|使用我们的PAA设备，您可以快速转变工作流程并显著提高效率。|g' zh/about.html

# 翻译Vision描述
sed -i 's|Stratronix is built on a long-term vision:|Stratronix建立在长期愿景之上：|g' zh/about.html

# 翻译步骤描述
sed -i 's|Establish the fundamental infrastructure layer for AI agents|为AI代理建立基础基础设施层|g' zh/about.html
sed -i 's|Secure market leadership in the PAA category|在PAA类别中确保市场领导地位|g' zh/about.html
sed -i 's|Methodically grow into adjacent markets and applications|有条不紊地扩展到相邻市场和应用程序|g' zh/about.html
sed -i 's|Harness foundational AI infrastructure to drive global productivity|利用基础AI基础设施推动全球生产力|g' zh/about.html

# 翻译哲学描述
sed -i 's|The name Stratronix derives from "Stratum" (layered structure) — representing our belief:|Stratronix的名称来源于"Stratum"（分层结构）——代表我们的信念：|g' zh/about.html
sed -i 's|All intelligent systems must be built from foundational layers upward.|所有智能系统都必须从基础层向上构建。|g' zh/about.html
sed -i 's|We aim to become the infrastructure layer of the AI Agent economy.|我们的目标是成为AI代理经济的基础设施层。|g' zh/about.html

# 翻译Industry Shift描述
sed -i 's|From passive models to active agents|从被动模型到主动代理|g' zh/about.html
sed -i 's|Chat-based AI (LLMs)|基于聊天的AI（大语言模型）|g' zh/about.html
sed -i 's|Passive interaction|被动交互|g' zh/about.html
sed -i 's|Limited autonomy|有限的自主性|g' zh/about.html
sed -i 's|Task-specific agents|特定任务代理|g' zh/about.html
sed -i 's|Active problem-solving|主动问题解决|g' zh/about.html
sed -i 's|Full autonomy|完全自主性|g' zh/about.html

echo "About页面修复完成"

echo ""
echo "=== 修复完成 ==="
echo "已修复："
echo "1. Home页面：Core Values和Featured Performance描述"
echo "2. Products页面：产品描述、规格标签、应用场景"
echo "3. About页面：使命、愿景、哲学、行业转变描述"
echo ""
echo "现在中文版本应该是完全正宗的中文内容。"