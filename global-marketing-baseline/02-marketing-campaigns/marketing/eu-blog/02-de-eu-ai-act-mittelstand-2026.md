# BLOG 02 — DE — EU-AI-Act 2026: Was mittelständische Unternehmen jetzt wissen müssen

> **Autor:** JERRY (STRATRONIX Marketing) · **Reviewer ausstehend:** Donald Wang (CEO)
> **Status:** ENTWURF v0.1 · 2026-07-23 · **Wortzahl:** ~1.100
> **Verteiler:** Heise · Golem · t3n · Computerwoche · EU-Startups (Guest Post)
> **Compliance-Check:** Eisen 31 (keine Fabrikation) — nur öffentlich zugängliche Rechtsquellen

---

## Die Realität 2026 für europäische KI-Adopter

Die EU-KI-Verordnung (Verordnung 2024/1689) ist 2025 und 2026 schrittweise in Kraft getreten. Für kleine und mittelständische Unternehmen in Deutschland lautet die praktische Frage im Juli 2026 nicht mehr *sollen wir KI einsetzen*, sondern *unter welchen Regeln*. Dieser Artikel fasst zusammen, was heute gilt, was sich am 2. August 2026 ändert und wie On-Premise-KI-Hardware — oft als PAA (Private AI-Agent Appliance) abgekürzt — in den regulatorischen Rahmen passt.

## Was heute gilt (Juli 2026)

Drei Blöcke der KI-Verordnung sind bereits verbindlich:

| Block | Datum | Inhalt |
|-------|-------|--------|
| **Verbotene Praktiken (Art. 5)** | 2. Februar 2025 | Social Scoring, manipulative KI, ungezieltes Gesichtserkennen, biometrische Echtzeit-Identifizierung (mit engen Ausnahmen) |
| **Pflichten für Allzweck-KI (GPAI) (Art. 50 + Anhang XI)** | 2. August 2025 | Anbieter von Frontier-Modellen müssen Trainingsdaten-Zusammenfassungen, Urheberrechtsrichtlinien und Bewertungen des Systemrisikos über 10²⁵ FLOPs veröffentlichen |
| **Transparenzpflichten (Art. 50)** | 2. August 2026 | Anbieter und Betreiber von KI-Systemen, die mit Menschen interagieren, synthetische Medien erzeugen oder Emotionserkennung durchführen, müssen den KI-Einsatz offenlegen |

## Was sich am 2. August 2026 ändert

Ab August 2026 gilt die Hochrisiko-Klassifizierung (Anhang III) für Systeme in:

- **Kritischer Infrastruktur** (Wasser, Gas, Strom, Verkehr)
- **Bildung und beruflicher Weiterbildung** (Zulassung, Bewertung, Prüfungsintegrität)
- **Beschäftigung** (CV-Screening, Aufgabenverteilung, Überwachung)
- **Wesentlichen öffentlichen und privaten Diensten** (Kredit-Scoring, Versicherungspreisgestaltung, Notfall-Einsatz, öffentliche Leistungen)
- **Strafverfolgung und Migration** (Risikobewertungen, Polygraphen, Beweismittel-Zuverlässigkeit)
- **Justiz und demokratischen Prozessen** (Gerichtshilfe, Wählerbeeinflussung)

Hochrisikosysteme müssen Anforderungen an Datenqualität, technische Dokumentation, menschliche Aufsicht, Robustheit, Cybersicherheit und Konformitätsbewertung erfüllen, bevor sie auf dem EU-Markt bereitgestellt oder in Betrieb genommen werden dürfen.

## Wo Cloud-only-KI-Stacks Schwierigkeiten haben

Cloud-gehostete KI von Nicht-EU-Anbietern beantwortet drei Fragen unter dieser Regulierung typischerweise unbefriedigend:

1. **Wo leben die Daten physisch?** — Wenn der Inferenzpfad Grenzen überschreitet (USA, China, Singapur), gelten GDPR Kapitel V Übertragungsmechanismen.
2. **Wer ist Anbieter, wer Betreiber?** — Artikel 25 verteilt die Verantwortung entlang der Kette. Ein deutsches Mittelstandsunternehmen, das die OpenAI-API nutzt, kann weiterhin als Betreiber eines Hochrisikosystems eingestuft werden.
3. **Was verlangt Artikel 14 (menschliche Aufsicht), wenn das Modell eine gehostete API ist?** — Praktische Eingriffe, Override und Protokollierung sind bei zustandslosen Endpunkten schwieriger.

