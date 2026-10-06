#!/usr/bin/env python3
"""Translate V2.0 English HTML pages to Simplified Chinese, preserving line counts exactly."""

import re, os

SRC_DIR = "/home/donald/文档/网站2.0-V2.0-2026-10-03/官方网站-代码"
OUT_DIR = "/home/donald/.openclaw/workspace/stratronix-website-new/zh"

TAOBAO_SHOP = "https://item.taobao.com/item.htm?abbucket=17&id=1061672053581"

# Words to keep in English (brand names, product names, technical terms)
KEEP_EN = [
    "STRATRONIX", "STA-100", "Workie", "PAA", "OpenClaw",
    "AI", "IM", "CRM", "ERP", "API", "LLM", "RAG", "RAG",
    "GB", "DDR4", "eMMC", "ARM", "CPU", "RAM", "USB", "HDMI",
    "Wi-Fi", "Linux", "Ubuntu", "XFCE", "HTML", "CSS", "JSON",
    "GPT", "Claude", "Gemini", "DeepSeek", "Mistral", "xAI",
    "Anthropic", "OpenAI", "Google", "Qwen", "Llama", "Phi",
    "Slack", "Teams", "WhatsApp", "WeChat", "Feishu", "Telegram",
    "Discord", "LINE", "KakaoTalk", "Signal", "Webex",
    "GDPR", "EU AI Act", "HIPAA", "FCC", "CE", "ISO",
    "SOC 2", "BSD", "MIT", "Apache",
    "NFT", "NFTs", "NFT's",
    "CEO", "COO", "CFO", "CTO", "SKU", "PDF", "CSV", "XLSX", "DOCX",
    "HTML", "XML", "SEO", "URL", "HTTP", "HTTPS", "FTP",
    "LAN", "WAN", "VPN", "SSH", "SSL", "TLS",
    "USB 3.0", "USB 2.0", "USB-C",
    "NVIDIA", "Intel", "AMD", "Arm",
    "Octa-core", "GHz", "GHz",
    "HDMI", "LED",
    "QR", "QR code",
    "MAC", "MAC OS",
    "Windows", "macOS",
    "Python", "JavaScript", "JS", "SDK",
    "REST", "API",
    "MCP", "MCP Server",
    "Qdrant", "Vector DB",
    "Llama 3.3 70B", "Qwen 2.5 72B",
    "MiFID II", "CNIL", "FCA",
    "Mittelstand",
    "NFT minting", "NFT collection",
]

def keep_en(word):
    """Return True if word should stay in English."""
    upper = word.upper()
    for k in KEEP_EN:
        if upper == k.upper():
            return True
    return False

def replace_price(text):
    """Replace $399 with ¥2,999 and similar price references."""
    # $399 USD → ¥2,999
    text = re.sub(r'\$399\s*USD', '¥2,999', text)
    text = re.sub(r'\$399', '¥2,999', text)
    # Other dollar amounts - only replace obvious product prices
    text = re.sub(r'\$(\d+)\s*USD', lambda m: f'¥{int(m.group(1)) * 7:,}', text)
    text = re.sub(r'\$(\d+)', lambda m: f'¥{int(m.group(1)) * 7:,}', text)
    return text

def online_shop_link(text):
    """Replace store.stratronix.ai Online Shop references with Taobao link."""
    # Replace ALL store.stratronix.ai links with Taobao
    text = re.sub(
        r'href="https://store\.stratronix\.ai"',
        f'href="{TAOBAO_SHOP}"',
        text
    )
    return text

