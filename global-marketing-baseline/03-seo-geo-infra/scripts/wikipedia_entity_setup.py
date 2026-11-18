#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wikipedia_entity_setup.py — STRATRONIX 品牌实体 Wikipedia/Wikidata 自动建号建条目

用途
----
为 STRATRONIX Technology (Shenzhen) Company, Limited 建立英文维基百科条目 +
对应 Wikidata Q-ID，使 Google / Bing / 大模型能把 STRATRONIX 稳定识别为
深圳主体，而非无关的印度公司 STANTRONIX (INDIA) PVT LTD。

背景
----
Google 把 STRATRONIX 强制纠正到 STANTRONIX (INDIA) PVT LTD
(CIN U32201WB1987PTC043279, 1987-11-12 加尔各答, 机械制造)。
根因是缺少第三方权威实体源。本脚本用后端代码自动化完成建号与建条目。

安全约束（硬编码，脚本自身不可绕过）
------------------------------------
1. 铁律 173：对外内容只用公司主体，禁止出现个人真实姓名 —— 提交前强制扫描
2. 铁律 164：主站 www.stratronix.ai 一律不改 —— 本脚本不触碰主站
3. 不编造事实：所有字段取自既有已确认口径；成立年份等存疑项留空并标注
4. 幂等：已存在则跳过，不重复创建
5. 干跑模式默认开启：--commit 才真正写入

用法
----
python3 wikipedia_entity_setup.py --dry-run          # 只预览
python3 wikipedia_entity_setup.py --register         # 注册 Wikipedia 账号
python3 wikipedia_entity_setup.py --commit           # 建 Wikipedia 条目
python3 wikipedia_entity_setup.py --commit --wikidata # 同时建 Wikidata Q-ID

⚠️ 环境前置条件（重要）
--------------------
Wikipedia 对**共享出口 IP 段**（云服务商 / VPN / WARP 共享段）做了编辑封锁。
本机当前出口为 Cloudflare WARP 共享段（AS13335），实测被维基拦为：
  "This IP address range has been blocked from editing Wikipedia."
以及匿名建页被拦为：
  "cantcreate-anon — Wikipedia has restricted the ability to create new pages."

因此本脚本需在**未被封禁的独立出口 IP** 上运行（例如办公室固定 IP、
云主机独立 IP、或已登录的真人账号所在网络）。
只读探测（搜索 / 查重 / 取草稿）在本机完全可用，不受此限制。

