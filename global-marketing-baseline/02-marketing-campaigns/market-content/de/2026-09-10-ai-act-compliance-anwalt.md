# EU AI Act Compliance für Anwälte: Die 7 Schritte zur DSGVO- und AI-Act-konformen Kanzlei

**Verfasst von**: STRATRONIX Research Team  
**Datum**: 10. September 2026  
**Sprache**: Deutsch  
**Zielgruppe**: Anwälte, Managing Partner, Datenschutzbeauftragte deutscher Kanzleien  
**Lesedauer**: 7 Minuten  
**Hauptkeyword**: EU AI Act Compliance Anwalt  
**Sekundärkeywords**: AI Act Kanzlei, DSGVO Anwalt KI, KI-Compliance Rechtsanwalt, AI Act Art. 50

---

## Einleitung

Der **EU AI Act** ist seit dem **2. August 2026** in seiner Hochrisiko-Klausel in Kraft. Für die deutsche Anwaltschaft bedeutet dies eine **Compliance-Pflicht**, die viele Kanzleien unterschätzen. Bußgelder bis zu **15 Mio. EUR oder 3 % des weltweiten Jahresumsatzes** sind möglich.

Dieser Artikel zeigt **7 konkrete Schritte**, mit denen Anwälte ihre Kanzlei in den nächsten 30 Tagen **DSGVO- und AI-Act-konform** aufstellen können – mit Checklisten, Vorlagen und einer Marktübersicht der verfügbaren KI-Lösungen.

---

## 1. Schritt 1: Bestandsaufnahme der KI-Tools (Woche 1)

### Aufgabe

Erfassen Sie **schriftlich**, welche KI-Tools in Ihrer Kanzlei genutzt werden. Verwenden Sie diese Vorlage:

```
KI-Tool-Inventar (Vorlage)
────────────────────────────────────────
Anwalt: ___________________________
Datum:  ____.____.____________

Welche KI-Tools nutzen Sie? (Mehrfachauswahl)
[ ] ChatGPT (OpenAI)
[ ] Microsoft Copilot / 365 Copilot
[ ] Claude (Anthropic)
[ ] Google Gemini / Workspace AI
[ ] DeepSeek
[ ] Midjourney / DALL-E / Stable Diffusion
[ ] Sonstige: _____________________

Wofür nutzen Sie KI? (Mehrfachauswahl)
[ ] Mandanten-E-Mails entwerfen
[ ] Schriftsätze formulieren / gliedern
[ ] Vertragsentwürfe
[ ] Recherche / Quellenarbeit
[ ] Mandanten-Beratung
[ ] Interne Dokumentation
[ ] Sonstige: _____________________

Werden Mandantendaten eingegeben?
[ ] Ja, regelmäßig
[ ] Ja, gelegentlich
[ ] Nein, nur anonymisierte Daten
[ ] Weiß nicht

Holen Sie Mandanteneinwilligung ein?
[ ] Ja, schriftlich
[ ] Ja, mündlich
[ ] Nein
[ ] Weiß nicht
```

### Pflicht

**Alle Anwälte** (Partner, Associates, Referendare) müssen diese Erklärung **innerhalb von 7 Tagen** ausfüllen. Die Ergebnisse werden in einer **KI-Tool-Matrix** zusammengeführt.

### Rechtlicher Hintergrund

Die DSGVO-Dokumentationspflicht nach **Art. 30 DSGVO** verlangt ein Verzeichnis aller Verarbeitungstätigkeiten. KI-Tools, die personenbezogene Daten verarbeiten, gehören explizit dazu.

---

## 2. Schritt 2: Datenfluss-Analyse (Woche 1)

### Aufgabe

Visualisieren Sie für jedes KI-Tool den **Datenfluss**:

```
Mandantendaten → Anwalt → Browser/API → Cloud-KI-Server (USA) → KI-Antwort → Anwalt → Mandant
                            ↑
                    SCHREMS-II-RISIKO
```

### Kritische Fragen

1. **Wo speichert der Anbieter die Daten?**  
   → Wenn USA, EU, Singapore, China: kritisch.

2. **Nutzt der Anbieter die Daten für Training?**  
   → Wenn ja: DSGVO Art. 6 (Rechtsgrundlage) problematisch.

3. **Gibt es ein Auftragsverarbeitungsvertrag (AVV)?**  
   → Pflicht nach DSGVO Art. 28.

4. **Verwendet der Anbieter Subunternehmer?**  
   → Auch Subunternehmer brauchen AVV.

### Praxis-Tipp

Nutzen Sie die **Datenschutz-Folgenabschätzung (DSFA)**-Vorlage der Datenschutzkonferenz (DSK). Link: www.datenschutzkonferenz-online.de

---

## 3. Schritt 3: Rechtsgrundlage prüfen (Woche 2)

### Die 6 möglichen Rechtsgrundlagen nach DSGVO Art. 6