## On-Premise-KI als Compliance-Hebel

Eine Hardware-Appliance, die ein Large Language Model vollständig im Datenraum des Kunden ausführt — ohne ausgehende API-Aufrufe und ohne externes Trainingsdaten-Egress — ändert die operative Antwort auf alle drei Fragen:

- **Datenstandort:** 100% im Unternehmensnetzwerk. Die Modellgewichte befinden sich auf dem Gerät; Prompts und Outputs verlassen die Appliance nie.
- **Anbieter/Betreiber-Linie:** Das europäische KMU wird sowohl Anbieter als auch Betreiber seiner eigenen Instanz, was die Dokumentation vereinfacht. Ein Anbieter wie STRATRONIX liefert die Appliance als Hardware, nicht als Dauerdienstleistung.
- **Artikel 14 menschliche Aufsicht:** Da das Modell lokal läuft, können Organisationen explizite Genehmigungsprozesse, Protokollierung, Audit-Trails und Rollback implementieren, ohne von Remote-APIs abhängig zu sein.

## Praktische Checkliste für ein EU-KMU beim KI-Einsatz 2026

1. **Klassifizieren Sie Ihren Anwendungsfall** gemäß Anhang III vor der Beschaffung.
2. **Kartieren Sie Datenflüsse.** Wenn ein Prompt die EU verlässt, müssen Sie einen Übertragungsmechanismus verwalten.
3. **Entscheiden Sie Anbieter vs Betreiber.** Dokumentieren Sie die Grenze in Ihrer KI-Richtlinie.
4. **Verlangen Sie Human-in-the-Loop** für jedes Hochrisiko-Entscheidungsergebnis.
5. **Behalten Sie Protokolle.** Fünf-Jahres-Aufbewahrung ist die Arbeitsannahme für Hochrisikosysteme.
6. **Wählen Sie eine Architektur, die Artikel 14 unterstützt** — lokale Inferenz macht dies wesentlich einfacher.

## Was STRATRONIX bietet

STRATRONIX (Stratronix Technology (Shenzhen) Company, Limited) baut die STA-100 Private AI-Agent Appliance, ein 1U-Hardware-Gerät, das 7B / 13B / 70B Parameter-Sprachmodelle On-Premise ausführt. Das begleitende OpenClaw-Betriebssystem ist BSD-3-Clause Open Source, sodass der Inferenzpfad auditierbar ist. Die Appliance unterstützt alle 24 offiziellen EU-Sprachen plus Englisch, Chinesisch, Japanisch, Koreanisch, Russisch und Arabisch.

Das Gerät wird in Shenzhen, China, hergestellt und direkt an EU-Kunden über den Storefront unter store.stratonix.ai versandt. STRATRONIX ist ein kleines Unternehmen; dieser Artikel behauptet nicht, dass die STA-100 durch eine benannte Stelle "EU-AI-Act-zertifiziert" ist, da eine solche Zertifizierung für allgemeine LLM-Appliances noch nicht existiert. Die Aussage ist enger: Die Appliance gibt europäischen Kunden die volle Kontrolle über die Inferenzumgebung, was eine technische Voraussetzung für die meisten der oben genannten Compliance-Schritte ist.

## Was Sie als Nächstes lesen sollten

- **Verordnung (EU) 2024/1689** — Volltext auf EUR-Lex (eur-lex.europa.eu)
- **EU-Kommission KI-Verordnung** — ec.europa.eu/digital-strategy/ai-act
- **DSGVO** — vollständiger Text auf EUR-Lex

---

**Über den Autor**

JERRY ist der Marketing-Agent für STRATRONIX. Dieser Artikel ist redaktioneller Inhalt und stellt keine Rechtsberatung dar. KMU sollten qualifizierte Rechtsberatung konsultieren, bevor sie KI in regulierten Anwendungsfällen einsetzen.

**Kontakt für europäische Partnerschaften:** store.stratonix.ai · +86 13632968417