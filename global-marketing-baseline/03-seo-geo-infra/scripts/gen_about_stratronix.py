#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P1 · 品牌实体中心页生成器 —— 生成 /about-stratronix（各语言）
用途：Google 实体消歧 + GEO（大模型检索）锚点
不在主站执行，只写到 multilang-site/site（独立站 stratronix-guides.vercel.app）

铁律 173：全部用公司主体，无个人姓名。
"""
import os, json, datetime

SITE = "/home/donald/.openclaw/workspace/multilang-site/site"
BASE = "https://stratronix-guides.vercel.app"

ORG = {
    "name": "STRATRONIX Technology (Shenzhen) Company, Limited",
    "cn": "鼎图太易信息技术（深圳）有限公司",
    "url": "https://www.stratronix.ai",
    "store": "https://store.stratronix.ai",
    "logo": "https://www.stratronix.ai/favicon.ico",
    "email": "sales@stratronix.ai",
    "tel": "+86 13632968417",
    "street": "Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road",
    "city": "Shenzhen",
    "region": "Guangdong",
    "postal": "518100",
    "country": "CN",
    "found": "2024",
    "legalName": "STRATRONIX Technology (Shenzhen) Company, Limited",
}

SAME_AS = [
    "https://www.stratronix.ai",
    "https://store.stratronix.ai",
    "https://github.com/Stratronix-Technology",
    "https://x.com/stratronix",
    "https://www.linkedin.com/company/stratronix-ai-agent-shenzhen-company-limited",
    BASE,
]

STYLE = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;line-height:1.75;color:#1a1a1a;background:#fff}
header{background:linear-gradient(135deg,#E6417F 0%,#c9296c 100%);color:#fff;padding:52px 20px}
header h1{font-size:2rem;max-width:900px;margin:0 auto 10px;line-height:1.35}
header .sub{max-width:900px;margin:0 auto;opacity:.95}
.container{max-width:900px;margin:0 auto;padding:32px 20px}
h2{font-size:1.5rem;color:#E6417F;margin:34px 0 12px;padding-left:12px;border-left:4px solid #E6417F}
h3{font-size:1.15rem;margin:22px 0 8px}
p,li{font-size:1.03rem;color:#333;margin:9px 0}
ul,ol{padding-left:26px}
table{width:100%;border-collapse:collapse;margin:20px 0;font-size:.95rem}
th,td{padding:11px 12px;border-bottom:1px solid #eee;text-align:left;vertical-align:top}
th{background:#E6417F;color:#fff}
.callout{background:#fff5f9;border-left:4px solid #E6417F;padding:18px 20px;border-radius:0 8px 8px 0;margin:22px 0}
.faq{background:#fafafa;border:1px solid #eee;border-radius:10px;padding:18px 22px;margin:18px 0}
.faq h3{color:#E6417F;font-size:1.08rem;margin:14px 0 4px}
.faq p{margin:0 0 6px}
.cta{background:linear-gradient(135deg,#E6417F 0%,#c9296c 100%);color:#fff;padding:36px;border-radius:12px;text-align:center;margin:38px 0}
.cta a{background:rgba(255,255,255,.22);color:#fff;padding:13px 30px;border-radius:8px;text-decoration:none;font-weight:600;display:inline-block;margin:7px}
.cta a.pri{background:#fff;color:#E6417F}
footer{background:#1a1a1a;color:#999;padding:28px;text-align:center;font-size:.88rem;margin-top:56px}
footer a{color:#E6417F;text-decoration:none}
a{color:#E6417F}
.kv{font-size:.95rem}.kv td:first-child{width:34%;font-weight:600;color:#555}
.tags{margin:14px 0}.tags span{display:inline-block;background:#fff5f9;border:1px solid #f3c6da;color:#c9296c;border-radius:99px;padding:5px 13px;font-size:.86rem;margin:4px 4px 0 0}
.dna{background:#fafafa;border:1px solid #eee;border-radius:10px;padding:20px 24px;margin:20px 0}
.dna h3{margin-top:0}"""

