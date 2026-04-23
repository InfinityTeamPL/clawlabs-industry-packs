# Portale HR — programistyczny dostęp (zweryfikowane 2026-04-22)

## 1. Otwarte RSS/Atom (działają, zwracają XML z itemami)

| Portal | Feed URL | Ostatni wpis | Cadence |
|---|---|---|---|
| Money.pl (ogólny) | https://www.money.pl/rss/ | 2026-04-22 | kilka/dzień |
| Legalis (C.H. Beck) | https://legalis.pl/feed/ | 2026-04-21 | codziennie, 3-5/dzień |
| Kadromierz (blog) | https://kadromierz.pl/blog/feed/ | 2026-02-24 | 2-4/miesiąc |

**Przykład Legalis:**
```xml
<item><title>200 tys. zł za podszywanie się pod radcę prawnego</title>
<link>https://legalis.pl/200-tys-zl-za-podszywanie-sie-pod-radce-prawnego/</link>
<pubDate>Tue, 21 Apr 2026 06:14:28 +0000</pubDate>
<category>Prawo gospodarcze</category>
```

## 2. Sitemap XML (Google News format — alternatywa dla RSS)

| Portal | URL | Uwagi |
|---|---|---|
| Prawo.pl (Wolters Kluwer) | https://prawo.pl/sitemap_news.xml | sekcja `/kadry/`, `news:publication_date` |
| Poradnikprzedsiębiorcy | https://poradnikprzedsiebiorcy.pl/sitemap.xml | index → articlesFirstPart...NinthPart |
| portalkadrowy.pl | https://www.portalkadrowy.pl/sitemap.xml.gz | dostępny |

**Przykład Prawo.pl kadry:**
```xml
<loc>https://www.prawo.pl/kadry/promocja-zmian-w-ustawie-o-pip-mrpips-o-kotkach,1543291.html</loc>
<news:publication_date>2026-04-21T17:00:00+02:00</news:publication_date>
```

## 3. Brak RSS/API — tylko HTML scrape

- **kadry.infor.pl** — `/feed`, `/rss` → 301 na infor.pl (brak feedu), listing HTML dostępny
- **gazetaprawna.pl** — wszystkie RSS/sitemap 404, robots.txt dopuszcza scraping poza `/szukaj`, `/ajax/`, `/api/`, `/drukowanie/`
- **rp.pl, praca.gov.pl, podatki.gov.pl** — brak feedów; `podatki.gov.pl` ma `<meta robots="noindex, nofollow">`
- **prawo.pl/feed, lex.pl/feed** — 404 (publiczny feed tylko przez sitemap_news)

## 4. Paywall / licencja

- **portalkadrowy.pl** (ex serwiskadrowy.pl) — paywall; robots dopuszcza indeksowanie
- **legalis.pl** — publiczny blog; SIP odrębnie płatny
- **lex.pl / prawo.pl** — newsy otwarte, komentarze/orzecznictwo za paywallem
- **gazetaprawna.pl, rp.pl, money.pl** — częściowy paywall (premium)
- **kadromierz.pl** — blog marketingowy, otwarty; ToS nie zezwala wprost na komercyjne re-use (wymaga cytatu + link wg art. 29 pr.aut.)
- **poradnikprzedsiebiorcy.pl** — regulamin ifirma.pl/wfirma, zakaz kopiowania bez zgody

## 5. Oficjalne REST API do aktualności

Żaden z listy **nie** wystawia publicznego REST API. Wolters Kluwer (lex/prawo.pl) i C.H. Beck (legalis) mają komercyjne SIP API tylko dla subskrybentów.

## 6. Feedy gotowe do cron-pull

```
https://legalis.pl/feed/
https://kadromierz.pl/blog/feed/
https://www.money.pl/rss/
https://prawo.pl/sitemap_news.xml
https://poradnikprzedsiebiorcy.pl/sitemap.xml
https://www.portalkadrowy.pl/sitemap.xml.gz
```
