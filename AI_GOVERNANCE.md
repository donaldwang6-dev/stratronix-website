# AI Governance Policy — STRATRONIX-MAIN

**Status: LOCKED**
**Domain: www.stratronix.ai**
**Repository: stratronix-main (donaldwang6-dev/stratronix-website)**

---

## 1. Authority Model

The OpenClaw AI agent operating on STRATRONIX-MAIN has the following
authoritative boundaries:

- **MAIN SITE = LOCKED**
- **STORE = AUTHORIZED** (separate repository, separate AI instance)

---

## 2. Scope of AI Access on STRATRONIX-MAIN

### READ
- Read source code
- Read pages
- Read components
- Read CSS
- Read layout
- Read navigation
- Read language system
- Read redirects
- Read routes
- Read SEO
- Read metadata

### WRITE — ❌ FORBIDDEN
- Modify source code
- Modify pages
- Modify components
- Modify CSS
- Modify layout
- Modify navigation
- Modify language system
- Modify redirects
- Modify routes
- Modify SEO
- Modify metadata
- Modify database
- Modify environment variables
- Modify DNS
- Modify Vercel configuration
- Modify GitHub repository
- Modify deployment settings
- Create commits
- Create pull requests
- Merge pull requests
- Deploy production
- Revert commits
- Restore previous versions

---

## 3. The Only Exception

The AI agent may modify this main site **only when all of the following are true**:

1. The Owner has issued an **explicit, separate, written authorization**
   describing the exact files to be modified.
2. The Owner has acknowledged the modification will be deployed to
   `www.stratronix.ai` (production).
3. The modification is logged with a clear rationale in MEMORY.md.

Any ambiguity → STOP, do not guess, ask the Owner.

---

## 4. Change Classification (5 Levels)

| Level | Type | AI Handling |
|-------|------|-------------|
| LEVEL 1 | CONTENT (text, descriptions) | Direct edit allowed only with explicit authorization |
| LEVEL 2 | VISUAL (images, spacing, fonts) | Requires Owner review |
| LEVEL 3 | FUNCTIONAL (search, forms, integrations) | STOP, request approval |
| LEVEL 4 | DATABASE (schema, migrations) | STOP, request approval |
| LEVEL 5 | ARCHITECTURAL (framework rewrite, route rewrite) | STOP, request approval |

---

## 5. Version Lock Policy

The current production version is **V2.0** (preserved 2026-10-03):

```
/home/donald/文档/网站2.0-V2.0-2026-10-03/
```

V2.0 is LOCKED. Any post-V2.0 changes create new versioned folders:

```
/home/donald/文档/网站2.0-V2.X-YYYY-MM-DD/
```

Each versioned folder must include:
- MANIFEST.txt (file inventory)
- README.md (change description)

---

## 6. Iron Rules Referenced

This policy implements and supersedes all earlier rules:

- **铁律 14 / 48**: Main site strictly forbidden to modify
- **铁律 122**: Git commit LOCKED — never auto-commit multiple files
- **铁律 123**: Both sites require explicit authorization for modification
- **铁律 124**: STRATRONIX PRODUCTION ISOLATION POLICY
- **铁律 125**: V2.0 LOCKED + version backup workflow
- **铁律 126**: Forbidden git commands (`git add .`, `git reset --hard`, etc.)
- **铁律 127**: Safe git workflow (status → diff → add approved → diff cached → commit → push)
- **铁律 128**: OpenClaw 4-lock security architecture

---

## 7. Final Rule

```
MAIN SITE MUST REMAIN EXACTLY AS PRESERVED.

ONLY THE OWNER MAY AUTHORIZE CHANGES.

THE AI MUST NEVER ASSUME AUTHORITY.
```

**Approved and LOCKED by Owner: 汪杰 (Donald)**
**Effective Date: 2026-10-04**