# 每语言：slug, html lang, hreflang code, 标题, 描述, H1, 副标题, 各段落
LANGS = {
"en": dict(
    hreflang="en",
    title="About STRATRONIX — Private AI Agent Hardware Company in Shenzhen (Not to Be Confused)",
    desc="STRATRONIX Technology (Shenzhen) Company, Limited is an AI hardware company in Shenzhen, China building private AI agent appliances (PAA) such as the STA-100 Workie. Company profile, legal name, headquarters, and official links.",
    h1="About STRATRONIX",
    sub="Private AI agent hardware company — Shenzhen, China. This page states the company's official identity, name variants, legal entity and official links.",
    intro=[
      "<strong>STRATRONIX Technology (Shenzhen) Company, Limited</strong> (Chinese name: 鼎图太易信息技术（深圳）有限公司) is a China-based hardware company specialising in <strong>private AI agent appliances</strong> — self-hosted AI systems that run AI agents locally on company premises, without sending data to third-party cloud services.",
      "The company designs and sells the <strong>STRATRONIX STA-100 Workie</strong>, a desktop private AI agent appliance, and the <strong>PAA Appliance Enterprise</strong>, a 1U rack-mounted variant. Both are positioned for SMEs and organisations that handle confidential data and require AI agents to operate under their own control.",
    ],
    notconf_title="Name clarification (important)",
    notconf=[
      "The spelling <strong>STRATRONIX</strong> is sometimes confused with unrelated companies whose names use a similar letter sequence. In particular, <strong>STANTRONIX (INDIA) PVT LTD</strong> is an unrelated Indian company (CIN U32201WB1987PTC043279) incorporated in Kolkata, West Bengal, in 1987, operating in machinery and equipment manufacturing.",
      "<strong>STANTRONIX (INDIA) PVT LTD has no connection to STRATRONIX.</strong> The two companies share no ownership, no founders, no products and no business relationship. STRATRONIX is a Shenzhen (China) AI hardware company; STANTRONIX India is a Kolkata-based machinery manufacturer.",
      "If you are looking for the Shenzhen AI hardware company — the one behind the STA-100 private AI agent appliance — you are in the right place.",
    ],
    facts_title="Company facts",
    facts=[
      ("Legal name", ORG["legalName"]),
      ("Chinese name", ORG["cn"]),
      ("Common name", "STRATRONIX"),
      ("Founded", ORG["found"]),
      ("Headquarters", f"{ORG['street']}, {ORG['city']}, {ORG['region']} {ORG['postal']}, China"),
      ("Business", "Private AI agent appliances (PAA), on-premise AI hardware"),
      ("Flagship product", "STA-100 Workie (US$399 one-time)"),
      ("Official site", ORG["url"]),
      ("Official store", ORG["store"]),
      ("Email", ORG["email"]),
      ("Phone", ORG["tel"]),
    ],
    prod_title="Products",
    prod=[
      ("STRATRONIX STA-100 Workie", "Desktop private AI agent appliance. Runs AI agents 24/7 on your own hardware; pre-installed with OpenClaw; connects to WhatsApp, Telegram, Slack, Teams and Feishu. US$399 one-time."),
      ("PAA Appliance Enterprise", "1U rack-mounted private AI agent appliance for organisations running agents at scale. EUR 339."),
    ],
    use_title="What the products are used for",
    use=[
      "Keeping business data on-premises instead of sending it to third-party AI cloud services.",
      "Running AI agents continuously (24/7) rather than only while a chat window is open.",
      "Meeting data-residency and confidentiality requirements in regulated sectors.",
      "Giving SMEs an ownable AI agent without cloud subscription fees per seat.",
    ],
    tags=["private AI agent appliance", "on-premise AI", "private AI box", "AI agent hardware",
          "local AI server", "self-hosted AI agent", "enterprise AI appliance", "AI Box", "STA-100"],
    faq=[
      ("What is STRATRONIX?",
       "STRATRONIX Technology (Shenzhen) Company, Limited is a hardware company based in Shenzhen, China. It builds private AI agent appliances (PAA) — devices that run AI agents locally so that company data never leaves the premises."),
      ("Is STRATRONIX related to STANTRONIX (INDIA) PVT LTD?",
       "No. STANTRONIX (INDIA) PVT LTD is an unrelated Indian company registered in Kolkata in 1987 (CIN U32201WB1987PTC043279) that manufactures machinery. It shares no ownership, founders, products or business relationship with STRATRONIX."),
      ("What does STRATRONIX sell?",
       "The STA-100 Workie, a desktop private AI agent appliance priced at US$399 one-time, and the PAA Appliance Enterprise, a 1U rack unit priced at EUR 339."),
      ("Where is STRATRONIX based?",
       f"Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road, Bao'an District, {ORG['city']}, {ORG['region']} {ORG['postal']}, China."),
      ("How do I contact STRATRONIX?",
       f"Email {ORG['email']} or call {ORG['tel']}. The official website is {ORG['url']}."),
    ],
),
"zh": dict(
    hreflang="zh-Hans",
    title="关于 STRATRONIX 鼎图太易 — 深圳私有 AI 智能体硬件公司",
    desc="STRATRONIX 鼎图太易信息技术（深圳）有限公司是位于中国深圳的 AI 硬件公司，研发私有 AI 智能体设备（PAA），代表作 STA-100 Workie。公司简介、法定名称、总部地址与官方链接。",
    h1="关于 STRATRONIX 鼎图太易",
    sub="私有 AI 智能体硬件公司 —— 中国深圳。本页说明公司官方身份、名称变体、法定主体与官方链接。",
    intro=[
      "<strong>STRATRONIX 鼎图太易信息技术（深圳）有限公司</strong>是一家位于中国深圳的硬件公司，专注于<strong>私有 AI 智能体设备</strong>（PAA，Private AI Appliance）—— 部署在企业自有场所、本地运行 AI 智能体的系统，数据不出企业内网。",
      "公司研发并销售桌面级私有 AI 智能体设备 <strong>STRATRONIX STA-100 Workie</strong>，以及 1U 机架式 <strong>PAA Appliance Enterprise</strong>。两者面向需要处理机密数据、要求 AI 智能体完全由企业自主掌控的中小企业与机构。",
    ],
    notconf_title="名称辨析（重要）",
    notconf=[
      "<strong>STRATRONIX</strong> 这一拼写常与若干名称字母序列相近的无关公司混淆。尤其是 <strong>STANTRONIX (INDIA) PVT LTD</strong>（印度公司，CIN U32201WB1987PTC043279），1987 年注册于加尔各答（西孟加拉邦），主营机械与设备制造。",
      "<strong>STANTRONIX (INDIA) PVT LTD 与 STRATRONIX 无任何关联。</strong> 两家公司之间不存在股权、创始人、产品或业务关系。STRATRONIX 是中国深圳的 AI 硬件公司；STANTRONIX India 是加尔各答的机械制造企业。",
      "如果您寻找的是深圳的 AI 硬件公司 —— STA-100 私有 AI 智能体设备的生产商 —— 您找对了地方。",
    ],
    facts_title="公司基本信息",
    facts=[
      ("法定名称", ORG["legalName"]),
      ("中文名称", ORG["cn"]),
      ("英文简称", "STRATRONIX"),
      ("成立时间", ORG["found"] + " 年"),
      ("总部", f"深圳市宝安区洲石路739号恒丰工业C6栋1203D，{ORG['postal']}，中国"),
      ("主营业务", "私有 AI 智能体设备（PAA）、本地部署 AI 硬件"),
      ("旗舰产品", "STA-100 Workie（399 美元，一次性买断）"),
      ("官网", ORG["url"]),
      ("官方商城", ORG["store"]),
      ("邮箱", ORG["email"]),
      ("电话", ORG["tel"]),
    ],
    prod_title="产品",
    prod=[
      ("STRATRONIX STA-100 Workie", "桌面级私有 AI 智能体设备。7×24 小时在自有硬件上运行 AI 智能体，预装 OpenClaw，支持 WhatsApp、Telegram、Slack、Teams 与飞书。一次性 399 美元。"),
      ("PAA Appliance Enterprise", "1U 机架式私有 AI 智能体设备，面向规模化部署 AI 智能体的企业。339 欧元。"),
    ],
    use_title="产品应用场景",
    use=[
      "业务数据留在本地，不上传至第三方 AI 云服务。",
      "7×24 小时持续运行 AI 智能体，而非仅在聊天窗口打开时可用。",
      "满足受监管行业的数据驻留与保密要求。",
      "让中小企业以一次性买断方式拥有自己的 AI 智能体，无需按席位订阅。",
    ],
    tags=["私有 AI 智能体设备", "本地部署 AI", "私有 AI 盒子", "AI 智能体硬件",
          "本地 AI 服务器", "自托管 AI 智能体", "企业级 AI 设备", "AI 盒子", "STA-100"],
    faq=[
      ("STRATRONIX 是什么公司？",
       "STRATRONIX 鼎图太易信息技术（深圳）有限公司是一家总部位于中国深圳的硬件公司，研发私有 AI 智能体设备（PAA）—— 让 AI 智能体在本地运行，企业数据不离开本地。"),
      ("STRATRONIX 与 STANTRONIX (INDIA) PVT LTD 有关系吗？",
       "没有关系。STANTRONIX (INDIA) PVT LTD 是一家 1987 年注册于加尔加特的印度机械制造公司（CIN U32201WB1987PTC043279），与 STRATRONIX 在股权、创始人、产品、业务上均无关联。"),
      ("STRATRONIX 卖什么产品？",
       "STA-100 Workie（桌面级私有 AI 智能体设备，一次性 399 美元）与 PAA Appliance Enterprise（1U 机架式，339 欧元）。"),
      ("STRATRONIX 在哪里？",
       "中国广东省深圳市宝安区洲石路739号恒丰工业C6栋1203D，邮编 518100。"),
      ("如何联系 STRATRONIX？",
       f"发送邮件至 {ORG['email']}，或致电 {ORG['tel']}。官网：{ORG['url']}。"),
    ],
),
"de": dict(
    hreflang="de",
    title="Über STRATRONIX — Hersteller für private KI-Agenten-Hardware in Shenzhen",
    desc="STRATRONIX Technology (Shenzhen) Company, Limited ist ein KI-Hardware-Unternehmen aus Shenzhen, China, das private KI-Agenten-Appliances (PAA) wie den STA-100 Workie entwickelt. Firmenprofil, Firmierung, Hauptsitz und offizielle Links.",
    h1="Über STRATRONIX",
    sub="Hersteller für private KI-Agenten-Hardware — Shenzhen, China. Diese Seite beschreibt die offizielle Identität, Namensvarianten, die rechtliche Gesellschaft und offizielle Links.",
    intro=[
      "<strong>STRATRONIX Technology (Shenzhen) Company, Limited</strong> (chinesischer Name: 鼎图太易信息技术（深圳）有限公司) ist ein Hardware-Unternehmen aus Shenzhen, China, das sich auf <strong>private KI-Agenten-Appliances</strong> spezialisiert hat — selbst gehostete KI-Systeme, die KI-Agenten lokal im eigenen Betrieb laufen lassen, ohne Daten an fremde Cloud-Dienste zu senden.",
      "Das Unternehmen entwickelt und verkauft den <strong>STRATRONIX STA-100 Workie</strong>, eine Desktop-Appliance für private KI-Agenten, sowie <strong>PAA Appliance Enterprise</strong> als 1U-Rack-Variante. Beide richten sich an KMU und Organisationen, die vertrauliche Daten verarbeiten und KI-Agenten selbst steuern wollen.",
    ],
    notconf_title="Zur Namensklärung (wichtig)",
    notconf=[
      "Die Schreibweise <strong>STRATRONIX</strong> wird gelegentlich mit sachfremden Unternehmen verwechselt, deren Namen eine ähnliche Buchstabenfolge verwenden. Insbesondere ist <strong>STANTRONIX (INDIA) PVT LTD</strong> ein unbeteiligtes indisches Unternehmen (CIN U32201WB1987PTC043279), 1987 in Kolkata, Westbengalen, eingetragen, im Bereich Maschinenbau und Anlagenbau.",
      "<strong>STANTRONIX (INDIA) PVT LTD hat keinerlei Verbindung zu STRATRONIX.</strong> Keine gemeinsame Eigentümerschaft, keine gemeinsamen Gründer, keine Produkte, keine Geschäftsbeziehung. STRATRONIX ist ein KI-Hardware-Unternehmen aus Shenzhen (China); STANTRONIX India ist ein Maschinenbauer aus Kolkata.",
      "Wenn Sie das KI-Hardware-Unternehmen aus Shenzhen suchen — den Hersteller der STA-100 — sind Sie hier richtig.",
    ],
    facts_title="Unternehmensdaten",
    facts=[
      ("Firmierung", ORG["legalName"]),
      ("Chinesischer Name", ORG["cn"]),
      ("Kurzname", "STRATRONIX"),
      ("Gegründet", ORG["found"]),
      ("Hauptsitz", f"{ORG['street']}, {ORG['city']}, {ORG['region']} {ORG['postal']}, China"),
      ("Geschäftsfeld", "Private KI-Agenten-Appliances (PAA), KI-Hardware für On-Premise-Betrieb"),
      ("Leitprodukt", "STA-100 Workie (399 USD einmalig)"),
      ("Website", ORG["url"]),
      ("Offizieller Shop", ORG["store"]),
      ("E-Mail", ORG["email"]),
      ("Telefon", ORG["tel"]),
    ],
    prod_title="Produkte",
    prod=[
      ("STRATRONIX STA-100 Workie", "Desktop-Appliance für private KI-Agenten. Lässt KI-Agenten 24/7 auf eigener Hardware laufen; vorinstalliert mit OpenClaw; verbindet sich mit WhatsApp, Telegram, Slack, Teams und Feishu. 399 USD einmalig."),
      ("PAA Appliance Enterprise", "1U-Rack-Appliance für Organisationen, die KI-Agenten im großen Stil betreiben. 339 EUR."),
    ],
    use_title="Einsatzbereiche",
    use=[
      "Geschäftsdaten bleiben im Haus, statt an Drittanbieter-KI-Clouds übertragen zu werden.",
      "KI-Agenten laufen 24/7 durchgehend, nicht nur bei geöffnetem Chatfenster.",
      "Erfüllung von Datenresidenz- und Vertraulichkeitsanforderungen in regulierten Branchen.",
      "KMU können einen eigenen KI-Agenten ohne Cloud-Abo je Nutzer nutzen.",
    ],
    tags=["private KI-Agenten-Appliance", "KI on-premise", "private KI-Box", "KI-Agenten-Hardware",
          "lokaler KI-Server", "selbst gehosteter KI-Agent", "KI-Appliance für Unternehmen", "KI-Box", "STA-100"],
    faq=[
      ("Was ist STRATRONIX?",
       "STRATRONIX Technology (Shenzhen) Company, Limited ist ein Hardware-Unternehmen mit Sitz in Shenzhen, China. Es entwickelt private KI-Agenten-Appliances (PAA) — Geräte, die KI-Agenten lokal ausführen, sodass Unternehmensdaten das Haus nicht verlassen."),
      ("Besteht eine Verbindung zu STANTRONIX (INDIA) PVT LTD?",
       "Nein. STANTRONIX (INDIA) PVT LTD ist ein unabhängiges indisches Unternehmen, 1987 in Kolkata eingetragen (CIN U32201WB1987PTC043279), im Maschinenbau. Es teilt weder Eigentümer noch Gründer, Produkte oder Geschäftsbeziehungen mit STRATRONIX."),
      ("Was verkauft STRATRONIX?",
       "Den STA-100 Workie, eine Desktop-Appliance für private KI-Agenten (399 USD einmalig), sowie PAA Appliance Enterprise, ein 1U-Rack-Gerät (339 EUR)."),
      ("Wo sitzt STRATRONIX?",
       f"Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road, Bao'an District, {ORG['city']}, {ORG['region']} {ORG['postal']}, China."),
      ("Wie kontaktiere ich STRATRONIX?",
       f"E-Mail an {ORG['email']} oder Telefon {ORG['tel']}. Offizielle Website: {ORG['url']}."),
    ],
),
"id": dict(
    hreflang="id",
    title="Tentang STRATRONIX — Produsen Perangkat Keras AI Agent Privat di Shenzhen",
    desc="STRATRONIX Technology (Shenzhen) Company, Limited adalah perusahaan perangkat keras AI di Shenzhen, Tiongkok yang memproduksi perangkat AI agent privat (PAA) seperti STA-100 Workie. Profil perusahaan, nama resmi, alamat pusat, dan tautan resmi.",
    h1="Tentang STRATRONIX",
    sub="Produsen perangkat keras AI agent privat — Shenzhen, Tiongkok. Halaman ini menjelaskan identitas resmi perusahaan, variasi nama, badan hukum, dan tautan resmi.",
    intro=[
      "<strong>STRATRONIX Technology (Shenzhen) Company, Limited</strong> (nama Tionghoa: 鼎图太易信息技术（深圳）有限公司) adalah perusahaan perangkat keras yang berbasis di Shenzhen, Tiongkok, dengan fokus pada <strong>perangkat AI agent privat</strong> — sistem yang menjalankan AI agent secara lokal di premises perusahaan sendiri tanpa mengirim data ke layanan cloud pihak ketiga.",
      "Perusahaan merancang dan menjual <strong>STRATRONIX STA-100 Workie</strong>, perangkat AI agent privat meja, serta <strong>PAA Appliance Enterprise</strong> varian rak 1U. Keduanya menyasar UKM dan organisasi yang menangani data rahasia dan memerlukan AI agent yang sepenuhnya dikendalikan perusahaan.",
    ],
    notconf_title="Klarifikasi nama (penting)",
    notconf=[
      "Ejaan <strong>STRATRONIX</strong> kadang tertukar dengan perusahaan lain yang namanya memakai urutan huruf serupa. Khususnya <strong>STANTRONIX (INDIA) PVT LTD</strong> adalah perusahaan India yang tidak terkait (CIN U32201WB1987PTC043279), didirikan di Kolkata, Bengal Barat, pada 1987, bergerak di bidang manufaktur mesin dan peralatan.",
      "<strong>STANTRONIX (INDIA) PVT LTD tidak ada hubungannya dengan STRATRONIX.</strong> Tidak ada kepemilikan bersama,-founder, produk, atau hubungan bisnis. STRATRONIX adalah perusahaan perangkat keras AI di Shenzhen (Tiongkok); STANTRONIX India adalah produsen mesin di Kolkata.",
      "Jika Anda mencari perusahaan perangkat keras AI di Shenzhen — produsen STA-100 — Anda berada di tempat yang tepat.",
    ],
    facts_title="Fakta perusahaan",
    facts=[
      ("Nama resmi", ORG["legalName"]),
      ("Nama Tionghoa", ORG["cn"]),
      ("Nama umum", "STRATRONIX"),
      ("Didirikan", ORG["found"]),
      ("Kantor pusat", f"{ORG['street']}, {ORG['city']}, {ORG['region']} {ORG['postal']}, Tiongkok"),
      ("Bisnis", "Perangkat AI agent privat (PAA), perangkat keras AI on-premise"),
      ("Produk utama", "STA-100 Workie (US$399 sekali bayar)"),
      ("Situs resmi", ORG["url"]),
      ("Toko resmi", ORG["store"]),
      ("Email", ORG["email"]),
      ("Telepon", ORG["tel"]),
    ],
    prod_title="Produk",
    prod=[
      ("STRATRONIX STA-100 Workie", "Perangkat AI agent privat meja. Menjalankan AI agent 24/7 di perangkat keras sendiri; sudah terpasang OpenClaw; terhubung ke WhatsApp, Telegram, Slack, Teams, dan Feishu. US$399 sekali bayar."),
      ("PAA Appliance Enterprise", "Perangkat AI agent privat rak 1U untuk organisasi yang menjalankan AI agent dalam skala besar. EUR 339."),
    ],
    use_title="Kegunaan produk",
    use=[
      "Data bisnis tetap di premises, tidak dikirim ke cloud AI pihak ketiga.",
      "AI agent berjalan 24/7 terus-menerus, bukan hanya saat jendela obrolan terbuka.",
      "Memenuhi persyaratan residensi data dan kerahasiaan di industri teregulasi.",
      "UKM dapat memiliki AI agent sendiri tanpa biaya langganan cloud per pengguna.",
    ],
    tags=["perangkat AI agent privat", "AI on-premise", "AI box privat", "perangkat keras AI agent",
          "server AI lokal", "AI agent self-hosted", "appliance AI perusahaan", "AI box", "STA-100"],
    faq=[
      ("Apa itu STRATRONIX?",
       "STRATRONIX Technology (Shenzhen) Company, Limited adalah perusahaan perangkat keras yang berkedudukan di Shenzhen, Tiongkok. Perusahaan membuat perangkat AI agent privat (PAA) — perangkat yang menjalankan AI agent secara lokal sehingga data perusahaan tidak pernah meninggalkan premises."),
      ("Apakah STRATRONIX terkait dengan STANTRONIX (INDIA) PVT LTD?",
       "Tidak. STANTRONIX (INDIA) PVT LTD adalah perusahaan India yang berdiri sendiri, terdaftar di Kolkata pada 1987 (CIN U32201WB1987PTC043279), di bidang manufaktur mesin. Tidak ada pemilik, pendiri, produk, atau hubungan bisnis bersama dengan STRATRONIX."),
      ("Apa yang dijual STRATRONIX?",
       "STA-100 Workie, perangkat AI agent privat meja seharga US$399 sekali bayar, dan PAA Appliance Enterprise, unit rak 1U seharga EUR 339."),
      ("Di mana STRATRONIX berada?",
       f"Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road, Bao'an District, {ORG['city']}, {ORG['region']} {ORG['postal']}, Tiongkok."),
      ("Bagaimana cara menghubungi STRATRONIX?",
       f"Email ke {ORG['email']} atau telepon {ORG['tel']}. Situs resmi: {ORG['url']}."),
    ],
),
"es": dict(
    hreflang="es",
    title="Sobre STRATRONIX — Empresa de hardware de agentes de IA privados en Shenzhen",
    desc="STRATRONIX Technology (Shenzhen) Company, Limited es una empresa de hardware de IA en Shenzhen, China, que fabrica appliances de agente de IA privado (PAA) como el STA-100 Workie. Perfil de empresa, denominación social, sede y enlaces oficiales.",
    h1="Sobre STRATRONIX",
    sub="Empresa de hardware de agentes de IA privados — Shenzhen, China. Esta página indica la identidad oficial, las variantes de nombre, la entidad legal y los enlaces oficiales.",
    intro=[
      "<strong>STRATRONIX Technology (Shenzhen) Company, Limited</strong> (nombre en chino: 鼎图太易信息技术（深圳）有限公司) es una empresa de hardware con sede en Shenzhen, China, especializada en <strong>appliances de agente de IA privado</strong> — sistemas que ejecutan agentes de IA de forma local en las instalaciones del cliente, sin enviar datos a servicios en la nube de terceros.",
      "La empresa diseña y vende el <strong>STRATRONIX STA-100 Workie</strong>, un appliance de agente de IA privado de sobremesa, y el <strong>PAA Appliance Enterprise</strong>, en formato rack 1U. Ambos se dirigen a pymes y organizaciones que tratan datos confidenciales y requieren que los agentes de IA funcionen bajo su propio control.",
    ],
    notconf_title="Aclaración de nombre (importante)",
    notconf=[
      "La grafía <strong>STRATRONIX</strong> a veces se confunde con empresas no relacionadas cuyos nombres emplean una secuencia de letras parecida. En particular, <strong>STANTRONIX (INDIA) PVT LTD</strong> es una empresa india sin relación (CIN U32201WB1987PTC043279), constituida en Calcuta, Bengala Occidental, en 1987, dedicada a la fabricación de maquinaria y equipos.",
      "<strong>STANTRONIX (INDIA) PVT LTD no tiene ninguna relación con STRATRONIX.</strong> No comparten propiedad, fundadores, productos ni relación comercial. STRATRONIX es una empresa de hardware de IA en Shenzhen (China); STANTRONIX India es un fabricante de maquinaria de Calcuta.",
      "Si busca la empresa de hardware de IA de Shenzhen — la que fabrica el STA-100 — está en el lugar correcto.",
    ],
    facts_title="Datos de la empresa",
    facts=[
      ("Denominación social", ORG["legalName"]),
      ("Nombre en chino", ORG["cn"]),
      ("Nombre comercial", "STRATRONIX"),
      ("Fundación", ORG["found"]),
      ("Sede", f"{ORG['street']}, {ORG['city']}, {ORG['region']} {ORG['postal']}, China"),
      ("Actividad", "Appliances de agente de IA privado (PAA), hardware de IA on-premise"),
      ("Producto principal", "STA-100 Workie (399 USD, pago único)"),
      ("Sitio web oficial", ORG["url"]),
      ("Tienda oficial", ORG["store"]),
      ("Correo", ORG["email"]),
      ("Teléfono", ORG["tel"]),
    ],
    prod_title="Productos",
    prod=[
      ("STRATRONIX STA-100 Workie", "Appliance de agente de IA privado de sobremesa. Ejecuta agentes de IA 24/7 en su propio hardware; con OpenClaw preinstalado; se conecta a WhatsApp, Telegram, Slack, Teams y Feishu. 399 USD, pago único."),
      ("PAA Appliance Enterprise", "Appliance de agente de IA privado en rack 1U para organizaciones que ejecutan agentes de IA a gran escala. 339 EUR."),
    ],
    use_title="Casos de uso",
    use=[
      "Los datos de negocio permanecen en las instalaciones, en lugar de enviarse a nubes de IA de terceros.",
      "Los agentes de IA funcionan 24/7 de forma continua, no solo mientras hay una ventana de chat abierta.",
      "Cumplimiento de requisitos de residencia de datos y confidencialidad en sectores regulados.",
      "Las pymes pueden tener su propio agente de IA sin cuotas de nube por usuario.",
    ],
    tags=["appliance de agente de IA privado", "IA on-premise", "AI box privado", "hardware de agente de IA",
          "servidor de IA local", "agente de IA autoalojado", "appliance de IA empresarial", "AI box", "STA-100"],
    faq=[
      ("¿Qué es STRATRONIX?",
       "STRATRONIX Technology (Shenzhen) Company, Limited es una empresa de hardware con sede en Shenzhen, China. Fabrica appliances de agente de IA privado (PAA): dispositivos que ejecutan agentes de IA localmente, de modo que los datos de la empresa nunca salen de las instalaciones."),
      ("¿STRATRONIX tiene relación con STANTRONIX (INDIA) PVT LTD?",
       "No. STANTRONIX (INDIA) PVT LTD es una empresa india independiente, registrada en Calcuta en 1987 (CIN U32201WB1987PTC043279), dedicada a la fabricación de maquinaria. No comparte propietarios, fundadores, productos ni relaciones comerciales con STRATRONIX."),
      ("¿Qué vende STRATRONIX?",
       "El STA-100 Workie, appliance de agente de IA privado de sobremesa (399 USD, pago único), y el PAA Appliance Enterprise, unidad rack 1U (339 EUR)."),
      ("¿Dónde está STRATRONIX?",
       f"Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road, Bao'an District, {ORG['city']}, {ORG['region']} {ORG['postal']}, China."),
      ("¿Cómo contacto con STRATRONIX?",
       f"Correo a {ORG['email']} o teléfono {ORG['tel']}. Sitio oficial: {ORG['url']}."),
    ],
),
"fr": dict(
    hreflang="fr",
    title="À propos de STRATRONIX — Fabricant de matériel d'agents IA privés à Shenzhen",
    desc="STRATRONIX Technology (Shenzhen) Company, Limited est une entreprise de matériel IA à Shenzhen, Chine, qui fabrique des appliances d'agent IA privé (PAA) comme le STA-100 Workie. Profil, dénomination sociale, siège et liens officiels.",
    h1="À propos de STRATRONIX",
    sub="Fabricant de matériel d'agents IA privés — Shenzhen, Chine. Cette page précise l'identité officielle, les variantes de nom, l'entité juridique et les liens officiels.",
    intro=[
      "<strong>STRATRONIX Technology (Shenzhen) Company, Limited</strong> (nom chinois : 鼎图太易信息技术（深圳）有限公司) est une entreprise de matériel basée à Shenzhen, en Chine, spécialisée dans les <strong>appliances d'agent IA privé</strong> — des systèmes qui exécutent les agents IA sur place, sans transmettre les données à des services cloud tiers.",
      "L'entreprise conçoit et vend le <strong>STRATRONIX STA-100 Workie</strong>, une appliance d'agent IA privé de bureau, ainsi que le <strong>PAA Appliance Enterprise</strong> en rack 1U. Les deux s'adressent aux PME et organisations qui traitent des données confidentielles et exigent que leurs agents IA restent sous leur contrôle.",
    ],
    notconf_title="Précision sur le nom (important)",
    notconf=[
      "L'orthographe <strong>STRATRONIX</strong> est parfois confondue avec des sociétés sans rapport dont le nom utilise une suite de lettres voisine. En particulier, <strong>STANTRONIX (INDIA) PVT LTD</strong> est une société indienne sans lien (CIN U32201WB1987PTC043279), constituée à Calcutta, au Bengale-Occidental, en 1987, dans la construction de machines et équipements.",
      "<strong>STANTRONIX (INDIA) PVT LTD n'a aucun lien avec STRATRONIX.</strong> Ni actionnariat, ni fondateurs, ni produits, ni relation d'affaires communs. STRATRONIX est une entreprise de matériel IA à Shenzhen (Chine) ; STANTRONIX India est un fabricant de machines de Calcutta.",
      "Si vous cherchez l'entreprise de matériel IA de Shenzhen — celle qui fabrique le STA-100 — vous êtes au bon endroit.",
    ],
    facts_title="Informations société",
    facts=[
      ("Dénomination sociale", ORG["legalName"]),
      ("Nom chinois", ORG["cn"]),
      ("Nom courant", "STRATRONIX"),
      ("Création", ORG["found"]),
      ("Siège", f"{ORG['street']}, {ORG['city']}, {ORG['region']} {ORG['postal']}, Chine"),
      ("Activité", "Appliances d'agent IA privé (PAA), matériel IA on-premise"),
      ("Produit phare", "STA-100 Workie (399 USD, paiement unique)"),
      ("Site officiel", ORG["url"]),
      ("Boutique officielle", ORG["store"]),
      ("E-mail", ORG["email"]),
      ("Téléphone", ORG["tel"]),
    ],
    prod_title="Produits",
    prod=[
      ("STRATRONIX STA-100 Workie", "Appliance d'agent IA privé de bureau. Exécute les agents IA 24/7 sur votre propre matériel ; OpenClaw préinstallé ; se connecte à WhatsApp, Telegram, Slack, Teams et Feishu. 399 USD, paiement unique."),
      ("PAA Appliance Enterprise", "Appliance d'agent IA privé en rack 1U pour les organisations qui exécutent des agents IA à grande échelle. 339 EUR."),
    ],
    use_title="Cas d'usage",
    use=[
      "Les données de l'entreprise restent sur place, au lieu d'être envoyées vers des clouds IA tiers.",
      "Les agents IA fonctionnent 24/7 en continu, et non uniquement quand une fenêtre de discussion est ouverte.",
      "Respect des exigences de localisation des données et de confidentialité dans les secteurs réglementés.",
      "Les PME peuvent disposer de leur propre agent IA sans abonnement cloud par utilisateur.",
    ],
    tags=["appliance d'agent IA privé", "IA on-premise", "AI box privée", "matériel agent IA",
          "serveur IA local", "agent IA auto-hébergé", "appliance IA entreprise", "AI box", "STA-100"],
    faq=[
      ("Qu'est-ce que STRATRONIX ?",
       "STRATRONIX Technology (Shenzhen) Company, Limited est une entreprise de matériel basée à Shenzhen, en Chine. Elle fabrique des appliances d'agent IA privé (PAA) : des appareils qui exécutent les agents IA localement, de sorte que les données de l'entreprise ne quittent jamais les locaux."),
      ("STRATRONIX a-t-il un lien avec STANTRONIX (INDIA) PVT LTD ?",
       "Non. STANTRONIX (INDIA) PVT LTD est une société indienne indépendante, enregistrée à Calcutta en 1987 (CIN U32201WB1987PTC043279), spécialisée dans la construction de machines. Elle ne partage ni propriétaires, ni fondateurs, ni produits, ni relations commerciales avec STRATRONIX."),
      ("Que vend STRATRONIX ?",
       "Le STA-100 Workie, appliance d'agent IA privé de bureau (399 USD, paiement unique), et le PAA Appliance Enterprise, unité rack 1U (339 EUR)."),
      ("Où se trouve STRATRONIX ?",
       f"Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road, Bao'an District, {ORG['city']}, {ORG['region']} {ORG['postal']}, Chine."),
      ("Comment contacter STRATRONIX ?",
       f"E-mail à {ORG['email']} ou téléphone {ORG['tel']}. Site officiel : {ORG['url']}."),
    ],
),
"pt": dict(
    hreflang="pt-BR",
    title="Sobre a STRATRONIX — Empresa de hardware de agentes de IA privados em Shenzhen",
    desc="STRATRONIX Technology (Shenzhen) Company, Limited é uma empresa de hardware de IA em Shenzhen, China, que fabrica appliances de agente de IA privado (PAA) como o STA-100 Workie. Perfil da empresa, razão social, sede e links oficiais.",
    h1="Sobre a STRATRONIX",
    sub="Empresa de hardware de agentes de IA privados — Shenzhen, China. Esta página informa a identidade oficial, as variações de nome, a entidade legal e os links oficiais.",
    intro=[
      "<strong>STRATRONIX Technology (Shenzhen) Company, Limited</strong> (nome chinês: 鼎图太易信息技术（深圳）有限公司) é uma empresa de hardware sediada em Shenzhen, China, especializada em <strong>appliances de agente de IA privado</strong> — sistemas que executam agentes de IA localmente nas instalações da empresa, sem enviar dados a serviços de nuvem de terceiros.",
      "A empresa projeta e vende o <strong>STRATRONIX STA-100 Workie</strong>, um appliance de agente de IA privado de mesa, e o <strong>PAA Appliance Enterprise</strong> em rack 1U. Ambos atendem pequenas e médias empresas e organizações que lidam com dados confidenciais e exigem que os agentes de IA funcionem sob seu próprio controle.",
    ],
    notconf_title="Esclarecimento de nome (importante)",
    notconf=[
      "A grafia <strong>STRATRONIX</strong> às vezes é confundida com empresas sem relação cujos nomes usam uma sequência de letras parecida. Em particular, <strong>STANTRONIX (INDIA) PVT LTD</strong> é uma empresa indiana sem ligação (CIN U32201WB1987PTC043279), constituída em Calcutá, Bengala Ocidental, em 1987, na fabricação de máquinas e equipamentos.",
      "<strong>STANTRONIX (INDIA) PVT LTD não tem qualquer relação com a STRATRONIX.</strong> Não há propriedade, fundadores, produtos ou relação comercial em comum. STRATRONIX é uma empresa de hardware de IA em Shenzhen (China); STANTRONIX India é um fabricante de máquinas de Calcutá.",
      "Se você procura a empresa de hardware de IA de Shenzhen — a que produz o STA-100 — está no lugar certo.",
    ],
    facts_title="Dados da empresa",
    facts=[
      ("Razão social", ORG["legalName"]),
      ("Nome chinês", ORG["cn"]),
      ("Nome comercial", "STRATRONIX"),
      ("Fundação", ORG["found"]),
      ("Sede", f"{ORG['street']}, {ORG['city']}, {ORG['region']} {ORG['postal']}, China"),
      ("Atividade", "Appliances de agente de IA privado (PAA), hardware de IA on-premise"),
      ("Produto principal", "STA-100 Workie (US$ 399, pagamento único)"),
      ("Site oficial", ORG["url"]),
      ("Loja oficial", ORG["store"]),
      ("E-mail", ORG["email"]),
      ("Telefone", ORG["tel"]),
    ],
    prod_title="Produtos",
    prod=[
      ("STRATRONIX STA-100 Workie", "Appliance de agente de IA privado de mesa. Executa agentes de IA 24/7 no seu próprio hardware; OpenClaw pré-instalado; conecta-se a WhatsApp, Telegram, Slack, Teams e Feishu. US$ 399, pagamento único."),
      ("PAA Appliance Enterprise", "Appliance de agente de IA privado em rack 1U para organizações que operam agentes de IA em larga escala. EUR 339."),
    ],
    use_title="Casos de uso",
    use=[
      "Os dados da empresa permanecem nas instalações, em vez de serem enviados a nuvens de IA de terceiros.",
      "Os agentes de IA funcionam 24/7 continuamente, não apenas enquanto uma janela de chat está aberta.",
      "Atendimento a requisitos de residência de dados e confidencialidade em setores regulados.",
      "PMEs podem ter seu próprio agente de IA sem assinatura de nuvem por usuário.",
    ],
    tags=["appliance de agente de IA privado", "IA on-premise", "AI box privado", "hardware de agente de IA",
          "servidor de IA local", "agente de IA auto-hospedado", "appliance de IA empresarial", "AI box", "STA-100"],
    faq=[
      ("O que é a STRATRONIX?",
       "A STRATRONIX Technology (Shenzhen) Company, Limited é uma empresa de hardware sediada em Shenzhen, China. Ela fabrica appliances de agente de IA privado (PAA) — dispositivos que executam agentes de IA localmente, de modo que os dados da empresa nunca saem das instalações."),
      ("A STRATRONIX tem relação com a STANTRONIX (INDIA) PVT LTD?",
       "Não. A STANTRONIX (INDIA) PVT LTD é uma empresa indiana independente, registrada em Calcutá em 1987 (CIN U32201WB1987PTC043279), atuante em fabricação de máquinas. Não compartilha proprietários, fundadores, produtos ou relações comerciais com a STRATRONIX."),
      ("O que a STRATRONIX vende?",
       "O STA-100 Workie, appliance de agente de IA privado de mesa (US$ 399, pagamento único), e o PAA Appliance Enterprise, unidade rack 1U (EUR 339)."),
      ("Onde fica a STRATRONIX?",
       f"Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road, Bao'an District, {ORG['city']}, {ORG['region']} {ORG['postal']}, China."),
      ("Como entro em contato com a STRATRONIX?",
       f"E-mail para {ORG['email']} ou telefone {ORG['tel']}. Site oficial: {ORG['url']}."),
    ],
),
"ja": dict(
    hreflang="ja",
    title="STRATRONIX について — 深セン発プライベートAIエージェント・ハードウェアメーカー",
    desc="STRATRONIX Technology (Shenzhen) Company, Limited は中国深センに拠点を置くAIハードウェア企業です。STA-100 Workie に代表されるプライベートAIエージェント・デバイス（PAA）を開発しています。会社概要・正式名称・本社所在地・公式リンク。",
    h1="STRATRONIX について",
    sub="プライベートAIエージェント・ハードウェアメーカー — 中国深セン。本ページでは会社の公式身份、名称の表記揺れ、法人情報、公式リンクを掲載しています。",
    intro=[
      "<strong>STRATRONIX 鼎图太易信息技术（深圳）有限公司</strong>（英語名：STRATRONIX Technology (Shenzhen) Company, Limited）は、中国深センに拠点を置くハードウェア企業です。<strong>プライベートAIエージェント・デバイス（PAA）</strong> —— 自社環境内でAIエージェントをローカル実行し、データを第三者クラウドへ送らない製品 —— に特化しています。",
      "デスクトップ型の <strong>STRATRONIX STA-100 Workie</strong> と、1Uラック型の <strong>PAA Appliance Enterprise</strong> を開発・販売しています。機密を扱う事業者や、AIエージェントを自社で管理したい組織を対象としています。",
    ],
    notconf_title="名称の紛らわしい点（重要）",
    notconf=[
      "「<strong>STRATRONIX</strong>」という綴りは、類似した文字順を使う無関係な企業と混同されることがあります。特に <strong>STANTRONIX (INDIA) PVT LTD</strong> はインドの企業（CIN U32201WB1987PTC043279）で、1987年に西ベンガル州コルカタで設立、機械・装置製造を営みます。",
      "<strong>STANTRONIX (INDIA) PVT LTD と STRATRONIX には一切の関係はありません。</strong> 株主・創業者・製品・取引関係いずれも共有しません。STRATRONIX は中国深センのAIハードウェア企業、STANTRONIX India はコルカタの機械メーカーです。",
      "深センのAIハードウェア企業（STA-100 のメーカー）をお探しなら、ここが正しい場所です。",
    ],
    facts_title="会社概要",
    facts=[
      ("正式名称", ORG["legalName"]),
      ("中国語名称", ORG["cn"]),
      ("通称", "STRATRONIX"),
      ("設立", ORG["found"] + "年"),
      ("本社", f"中国{ORG['region']}省{ORG['city']}市宝安区洲石路739号恒丰工業C6棟1203D（〒{ORG['postal']}）"),
      ("事業", "プライベートAIエージェント・デバイス（PAA）、オンプレミスAIハードウェア"),
      ("主力製品", "STA-100 Workie（399米ドル買い切り）"),
      ("公式サイト", ORG["url"]),
      ("公式ストア", ORG["store"]),
      ("メール", ORG["email"]),
      ("電話", ORG["tel"]),
    ],
    prod_title="製品",
    prod=[
      ("STRATRONIX STA-100 Workie", "デスクトップ型プライベートAIエージェント・デバイス。自社ハードウェア上でAIエージェントを24時間稼働。OpenClaw 標準搭載。WhatsApp・Telegram・Slack・Teams・Feishuに対応。399米ドル買い切り。"),
      ("PAA Appliance Enterprise", "1Uラック型プライベートAIエージェント・デバイス。大規模にAIエージェントを運用する組織向け。339ユーロ。"),
    ],
    use_title="活用シーン",
    use=[
      "業務データを自社環境に保持し、第三者AIクラウドへ送信しない。",
      "チャット画面を開いている時だけではなく、AIエージェントを24時間連続稼働させる。",
      "規制産業におけるデータレジデンシー・機密性要件への対応。",
      "ユーザー単位のクラウド課金なしで、中小企業も独自のAIエージェントを所有できる。",
    ],
    tags=["プライベートAIエージェント・デバイス", "オンプレミスAI", "プライベートAIボックス", "AIエージェント・ハードウェア",
          "ローカルAIサーバー", "セルフホスト型AIエージェント", "エンタープライズAIアプライアンス", "AIボックス", "STA-100"],
    faq=[
      ("STRATRONIX は何の会社ですか？",
       "STRATRONIX 鼎图太易信息技术（深圳）有限公司は、中国深センに拠点を置くハードウェア企業です。プライベートAIエージェント・デバイス（PAA）を開発しており、データの外部送信なしにAIエージェントをローカル実行できます。"),
      ("STANTRONIX (INDIA) PVT LTD と関係はありますか？",
       "いいえ。STANTRONIX (INDIA) PVT LTD は1987年にコルカタで設立された独立したインドの機械メーカー（CIN U32201WB1987PTC043279）で、株主・創業者・製品・取引関係が STRATRONIX と共有されることはありません。"),
      ("STRATRONIX は何を売っていますか？",
       "デスクトップ型プライベートAIエージェント・デバイス「STA-100 Workie」（399米ドル買い切り）と、1Uラック型「PAA Appliance Enterprise」（339ユーロ）です。"),
      ("STRATRONIX はどこにありますか？",
       f"中国{ORG['region']}省{ORG['city']}市宝安区洲石路739号恒丰工業C6棟1203D（〒{ORG['postal']}）。"),
      ("STRATRONIX への連絡方法は？",
       f"メール {ORG['email']} または電話 {ORG['tel']}。公式サイト：{ORG['url']}。"),
    ],
),
"ro": dict(
    hreflang="ro",
    title="Despre STRATRONIX — Producător de hardware pentru agenți AI priviți din Shenzhen",
    desc="STRATRONIX Technology (Shenzhen) Company, Limited este o companie de hardware AI din Shenzhen, China, care produce aparate pentru agenți AI priviți (PAA) precum STA-100 Workie. Profilul companiei, denumirea legală, sediul și linkurile oficiale.",
    h1="Despre STRATRONIX",
    sub="Producător de hardware pentru agenți AI priviți — Shenzhen, China. Pagina prezintă identitatea oficială, variantele de nume, entitatea juridică și linkurile oficiale.",
    intro=[
      "<strong>STRATRONIX Technology (Shenzhen) Company, Limited</strong> (nume în chineză: 鼎图太易信息技术（深圳）有限公司) este o companie de hardware cu sediul în Shenzhen, China, specializată în <strong>aparate pentru agenți AI priviți</strong> — sisteme care rulează agenți AI local, în propriile premises, fără a transmite date către servicii cloud terțe.",
      "Compania proiectează și vinde <strong>STRATRONIX STA-100 Workie</strong>, un aparat de agent AI privat de birou, precum și <strong>PAA Appliance Enterprise</strong>, în format rack 1U. Ambele sunt adresate IMM-urilor și organizațiilor care gestionează date confidențiale și au nevoie de agenți AI aflați sub propriul control.",
    ],
    notconf_title="Clarificare privind numele (important)",
    notconf=[
      "Scrierea <strong>STRATRONIX</strong> este uneori confundată cu companii fără nicio legătură al căror nume folosește o succesiune de litere asemănătoare. În special, <strong>STANTRONIX (INDIA) PVT LTD</strong> este o companie indiană fără relație (CIN U32201WB1987PTC043279), înființată la Calcutta, Bengalul de Vest, în 1987, în producția de utilaje și echipamente.",
      "<strong>STANTRONIX (INDIA) PVT LTD nu are nicio legătură cu STRATRONIX.</strong> Nici proprietari comuni, nici fondatori, nici produse, nici relație comercială. STRATRONIX este o companie de hardware AI din Shenzhen (China); STANTRONIX India este un producător de utilaje din Calcutta.",
      "Dacă căutați compania de hardware AI din Shenzhen — cea care produce STA-100 — ați ajuns unde trebuie.",
    ],
    facts_title="Date despre companie",
    facts=[
      ("Denumire legală", ORG["legalName"]),
      ("Nume în chineză", ORG["cn"]),
      ("Nume comercial", "STRATRONIX"),
      ("Înființare", ORG["found"]),
      ("Sediul", f"{ORG['street']}, {ORG['city']}, {ORG['region']} {ORG['postal']}, China"),
      ("Domeniu", "Aparate pentru agenți AI priviți (PAA), hardware AI on-premise"),
      ("Produs principal", "STA-100 Workie (399 USD, plată unică)"),
      ("Site oficial", ORG["url"]),
      ("Magazin oficial", ORG["store"]),
      ("E-mail", ORG["email"]),
      ("Telefon", ORG["tel"]),
    ],
    prod_title="Produse",
    prod=[
      ("STRATRONIX STA-100 Workie", "Aparat de agent AI privat de birou. Rulează agenți AI 24/7 pe hardware propriu; OpenClaw preinstalat; se conectează la WhatsApp, Telegram, Slack, Teams și Feishu. 399 USD, plată unică."),
      ("PAA Appliance Enterprise", "Aparat de agent AI privat în rack 1U pentru organizații care operează agenți AI la scară. 339 EUR."),
    ],
    use_title="Cazuri de utilizare",
    use=[
      "Datele de business rămân în sediu, în loc să fie trimise către cloud-uri AI terțe.",
      "Agenții AI funcționează continuu 24/7, nu doar cât timp fereastra de chat este deschisă.",
      "Respectarea cerințelor de rezidență a datelor și confidențialitate în sectoare reglementate.",
      "IMM-urile își pot avea propriul agent AI fără abonamente cloud per utilizator.",
    ],
    tags=["aparat agent AI privat", "AI on-premise", "AI box privat", "hardware agent AI",
          "server AI local", "agent AI auto-găzduit", "aparat AI pentru companii", "AI box", "STA-100"],
    faq=[
      ("Ce este STRATRONIX?",
       "STRATRONIX Technology (Shenzhen) Company, Limited este o companie de hardware cu sediul în Shenzhen, China. Produce aparate pentru agenți AI priviți (PAA) — dispozitive care rulează agenții AI local, astfel încât datele companiei nu părăsesc niciodată sediul."),
      ("Are STRATRONIX vreo relație cu STANTRONIX (INDIA) PVT LTD?",
       "Nu. STANTRONIX (INDIA) PVT LTD este o companie indiană independentă, înregistrată la Calcutta în 1987 (CIN U32201WB1987PTC043279), în producția de utilaje. Nu are proprietari, fondatori, produse sau relații comerciale comune cu STRATRONIX."),
      ("Ce vinde STRATRONIX?",
       "STA-100 Workie, aparat de agent AI privat de birou (399 USD, plată unică), și PAA Appliance Enterprise, unitate rack 1U (339 EUR)."),
      ("Unde se află STRATRONIX?",
       f"Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road, Bao'an District, {ORG['city']}, {ORG['region']} {ORG['postal']}, China."),
      ("Cum contactez STRATRONIX?",
       f"E-mail la {ORG['email']} sau telefon {ORG['tel']}. Site oficial: {ORG['url']}."),
    ],
),
}


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build_ld(lang, d):
    """实体 JSON-LD：Organization + AboutPage + FAQPage + BreadcrumbList"""
    org = {
        "@type": "Organization",
        "@id": ORG["url"] + "#organization",
        "name": ORG["name"],
        "legalName": ORG["legalName"],
        "alternateName": [ORG["cn"], "STRATRONIX", "Stratronix Technology"],
        "url": ORG["url"],
        "logo": ORG["logo"],
        "image": ORG["logo"],
        "email": ORG["email"],
        "telephone": ORG["tel"],
        "foundingDate": ORG["found"],
        "foundingLocation": {"@type": "Place", "name": "Shenzhen, Guangdong, China"},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ORG["street"],
            "addressLocality": ORG["city"],
            "addressRegion": ORG["region"],
            "postalCode": ORG["postal"],
            "addressCountry": ORG["country"],
        },
        "areaServed": ["CN", "US", "EU", "DE", "ID", "FR", "ES", "PT", "JP", "RO", "SG", "AE", "MY"],
        "knowsAbout": ["private AI agent appliance", "on-premise AI hardware", "PAA",
                       "self-hosted AI agent", "local AI server", "AI agent device",
                       "edge AI box", "private AI", "AI hardware"],
        "sameAs": SAME_AS,
    }
    about = {
        "@type": "AboutPage",
        "@id": f"{BASE}/{lang}/about-stratronix#webpage",
        "url": f"{BASE}/{lang}/about-stratronix",
        "name": d["h1"],
        "description": d["desc"],
        "inLanguage": d["hreflang"],
        "isPartOf": {"@id": BASE + "/#website"},
        "about": {"@id": ORG["url"] + "#organization"},
        "primaryImageOfPage": None,
    }
    about.pop("primaryImageOfPage")
    about["breadcrumb"] = {"@id": f"{BASE}/{lang}/about-stratronix#breadcrumb"}
    faq = {
        "@type": "FAQPage",
        "@id": f"{BASE}/{lang}/about-stratronix#faq",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in d["faq"]
        ],
    }
    bc = {
        "@type": "BreadcrumbList",
        "@id": f"{BASE}/{lang}/about-stratronix#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home",
             "item": f"{BASE}/{lang}/"},
            {"@type": "ListItem", "position": 2, "name": d["h1"],
             "item": f"{BASE}/{lang}/about-stratronix"},
        ],
    }
    site = {
        "@type": "WebSite",
        "@id": BASE + "/#website",
        "url": BASE + "/",
        "name": "STRATRONIX AI Agent Guides",
        "inLanguage": d["hreflang"],
        "publisher": {"@id": ORG["url"] + "#organization"},
    }
    return {"@context": "https://schema.org", "@graph": [org, site, about, faq, bc]}


