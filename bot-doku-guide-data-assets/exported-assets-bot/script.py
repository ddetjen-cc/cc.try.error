# Erstelle eine CSV-Datei mit häufigen Anfragen und Antworten für den CreaCheck Assistenten
import pandas as pd

# Daten für den Chatbot basierend auf den FAQs und allgemeinen Informationen
chatbot_data = {
    'Kategorie': [
        'Navigation', 'Navigation', 'Navigation', 'Navigation',
        'Werbemittel', 'Werbemittel', 'Werbemittel', 'Werbemittel', 'Werbemittel',
        'Editor', 'Editor', 'Editor', 'Editor', 'Editor',
        'Bestellung', 'Bestellung', 'Bestellung', 'Bestellung',
        'Mediathek', 'Mediathek', 'Mediathek',
        'Kampagnen', 'Kampagnen', 'Kampagnen',
        'Landingpages', 'Landingpages', 'Landingpages',
        'Support', 'Support', 'Support'
    ],
    'Frage': [
        'Wo finde ich meine Rechnungen?',
        'Wie melde ich mich an?',
        'Wie ändere ich mein Passwort?',
        'Wie kann ich neue Benutzer anlegen?',
        
        'Wie erstelle ich ein neues Werbemittel?',
        'Welche Werbemittel stehen zur Verfügung?',
        'Wie bestelle ich Werbemittel?',
        'Welche Lieferzeiten gibt es?',
        'Was kostet die Datenprüfung?',
        
        'Wie füge ich weitere Seiten hinzu?',
        'Wie bearbeite ich Texte?',
        'Wie lade ich Bilder hoch?',
        'Wie erstelle ich eine Vorschau-PDF?',
        'Wie speichere ich meine Arbeit?',
        
        'Welche Zahlungsmöglichkeiten gibt es?',
        'Wie verfolge ich meine Bestellung?',
        'Was ist eine Express-Bestellung?',
        'Kann ich ins Ausland liefern lassen?',
        
        'Wie erstelle ich einen neuen Ordner?',
        'Wie lade ich Bilder in die Mediathek hoch?',
        'Wie organisiere ich meine Bilder?',
        
        'Wie lege ich eine neue Kampagne an?',
        'Wie teile ich Werbemittel mit anderen?',
        'Wie lösche ich eine Kampagne?',
        
        'Wie erstelle ich eine Landingpage?',
        'Wie füge ich ein Kontaktformular hinzu?',
        'Wie verknüpfe ich Social Media?',
        
        'Wie erreiche ich den Support?',
        'Was sind die Öffnungszeiten?',
        'Wo finde ich Tutorials?'
    ],
    'Antwort': [
        'Ihre Rechnungen finden Sie nach dem Login im Dashboard unter "letzte Rechnungen" oder unter "Funktionen" > "Rechnungen".',
        'CDU-Mitglieder können sich selbst registrieren. Klicken Sie auf "Neu registrieren" und folgen Sie den Anweisungen.',
        'Sie können Ihr Passwort unter "Profil" > "Passwort ändern" > "speichern" ändern.',
        'Neue Benutzer können über die Benutzerverwaltung angelegt werden. Wenden Sie sich an Ihren Administrator.',
        
        'Klicken Sie in Ihrer Kampagne auf "neues Werbemittel anlegen", wählen Sie das gewünschte Format und geben Sie eine Bezeichnung ein.',
        'CreaCheck bietet eine große Auswahl: Flyer, Plakate, Social Media Posts, Visitenkarten, Broschüren, Landingpages und vieles mehr.',
        'Im Editor klicken Sie auf "Bestellen" oder in der Kampagnenübersicht auf "in den Warenkorb".',
        'Standard-, Express- und Overnight-Lieferung verfügbar. Die genauen Zeiten werden beim Bestellprozess angezeigt.',
        'Die manuelle Datenprüfung ist eine zusätzliche Option zur Qualitätssicherung durch unsere Grafiker.',
        
        'Klicken Sie bei Faltblättern auf "+2" oder "-2", bei Broschüren auf "+4" oder "-4" unter der entsprechenden Seite.',
        'Klicken Sie in das Textfeld. Die Formatierungsoptionen erscheinen automatisch entsprechend dem Corporate Design.',
        'Klicken Sie auf ein Bildelement und wählen Sie "Bildupload" oder "Mediathek" aus.',
        'Klicken Sie auf "Vorschau". Wichtig: Speichern Sie vorher Ihre Änderungen!',
        'Das System speichert automatisch alle 5 Minuten. Sie können auch manuell über "Speichern" sichern.',
        
        'Kreditkarte, PayPal oder Rechnung ab 250€ Mindestbestellwert.',
        'Sie erhalten einen Sendungsverfolgungslink per E-Mail. Alternativ: dialog@creacheck.com oder 0631-366-888.',
        'Express-Bestellungen müssen bis 11:30 Uhr eingehen für Lieferung am nächsten Werktag.',
        'Standardmäßig erfolgt keine Lieferung ins Ausland.',
        
        'Klicken Sie in der Mediathek auf "neuer Ordner" und vergeben Sie einen Namen.',
        'Klicken Sie unter "Medien" auf "Medien Hochladen" und wählen Sie Ihre Dateien aus.',
        'Nutzen Sie Ordnerstrukturen, verschieben Sie Bilder per Drag & Drop und vergeben Sie aussagekräftige Namen.',
        
        'Klicken Sie in der Menüleiste auf "Kampagnen" > "neue Kampagne anlegen" und vergeben Sie einen Namen.',
        'Klicken Sie beim Werbemittel auf das Teilen-Symbol und wählen Sie die gewünschten Benutzer aus.',
        'In der Kampagnenübersicht klicken Sie auf den roten Mülleimer bei der entsprechenden Kampagne.',
        
        'Wählen Sie bei "neues Werbemittel anlegen" eine Landingpage-Vorlage aus.',
        'Fügen Sie das Kontaktformular-Element hinzu und konfigurieren Sie die gewünschten Felder.',
        'Im Header können Sie Social Media Icons verknüpfen. Geben Sie die vollständigen Links (mit https://) ein.',
        
        'E-Mail: dialog@creacheck.com oder Telefon: 0631-366-888',
        'Montag bis Freitag, 8:00 - 17:00 Uhr',
        'Tutorials finden Sie im Editor unter dem Tutorial-Button oder in den Schulungsvideos.'
    ],
    'Keywords': [
        'rechnung, rechnungen, bezahlung, zahlung',
        'anmeldung, registrierung, login, zugang',
        'passwort, kennwort, ändern, vergessen',
        'benutzer, nutzer, account, verwaltung',
        
        'werbemittel, erstellen, neu, anlegen',
        'auswahl, verfügbar, werbemittel, arten',
        'bestellen, warenkorb, bestellung',
        'lieferzeit, versand, dauer',
        'datenprüfung, qualität, kontrolle',
        
        'seiten, hinzufügen, mehr, zusätzlich',
        'text, bearbeiten, formatierung, schrift',
        'bilder, hochladen, upload, fotos',
        'vorschau, pdf, ansicht, kontrolle',
        'speichern, sichern, automatisch',
        
        'zahlung, bezahlung, methoden, kreditkarte',
        'sendungsverfolgung, tracking, status',
        'express, schnell, eilig',
        'ausland, international, lieferung',
        
        'ordner, struktur, organisation',
        'mediathek, bilder, hochladen',
        'organisation, sortierung, verwaltung',
        
        'kampagne, neu, anlegen, erstellen',
        'teilen, freigeben, zusammenarbeit',
        'löschen, entfernen, kampagne',
        
        'landingpage, webseite, erstellen',
        'kontaktformular, anfrage, formular',
        'social media, verknüpfung, links',
        
        'support, hilfe, kontakt',
        'öffnungszeiten, erreichbarkeit',
        'tutorial, hilfe, anleitung'
    ]
}

df = pd.DataFrame(chatbot_data)
df.to_csv('creacheck_chatbot_knowledge_base.csv', index=False, encoding='utf-8')

print("Wissensdatenbank für CreaCheck Assistenten erstellt:")
print(f"Anzahl Einträge: {len(df)}")
print("\nErste 5 Einträge:")
print(df.head())