def translate_file(filepath, outpath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result_lines = []
    for line in lines:
        text = line

        # 1. Change lang attribute
        text = re.sub(r'\blang="en(-GB)?"', 'lang="zh-CN"', text)
        text = re.sub(r"\blang='en(-GB)?'", "lang='zh-CN'", text)

        # 2. Translate text content (inline translations)
        text = translate_line(text)

        # 3. Replace Online Shop links
        text = online_shop_link(text)

        # 4. Replace $399 with ¥2,999
        text = replace_price(text)

        result_lines.append(text)

    # Verify line count
    src_lines = len(lines)
    out_lines = len(result_lines)
    print(f"  {os.path.basename(filepath)}: {src_lines} → {out_lines} lines {'✓' if src_lines == out_lines else '✗ MISMATCH'}")

    with open(outpath, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)

def translate_line(text):
    """Apply all translations to a single line of text."""
    # Navigation
    text = re.sub(r'(?<!")>Home(?!<)', '>首页', text)
    text = re.sub(r'(?<!")>About(?!<)', '>关于我们', text)
    text = re.sub(r'(?<!")>About Us(?!<)', '>关于我们', text)
    text = re.sub(r'(?<!")>Products(?!<)', '>产品', text)
    text = re.sub(r'(?<!")>AI Use(?!<)', '>AI应用', text)
    text = re.sub(r'(?<!")>News(?!<)', '>新闻', text)
    text = re.sub(r'(?<!")>Contact(?!<)', '>联系我们', text)
    text = re.sub(r'(?<!")>Contact Us(?!<)', '>联系我们', text)

    # Hero sections
    text = re.sub(r'(?<!")About STRATRONIX(?!")', '关于 STRATRONIX', text)
    text = re.sub(r'Creating the', '创造', text)
    text = re.sub(r'Personal AI Office Assistant', '个人AI办公助手', text)
    text = re.sub(r'Category', '品类', text)

    # Common UI text
    text = re.sub(r'Buy Now', '立即购买', text)
    text = re.sub(r'View Hardware Specs', '查看硬件规格', text)
    text = re.sub(r'View Specs', '查看规格', text)
    text = re.sub(r'View Product', '查看产品', text)
    text = re.sub(r'Contact Sales', '联系销售', text)
    text = re.sub(r'Enterprise Inquiry', '企业咨询', text)
    text = re.sub(r'Request Custom Dev Quote', '申请定制开发报价', text)
    text = re.sub(r'Request a Quote', '申请报价', text)

    # Section labels
    text = re.sub(r'Our Mission', '我们的使命', text)
    text = re.sub(r'Our Two Businesses', '我们的两大业务', text)
    text = re.sub(r'AI Agent Development', 'AI Agent 定制开发', text)
    text = re.sub(r'Building from the ground up', '从零开始构建', text)
    text = re.sub(r'Long-term Vision', '长期愿景', text)
    text = re.sub(r'Our Philosophy', '我们的理念', text)

    text = re.sub(r'What We Do', '我们的业务', text)
    text = re.sub(r'Two Core Businesses, One Mission', '两大核心业务，一个使命', text)
    text = re.sub(r'Hardware for individuals \+ Custom AI Agent development for enterprises', '硬件面向个人 + 定制 AI Agent 服务面向企业', text)

    # Business cards
    text = re.sub(r'Product Business', '产品业务', text)
    text = re.sub(r'Service Business', '服务业务', text)
    text = re.sub(r'STA-100 Workie Hardware', 'STA-100 Workie 硬件', text)
    text = re.sub(r'Personal AI Office Assistant · B2C \+ B2B', '个人AI办公助手 · B2C + B2B', text)
    text = re.sub(r'Custom-built AI Agent Development', '定制 AI Agent 开发', text)
    text = re.sub(r'Enterprise AI Solutions · B2B Service', '企业AI解决方案 · B2B服务', text)

    text = re.sub(r'Direct-to-customer online sales at \$399 USD \(one-time\)', '一次性购买，直达客户，¥2,999', text)
    text = re.sub(r'Pre-installed OpenClaw \+ Linux Ubuntu', '预装 OpenClaw + Linux Ubuntu', text)
    text = re.sub(r'24/7 AI agent linked to', '24/7 AI Agent 连接', text)
    text = re.sub(r'Privacy-first local processing', '隐私优先，本地处理', text)
    text = re.sub(r'Global shipping · 2-year warranty', '全球发货 · 2年质保', text)
    text = re.sub(r'View Hardware Specs →', '查看硬件规格 →', text)
    text = re.sub(r'🛒 Buy Now', '🛒 立即购买', text)

    text = re.sub(r'Industry-specific AI agents', '行业专属 AI Agents', text)
    text = re.sub(r'Integration with your internal tools and databases', '与内部工具和数据库集成', text)
    text = re.sub(r'Custom knowledge base and SOP training', '定制知识库和 SOP 培训', text)
    text = re.sub(r'Ongoing model tuning and optimization', '持续模型调优与优化', text)
    text = re.sub(r'From requirements to production in 6-8 weeks', '从需求到上线只需 6-8 周', text)
    text = re.sub(r'See Development Workflow →', '查看开发流程 →', text)

    # Vision section
    text = re.sub(r'Building from the ground up', '从零开始构建', text)
    text = re.sub(r'Stratronix is built on a long-term vision:', 'Stratronix 建立在长期愿景之上：', text)
    text = re.sub(r'Build a PAA foundation', '构建 PAA 基础设施', text)
    text = re.sub(r'Establish the fundamental infrastructure layer for AI agents', '为 AI Agents 建立基础设了一层', text)
    text = re.sub(r'Establish stronghold', '建立据点', text)
    text = re.sub(r'Secure market leadership in the PAA category', '在 PAA 品类中确立市场领先地位', text)
    text = re.sub(r'Expand systematically', '系统化扩张', text)
    text = re.sub(r'Methodically grow into adjacent markets and applications', '有条不紊地拓展相邻市场与应用', text)
    text = re.sub(r'Leverage the productivity from the bottom layer of the world', '从全球底层挖掘生产力', text)
    text = re.sub(r'Harness foundational AI infrastructure to drive global productivity', '利用基础 AI 基础设施推动全球生产力', text)

    text = re.sub(r'The name Stratronix derives from "Stratum"', 'Stratronix 这个名字源自"Stratum"（层级）', text)
    text = re.sub(r'\(layered structure\)', '（层级结构）', text)
    text = re.sub(r'representing our belief: All intelligent systems must be built from foundational layers upward\.',
                  '代表我们的信念：所有智能系统都必须从基础层向上构建。', text)
    text = re.sub(r'We aim to become the infrastructure layer of the AI Agent economy\.',
                  '我们的目标是成为 AI Agent 经济的基础设施层。', text)

    # Development workflow
    text = re.sub(r'From Idea to Production — 7 Steps', '从创意到生产 — 7个步骤', text)
    text = re.sub(r'Our proven AI Agent development workflow', '我们成熟的 AI Agent 开发流程', text)
    text = re.sub(r'Our Process', '我们的流程', text)
    text = re.sub(r'Vision & Strategy', '愿景与战略', text)

    text = re.sub(r'Step into System', '走进系统', text)
    text = re.sub(r'We start by deeply understanding your business environment, workflows, and the people who use them\. Field research, interviews, and workflow mapping\.',
                  '我们从深入了解您的业务环境、工作流程及使用者开始。实地研究、访谈与流程梳理。', text)
    text = re.sub(r'Discovery · 1 week', '发现阶段 · 1周', text)

    text = re.sub(r'Train AI', '训练 AI', text)
    text = re.sub(r'Feed the AI with your company-specific data, SOPs, product catalogs, customer profiles and historical interactions\. Build domain expertise\.',
                  '向 AI 喂入您的公司专属数据、SOP、产品目录、客户画像和历史交互数据，构建领域专业知识。', text)
    text = re.sub(r'Knowledge Base · 1-2 weeks', '知识库 · 1-2周', text)

    text = re.sub(r'Build Up Needs', '构建需求', text)
    text = re.sub(r'Translate business requirements into AI capabilities\. Define triggers, actions, escalation rules and quality thresholds for each use case\.',
                  '将业务需求转化为 AI 能力。为每个用例定义触发器、动作、升级规则和质量阈值。', text)
    text = re.sub(r'Spec Design · 1 week', '规格设计 · 1周', text)

    text = re.sub(r'Update System', '更新系统', text)
    text = re.sub(r'Build the AI Agent on the STA-100 platform with custom integrations, prompt engineering, and security guardrails\. Cloud \+ edge hybrid ready\.',
                  '在 STA-100 平台上构建 AI Agent，包含自定义集成、提示工程和安全护栏。云+边缘混合就绪。', text)
    text = re.sub(r'Build · 2-3 weeks', '构建 · 2-3周', text)

    text = re.sub(r'Test Application', '测试应用', text)
    text = re.sub(r'Rigorous testing: unit tests, scenario tests, edge cases, performance benchmarks\. Real-user pilot with feedback loops and iteration\.',
                  '严格测试：单元测试、场景测试、边缘案例、性能基准。真实用户试点并持续迭代反馈。', text)
    text = re.sub(r'QA · 1-2 weeks', '质量保证 · 1-2周', text)

    text = re.sub(r'Security', '安全加固', text)
    text = re.sub(r'Full security audit: data encryption, access control, audit logs, GDPR/data sovereignty compliance, penetration testing\.',
                  '全面安全审计：数据加密、访问控制、审计日志、GDPR/数据主权合规、渗透测试。', text)
    text = re.sub(r'Hardening · 1 week', '加固 · 1周', text)

    text = re.sub(r'Ready to Product', '准备上线', text)
    text = re.sub(r'Production deployment with monitoring dashboards, SLA tracking, knowledge base updates, and continuous improvement cycle\.',
                  '生产部署，含监控仪表板、SLA 跟踪、知识库更新和持续改进循环。', text)
    text = re.sub(r'Launch \+ Support · Ongoing', '上线 + 支持 · 持续', text)

    # Industry shift
    text = re.sub(r'Industry Shift', '行业变革', text)
    text = re.sub(r'AI 2\.0 — The Agent Era', 'AI 2.0 — Agent 时代', text)
    text = re.sub(r'AI 1\.0 — Model Era', 'AI 1.0 — 模型时代', text)
    text = re.sub(r'Chat-based AI \(LLMs\)', '基于聊天的 AI（LLM）', text)
    text = re.sub(r'Passive interaction', '被动交互', text)
    text = re.sub(r'Human-driven', '人类驱动', text)
    text = re.sub(r'Single-task focused', '单一任务', text)
    text = re.sub(r'Cloud-dependent', '依赖云端', text)
    text = re.sub(r'AI 2\.0 — Agent Era <span style="color:var\(brand\);">★ Our Focus</span>', 'AI 2.0 — Agent 时代 <span style="color:var(brand);">★ 我们的重点</span>', text)
    text = re.sub(r'Autonomous AI Agents', '自主 AI Agents', text)
    text = re.sub(r'Task execution', '任务执行', text)
    text = re.sub(r'Continuous operation', '持续运行', text)
    text = re.sub(r'System-level intelligence', '系统级智能', text)
    text = re.sub(r'Edge computing capable', '支持边缘计算', text)
    text = re.sub(r'Agents Will Become', 'Agent 将成为', text)
    text = re.sub(r'Digital employees', '数字员工', text)
    text = re.sub(r'Operational systems', '运营系统', text)
    text = re.sub(r'Decision engines', '决策引擎', text)
    text = re.sub(r'Productivity multipliers', '生产力倍增器', text)
    text = re.sub(r'Business infrastructure', '商业基础设施', text)

    # CTA sections
    text = re.sub(r"Start With a <span style=\"color:var\(brand\)\">Workie</span>, Or Build <span style=\"color:var\(brand\)\">Custom</span>",
                  "从 <span style=\"color:var(brand)\">Workie</span> 开始，或定制 <span style=\"color:var(brand)\">专属</span>", text)
    text = re.sub(r"Buy a STA-100 for \$399, or contact us for enterprise custom AI Agent development\.",
                  "购买 STA-100（¥2,999），或联系我们定制企业 AI Agent 开发。", text)

    text = re.sub(r"Ready to Power Your <span style=\"color:var\(brand\)\">AI Office</span>\?",
                  "准备好为您的 <span style=\"color:var(brand)\">AI 办公室</span> 赋能了吗？", text)
    text = re.sub(r"STA-100 Workie — <strong style=\"color:var\(brand\)\">\$399 USD</strong> one-time\. No subscription\. Free global shipping\. 2-year warranty\.",
                  "STA-100 Workie — 一次性 <strong style=\"color:var(brand)\">¥2,999</strong>，无订阅费，全球免费发货，2年质保。", text)
    text = re.sub(r"Ready to Power Your <span style=\"color:var\(brand\)\">AI Office</span>\?",
                  "准备好为您的 <span style=\"color:var(brand)\">AI 办公室</span> 赋能了吗？", text)

    text = re.sub(r"Buy Workie — \$399", "立即购买 Workie — ¥2,999", text)
    text = re.sub(r"AI Use Cases", "AI 应用场景", text)

    text = re.sub(r"Ready to Meet <span style=\"color:var\(brand\)\">Your AI Coworker</span>\?",
                  "准备好认识 <span style=\"color:var(brand)\">您的 AI 同事</span> 了吗？", text)
    text = re.sub(r"STA-100 Workie starts at <strong style=\"color:var\(brand\)\">\$399 USD</strong>\. One-time purchase\. No subscription\. Global shipping\.",
                  "STA-100 Workie 起售价 <strong style=\"color:var(brand)\">¥2,999</strong>，一次性购买，无订阅费，全球发货。", text)

    # Mission values
    text = re.sub(r'Enhance productivity across individuals, businesses, and industries\.',
                  '提升个人、企业和整个行业的生产力。', text)
    text = re.sub(r'With our PAA device, you can rapidly transform workflows and significantly improve efficiency\.',
                  '借助我们的 PAA 设备，您可以快速转型工作流程，显著提升效率。', text)
    text = re.sub(r'⚡ Accelerate Transformation', '⚡ 加速转型', text)
    text = re.sub(r'Rapidly upgrade traditional workflows to AI-powered automation',
                  '快速将传统工作流程升级为 AI 驱动的自动化', text)
    text = re.sub(r'📈 Boost Efficiency', '📈 提升效率', text)
    text = re.sub(r'Significantly improve operational efficiency across all business processes',
                  '显著提升所有业务流程的运营效率', text)
    text = re.sub(r'🚀 Empower SMB Teams and Private Ones', '🚀 赋能中小型团队和私有场景', text)
    text = re.sub(r'Enable individuals and teams to achieve more with intelligent assistance',
                  '让个人和团队通过智能辅助实现更多', text)

    # Trust foundation
    text = re.sub(r"STRATRONIX is the pioneer of PAA — Personal AI Office Assistant, creating a new category of Office AI products designed to enhance everyday productivity\. We build private AI-powered assistants and customized AI Agent solutions for individuals, businesses, and industries\.",
                  "STRATRONIX 是 PAA（个人 AI 办公助手）的先驱，创建了旨在提升日常工作效率的全新办公 AI 产品品类。我们为个人、企业和行业打造私有 AI 助手和定制 AI Agent 解决方案。", text)
    text = re.sub(r"Building the next generation of AI-powered productivity\.",
                  "构建下一代 AI 驱动的生产力。", text)

    # Footer
    text = re.sub(r'Products', '产品', text)
    text = re.sub(r'Company', '公司', text)
    text = re.sub(r'Resources', '资源', text)
    text = re.sub(r'Social', '社交', text)
    text = re.sub(r'STA-100 Workie', 'STA-100 Workie', text)
    text = re.sub(r'🛒 Online Shop', '🛒 在线商店', text)
    text = re.sub(r'Online Shop', '在线商店', text)
    text = re.sub(r'About Us', '关于我们', text)
    text = re.sub(r'Enterprise Inquiry', '企业咨询', text)
    text = re.sub(r'Custom AI Agent Dev', '定制 AI Agent 开发', text)
    text = re.sub(r'Buy STA-100', '购买 STA-100', text)
    text = re.sub(r'Stafford Contact', '联系销售', text)
    text = re.sub(r'Privacy Policy', '隐私政策', text)
    text = re.sub(r'Terms of Service', '服务条款', text)
    text = re.sub(r'All rights reserved', '保留所有权利', text)
    text = re.sub(r'Mon-Fri 9:00-18:00', '周一至周五 9:00-18:00', text)
    text = re.sub(r'Business Hours', '工作时间', text)
    text = re.sub(r'Monday – Friday: 9:00 – 18:00 \(GMT\+8\)', '周一至周五：9:00 – 18:00（北京时间）', text)
    text = re.sub(r'Weekend: Closed', '周末：休息', text)
    text = re.sub(r'Worldwide Shipping', '全球发货', text)
    text = re.sub(r'We ship to 195\+ countries\.', '我们发货至 195+ 个国家和地区。', text)
    text = re.sub(r'View shipping rates →', '查看发货费用 →', text)

    # AI Use page
    text = re.sub(r'AI Use Cases · Workie', 'AI 应用场景 · Workie', text)
    text = re.sub(r"Give Your IM an <span class=\"pink\">AI Brain</span>",
                  "为您的 IM 赋予 <span class=\"pink\">AI 大脑</span>", text)
    text = re.sub(r'STA-100 Workie is a Personal AI Office Assistant \(PAA\) that lives in your messaging apps',
                  'STA-100 Workie 是一款个人 AI 办公助手（PAA），内置于您的消息应用中', text)
    text = re.sub(r'Six Powerful Use Cases', '六大强大应用场景', text)
    text = re.sub(r'What Can Workie Do For You\?', 'Workie 能为您做什么？', text)
    text = re.sub(r'From daily content creation to complex data analysis — Workie handles the work that drains your day\.',
                  '从日常内容创作到复杂数据分析 — Workie 处理那些消耗您整天的工作。', text)

    text = re.sub(r'01', '01', text)
    text = re.sub(r'02', '02', text)
    text = re.sub(r'03', '03', text)
    text = re.sub(r'04', '04', text)
    text = re.sub(r'05', '05', text)
    text = re.sub(r'06', '06', text)

    text = re.sub(r'Personal Content Creation', '个人内容创作', text)
    text = re.sub(r'Daily Creative Output', '日常创意输出', text)
    text = re.sub(r"Drafts social posts, blog articles, emails and marketing copy in your voice\. Knows your style, audience and brand guidelines\. Ready-to-publish output in seconds\.",
                  "以您的风格起草社交帖子、博客文章、邮件和营销文案。了解您的风格、受众和品牌指南，几秒内生成可发布内容。", text)
    text = re.sub(r'Blog Writing', '博客写作', text)
    text = re.sub(r'Social Media', '社交媒体', text)
    text = re.sub(r'Email Drafts', '邮件起草', text)

    text = re.sub(r'Document Creation', '文档创建', text)
    text = re.sub(r'Proposals · Reports · Contracts', '方案 · 报告 · 合同', text)
    text = re.sub(r"Generates structured documents with proper formatting, citations and references\. Pulls from your local knowledge base to ensure consistency across all deliverables\.",
                  "生成格式规范、引用完整的结构化文档。从本地知识库提取信息，确保所有交付物的一致性。", text)
    text = re.sub(r'Proposals', '商业方案', text)
    text = re.sub(r'Reports', '报告', text)
    text = re.sub(r'Contracts', '合同', text)

    text = re.sub(r'Daily Office Job', '日常办公', text)
    text = re.sub(r'24/7 Coworker Support', '24/7 同事支持', text)
    text = re.sub(r"Schedules meetings, manages inbox, tracks tasks, summarizes long documents, drafts responses\. Always on, always ready — like having a personal assistant that never sleeps\.",
                  "安排会议、管理收件箱、跟踪任务、摘要长文档、起草回复。随时在线、随时就绪 — 就像拥有一个永不疲倦的私人助理。", text)
    text = re.sub(r'Calendar', '日历', text)
    text = re.sub(r'Inbox', '收件箱', text)
    text = re.sub(r'Summaries', '摘要', text)

    text = re.sub(r'Data Analysis & Research', '数据分析与研究', text)
    text = re.sub(r'From Raw Data to Insights', '从原始数据到洞察', text)
    text = re.sub(r"Reads CSV/Excel files, runs analysis, generates charts and produces executive summaries\. Searches the web for market research and competitive intelligence on demand\.",
                  "读取 CSV/Excel 文件、执行分析、生成图表并制作高管摘要。按需搜索网络进行市场研究和竞品情报。", text)
    text = re.sub(r'Excel/CSV', 'Excel/CSV', text)
    text = re.sub(r'Charts', '图表', text)
    text = re.sub(r'Research', '研究', text)

    text = re.sub(r'24/7 AI Customer Service', '24/7 AI 客服', text)
    text = re.sub(r'E-commerce Ready', '电商适用', text)
    text = re.sub(r"Responds to customer inquiries, processes orders, tracks shipments and handles returns\. Multi-language support for global businesses\. Never misses a customer message\.",
                  "回复客户咨询、处理订单、追踪发货并处理退货。面向全球企业的多语言支持，绝不遗漏任何客户消息。", text)
    text = re.sub(r'E-commerce', '电商', text)
    text = re.sub(r'Multi-lang', '多语言', text)
    text = re.sub(r'Auto Reply', '自动回复', text)

    text = re.sub(r'Sales & Marketing Automation', '销售与营销自动化', text)
    text = re.sub(r'Pipeline & Content Engine', '管线与内容引擎', text)
    text = re.sub(r"Tracks sales pipeline, drafts outreach messages, monitors competitor activity, generates lead reports\. Works alongside your CRM to keep deals moving\.",
                  "跟踪销售管线、起草外展消息、监控竞品动态、生成线索报告。与您的 CRM 协同推动交易进展。", text)
    text = re.sub(r'Pipeline', '管线', text)
    text = re.sub(r'Outreach', '外展', text)
    text = re.sub(r'CRM Sync', 'CRM 同步', text)

    # IM connections
    text = re.sub(r'Global IM Support', '全球 IM 支持', text)
    text = re.sub(r"Empower your team IMs with AI Brain",
                  "用 AI 大脑赋能团队 IM", text)
    text = re.sub(r'STA-100 Workie connects to every messaging platform your team already uses',
                  'STA-100 Workie 连接团队已使用的所有消息平台', text)
    text = re.sub(r'North America', '北美', text)
    text = re.sub(r'Europe', '欧洲', text)
    text = re.sub(r'APAC', '亚太', text)
    text = re.sub(r'Global', '全球', text)

    # Office roles
    text = re.sub(r'Office Roles', '办公角色', text)
    text = re.sub(r'Powering Multiple Roles in Office as One Productivity Tool',
                  '一个生产力工具，赋能办公室多重角色', text)
    text = re.sub(r'STA-100 Workie adapts to every team function — one AI agent, endless workflows',
                  'STA-100 Workie 适配每个团队职能 — 一个 AI Agent，无限工作流', text)
    text = re.sub(r'Sales', '销售', text)
    text = re.sub(r'Marketing', '市场', text)
    text = re.sub(r'Legal', '法务', text)
    text = re.sub(r'Finance / Stock', '金融/股票', text)
    text = re.sub(r'Administration', '行政', text)
    text = re.sub(r'E-commerce', '电商', text)
    text = re.sub(r'Human Resources', '人力资源', text)
    text = re.sub(r'Operations', '运营', text)
    text = re.sub(r'Finance', '财务', text)

    text = re.sub(r'Lead generation · Pipeline · CRM sync · Outreach', '线索生成 · 管线 · CRM 同步 · 外展', text)
    text = re.sub(r'Content · Social media · Campaigns · Reports', '内容 · 社交媒体 · 活动 · 报告', text)
    text = re.sub(r'Contract review · Compliance · Policy docs', '合同审核 · 合规 · 政策文档', text)
    text = re.sub(r'Financial reports · Market data · Investment analysis', '财务报告 · 市场数据 · 投资分析', text)
    text = re.sub(r'Schedule · Inbox · Travel booking · Summaries', '日程 · 收件箱 · 差旅预订 · 摘要', text)
    text = re.sub(r'Product listing · Customer service · Inventory', '商品上架 · 客服 · 库存', text)
    text = re.sub(r'Resume screening · Onboarding · Training', '简历筛选 · 入职 · 培训', text)
    text = re.sub(r'Process automation · Task tracking · Workflows', '流程自动化 · 任务跟踪 · 工作流', text)

    # AI Agent ≠ Chatbot
    text = re.sub(r'Key Difference', '关键区别', text)
    text = re.sub(r'AI Agent ≠ Chatbot', 'AI Agent ≠ 聊天机器人', text)
    text = re.sub(r"Workie is a real digital coworker, not just a chatbot",
                  "Workie 是真正的数字同事，不只是聊天机器人", text)
    text = re.sub(r'Traditional Chatbot', '传统聊天机器人', text)
    text = re.sub(r'Chat Only', '仅聊天', text)
    text = re.sub(r'Responds to one message at a time', '一次只回复一条消息', text)
    text = re.sub(r'No memory across sessions', '跨会话无记忆', text)
    text = re.sub(r'No access to your files or data', '无法访问您的文件或数据', text)
    text = re.sub(r"Can't execute tasks autonomously", '无法自主执行任务', text)
    text = re.sub(r'Requires constant human guidance', '需要持续人工指导', text)
    text = re.sub(r'Data goes to external cloud servers', '数据发送到外部云服务器', text)
    text = re.sub(r'Workie AI Agent', 'Workie AI Agent', text)
    text = re.sub(r'AI Agent', 'AI Agent', text)
    text = re.sub(r'Works continuously 24/7 in background', '后台持续 24/7 运行', text)
    text = re.sub(r'Remembers everything, learns from context', '记住一切，从上下文学习', text)
    text = re.sub(r'Full access to your files, email, calendar', '完全访问您的文件、邮件和日历', text)
    text = re.sub(r'Executes tasks autonomously on command', '按指令自主执行任务', text)
    text = re.sub(r'Handles repetitive work automatically', '自动处理重复性工作', text)
    text = re.sub(r'All data stays local, never leaves device', '所有数据留在本地，绝不离开设备', text)

    # Products page
    text = re.sub(r'STA-100 Workie · Hardware', 'STA-100 Workie · 硬件', text)
    text = re.sub(r"The <span class=\"pink\">Hardware</span> That Powers Your AI Office",
                  "为您的 AI 办公室提供动力的 <span class=\"pink\">硬件</span>", text)
    text = re.sub(r"Workie is a dedicated AI agent that runs 24/7 on the STA-100 hardware, connected to your favorite messaging apps\. Unlike cloud-based chatbots, Workie lives in your local network — your data will stay in your device and become your permanent data asset\.",
                  "Workie 是一款专用 AI Agent，在 STA-100 硬件上 24/7 运行，连接您喜爱的消息应用。与基于云的聊天机器人不同，Workie 生活在您的本地网络中 — 您的数据将保留在设备中，成为您的永久数据资产。", text)
    text = re.sub(r"Works inside", "支持", text)
    text = re.sub(r"No app download — just message it like a colleague", "无需下载 App，像同事一样发消息即可", text)
    text = re.sub(r"Cloud API Keys from Multi-LLM:", "多 LLM 云端 API Key：", text)
    text = re.sub(r"Local memory — remembers your projects and preferences", "本地记忆 — 记住您的项目和偏好", text)
    text = re.sub(r"Full system access: email, calendar, files, terminal", "完整系统访问：邮件、日历、文件、终端", text)
    text = re.sub(r"GDPR & data sovereignty compliant", "符合 GDPR 和数据主权要求", text)

    text = re.sub(r'Full Specifications', '完整规格', text)
    text = re.sub(r'Engineered for AI Workloads', '为 AI 工作负载而生', text)
    text = re.sub(r'Built on proven enterprise hardware standards with 6-layer PCBA', '基于成熟的企业硬件标准，6层 PCBA 设计', text)
    text = re.sub(r'Processor & Memory', '处理器与内存', text)
    text = re.sub(r'Power & Thermal', '电源与散热', text)
    text = re.sub(r'Agent and Size', 'Agent 与尺寸', text)
    text = re.sub(r'Connectivity', '连接性', text)

    text = re.sub(r'CPU', 'CPU', text)
    text = re.sub(r'RAM', '内存', text)
    text = re.sub(r'Storage \(Built-in\)', '存储（内置）', text)
    text = re.sub(r'Storage Expansion', '存储扩展', text)
    text = re.sub(r'Up to 512GB \(Extended micro SD slot\)', '最高 512GB（扩展 micro SD 卡槽）', text)
    text = re.sub(r'Power Consumption', '功耗', text)
    text = re.sub(r'Power Supply', '电源适配器', text)
    text = re.sub(r'Thermal Design', '散热设计', text)
    text = re.sub(r'PCB Layers', 'PCB 层数', text)
    text = re.sub(r'Built-in Agent', '内置 Agent', text)
    text = re.sub(r'Dimensions', '尺寸', text)
    text = re.sub(r'Weight', '重量', text)
    text = re.sub(r'OS Pre-installed', '预装操作系统', text)
    text = re.sub(r'GUI', '图形界面', text)
    text = re.sub(r'Wi-Fi', 'Wi-Fi', text)
    text = re.sub(r'Ethernet', '以太网', text)
    text = re.sub(r'Video Output', '视频输出', text)
    text = re.sub(r'Card Slot', '卡槽', text)

    text = re.sub(r'10 Core Features', '10 大核心功能', text)
    text = re.sub(r'Why STA-100\?', '为什么选 STA-100？', text)
    text = re.sub(r'Ten pillars of the Personal AI Office Assistant', '个人 AI 办公助手的十大支柱', text)
    text = re.sub(r'Local Data', '本地数据', text)
    text = re.sub(r'Permanent Data Asset', '永久数据资产', text)
    text = re.sub(r'One-Click Startup', '一键启动', text)
    text = re.sub(r'OpenClaw Security', 'OpenClaw 安全', text)
    text = re.sub(r'24/7 Always Online', '24/7 永远在线', text)
    text = re.sub(r'AI Core', 'AI 核心', text)
    text = re.sub(r'4GB DDR4 \+ 32GB', '4GB DDR4 + 32GB', text)
    text = re.sub(r'Wi-Fi \+ GbE', 'Wi-Fi + 千兆以太网', text)
    text = re.sub(r'Multi-LLM API Key', '多 LLM API Key', text)
    text = re.sub(r'Slack/Teams/Whatsapp etc\.', 'Slack/Teams/WhatsApp 等', text)

    text = re.sub(r'Product Gallery', '产品图库', text)
    text = re.sub(r'Every Angle, Every Detail', '每个角度，每个细节', text)
    text = re.sub(r'Front View', '正面视图', text)
    text = re.sub(r'Side View', '侧面视图', text)
    text = re.sub(r'Ports Detail', '接口详情', text)
    text = re.sub(r'Desktop Setup', '桌面配置', text)
    text = re.sub(r'5-Angle Views', '五视角', text)

    text = re.sub(r'Built Different', '与众不同', text)
    text = re.sub(r'Enterprise-Grade <span class="pink">Hardware Standards</span>',
                  '企业级 <span class="pink">硬件标准</span>', text)
    text = re.sub(r'<strong>6-Layer PCBA</strong> — Superior signal integrity and anti-electromagnetic interference',
                  '<strong>6层 PCBA</strong> — 卓越的信号完整性和抗电磁干扰', text)
    text = re.sub(r'<strong>OpenClaw Pre-installed</strong> — Out-of-box AI, no OS installation needed',
                  '<strong>预装 OpenClaw</strong> — 开箱即用 AI，无需安装操作系统', text)
    text = re.sub(r'<strong>XFCE GUI OS</strong> — Lightweight Linux desktop, familiar and easy to use',
                  '<strong>XFCE 图形界面 OS</strong> — 轻量级 Linux 桌面，熟悉易用', text)
    text = re.sub(r'<strong>Multi-LLM API Key</strong> — Anthropic, OpenAI, Google, Mistral, xAI, DeepSeek',
                  '<strong>多 LLM API Key</strong> — Anthropic、OpenAI、Google、Mistral、xAI、DeepSeek', text)
    text = re.sub(r'<strong>All Major IMs</strong> — WhatsApp, Telegram, Discord, Slack, WeChat, Feishu',
                  '<strong>支持所有主流 IM</strong> — WhatsApp、Telegram、Discord、Slack、WeChat、Feishu', text)

    text = re.sub(r'Package Contents', '包装内容', text)
    text = re.sub(r'Everything You Need in the Box', '包装内含您所需一切', text)
    text = re.sub(r'Main Unit', '主机', text)
    text = re.sub(r'Video Output', '视频输出', text)
    text = re.sub(r'8-10-min setup manual', '8-10分钟设置手册', text)

    # Contact page
    text = re.sub(r'Contact Us', '联系我们', text)
    text = re.sub(r"Let's Talk <span class=\"pink\">PAA</span>", "聊聊 <span class=\"pink\">PAA</span>", text)
    text = re.sub(r"Whether you're interested in the STA-100 Workie, looking for enterprise solutions, or have questions about custom AI Agent development — we're here to help\.",
                  "无论您对 STA-100 Workie 感兴趣、寻求企业解决方案，还是有定制 AI Agent 开发的问题 — 我们随时为您服务。", text)
    text = re.sub(r'Email', '邮箱', text)
    text = re.sub(r'For product inquiries, quotes, and general questions', '产品咨询、报价及一般问题', text)
    text = re.sub(r'WeChat / WhatsApp', '微信 / WhatsApp', text)
    text = re.sub(r'Scan the QR code or add:', '扫描二维码或添加：', text)
    text = re.sub(r'Office Address', '办公地址', text)
    text = re.sub(r'Send us a message', '发送消息', text)
    text = re.sub(r'First Name \*', '名 *', text)
    text = re.sub(r'Last Name \*', '姓 *', text)
    text = re.sub(r'Email \*', '邮箱 *', text)
    text = re.sub(r'Company', '公司', text)
    text = re.sub(r'Your company name', '您的公司名称', text)
    text = re.sub(r'Inquiry Type', '咨询类型', text)
    text = re.sub(r'Product Inquiry', '产品咨询', text)
    text = re.sub(r'Enterprise Solution', '企业解决方案', text)
    text = re.sub(r'Custom AI Agent Development', '定制 AI Agent 开发', text)
    text = re.sub(r'Technical Support', '技术支持', text)
    text = re.sub(r'Partnership', '商务合作', text)
    text = re.sub(r'Media / Press', '媒体/新闻', text)
    text = re.sub(r'Other', '其他', text)
    text = re.sub(r'Message \*', '留言 *', text)
    text = re.sub(r'Tell us about your project or question\.{3,}', '请告诉我们您的项目或问题……', text)
    text = re.sub(r'Send Message', '发送消息', text)
    text = re.sub(r'Find Us in <span style="color: var\(brand\);">Shenzhen</span>', '我们在 <span style="color: var(brand);">深圳</span> 等您', text)

    # News page
    text = re.sub(r'News & Updates', '新闻与动态', text)
    text = re.sub(r'Stay Ahead in the <span class="pink">PAA World</span>', '走在 <span class="pink">PAA 世界</span>的前沿', text)
    text = re.sub(r'Product launches, exhibition recaps, category insights, and company milestones from STRATRONIX\.',
                  '来自 STRATRONIX 的产品发布、展会回顾、品类洞察和公司里程碑。', text)

    text = re.sub(r'<span class="tag exhibition">Exhibition</span>', '<span class="tag exhibition">展会</span>', text)
    text = re.sub(r'STRATRONIX at IOTE 2026 — Booth 12B62-1, Shenzhen', 'STRATRONIX 亮相 IOTE 2026 — 深圳 12B62-1 展位', text)
    text = re.sub(r'We exhibited the STA-100 Workie at the 25th International Internet of Things Exhibition in Shenzhen\. Hundreds of visitors experienced live how Workie answers questions in WeChat, drafts reports in Feishu, and runs 24/7 on a 5-watt device\.',
                  '我们在深圳第25届国际物联网展上展出了 STA-100 Workie。数百位参观者现场体验了 Workie 在微信中回答问题、在飞书中起草报告、以5瓦功耗 24/7 运行的演示。', text)
    text = re.sub(r'📍 Shenzhen Convention & Exhibition Center → Read recap', '📍 深圳国际会展中心 → 阅读回顾', text)

    text = re.sub(r'<span class="tag product">Product Launch</span>', '<span class="tag product">产品发布</span>', text)
    text = re.sub(r'STRATRONIX Launches First Lightweight Private AI Agent Device - STA-100', 'STRATRONIX 推出首款轻量级私有 AI Agent 设备 — STA-100', text)
    text = re.sub(r"We're excited to announce that STRATRONIX's first lightweight Private AI Agent device STA-100 has entered final testing and is about to launch officially!",
                  "我们激动地宣布，STRATRONIX 首款轻量级私有 AI Agent 设备 STA-100 已进入最终测试阶段，即将正式发布！", text)
    text = re.sub(r"Key Features:", "核心特点：", text)
    text = re.sub(r"🖥️ XFCE Stable OS — Lightweight Linux desktop, server-grade stability", "🖥️ XFCE 稳定 OS — 轻量级 Linux 桌面，服务器级稳定性", text)
    text = re.sub(r"⚡ Octa-core ARM — Ultra-low power, only ~15 kWh/month running 24/7", "⚡ 八核 ARM — 超低功耗，24/7 运行仅约 15 千瓦时/月", text)
    text = re.sub(r"🔧 Built-in OpenClaw Framework — Out-of-the-box AI Agent runtime", "🔧 内置 OpenClaw 框架 — 开箱即用的 AI Agent 运行时", text)
    text = re.sub(r"🚀 Easy Deployment — 20 minutes to complete, no IT specialist needed", "🚀 轻松部署 — 20分钟完成，无需 IT 专业人员", text)
    text = re.sub(r"🏠 Wide Range of Applications — Education, healthcare, retail, home assistant", "🏠 应用广泛 — 教育、医疗、零售、家庭助手", text)
    text = re.sub(r"STA-100 is a private AI Agent device for individuals and small businesses\. All data stored locally, no cloud dependency, complete privacy and control\. Compact desktop form factor — just connect to any monitor and go\.",
                  "STA-100 是一款面向个人和小型企业的私有 AI Agent 设备。所有数据本地存储，无需依赖云端，隐私和控制权完全由您掌握。紧凑的桌面外形 — 只需连接任意显示器即可使用。", text)
    text = re.sub(r'🚀 Online shop now open → View product', '🚀 网上商店已开业 → 查看产品', text)

    text = re.sub(r'<span class="tag category">Category</span>', '<span class="tag category">品类</span>', text)
    text = re.sub(r'STRATRONIX Defines the PAA Category — Personal AI Office Assistant', 'STRATRONIX 定义 PAA 品类 — 个人 AI 办公助手', text)
    text = re.sub(r"We're announcing a new product category: the PAA — Personal AI Office Assistant\. Unlike chatbots or mini PCs, PAA devices are local-first, always-on, and native to your existing messaging apps\. They give IM an AI brain\.",
                  "我们宣布一个新 product 品类：PAA — 个人 AI 办公助手。与聊天机器人或迷你 PC 不同，PAA 设备以本地为先、永远在线、原生集成于您现有的消息应用中。它们为 IM 赋予 AI 大脑。", text)
    text = re.sub(r'📖 Category definition → Read announcement', '📖 品类定义 → 阅读公告', text)

    # Newsletter
    text = re.sub(r'Stay Updated', '保持更新', text)
    text = re.sub(r'Get <span class="pink">STRATRONIX</span> in Your Inbox', '在您的收件箱中获取 <span class="pink">STRATRONIX</span> 动态', text)
    text = re.sub(r'Product launches, AI Agent case studies, and category insights\. No spam — one email per month, unsubscribe anytime\.',
                  '产品发布、AI Agent 案例研究和品类洞察。无垃圾邮件 — 每月一封，随时退订。', text)
    text = re.sub(r'your\.email@company\.com', 'your.email@company.com', text)
    text = re.sub(r'Subscribe', '订阅', text)

    # sta100-buy page
    text = re.sub(r'STA-100 Workie – Plug-in Private AI Agent', 'STA-100 Workie – 插电式私有 AI Agent', text)
    text = re.sub(r'⚡ 15W/Month', '⚡ 15W/月', text)
    text = re.sub(r'🌐 24/7 Always Online', '🌐 24/7 永远在线', text)
    text = re.sub(r'⏱️ 8-10 min Setup', '⏱️ 8-10 分钟设置', text)
    text = re.sub(r'Plug-in Private AI Agent\. No Cloud\. No Subscription\. No Compromises\.',
                  '插电式私有 AI Agent。无云。无订阅。不妥协。', text)
    text = re.sub(r'\$399 <small>USD</small>', '¥2,999 <small>CNY</small>', text)
    text = re.sub(r'Buy Now — \$399 USD', '立即购买 — ¥2,999', text)

    text = re.sub(r'Why Choose', '为什么选择', text)
    text = re.sub(r'Everything You Need\.<br>Nothing You Don\'t\.', '您需要的一切。<br>您不需要的，都没有。', text)
    text = re.sub(r'Built for professionals who need real AI capability without surrendering their data to the cloud\.',
                  '为需要真正 AI 能力而不必将数据交给云端的专业人士打造。', text)
    text = re.sub(r'100% Private', '100% 私有', text)
    text = re.sub(r'All data stays on your device\. No cloud, no tracking, no leaks\. Your work is yours alone\.',
                  '所有数据保留在您的设备上。无云、无追踪、无泄露。您的作品只属于您。', text)
    text = re.sub(r'OpenClaw Ready', 'OpenClaw 就绪', text)
    text = re.sub(r'Pre-installed with OpenClaw AI Agent\. Just plug in and start\. No setup nightmares\.',
                  '预装 OpenClaw AI Agent。插上电源即可开始，无噩梦级配置。', text)
    text = re.sub(r'Worldwide Shipping', '全球发货', text)
    text = re.sub(r'195 countries supported\. Ships in 1-3 business days from Shenzhen\.',
                  '支持 195 个国家和地区。从深圳发货，1-3 个工作日。', text)
    text = re.sub(r'2-Year Warranty', '2年质保', text)
    text = re.sub(r'Full hardware warranty plus lifetime software updates\. We stand behind our hardware\.',
                  '全面硬件质保加终身软件更新。我们为硬件提供保障。', text)
    text = re.sub(r'Built For Real Work', '为真实工作而建', text)
    text = re.sub(r'One appliance, every workflow — from home office to industrial edge\. Versatile by design\.',
                  '一台设备，胜任所有工作流 — 从家庭办公室到工业边缘，按需设计，多才多艺。', text)

    text = re.sub(r'Use Cases', '应用场景', text)
    text = re.sub(r'Powering Professionals<br>Across Every Industry', '为各行业<br>专业人士赋能', text)
    text = re.sub(r'STA-100 adapts to your workflow\. Deploy once, use forever — on your desk, in the field, or at the edge\.',
                  'STA-100 适配您的工作流。部署一次，使用终身 — 在您的桌上、在现场、或在边缘。', text)

    text = re.sub(r'Home Office', '家庭办公室', text)
    text = re.sub(r'Run AI assistants, summarize documents, draft emails, schedule meetings — all on your desk, with zero cloud dependency\. Your family\'s conversations never leave the house\.',
                  '运行 AI 助手、摘要文档、起草邮件、安排会议 — 全部在您的桌上完成，零云依赖。家人的对话绝不离开家门。', text)
    text = re.sub(r'Small Business', '小型企业', text)
    text = re.sub(r'Customer support AI, document automation, internal knowledge base\. 1 device / 1 agent dedicated to your workflow\. No SaaS subscription lock-in\.',
                  '客服 AI、文档自动化、内部知识库。1台设备 / 1个 Agent 专注您的工作流。无 SaaS 订阅锁定。', text)
    text = re.sub(r'Legal & Healthcare', '法律与医疗', text)
    text = re.sub(r'HIPAA / GDPR / attorney-client privilege compliance\. Process sensitive documents on-device\. No third-party AI access to client data\. Pass any compliance audit\.',
                  '符合 HIPAA / GDPR / 律师-客户特权。设备端处理敏感文档。无第三方 AI 访问客户数据。通过任何合规审计。', text)
    text = re.sub(r'Research & Education', '研究与教育', text)
    text = re.sub(r'Local LLM inference, dataset analysis, paper drafting\. No per-token API fees\. Pair with API endpoints for larger models on demand\.',
                  '本地 LLM 推理、数据集分析、论文起草。无按 token 计费的 API 费用。可按需配合 API 端点使用更大模型。', text)
    text = re.sub(r'Industrial & Edge', '工业与边缘', text)
    text = re.sub(r'Pair with 4G LTE \+ GPS modules for remote sites, vehicles, factories\. Works without internet\. Industrial temperature range supported\.',
                  '配合 4G LTE + GPS 模块用于偏远场地、车辆、工厂。无互联网也能工作。支持工业级温度范围。', text)
    text = re.sub(r'Developers', '开发者', text)
    text = re.sub(r'NO\. It runs by connecting to Cloud API Keys\.', '不运行本地 LLM。通过连接云端 API Key 运行。', text)

    text = re.sub(r'Hardware Specs', '硬件规格', text)
    text = re.sub(r'Built Hardware\.<br>Real Performance\.', '真正硬件。<br>真实性能。', text)
    text = re.sub(r'Purpose-built for 24/7 AI workloads — not repurposed consumer hardware\.',
                  '为 24/7 AI 工作负载专门打造 — 不是改装消费级硬件。', text)
    text = re.sub(r'Processor', '处理器', text)
    text = re.sub(r'8-core ARM Cortex', '8核 ARM Cortex', text)
    text = re.sub(r'4 GB DDR4', '4 GB DDR4', text)
    text = re.sub(r'Storage', '存储', text)
    text = re.sub(r'32 GB eMMC \(expandable to 16TB\)', '32 GB eMMC（可扩展至 16TB）', text)
    text = re.sub(r'Power', '电源', text)
    text = re.sub(r'15W/Month', '15W/月', text)
    text = re.sub(r'Connectivity', '连接性', text)
    text = re.sub(r'Gigabit Ethernet \+ 5G WiFi', '千兆以太网 + 5G WiFi', text)
    text = re.sub(r'Display', '显示屏', text)
    text = re.sub(r'3\.5" Touch Screen', '3.5" 触摸屏', text)
    text = re.sub(r'OS', '操作系统', text)
    text = re.sub(r'OpenClaw Pre-installed', '预装 OpenClaw', text)

    text = re.sub(r'In The Box', '包装内容', text)
    text = re.sub(r'Everything You Need<br>to Get Started', '开始使用<br>所需的一切', text)
    text = re.sub(r'Unbox, plug in, and start working in under 10 minutes\. No tools required\.',
                  '开箱、插电、10分钟内开始工作。无需工具。', text)
    text = re.sub(r'STA-100 Device', 'STA-100 主机', text)
    text = re.sub(r'Power Adapter', '电源适配器', text)
    text = re.sub(r'Ethernet Cable', '网线', text)
    text = re.sub(r'Quick Start Guide', '快速入门指南', text)
    text = re.sub(r'2-Year Warranty Card', '2年质保卡', text)

    text = re.sub(r'Compare', '对比', text)
    text = re.sub(r'One Product\.<br>Zero Compromises\.', '一款产品。<br>零妥协。', text)
    text = re.sub(r'Simple, honest pricing\. No hidden fees, no usage limits, no subscriptions\.',
                  '简单诚实的定价。无隐藏费用，无使用限制，无订阅。', text)
    text = re.sub(r'Price', '价格', text)
    text = re.sub(r'\$399 USD', '¥2,999', text)
    text = re.sub(r'Storage', '存储', text)
    text = re.sub(r'32 GB \(up to 16TB\)', '32 GB（最高 16TB）', text)
    text = re.sub(r'Concurrent AI Agents', '并发 AI Agents', text)
    text = re.sub(r'1 Device / 1 Agent', '1台设备 / 1个 Agent', text)
    text = re.sub(r'Best For', '最适合', text)
    text = re.sub(r'Privacy-sensitive professionals, home office, SMEs, developers',
                  '注重隐私的专业人士、家庭办公室、中小企业、开发者', text)

    text = re.sub(r'Testimonials', '用户评价', text)
    text = re.sub(r'Trusted by Professionals<br>Worldwide', '全球专业人士<br>信赖之选', text)
    text = re.sub(r'Real users\. Real results\. Real privacy\.', '真实用户。真实结果。真实隐私。', text)

    text = re.sub(r'"Set it up in 10 minutes\. Replaced three SaaS subscriptions\. The fact that nothing leaves my office network is the real killer feature\."',
                  '"10分钟完成设置。取代了三个 SaaS 订阅。真正杀手级功能是——没有任何东西离开我的办公室网络。"', text)
    text = re.sub(r'IT Consultant, United States', 'IT 顾问，美国', text)
    text = re.sub(r'"Cloud AI was a non-starter due to HIPAA\. The STA-100 on our desk let us deploy GPT-level assistants with full compliance\."',
                  '"由于 HIPAA，云端 AI 完全不可行。桌上的 STA-100 让我们能够以完全合规的方式部署 GPT 级助手。"', text)
    text = re.sub(r'Clinic Director, Canada', '诊所主任，加拿大', text)
    text = re.sub(r'"PAA Standard replaced our document review SaaS\. Paid for itself in the first month\. OpenClaw agents handle intake 24/7\."',
                  '"PAA 标准版取代了我们的文档审核 SaaS。第一个月就收回成本。OpenClaw Agents 24/7 处理接待工作。"', text)
    text = re.sub(r'Attorney, United Kingdom', '律师，英国', text)

    text = re.sub(r'FAQ', '常见问题', text)
    text = re.sub(r'Questions\?<br>We\'ve Got Answers\.', '有问题？<br>我们有答案。', text)
    text = re.sub(r'What is OpenClaw and why is it pre-installed\?', '什么是 OpenClaw，为什么预装？', text)
    text = re.sub(r'OpenClaw is a private AI agent appliance platform\. It\'s pre-installed so the device works the moment you plug it in — no software installation, no configuration required\. You get a fully operational AI agent on your network, under your control\.',
                  'OpenClaw 是一个私有 AI Agent 设备平台。预装是为了让您插上电源的那一刻设备就能工作 — 无需安装软件，无需配置。您得到的是一个完全可运行、完全由您控制的网络 AI Agent。', text)
    text = re.sub(r'Does STA-100 work without internet\?', 'STA-100 在没有互联网的情况下能工作吗？', text)
    text = re.sub(r'Yes\. STA-100 runs entirely on-device\. It can function fully offline\. Internet is only needed for initial setup and optional cloud model API access if you choose to use external LLM providers\.',
                  '可以。STA-100 完全在设备上运行。它可以完全离线工作。互联网仅在初始设置时需要，如果您选择使用外部 LLM 提供商，也可以通过 API 访问。', text)
    text = re.sub(r'Can I run my own LLMs \(Llama, Mistral, etc\.\)\?', '我可以运行自己的 LLM（Llama、Mistral 等）吗？', text)
    text = re.sub(r'Absolutely\. STA-100 supports local LLM inference via OpenClaw\. You can run Llama, Mistral, Phi, and other open-weight models directly on the device without any cloud dependency\.',
                  '完全可以。STA-100 通过 OpenClaw 支持本地 LLM 推理。您可以直接在设备上运行 Llama、Mistral、Phi 等开源模型，完全无需依赖云端。', text)
    text = re.sub(r'How is this different from ChatGPT\?', '这和 ChatGPT 有什么不同？', text)
    text = re.sub(r'ChatGPT sends your data to OpenAI\'s servers\. STA-100 keeps all data on your local network\. No subscription fees, no data harvesting, no rate limits, no internet required\. You own the hardware, you own the AI\.',
                  'ChatGPT 将您的数据发送到 OpenAI 的服务器。STA-100 将所有数据保留在您的本地网络上。无订阅费、无数据采集、无速率限制、无需互联网。您拥有硬件，您拥有 AI。', text)
    text = re.sub(r'What about support and warranty\?', '支持和质保呢？', text)
    text = re.sub(r'Every STA-100 comes with a 2-year full hardware warranty and lifetime software updates\. Support is available via email at info@stratronix\.ai during Mon-Fri 9:00-18:00 CST\.',
                  '每台 STA-100 均配备 2 年全面硬件质保和终身软件更新。周一至周五 9:00-18:00（北京时间）可通过 info@stratronix.ai 获得支持。', text)
    text = re.sub(r'Do you ship to my country\?', '你们发货到我的国家吗？', text)
    text = re.sub(r'We ship to 195 countries worldwide via standard international carriers\. Most orders ship within 1-3 business days from our Shenzhen warehouse\. Shipping costs and delivery times vary by destination\.',
                  '我们通过标准国际承运人向全球 195 个国家和地区发货。大多数订单从深圳仓库在 1-3 个工作日内发货。运费和交付时间因目的地而异。', text)
    text = re.sub(r'Can I return it if it doesn\'t work for me\?', '如果不适合我能退货吗？', text)
    text = re.sub(r'Yes\. We offer a 30-day return policy for undamaged devices in original packaging\. Contact info@stratronix\.ai to initiate a return\. Return shipping costs are the buyer\'s responsibility unless the device is defective\.',
                  '可以。我们为包装完整且未损坏的设备提供 30 天退货政策。请联系 info@stratronix.ai 发起退货。除设备有缺陷外，退回运费由买方承担。', text)
    text = re.sub(r'Is bulk/enterprise pricing available\?', '有批量/企业定价吗？', text)
    text = re.sub(r'Yes\. We offer volume discounts for enterprise and bulk orders \(5\+ units\)\. Contact our sales team at info@stratronix\.ai for a custom quote tailored to your organization\'s needs\.',
                  '有。我们为企业和批量订单（5台以上）提供批量折扣。请联系我们的销售团队 info@stratronix.ai 获取根据您组织需求定制的报价。', text)

    text = re.sub(r'Get Started Today', '今日开始', text)
    text = re.sub(r'Ready to meet your<br>AI coworker\?', '准备好认识您的<br>AI 同事了吗？', text)
    text = re.sub(r"Stop paying monthly for AI that sells your data\. One device\. One-time price\. Lifetime ownership\.",
                  "停止为出卖您数据的 AI 每月付费。一台设备，一次性价格，终身拥有。", text)
    text = re.sub(r'USD — One-time purchase\. No subscription\. Global shipping\.', 'CNY — 一次性购买，无订阅费，全球发货。', text)

    # 404
    text = re.sub(r'Page Not Found \(404\) \| STRATRONIX Private AI', '页面未找到（404）| STRATRONIX 私有 AI', text)
    text = re.sub(r'Page Not Found', '页面未找到', text)
    text = re.sub(r"The page you're looking for doesn't exist or has been moved\.", "您查找的页面不存在或已移动。", text)
    text = re.sub(r"Let me help you find what you need\.", "让我帮您找到所需内容。", text)
    text = re.sub(r'Back to Home', '返回首页', text)
    text = re.sub(r'Browse Products', '浏览产品', text)
    text = re.sub(r'Contact Us', '联系我们', text)
    text = re.sub(r'Popular Pages', '热门页面', text)
    text = re.sub(r'Latest News', '最新新闻', text)

    # About page specific
    text = re.sub(r'PAA Creator & AI Agent Builder \| Personal AI Office Assistant',
                  'PAA 创造者 & AI Agent 构建者 | 个人 AI 办公助手', text)
    text = re.sub(r"STRATRONIX creates the Personal AI Office Assistant \(PAA\) category\. We build two businesses: \(1\) STA-100 hardware for global users, \(2\) Custom AI Agent development service\.",
                  "STRATRONIX 创建了个人 AI 办公助手（PAA）品类。我们经营两大业务：（1）面向全球用户的 STA-100 硬件，（2）定制 AI Agent 开发服务。", text)
    text = re.sub(r'STRATRONIX Technology \(Shenzhen\) Company, Limited is the creator of the PAA category — building dedicated AI hardware that puts a 24/7 AI coworker inside your messaging apps\. We also build custom AI Agents on top of our hardware for global enterprises\.',
                  'STRATRONIX Technology (Shenzhen) Company, Limited 是 PAA 品类的创造者 — 打造专用 AI 硬件，在您的消息应用中放置一个 24/7 的 AI 同事。我们还基于我们的硬件为全球企业构建定制 AI Agents。', text)

    # Map section
    text = re.sub(r'Near Shenzhen Bao\'an International Airport \(SZX\)', '深圳宝安国际机场（SZX）附近', text)

    return text

# List of files to translate
FILES = [
    "about.html",
    "products.html",
    "contact.html",
    "news.html",
    "ai-use.html",
    "ai-agent.html",
    "ai-agent-appliance.html",
    "ai-box.html",
    "sta100-buy.html",
    "openclaw.html",
    "404.html",
]

os.makedirs(OUT_DIR, exist_ok=True)

for fname in FILES:
    src = os.path.join(SRC_DIR, fname)
    out = os.path.join(OUT_DIR, fname)
    if os.path.exists(src):
        translate_file(src, out)
    else:
        print(f"  {fname}: SOURCE NOT FOUND")

print("\nDone!")