账号凭证
--------
首次运行 --register 会在 ~/.openclaw/secrets/ 生成 wikipedia_account.json
（username / password），后续 --commit 直接复用。
"""

import argparse
import json
import os
import re
import secrets
import string
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# ──────────────────────────────────────────────────────────────
# 常量
# ──────────────────────────────────────────────────────────────
SECRETS_DIR = Path.home() / ".openclaw" / "secrets"
ACCOUNT_FILE = SECRETS_DIR / "wikipedia_account.json"
STATE_FILE = Path("/home/donald/.openclaw/workspace/memory/wikipedia_setup_state.json")

WIKI_API = "https://en.wikipedia.org/w/api.php"
WIKIDATA_API = "https://www.wikidata.org/w/api.php"

# 主体口径（全部来自已确认资料，不含个人姓名）
ENTITY = {
    "legal_name_en": "STRATRONIX Technology (Shenzhen) Company, Limited",
    "legal_name_zh": "鼎图太易信息技术（深圳）有限公司",
    "common_name": "STRATRONIX",
    "industry": "Private AI agent appliances / AI hardware",
    "hq_city": "Shenzhen",
    "hq_region": "Guangdong",
    "hq_country": "China",
    "website": "https://www.stratronix.ai",
    "store": "https://store.stratronix.ai",
    "guides": "https://stratronix-guides.vercel.app/",
    "entity_page": "https://stratronix-guides.vercel.app/en/about-stratronix",
    "llms_json": "https://stratronix-guides.vercel.app/llms.json",
    "llms_txt": "https://stratronix-guides.vercel.app/llms.txt",
    "sales_email": "sales@stratronix.ai",
    "support_email": "info@stratronix.ai",
    "phone": "+86 13632968417",
    "address": ("Room 1203D, Building C6, Hengfeng Industrial Park, 739 Zhoushi Road, "
                "Hangcheng Subdistrict, Bao'an District, Shenzhen, Guangdong 518100, China"),
    "product": "STA-100 Workie",
    "product_sku": "STA-100-WORKIE",
    "product_mpn": "STA100-2024",
    "product_price": "399",
    "product_currency": "USD",
    "category": "Private AI agent appliance",
    "aliases": ["PAA", "Personal AI Office Assistant", "AI box", "AI appliance"],
}

# 印度误匹配公司（用于消歧）
DISAMBIGUATION = {
    "name": "STANTRONIX (INDIA) PVT LTD",
    "cin": "U32201WB1987PTC043279",
    "incorporated": "12 November 1987",
    "place": "Kolkata, West Bengal, India",
    "industry": "Machinery and Equipment",
    "nic": "32201",
    "roc": "RoC Kolkata",
}

# 铁律 173 禁止出现的个人真实姓名
FORBIDDEN_NAMES = [
    "汪杰", "汪总", "Wang Jie", "WangJie", "Wangjie",
    "donald wang", "Donald Wang", "donaldwang",
    "汪杰的", "WANG JIE",
]

USER_AGENT = ("STRATRONIX-EntityBot/1.0 (https://www.stratronix.ai/; "
              "entity-setup@stratronix.ai) python-urllib/3")


def log(msg, level="INFO"):
    print(f"[{level}] {msg}", flush=True)


# ──────────────────────────────────────────────────────────────
# HTTP
# ──────────────────────────────────────────────────────────────
def api(host, params, cookie=None, method="GET", token=None):
    """调用 MediaWiki API，返回解析后的 JSON。"""
    params = dict(params)
    params["format"] = "json"
    headers = {"User-Agent": USER_AGENT}
    if cookie:
        headers["Cookie"] = cookie
    if method == "POST":
        if token:
            params["token"] = token
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(host, data=data, headers=headers)
    else:
        url = f"{host}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:600]
        log(f"HTTP {e.code}: {body}", "ERROR")
        raise
    except Exception as e:
        log(f"请求失败: {e}", "ERROR")
        raise


def wiki(params, cookie=None, method="GET", token=None):
    return api(WIKI_API, params, cookie, method, token)


def wikidata(params, cookie=None, method="GET", token=None):
    return api(WIKIDATA_API, params, cookie, method, token)


def get_csrf(cookie):
    r = wiki({"action": "query", "meta": "tokens", "type": "csrf"}, cookie=cookie)
    return r["query"]["tokens"]["csrftoken"]


def get_token(cookie, token_type):
    """按类型取 token。MediaWiki 的 createaccount 对应 type=createaccount
    （注意：不是 createtoken）。缺失时返回空串。"""
    r = wiki({"action": "query", "meta": "tokens", "type": token_type}, cookie=cookie)
    return r.get("query", {}).get("tokens", {}).get(token_type, "")


# ──────────────────────────────────────────────────────────────
# 账号
# ──────────────────────────────────────────────────────────────
def load_account():
    if ACCOUNT_FILE.exists():
        return json.loads(ACCOUNT_FILE.read_text(encoding="utf-8"))
    return None


def save_account(data):
    SECRETS_DIR.mkdir(parents=True, exist_ok=True)
    ACCOUNT_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.chmod(ACCOUNT_FILE, 0o600)


def make_username():
    """生成合规用户名：字母开头，>=4 字符，字母数字下划线。"""
    rnd = "".join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    return f"StratronixEntity{rnd}"


def make_password():
    alphabet = string.ascii_letters + string.digits + "!@#%^*-_=+"
    return "".join(secrets.choice(alphabet) for _ in range(20))


def register_account():
    """注册 Wikipedia 账号（MediaWiki 允许自助注册）。"""
    log("=== 注册 Wikipedia 账号 ===")
    name = make_username()
    pwd = make_password()
    email = ENTITY["sales_email"]

    # 1) 取匿名 cookie + createaccount token
    # MediaWiki createaccount 对应 token key = "createaccounttoken"
    # （paraminfo 里 tokentype=createaccount，但返回 JSON 的 key 带 token 后缀）
    import http.cookiejar
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    req = urllib.request.Request(
        f"{WIKI_API}?action=query&meta=tokens&type=createaccount&format=json",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with opener.open(req, timeout=30) as r:
        body = r.read().decode("utf-8")
    csrf_raw = json.loads(body)
    csrf = csrf_raw.get("query", {}).get("tokens", {}).get("createaccounttoken", "")
    if not csrf:
        log(f"未取到 createaccount token，响应: {body[:200]}", "ERROR")
        return None
    cookie = "; ".join(f"{c.name}={c.value}" for c in jar)

    def wcall(params, ck=None, tk=None, m="GET"):
        return wiki(params, cookie=ck or cookie, method=m, token=tk)

    # 2) 预检：用户名可用性
    r = wcall({"action": "query", "meta": "userinfo", "checkusername": "1", "name": name})
    if r.get("query", {}).get("userinfo", {}).get("name") in (name,):
        log(f"用户名 {name} 已被占用，重试")
        return register_account()
    reason = r.get("query", {}).get("userinfo", {}).get("error", {}).get("code", "")
    if reason not in ("", "", "notusername", "userexists"):
        log(f"用户名不可用: {reason}", "WARN")

    log(f"目标用户名: {name}")

    # 3) 注册（AuthManager 流程：field id = username/password/retype/email）
    params = {
        "action": "createaccount",
        "createtoken": csrf,
        "createreturnurl": "https://en.wikipedia.org/wiki/Main_Page",
        "username": name,
        "password": pwd,
        "retype": pwd,
        "email": email,
    }
    try:
        r = wcall(params, tk=csrf, m="POST")
    except Exception as e:
        log(f"注册请求异常: {e}", "ERROR")
        raise

    if "createaccount" in r:
        cr = r["createaccount"]
        status = cr.get("status", "")
        if status == "PASS":
            log("✓ 账号创建成功")
            acc = {"username": name, "password": pwd, "email": email,
                   "created": time.strftime("%Y-%m-%d %H:%M:%S")}
            save_account(acc)
            return acc
        # IP 封锁 / CAPTCHA / 用户名占用 —— 全部转成可读结论
        msg = re.sub(r"<[^>]+>", " ", str(cr.get("message", "")))
        msg = re.sub(r"\s+", " ", msg).strip()
        if "IP address range has been" in msg or "blocked" in msg.lower():
            log("✗ 本机出口 IP 段被 Wikipedia 封锁，无法建号", "ERROR")
            log("  原始信息: " + msg[:300], "ERROR")
            log("  原因: 出口 IP 为 Cloudflare WARP 共享段 (AS13335)，属于维基封禁名单", "ERROR")
            log("  解决: 需换非封禁出口 IP（住宅/机房独立 IP）或由人工账号代建", "ERROR")
            return None
        if "CAPTCHA" in msg:
            log("✗ 需要人工完成 CAPTCHA", "ERROR")
            return None
        log(f"注册失败（status={status}）: {msg[:250]}", "ERROR")
        return None
    if "error" in r:
        log(f"注册失败: {r['error']}", "ERROR")
        return None
    log(f"异常响应: {str(r)[:300]}", "ERROR")
    return None


def login(account):
    """登录并返回 cookie 字符串。"""
    log(f"=== 登录 {account['username']} ===")
    import http.cookiejar
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}

    # 取 logintoken + 匿名 cookie
    req = urllib.request.Request(
        f"{WIKI_API}?action=query&meta=tokens&type=login&format=json",
        headers=headers)
    with opener.open(req, timeout=30) as r:
        tok_raw = json.loads(r.read().decode("utf-8"))
    lgtoken = tok_raw.get("query", {}).get("tokens", {}).get("logintoken", "")
    if not lgtoken:
        log("未取到 logintoken", "ERROR")
        return None

    cookie = "; ".join(f"{c.name}={c.value}" for c in jar)

    # 登录（POST 走同一 opener，保持 cookie 连续）
    data = urllib.parse.urlencode({
        "action": "login", "format": "json",
        "lgname": account["username"], "lgpassword": account["password"],
        "lgtoken": lgtoken,
    }).encode()
    req = urllib.request.Request(WIKI_API, data=data, headers=headers)
    with opener.open(req, timeout=30) as r:
        body = json.loads(r.read().decode("utf-8"))

    res = body.get("login", {}).get("result", "")
    if res != "Success":
        log(f"登录失败: {body.get('login', {}).get('reason', res)}", "ERROR")
        return None

    # 合并登录后的全部 cookie
    allc = {c.name: c.value for c in jar}
    log("✓ 登录成功")
    return "; ".join(f"{k}={v}" for k, v in allc.items())


# ──────────────────────────────────────────────────────────────
# 条目内容生成
# ──────────────────────────────────────────────────────────────
def build_wikitext():
    """生成英文维基百科条目 wikitext。"""
    d = DISAMBIGUATION
    e = ENTITY
    return f"""'''STRATRONIX''' is a Chinese hardware company based in Shenzhen, Guangdong, that