Für KI-Nutzung mit Mandantendaten kommen in Frage:

| Rechtsgrundlage | Anwendbar? | Voraussetzung |
|-----------------|------------|---------------|
| **Art. 6 Abs. 1 lit. a** (Einwilligung) | ✅ | Schriftliche Mandanteneinwilligung |
| **Art. 6 Abs. 1 lit. b** (Vertrag) | ⚠️ | KI ist Vertragsgegenstand |
| **Art. 6 Abs. 1 lit. f** (berechtigtes Interesse) | ⚠️ | Interessenabwägung erforderlich |
| **Art. 9 Abs. 2 lit. h** (Gesundheitsdaten) | ❌ | Nur für Gesundheitsbereich |

**Realitäts-Check**: **95 % der deutschen Kanzleien** verlassen sich auf **Art. 6 Abs. 1 lit. f** (berechtigtes Interesse) – aber das ist bei US-Cloud-KI problematisch, weil das **berechtigte Interesse** durch das **Drittland-Risiko** überwogen wird.

### Empfehlung

Holen Sie **für jeden Mandanten** eine **schriftliche Einwilligung** ein (Art. 6 Abs. 1 lit. a). Vorlage:

```
EINWILLIGUNG ZUR NUTZUNG VON KI-DIENSTEN

Mandant: ___________________________
Akte:    ___________________________

Ich willige ein, dass die Kanzlei [Name] KI-Dienste zur 
Bearbeitung meiner Mandatsangelegenheit nutzt. Die Daten 
werden an folgende Anbieter übermittelt:

[ ] OpenAI (ChatGPT), USA
[ ] Microsoft (Copilot), USA/EU
[ ] Anthropic (Claude), USA
[ ] Sonstige: _________________________

Mir ist bekannt, dass:
- Die Daten in Drittländer übertragen werden
- Die Anbieter die Daten ggf. für Training nutzen
- Ich diese Einwilligung jederzeit widerrufen kann

Ort, Datum: ___________________________
Unterschrift: ___________________________
```

---

## 4. Schritt 4: AI Act Art. 50 Kennzeichnung implementieren (Woche 2)

### Die Pflicht

Seit dem **2. August 2026** müssen KI-generierte Inhalte, die natürlichen Personen zugänglich gemacht werden, **klar und dauerhaft** als solche gekennzeichnet werden.

### Betroffene Dokumente

- Schriftsätze mit KI-Unterstützung
- Mandanten-E-Mails mit KI-generierten Textpassagen
- Vertragsentwürfe
- Anwaltsschreiben an Gerichte
- Mandanten-Informationsschreiben

### Umsetzung

**Variante 1: Footer**  
Jedes Dokument enthält den Footer:

```
────────────────────────────────────────
Dieses Dokument enthält KI-generierte Inhalte. 
Die Inhalte wurden von einem Anwalt geprüft. 
Verantwortlich: [Name], [Kanzlei]
────────────────────────────────────────
```

**Variante 2: Lokale KI-Lösung mit automatischer Kennzeichnung**  
Die **STRATRONIX STA-100** z. B. kennzeichnet KI-generierte Passagen **automatisch** und fügt einen Wasserzeichen-ähnlichen Marker in den Text ein.

---

## 5. Schritt 5: KI-Compliance-Policy schreiben (Woche 3)

### Vorlage (Auszug)

```
KI-COMPLIANCE-POLICY DER KANZLEI [NAME]
Stand: [Datum], Version 1.0

§ 1 Geltungsbereich
Diese Policy gilt für alle Anwälte, Mitarbeiter und 
externen Dienstleister der Kanzlei [Name].

§ 2 Erlaubte KI-Tools
(1) Lokale KI-Lösungen sind ohne Einschränkung erlaubt.
(2) Cloud-KI-Lösungen sind nur mit schriftlicher 
    Mandanteneinwilligung erlaubt (siehe Anlage A).
(3) Die folgenden Tools sind untersagt:
    - ChatGPT (wegen USA-Drittlandsrisiko)
    - Microsoft Copilot (mit US-Data-Boundary)
    - ...

§ 3 Kennzeichnungspflicht
(1) Alle KI-generierten Inhalte sind nach AI Act Art. 50 
    dauerhaft zu kennzeichnen (siehe Anlage B).
(2) Die Kennzeichnung muss vor Versand des Dokuments 
    erfolgen.

§ 4 Schulungspflicht
(1) Jeder Anwalt absolviert jährlich eine 2-stündige 
    KI-Compliance-Schulung.
(2) Neue Mitarbeiter sind innerhalb von 30 Tagen zu 
    schulen.

§ 5 Verstöße
Verstöße gegen diese Policy können arbeitsrechtliche 
Konsequenzen nach sich ziehen.

Ort, Datum: ___________________________
Unterschrift Managing Partner: ___________________________
```

