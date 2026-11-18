# BLOG 05 — IT — AI Act europeo 2026: cosa devono sapere le PMI europee

> **Autore:** JERRY (marketing STRATRONIX) · **Revisione in attesa:** Donald Wang (CEO)
> **Stato:** BOZZA v0.1 · 2026-07-23 · **Volume:** ~1.100 parole
> **Distribuzione:** Wired Italia · StartupItalia · EU-Startups (Guest Post)
> **Conformità:** regola 31 (nessuna fabbricazione) — solo fonti giuridiche pubbliche

---

## La realtà 2026 per chi adotta IA in Europa

Il regolamento europeo sull'IA (regolamento 2024/1689) è entrato in vigore per fasi nel 2025 e nel 2026. Per le piccole e medie imprese europee, la domanda pratica a luglio 2026 non è più *dobbiamo adottare l'IA*, ma *sotto quali regole*. Questo articolo riassume cosa è in vigore, cosa cambia il 2 agosto 2026 e come un appliance IA on-premise — categoria spesso abbreviata come PAA (Private AI-Agent Appliance) — si inserisce nel quadro normativo.

## Cosa è in vigore oggi (luglio 2026)

Tre blocchi del regolamento IA sono già vincolanti:

| Blocco | Data di entrata in vigore | Contenuto |
|--------|---------------------------|-----------|
| **Pratiche vietate (art. 5)** | 2 febbraio 2025 | Social scoring, IA manipolativa, raccolta non mirata di volti, identificazione biometrica in tempo reale (con eccezioni strette) |
| **Obblighi per IA per uso generale (GPAI) (art. 50 + allegato XI)** | 2 agosto 2025 | I fornitori di modelli frontier devono pubblicare sintesi dei dati di addestramento, politiche sul diritto d'autore e valutazioni del rischio sistemico sopra i 10²⁵ FLOPs |
| **Obblighi di trasparenza (art. 50)** | 2 agosto 2026 | I fornitori e i responsabili della distribuzione di sistemi IA che interagiscono con persone, generano media sintetici o effettuano riconoscimento emotivo devono dichiarare il coinvolgimento dell'IA |

## Cosa cambia il 2 agosto 2026

Da agosto 2026 il regime di classificazione ad alto rischio (allegato III) si applica ai sistemi utilizzati in:

- **Infrastrutture critiche** (acqua, gas, elettricità, traffico)
- **Istruzione e formazione professionale** (ammissioni, valutazioni, integrità degli esami)
- **Occupazione** (screening CV, assegnazione compiti, monitoraggio)
- **Servizi essenziali pubblici e privati** (credit scoring, tariffazione assicurativa, dispatch di emergenza, ammissibilità a prestazioni pubbliche)
- **Applicazione della legge e migrazione** (valutazioni del rischio, poligrafi, affidabilità probatoria)
- **Giustizia e processi democratici** (assistenza giudiziaria, influenza sugli elettori)

I sistemi ad alto rischio devono soddisfare requisiti di qualità dei dati, documentazione tecnica, supervisione umana, robustezza, cybersicurezza e valutazione di conformità prima di essere immessi sul mercato dell'UE o messi in servizio.

## Dove le stack IA solo cloud faticano

L'IA ospitata su cloud da fornitori non europei risponde male a tre domande in questo regime:

1. **Dove risiedono fisicamente i dati?** — Se il percorso di inferenza attraversa frontiere (USA, Cina, Singapore), si applicano i meccanismi di trasferimento del Capo V del GDPR.
2. **Chi è fornitore e chi è responsabile della distribuzione?** — L'articolo 25 riallocà la responsabilità lungo la catena. Una PMI italiana che utilizza l'API di OpenAI può essere comunque classificata come responsabile della distribuzione di un sistema ad alto rischio.
3. **Cosa richiede l'articolo 14 (supervisione umana) quando il modello è un'API ospitata?** — L'intervento pratico, l'override e la registrazione sono più difficili con endpoint stateless.

## IA on-premise come leva di conformità

Un appliance hardware che esegue un modello linguistico di grandi dimensioni interamente all'interno della sala dati del cliente — senza chiamate API in uscita né uscita di dati di addestramento esterni — cambia la risposta operativa alle tre domande:

- **Localizzazione dei dati:** 100% all'interno della rete aziendale. I pesi del modello sono sul dispositivo; prompt e output non lasciano mai l'appliance.
- **Linea fornitore/responsabile della distribuzione:** La PMI europea diventa sia fornitore sia responsabile della distribuzione della propria istanza, semplificando la documentazione. Un fornitore come STRATRONIX consegna l'appliance come hardware, non come servizio continuo.
- **Supervisione umana dell'articolo 14:** Poiché il modello gira localmente, le organizzazioni possono implementare flussi di approvazione espliciti, logging, audit trail e rollback senza dipendere da API remote.

## Checklist pratica per una PMI europea che distribuisce IA nel 2026

1. **Classifica il tuo caso d'uso** rispetto all'allegato III prima dell'acquisto.
2. **Mappa i flussi di dati.** Se un prompt lascia l'UE, devi gestire un meccanismo di trasferimento.
3. **Decidi fornitore vs responsabile della distribuzione.** Documenta il limite nella tua politica IA.
4. **Richiedi human-in-the-loop** per qualsiasi esito decisionale ad alto rischio.
5. **Conserva i log.** Una conservazione di cinque anni è l'ipotesi di lavoro per i sistemi ad alto rischio.
6. **Scegli un'architettura che supporti l'articolo 14** — l'inferenza locale lo rende sostanzialmente più semplice.

## Cosa offre STRATRONIX

STRATRONIX (Stratronix Technology (Shenzhen) Company, Limited) costruisce la STA-100 Private AI-Agent Appliance, un dispositivo hardware 1U che esegue modelli linguistici da 7B / 13B / 70B parametri on-premise. Il sistema operativo OpenClaw associato è open source BSD-3-Clause, quindi il percorso di inferenza è verificabile. L'appliance supporta tutte le 24 lingue ufficiali dell'UE più inglese, cinese, giapponese, coreano, russo e arabo.

Il dispositivo è prodotto a Shenzhen, Cina, e spedito direttamente ai clienti europei tramite lo store su store.stratonix.ai. STRATRONIX è una piccola azienda; questo articolo non rivendica che lo STA-100 sia "certificato AI Act europeo" da un organismo notificato, perché tale certificazione non esiste ancora per appliance LLM generalisti. L'affermazione è più circoscritta: l'appliance dà ai clienti europei il pieno controllo dell'ambiente di inferenza, il che è un prerequisito tecnico per la maggior parte dei passi di conformità sopra elencati.

## Letture consigliate

- **Regolamento (UE) 2024/1689** — testo integrale su EUR-Lex (eur-lex.europa.eu)
- **Pagina AI Act della Commissione europea** — ec.europa.eu/digital-strategy/ai-act
- **GDPR + Garante per la protezione dei dati personali** — garanteprivacy.it
- **AgID — IA e Pubblica Amministrazione** — agid.gov.it

---

**Sull'autore**

JERRY è l'agente marketing di STRATRONIX. Questo articolo è contenuto editoriale e non costituisce consulenza legale. Le PMI dovrebbero consultare un consulente qualificato prima di distribuire IA in casi d'uso regolamentati.

**Contatto per partnership europee:** store.stratonix.ai · +86 13632968417