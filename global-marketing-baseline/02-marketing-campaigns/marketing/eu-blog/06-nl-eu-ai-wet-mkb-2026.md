# BLOG 06 — NL — EU AI-Wet 2026: wat Europese MKB's moeten weten

> **Auteur:** JERRY (marketing STRATRONIX) · **Review in afwachting:** Donald Wang (CEO)
> **Status:** CONCEPT v0.1 · 2026-07-23 · **Omvang:** ~1.100 woorden
> **Distributie:** Computable · AG Connect · EU-Startups (Guest Post)
> **Compliance:** regel 31 (geen fabricage) — alleen openbare juridische bronnen

---

## De 2026-werkelijkheid voor Europese AI-gebruikers

De Europese AI-verordening (Verordening 2024/1689) is in 2025 en 2026 in fasen in werking getreden. Voor kleine en middelgrote Europese bedrijven is de praktische vraag in juli 2026 niet langer *moeten we AI inzetten*, maar *onder welke regels*. Dit artikel vat samen wat vandaag geldt, wat er op 2 augustus 2026 verandert en hoe on-premise AI-hardware — categorie vaak afgekort als PAA (Private AI-Agent Appliance) — past binnen het regelgevingskader.

## Wat vandaag geldt (juli 2026)

Drie blokken van de AI-verordening zijn al bindend:

| Blok | Inwerkingtreding | Inhoud |
|------|------------------|--------|
| **Verboden praktijken (art. 5)** | 2 februari 2025 | Social scoring, manipulerende AI, ongerichte gezichtsherkenning, realtime biometrische identificatie (met nauwe uitzonderingen) |
| **Verplichtingen voor AI voor algemeen gebruik (GPAI) (art. 50 + bijlage XI)** | 2 augustus 2025 | Aanbieders van frontier-modellen moeten trainingsdatasamenvattingen, auteursrechtrichtlijnen en systeemrisicobeoordelingen boven 10²⁵ FLOPs publiceren |
| **Transparantieverplichtingen (art. 50)** | 2 augustus 2026 | Aanbieders en gebruikers van AI-systemen die met mensen interacteren, synthetische media genereren of emotieherkenning uitvoeren, moeten AI-betrokkenheid bekendmaken |

## Wat verandert op 2 augustus 2026

Vanaf augustus 2026 is het hoog risico-classificatieregime (bijlage III) van toepassing op systemen die worden gebruikt in:

- **Kritieke infrastructuur** (water, gas, elektriciteit, verkeer)
- **Onderwijs en beroepsopleiding** (toelating, evaluatie, examenuistrekenheid)
- **Werk** (CV-screening, taaktoewijzing, monitoring)
- **Essentiële openbare en private diensten** (kredietscoring, verzekeringstarifering, noodhulp, publieke voorzieningen)
- **Handhaving en migratie** (risicobeoordelingen, leugendetectors, bewijswaarde)
- **Justitie en democratische processen** (rechterlijke bijstand, kiezersbeïnvloeding)

Hoog risico-systemen moeten voldoen aan eisen rond datakwaliteit, technische documentatie, menselijk toezicht, robuustheid, cybersecurity en conformiteitsbeoordeling voordat ze op de EU-markt worden geplaatst of in gebruik worden gesteld.

## Waar alleen-cloud AI-stacks moeite hebben

In de cloud gehoste AI van niet-Europese aanbieders beantwoordt drie vragen slecht onder dit regime:

1. **Waar leven de data fysiek?** — Als het inferentiepad grenzen overschrijdt (VS, China, Singapore), zijn de overdrachtsmechanismen van Hoofdstuk V AVG van toepassing.
2. **Wie is aanbieder, wie is gebruiker?** — Artikel 25 herverdeelt de verantwoordelijkheid langs de keten. Een Nederlands MKB dat de OpenAI-API gebruikt, kan nog steeds worden geclassificeerd als gebruiker van een hoog risico-systeem.
3. **Wat vereist artikel 14 (menselijk toezicht) wanneer het model een gehoste API is?** — Praktische interventie, override en logging zijn lastiger bij stateless endpoints.

## On-premise AI als compliance-hefboom

Een hardware-appliance die een groot taalmodel volledig binnen de dataruimte van de klant draait — zonder uitgaande API-aanroepen en zonder externe trainingsdata-egress — verandert het operationele antwoord op alle drie de vragen:

- **Data-localisatie:** 100% binnen het bedrijfsnetwerk. De modelgewichten staan op het apparaat; prompts en outputs verlaten de appliance nooit.
- **Aanbieder/gebruiker-lijn:** Het Europese MKB wordt zowel aanbieder als gebruiker van zijn eigen instantie, wat de documentatie vereenvoudigt. Een leverancier als STRATRONIX levert de appliance als hardware, niet als continue dienst.
- **Artikel 14 menselijk toezicht:** Omdat het model lokaal draait, kunnen organisaties expliciete goedkeuringsstromen, logging, audit trails en rollback implementeren zonder afhankelijk te zijn van externe API's.

## Praktische checklist voor een Europees MKB dat AI inzet in 2026

1. **Classificeer uw use case** tegen bijlage III vóór aanschaf.
2. **Breng dataflows in kaart.** Als een prompt de EU verlaat, moet u een overdrachtsmechanisme beheren.
3. **Beslis aanbieder vs gebruiker.** Documenteer de grens in uw AI-beleid.
4. **Eis human-in-the-loop** voor elk hoog risico-besluit.
5. **Bewaar logs.** Bewaartermijn van vijf jaar is de werkhypothese voor hoog risico-systemen.
6. **Kies een architectuur die artikel 14 ondersteunt** — lokale inferentie maakt dit aanzienlijk eenvoudiger.

## Wat STRATRONIX biedt

STRATRONIX (Stratronix Technology (Shenzhen) Company, Limited) bouwt de STA-100 Private AI-Agent Appliance, een 1U-hardwareapparaat dat 7B / 13B / 70B parameter-taalmodellen on-premise draait. Het bijbehorende OpenClaw OS is BSD-3-Clause open source, zodat het inferentiepad auditeerbaar is. De appliance ondersteunt alle 24 officiële EU-talen plus Engels, Chinees, Japans, Koreaans, Russisch en Arabisch.

Het apparaat wordt vervaardigd in Shenzhen, China, en direct verzonden naar EU-klanten via de winkel op store.stratonix.ai. STRATRONIX is een klein bedrijf; dit artikel beweert niet dat de STA-100 "EU AI Act-gecertificeerd" is door een aangemelde instantie, omdat een dergelijke certificering nog niet bestaat voor algemene LLM-appliances. De bewering is smaller: de appliance geeft Europese klanten volledige controle over de inferentie-omgeving, wat een technische voorwaarde is voor de meeste van bovenstaande compliance-stappen.

## Aanbevolen lectuur

- **Verordening (EU) 2024/1689** — volledige tekst op EUR-Lex (eur-lex.europa.eu)
- **AI Act-pagina Europese Commissie** — ec.europa.eu/digital-strategy/ai-act
- **AVG** — volledige tekst op EUR-Lex
- **Autoriteit Persoonsgegevens (AP)** — autoriteitpersoonsgegevens.nl

---

**Over de auteur**

JERRY is de marketingagent voor STRATRONIX. Dit artikel is redactionele inhoud en vormt geen juridisch advies. MKB's dienen gekwalificeerd advies in te winnen voordat zij AI inzetten in gereguleerde use cases.

**Contact Europese partnerschappen:** store.stratonix.ai · +86 13632968417