# Online Shop Dashboard (shop.html)

**Live URLs (after Vercel deploy)**:
- EN: `https://www.stratronix.ai/en/shop.html`
- ZH: `https://www.stratronix.ai/zh/shop.html`

## 5 Modules

| # | Module | Data source | Status |
|---|--------|-------------|--------|
| 1 | Store URLs | Static list | ✅ Live (Vercel + trycloudflare + pending stratonix.ai) |
| 2 | PayPal | PayPal Orders API | ⏳ Awaiting client_id + secret |
| 2b | Invoice generator | Manual form (PDF) | ✅ Form ready, real PDF when PayPal wired |
| 3 | Product catalog | `/api/products` (live) | ✅ 10 products live |
| 4 | Traffic analytics | Google Analytics 4 | ⏳ Awaiting GA4 measurement ID |
| 5 | Roadmap | AI-generated + manual | ✅ 7 items (P0/P1/P2/P3) |

## Files added/modified

- `en/shop.html` (new, 28 KB)
- `zh/shop.html` (new, 26 KB)
- `en/index.html` (nav + CTA + Online Shop button)
- `en/products.html` (nav + main CTA → shop)
- `zh/index.html` (nav + CTA + 在线商店 button)
- `zh/products.html` (nav + main CTA → shop)

## To deploy

```bash
cd /home/donald/.openclaw/workspace/stratronix-website-new
git add en/shop.html zh/shop.html en/index.html en/products.html zh/index.html zh/products.html
git commit -m "Add Online Shop Dashboard"
git push origin main   # Vercel auto-deploys from GitHub
```

## To enable PayPal/Analytics

Add to Railway backend env:
```
PAYPAL_CLIENT_ID=
PAYPAL_CLIENT_SECRET=
GA4_MEASUREMENT_ID=
GA4_API_SECRET=
```

Then update `shop.html` JS to fetch from new backend endpoints.