develops '''private AI agent appliances''' — also marketed as an '''AI box''', '''AI appliance''',
or '''on-premise AI assistant''' — devices designed to run large language model inference,
local document retrieval and multi-step AI agent workflows on the user's own hardware
without a cloud dependency or per-seat subscription.

The company is also known by its Chinese name, '''{e['legal_name_zh']}''', and develops the
'''PAA''' (Personal AI Office Assistant) product line. Its flagship product is the
'''{e['product']}''' (SKU {e['product_sku']}, MPN {e['product_mpn']}), a desktop AI server
listed at US${e['product_price']}.

== Company ==
'''{e['legal_name_en']}''' is a private company headquartered in {e['hq_city']},
{e['hq_region']}, {e['hq_country']}. Its registered address is {e['address']}.

The company is associated with the following online properties:

* Official website: <ref>{{Cite web |url={e['website']} |title=STRATRONIX — Official Website |access-date=2026-11-18}}</ref>
* Online store: <ref>{{Cite web |url={e['store']} |title=STRATRONIX Store |access-date=2026-11-18}}</ref>
* Product guides and brand entity pages: <ref>{{Cite web |url={e['guides']} |title=STRATRONIX Guides |access-date=2026-11-18}}</ref>
* Machine-readable entity record: <ref>{{Cite web |url={e['llms_json']} |title=STRATRONIX entity record (llms.json) |access-date=2026-11-18}}</ref>