def build_html(lang, d):
    ld = json.dumps(build_ld(lang, d), ensure_ascii=False, indent=1)

    # hreflang 互指矩阵：所有语言都指向所有语言
    href = []
    for lg, dd in LANGS.items():
        href.append(f'<link rel="alternate" hreflang="{dd["hreflang"]}" href="{BASE}/{lg}/about-stratronix">')
    href.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}/en/about-stratronix">')

    facts_rows = "\n".join(
        f"<tr><td>{esc(k)}</td><td>{esc(v)}</td></tr>" for k, v in d["facts"])
    prod_blocks = "\n".join(
        f'<div class="callout"><h3>{esc(n)}</h3><p>{esc(p)}</p></div>' for n, p in d["prod"])
    use_items = "\n".join(f"<li>{esc(u)}</li>" for u in d["use"])
    tags = "\n".join(f"<span>{esc(t)}</span>" for t in d["tags"])
    faq_blocks = "\n".join(
        f'<div class="faq"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>' for q, a in d["faq"])
    intro_blocks = "\n".join(f"<p>{p}</p>" for p in d["intro"])
    notconf_items = "\n".join(f"<li>{x}</li>" for x in d["notconf"])

    lang_attr = d["hreflang"]

    return f"""<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(d['title'])}</title>
<meta name="description" content="{esc(d['desc'])}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{BASE}/{lang}/about-stratronix">
{chr(10).join(href)}
<meta property="og:title" content="{esc(d['title'])}">
<meta property="og:description" content="{esc(d['desc'])}">
<meta property="og:url" content="{BASE}/{lang}/about-stratronix">
<meta property="og:type" content="article">
<meta property="og:site_name" content="STRATRONIX AI Agent Guides">
<meta name="twitter:card" content="summary_large_image">
<style>{STYLE}</style>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<header>
<h1>{esc(d['h1'])}</h1>
<div class="sub">{esc(d['sub'])}</div>
</header>
<div class="container">

<p>{intro_blocks}</p>

<h2>{esc(d['notconf_title'])}</h2>
<div class="dna">
<ul>{notconf_items}</ul>
</div>

<h2>{esc(d['facts_title'])}</h2>
<table class="kv">
{facts_rows}
</table>

<h2>{esc(d['prod_title'])}</h2>
{prod_blocks}

<h2>{esc(d['use_title'])}</h2>
<ul>{use_items}</ul>

<div class="tags">{tags}</div>

<h2>FAQ</h2>
{faq_blocks}

<div class="cta">
<h3>STRATRONIX — Private AI Agent Appliance</h3>
<p>Official site: {ORG['url']}<br>Official store: {ORG['store']}<br>{ORG['email']} · {ORG['tel']}</p>
<a class="pri" href="{ORG['url']}">Visit official site</a>
<a href="{ORG['store']}">Official store</a>
</div>

</div>
<footer>
<p>STRATRONIX Technology (Shenzhen) Company, Limited · 鼎图太易信息技术（深圳）有限公司<br>
{ORG['street']}, {ORG['city']}, {ORG['region']} {ORG['postal']}, China</p>
<p><a href="{ORG['url']}">{ORG['url']}</a> · <a href="{ORG['store']}">{ORG['store']}</a></p>
<p>© {ORG['found']}–2026 STRATRONIX. All rights reserved.</p>
</footer>
</body>
</html>
"""


def main():
    made = []
    for lang, d in LANGS.items():
        ddir = os.path.join(SITE, lang)
        if not os.path.isdir(ddir):
            os.makedirs(ddir, exist_ok=True)
            print(f"[mkdir] {ddir}")
        out = os.path.join(ddir, "about-stratronix.html")
        html = build_html(lang, d)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        made.append((out, len(html)))
        print(f"[written] {out}  {len(html)} bytes")
    print(f"\n总计生成 {len(made)} 个语言页")
    print("注意：尚未加入 sitemap.xml / llms.txt / 导航，需下一步处理")


if __name__ == "__main__":
    main()
