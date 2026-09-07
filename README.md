<!-- generated from README.template.md - do not edit -->
<div align="center">

# Muhammad Saad Shafiq

### Senior Full Stack Engineer

**Lahore, Pakistan** · Open to roles and contract work

<a href="https://devsaadshafiq.vercel.app">
  <img src="https://img.shields.io/badge/Portfolio-devsaadshafiq.vercel.app-ff7a2f?style=for-the-badge&logoColor=white" alt="Portfolio"/>
</a>
<a href="mailto:dev.saadshafiq@gmail.com">
  <img src="https://img.shields.io/badge/Email-dev.saadshafiq%40gmail.com-6b3410?style=for-the-badge&logo=gmail&logoColor=ff7a2f" alt="Email"/>
</a>
<a href="https://www.linkedin.com/in/dev-saad-shafiq">
  <img src="https://img.shields.io/badge/LinkedIn-dev--saad--shafiq-6b3410?style=for-the-badge&logo=linkedin&logoColor=ff7a2f" alt="LinkedIn"/>
</a>

</div>

---

I build **payments- and identity-heavy products end to end**, where money and
regulation make the work hard. School canteens in Saudi Arabia taking payment
from a child's palm. A toll plaza on the Detroit–Windsor commercial crossing. A
licensed sportsbook in Tennessee. Founding member of an AI platform for
construction bidding, now leading its frontend and backend with a team of five.

## Live in the world

Four systems I built are in production right now. Open any of them.

