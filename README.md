# HDN-FIS: Institutionsanreicherung niedersächsischer Hochschulen in OpenAlex

Dieses Projekt zielt darauf ab, die Abdeckung niedersächsischer Hochschulen in OpenAlex zu optimieren. 

### 🏗️ Problem

Nicht immer ist eine korrekte Zuordnung einer Person zu einer (deutschen) wissenschaftlichen Einrichtung in bibliographischen Datenquellen (z.B. OpenAlex) gegeben.

<b>Beispiel:</b>

```json
{
      "author_position": "middle",
      "author": {
        "id": "https://openalex.org/A5057081490",
        "display_name": "Thorsten R. Doeppner",
        "orcid": "https://orcid.org/0000-0002-1222-9211"
      },
      "institutions": [
        
      ],
      "countries": [
        
      ],
      "is_corresponding": false,
      "raw_author_name": "Thorsten R. Doeppner",
      "raw_affiliation_strings": [
        "Department of Neurology, University Medical Center Goettingen, Goettingen, 37075, Germany"
      ],
      "affiliations": [
        {
          "raw_affiliation_string": "Department of Neurology, University Medical Center Goettingen, Goettingen, 37075, Germany",
          "institution_ids": [
            
          ]
        }
      ]
}
```

<b>Idee:</b> Anhand von Instititutionszuordnungen aus anderen offenen Datenquellen könnten Lücken geschlossen werden und ggf. fehlerhafte Zuordnungen korrigiert werden. 

## 📈 Daten

- [GERiT](https://gerit.org/de/service): Stand Januar 2025
- [OpenAlex](https://openalex.org): Stand März 2026
- [OPENBIB](https://zenodo.org/records/18429476): Stand Juli 2025

## Methode

### 🏫 Download Institutionsdaten

Um eine Liste mit allen wissenschaftlichen Institutionen in Deutschland zu erhalten, wurden zunächst sämtliche Stammdaten aus dem GERiT-Verzeichnis heruntergeladen. Die einzelnen Institutionen wurden dann auf Basis der Postleitzahl mit einem Bundesland verknüpft (siehe [Python-Skript](get_institutions.py)). Es wurden manuell Zuordnungen erstellt, sofern eine Postleitzahl nicht mit einem Bundesland verknüpft werden konnte. Die komplette Liste mit wissenschaftlichen Einrichtungen kann im Ordner [data/](data/inst_with_federal_state_filled.csv) heruntergeladen werden. Die Liste kann genutzt werden, um Einrichtungen nach ihren Bundesländern zu filtern.

### 🖇️ Verknüpfung der Institutionsdaten mit weiteren Datenquellen

Im nächsten Schritt wurden die Institutionsdaten mit Daten aus OpenAlex und OPENBIB angereichert. So ist es möglich, Institutionen nach dem Bundesland Niedersachsen zu filtern und nur Institutionen zu berücksichtigen, die in OPENBIB als Hochschule klassifiziert werden. Es folgt ein Vergleich der Institutionszuordnung in OpenAlex und OPENBIB.

## 🔎 Gap-Analyse

- Vergleich OpenAlex mit der Bielefelder Institutionskodierung
- [Link](docs/comparison.html)

## 🔨 Anreicherung in OpenAlex

Mithilfe des Datenabgleichs aus OpenAlex und OPENBIB lassen sich konkrete Verbesserungsvorschläge bei der Institutionszuordnung in OpenAlex ableiten. Diese können in der folgenden Tabelle eingesehen werden.

- Dieser Schritt erfolgt im April
- [Link](docs/download.html)