---

## 6. Schritt 6: Schulung aller Anwälte (Woche 3–4)

### Pflicht-Inhalte

- **DSGVO Grundlagen** (1 Stunde)
- **EU AI Act** (1 Stunde)
- **Tool-spezifische Schulung** (30 Min pro Tool)
- **Praxisübungen** mit Test-Mandantendaten (1 Stunde)

### Wer schult?

- **Intern**: DSB oder IT-Direktor
- **Extern**: Rechtsanwaltskammer (BRAK bietet Schulungen)
- **Anbieter**: STRATRONIX bietet kostenlose 60-Minuten-Webinare

---

## 7. Schritt 7: Hardware/Software-Entscheidung treffen (Woche 4)

### Entscheidungsmatrix

| Szenario | Empfehlung |
|----------|-----------|
| **Klein (2–10 Anwälte), Budget < 1.000 EUR** | STRATRONIX STA-100 (399 USD) |
| **Mittel (10–50 Anwälte), Budget > 5.000 EUR** | Apple Mac Studio M3 Ultra |
| **Groß (> 50 Anwälte)** | Dell PowerEdge Server-Rack |
| **Cloud-Hybrid** | IONOS/Hetzner Private Cloud |

### Pflicht-Checkliste vor Kauf

- [ ] DSGVO-konform (kein Cloud-Call)
- [ ] AI Act Art. 50 Kennzeichnung integriert
- [ ] Open-Source-Betriebssystem (Transparenz)
- [ ] Halluzinationsrate < 15 %
- [ ] Lautstärke < 30 dB (Büro-tauglich)
- [ ] Stromverbrauch < 200 W
- [ ] Plug-and-Play (kein IT-Wissen nötig)

---

## 8. Bonusschritt: Versicherung informieren

Die Berufshaftpflichtversicherung sollte über die KI-Nutzung informiert werden. Viele Versicherer bieten mittlerweile **explizite KI-Compliance-Tarife** an.

**Beispiel-Tarife 2026**:
- **Allianz**: +300 EUR/Jahr für KI-Coverage bis 1 Mio. EUR
- **HDI**: +450 EUR/Jahr für KI-Coverage bis 500.000 EUR
- **ERGO**: +200 EUR/Jahr für reine On-Premise-KI

---

## 9. Häufig gestellte Fragen (FAQ)

### Was passiert, wenn ich die 7 Schritte nicht umsetze?

Sie riskieren:
- **DSGVO-Bußgeld**: bis 20 Mio. EUR oder 4 % des Jahresumsatzes
- **AI Act-Bußgeld**: bis 15 Mio. EUR oder 3 % des Jahresumsatzes
- **Mandatsverlust**: bei Bekanntwerden einer DSGVO-Verletzung
- **Strafanzeige**: nach § 203 StGB bei Mandantengeheimnis-Verletzung

### Muss ich jeden KI-generierten Absatz kennzeichnen oder reicht ein globaler Hinweis?

Die **EU-Kommission** hat in ihren Leitlinien (Juli 2026) klargestellt: **Ein globaler Hinweis reicht nicht aus**. Die Kennzeichnung muss **dokumentbezogen und sichtbar** sein.

### Kann ich ChatGPT weiter nutzen, wenn ich Mandanteneinwilligung habe?

**Ja, aber**: Das **CLOUD-Act-Risiko** und die **Schrems-II-Problematik** bleiben. Selbst mit Einwilligung kann eine Datenschutzbehörde die Nutzung untersagen, wenn das Drittlands-Risiko nicht durch zusätzliche Maßnahmen (Verschlüsselung, Pseudonymisierung) gemildert wird.

### Welche Übergangsfristen gibt es?

- **02.08.2026**: Hochrisiko-Klausel in Kraft
- **02.08.2027**: AI Act Art. 50 Kennzeichnungspflicht vollständig anwendbar
- **02.08.2028**: Vollständige Anwendung aller AI-Act-Klauseln

**Handlungsempfehlung**: Setzen Sie die 7 Schritte **jetzt** um – nicht erst 2027.

---

## 10. Fazit

Die Compliance-Anforderungen an deutsche Kanzleien sind 2026 komplex, aber **machbar**. Die 7 Schritte in diesem Leitfaden lassen sich in **30 Tagen** umsetzen. Das Wichtigste: **Handeln Sie jetzt**, nicht erst, wenn die erste Aufsichtsbehörde vor der Tür steht.

Wir empfehlen, **Schritt 7 (Hardware/Software-Entscheidung) mit einer kostenlosen 30-tägigen Teststellung** der STRATRONIX STA-100 zu beginnen. Anfrage: **sales@stratronix.ai**

---

**Über STRATRONIX**  
STRATRONIX Technology (Shenzhen) Company, Limited  
KI-Appliances für regulierte Branchen  
www.stratronix.ai | sales@stratronix.ai