| System | What it does | |
|---|---|---|
| **Ambassador Bridge** | Toll payment and plaza lane control at the busiest US–Canada commercial crossing. Two apps: a geo-fenced driver wallet, and a plaza console for vehicle classification, ticketing, signboards and gates. | [ambassadorbridge.com](https://www.ambassadorbridge.com/) |
| **Schoollet** | School payments live across Saudi Arabia. Virtual student wallets, parent-controlled spending limits, and canteen tills that take QR **or a palm**. | [schoollet.com.sa](https://schoollet.com.sa/) |
| **VIP Play** | Licensed sportsbook for the regulated Tennessee market. Geofenced play boundaries, KYC onboarding, golden test suites. | [vipplayinc.com](https://vipplayinc.com/) |
| **Enteyoes** | Gym platform in Lahore. Four services built solo — Flutter app, FastAPI backend, Next.js console, and an OCR service that reads ID cards so members sign up from home. | [enteyoes.com](https://enteyoes.com/) |

<div align="center">

<img src="https://img.shields.io/badge/3.5_years-shipping_production_software-ff7a2f?style=flat-square" alt="3.5 years shipping production software"/>
<img src="https://img.shields.io/badge/5-engineers_led-6b3410?style=flat-square" alt="5 engineers led"/>
<img src="https://img.shields.io/badge/1-international_border_crossing-6b3410?style=flat-square" alt="1 international border crossing"/>
<img src="https://img.shields.io/badge/500%2B-users_on_palm_vein_payments-6b3410?style=flat-square" alt="500+ users on palm-vein payments"/>

</div>

## Selected work

**DiPGOS** — *INDUS Technologies · founding member, leading five · in pilot with WAPDA*

An AI platform taking a civil-construction tender from automated bid design
through to progress control on site. I wrote its document intelligence layer: a
tender package is prose specifications, cost spreadsheets and CAD drawings in one
folder, so every file is classified by title and type first, then routed to the
treatment its own type needs. Embedded at 384 dimensions into pgvector, answered
with hybrid keyword-and-semantic search fused by reciprocal rank — plus a
calculator tool, so figures in an answer are computed rather than generated.
→ [industechsol.com/#dipgos](https://industechsol.com/#dipgos)

**Ambassador Bridge toll system** — *Omnisoft · sole developer · in use at the crossing*

Commercial trucks cannot stop to fumble with an app, and the plaza cannot stop
working because one driver lost signal. So the driver side debits on geofence
entry, and the plaza console holds truth over real-time sockets — keeping a lane
running from its own state when the driver side drops off.

**Schoollet** — *Zentech Solutions · architected it, then took over delivery*

Every payment method available to a seven-year-old fails the same two ways: cards
get lost and PINs get forgotten. Both are unworkable at a till with a lunch queue
behind it. So: palm-vein biometrics, wired through native Android libraries into
both the enrolment app and the point-of-sale scanner. Nothing to carry, nothing
to remember. Live across 5+ schools and 10+ canteens with 500+ users.

**Enteyoes** — *independent client work · sole developer, four services*

425 commits in five weeks. The one system here not covered by an NDA — the code,
the live product and the architecture are all mine to show and discuss in full.

**Data acquisition suite** — *Zentech Solutions · sole developer*

25+ production scrapers across e-commerce, property, travel and recruitment.
Throughput held at 50,000 property listings per eight-hour run and 8,000 review
pages in under ten minutes, on GCP and AWS with output routed into BigQuery.

> Everything above except Enteyoes was built under NDA. Those systems are
> described and linked rather than shown — no code, no internal screenshots, no
> client data. What I can discuss is the engineering: the constraints, the
> architecture and the tradeoffs, which is what the write-ups on my
> [portfolio](https://devsaadshafiq.vercel.app) cover.

## Stack

Grouped by what it shipped, not by what I have heard of.

**Mobile** — Flutter, Dart, Android (Java/Kotlin), Clean Architecture, BLoC, unit and golden testing, SQLite
<br>*Shipped: Ambassador Bridge · Schoollet · VIP Play*

<img src="https://skillicons.dev/icons?i=flutter,dart,kotlin,java,androidstudio,sqlite" alt="Flutter, Dart, Kotlin, Java, Android Studio, SQLite"/>

**Backend** — Python, FastAPI, Django, Node.js, Express, Laravel/PHP, REST APIs, GraphQL
<br>*Shipped: Enteyoes · DiPGOS · Schoollet*

<img src="https://skillicons.dev/icons?i=py,fastapi,django,nodejs,express,laravel,php,graphql" alt="Python, FastAPI, Django, Node.js, Express, Laravel, PHP, GraphQL"/>

**Payments & identity** — Stripe, Telr, Apple In-App Purchase, virtual wallets, KYC verification, geofencing, palm-vein biometrics
<br>*Shipped: Schoollet · Ambassador Bridge · VIP Play*

**AI in production** — RAG pipelines, pgvector, sentence-transformers, LLM prompt engineering, Google Document AI, OCR (EasyOCR, Tesseract), OpenCV
<br>*Shipped: DiPGOS document intelligence · Enteyoes OCR service*

<img src="https://skillicons.dev/icons?i=opencv,selenium" alt="OpenCV, Selenium"/>

**Frontend** — TypeScript, React, Next.js, Tailwind CSS, deck.gl, MapLibre
<br>*Shipped: DiPGOS console · Enteyoes admin*

<img src="https://skillicons.dev/icons?i=ts,react,nextjs,tailwind" alt="TypeScript, React, Next.js, Tailwind CSS"/>

**Data & cloud** — PostgreSQL, MySQL, MongoDB, Redis, Celery, Playwright, Docker, AWS (EC2, S3), GCP, GitHub Actions, CI/CD, Datadog

<img src="https://skillicons.dev/icons?i=postgres,mysql,mongodb,redis,docker,aws,gcp,githubactions,git" alt="PostgreSQL, MySQL, MongoDB, Redis, Docker, AWS, GCP, GitHub Actions, Git"/>

## Experience

**Senior Full Stack Engineer** — INDUS Technologies, Lahore · *Jan 2026 — present · 8 months*  
Founding member of DiPGOS. Sole developer for its first two months, now leading frontend and backend platform work with a team of five.

**Full Stack Mobile App Developer** — Omnisoft, Lahore · *Aug 2024 — Jan 2026 · 1 year 5 months*  
Sole developer on the Ambassador Bridge toll system. Delivered marketplace, fintech and location-based products for European and North American clients.

**Full Stack Mobile App Developer** — Zentech Solutions, Lahore · *Jul 2023 — Aug 2024 · 1 year 1 month*  
Architected the Schoollet payments platform. Pre-launch work on a licensed US sportsbook. Built and operated 25+ production scrapers.

**Software Engineer** — New Elevation, Lahore · *Feb 2023 — Jul 2023 · 5 months*  
Supported an Oracle ATG e-commerce platform: backend log diagnosis, deployment conflicts, and SQL reporting with production-to-staging data audits.

**BSc Computer Science** — National University of Computer and Emerging Sciences (FAST-NUCES), Lahore · *2019 — 2023*

## A note on this profile

Most of what I have shipped sits in private repositories under NDA, so the
public activity graph here is a poor proxy for the work. The links above are the
better evidence — they are live systems you can open and use.

The public repositories here are mostly university coursework and small tools —
Unity games, image-processing assignments, shell scripts. They are genuinely
mine, and they are genuinely not what I do now.

If you need to see code, Enteyoes is the one I can open up, and I am happy to
walk through any of the NDA-covered systems at the architecture level.

<div align="center">
<br>

**[devsaadshafiq.vercel.app](https://devsaadshafiq.vercel.app)** · **[dev.saadshafiq@gmail.com](mailto:dev.saadshafiq@gmail.com)** · **[LinkedIn](https://www.linkedin.com/in/dev-saad-shafiq)**

<sub>Open to remote and relocation</sub>

</div>