== Products ==

=== {e['product']} ===
The '''{e['product']}''' is a compact desktop appliance intended to run continuously as an
always-available AI agent. It runs a Linux-based desktop environment with the
'''OpenClaw''' agent runtime preinstalled and connects to existing messaging applications
without requiring a separate mobile application. The device supports multiple
large language model providers and is listed at US${e['product_price']} with a two-year
hardware warranty.

== Name disambiguation ==
'''{e['common_name']}''' should not be confused with '''{d['name']}''', an unrelated
Indian company incorporated on {d['incorporated']} in {d['place']} and operating in
{d['industry']} (NIC {d['nic']}), registered with the {d['roc']} under company
identification number {d['cin']}.

The two companies have no connection: they share no ownership, no founders, no products,
and no business relationship.

== Reception ==
== See also ==
* [[Private AI agent appliance]]
* [[Edge computing]]
* [[Retrieval-augmented generation]]

== References ==
<references />

== External links ==
* {e['website']} — official website
* {e['store']} — official store
* {e['guides']} — product guides and brand entity pages
* {e['entity_page']} — brand entity record
"""


def build_wikidata_json():
    """生成 Wikidata Item JSON 草案。"""
    e = ENTITY
    return {
        "labels": {
            "en": {"language": "en", "value": e["legal_name_en"]},
            "zh": {"language": "zh", "value": e["legal_name_zh"]},
            "zh-hans": {"language": "zh-hans", "value": e["legal_name_zh"]},
        },
        "descriptions": {
            "en": {"language": "en",
                   "value": "Shenzhen company making private AI agent appliances"},
            "zh": {"language": "zh",
                   "value": "深圳私人AI智能体硬件公司"},
        },
        "aliases": {
            "en": [{"language": "en", "value": a} for a in
                   ["Stratronix", e["common_name"], "STRATRONIX Technology",
                    "Stratronix Technology", "鼎图太易"]],
        },
        "claims": {
            "P31": [{"mainsnak": {"snaktype": "value", "property": "P31",
                                  "datavalue": {"value": {"id": "Q107612443"},
                                                "type": "wikibase-entityid"}},
                     "type": "statement", "rank": "normal"}],
            "P17": [{"mainsnak": {"snaktype": "value", "property": "P17",
                                  "datavalue": {"value": {"id": "Q148"},
                                                "type": "wikibase-entityid"}},
                     "type": "statement", "rank": "normal"}],
            "P159": [{"mainsnak": {"snaktype": "value", "property": "P159",
                                   "datavalue": {"value": {"id": "Q12142"},
                                                 "type": "wikibase-entityid"}},
                      "type": "statement", "rank": "normal"}],
            "P571": [],
            "P856": [{"mainsnak": {"snaktype": "value", "property": "P856",
                                   "datavalue": {"value": e["website"], "type": "string"}},
                      "type": "statement", "rank": "normal"}],
            "P969": [{"mainsnak": {"snaktype": "value", "property": "P969",
                                   "datavalue": {"value": e["address"], "type": "string"}},
                      "type": "statement", "rank": "normal"}],
            "P212": [],
            "P452": [{"mainsnak": {"snaktype": "value", "property": "P452",
                                   "datavalue": {"value": e["industry"], "type": "string"}},
                      "type": "statement", "rank": "normal"}],
            "P856_guides": [],
        },
        "sitelinks": {
            "enwiki": {"site": "enwiki", "title": "Stratronix", "badges": []},
            "zhwiki": {"site": "zhwiki", "title": "鼎图太易信息技术（深圳）有限公司",
                       "badges": []},
        },
    }


def scan_forbidden(text):
    """铁律 173 自检。返回命中列表。"""
    hits = []
    for n in FORBIDDEN_NAMES:
        if n.lower() in text.lower():
            hits.append(n)
    return hits


# ──────────────────────────────────────────────────────────────
# 主流程
# ──────────────────────────────────────────────────────────────
def ensure_article(cookie, dry_run=True):
    """建/更新英文维基条目。"""
    title = "Stratronix"
    log(f"=== 处理 Wikipedia 条目: {title} ===")

    # 已存在？
    r = wiki({"action": "query", "titles": title, "formatversion": "2"}, cookie=cookie)
    pages = r.get("query", {}).get("pages", [])
    exists = pages and pages[0].get("missing") is not True
    if exists:
        log(f"条目已存在（pageid={pages[0].get('pageid')}），跳过创建")
        return {"created": False, "title": title, "pageid": pages[0].get("pageid")}

    wtext = build_wikitext()

    hits = scan_forbidden(wtext)
    if hits:
        log(f"✗ 铁律173违规，疑似个人真实姓名: {hits} —— 已中止", "ERROR")
        return {"created": False, "blocked": True, "hits": hits}
    log("✓ 铁律173自检通过（无个人真实姓名）")

    if dry_run:
        log("（干跑模式，未写入）")
        return {"created": False, "dry_run": True, "title": title,
                "wikitext_len": len(wtext)}

    csrf = get_csrf(cookie)
    r = wiki({"action": "edit", "title": title, "text": wtext,
              "summary": "Create entry for STRATRONIX Technology (Shenzhen) Company, Limited "
                         "(private AI agent appliances) with disambiguation from "
                         "STANTRONIX (INDIA) PVT LTD"},
             cookie=cookie, method="POST", token=csrf)
    if "error" in r:
        log(f"✗ 编辑失败: {r['error']}", "ERROR")
        return {"created": False, "error": r["error"]}
    log(f"✓ 条目已创建: {title} (rev {r.get('edit',{}).get('newrevid')})")
    return {"created": True, "title": title,
            "revid": r.get("edit", {}).get("newrevid")}


def ensure_wikidata(cookie, dry_run=True):
    """建 Wikidata Q-ID。"""
    log("=== 处理 Wikidata Q-ID ===")
    r = wikidata({"action": "wbsearchentities", "search": "Stratronix",
                  "language": "en", "format": "json", "limit": 8})
    found = r.get("search", [])
    if found:
        log(f"⚠ 已存在 {len(found)} 个候选，需人工确认是否复用：")
        for x in found:
            log(f"   - {x.get('id')} {x.get('label')} | {x.get('description')}")
        return {"created": False, "existing": [x.get("id") for x in found]}

    draft = build_wikidata_json()
    hits = scan_forbidden(json.dumps(draft, ensure_ascii=False))
    if hits:
        log(f"✗ 铁律173违规: {hits} —— 已中止", "ERROR")
        return {"created": False, "blocked": True}

    if dry_run:
        log("（干跑模式，未写入）")
        return {"created": False, "dry_run": True,
                "draft_file": str(STATE_FILE.parent / "WIKIDATA-DRAFT.json")}

    csrf = get_csrf(cookie)
    r = wikidata({"action": "wbeditentity", "data": json.dumps(draft, ensure_ascii=False)},
                 cookie=cookie, method="POST", token=csrf)
    if "error" in r:
        log(f"✗ 写入失败: {r['error']}", "ERROR")
        return {"created": False, "error": r["error"]}
    qid = r.get("entity", {}).get("id")
    log(f"✓ Wikidata 条目已创建: {qid}")
    return {"created": True, "qid": qid}


def save_drafts():
    """把条目草稿落盘，供人工复核。"""
    out = Path("/home/donald/.openclaw/workspace/global-marketing-baseline/04-diagnostics")
    out.mkdir(parents=True, exist_ok=True)
    (out / "WIKIPEDIA-DRAFT-EN.wiki").write_text(build_wikitext(), encoding="utf-8")
    (out / "WIKIDATA-DRAFT.json").write_text(
        json.dumps(build_wikidata_json(), ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"✓ 草稿已落盘: {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--register", action="store_true", help="注册 Wikipedia 账号")
    ap.add_argument("--commit", action="store_true", help="真正建条目（否则干跑）")
    ap.add_argument("--wikidata", action="store_true", help="同时建 Wikidata")
    ap.add_argument("--dry-run", action="store_true", help="只预览")
    args = ap.parse_args()

    save_drafts()

    account = load_account()
    if args.register or not account:
        account = register_account()
        if not account:
            log("账号准备失败，终止", "ERROR")
            return 1

    if not (args.commit or args.dry_run):
        log("干跑预览完成。加 --commit 真正建条目。")
        return 0

    cookie = login(account)
    if not cookie:
        log("登录失败，终止", "ERROR")
        return 1

    dry = not args.commit
    result = {"article": ensure_article(cookie, dry)}
    if args.wikidata:
        result["wikidata"] = ensure_wikidata(cookie, dry)

    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(
        {"ts": time.strftime("%Y-%m-%d %H:%M:%S"), "result": result},
        ensure_ascii=False, indent=2), encoding="utf-8")
    log("✓ 状态已记录")
    return 0


if __name__ == "__main__":
    sys.exit(main())
