import genanki

# Define a unique model ID (randomly generated) for the Anki cards
my_model_id = 1627392319

my_model = genanki.Model(
    my_model_id,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
    css="""
  .card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
  }
  """
)



# ============================================================
# KHÔLLES — GROUPE 8
# Semaines = semaines PRONOTE
# Semaine 1 = semaine du mardi 1er septembre 2026
# ============================================================

colles_by_week = {

    # Semaine Pronote 3 — 14 au 19 septembre
    3: [
        ("mardi",   "17:30", "Maths",        "M. Capelle",     60),
        ("lundi",   "16:00", "Anglais",      "Mme Lerouilly",  60),
    ],

    # Semaine Pronote 4 — 21 au 26 septembre
    4: [
        ("jeudi",   "14:00", "Maths",        "M. Briens",       60),
        ("mardi",   "13:00", "Physique",     "Mme Najid",       60),
        ("jeudi",   "14:00", "Français",     "Mme Glatigny",    60),
    ],

    # Semaine Pronote 5 — 28 septembre au 3 octobre
    5: [
        ("lundi",   "16:00", "Maths",        "M. Bruyère",      60),
        ("jeudi",   "14:00", "Anglais",      "Mme Thompson",    60),
    ],

    # Semaine Pronote 6 — 5 au 10 octobre
    6: [
        ("ma",      "17:00", "Maths",        "M. Lefebvre",     60),
        ("vendredi","13:00", "Informatique", "M. Michel",       60),
        ("jeudi",   "15:00", "Physique",     "M. Guillon",      60),
    ],

    # Semaine Pronote 7 — 12 au 17 octobre
    7: [
        ("jeudi",   "13:00", "Maths",        "M. Mahé",          60),
        ("jeudi",   "15:00", "Anglais",      "M. Romanski",      60),
    ],

    # Semaine Pronote 10 — 2 au 7 novembre
    10: [
        ("mardi",   "17:00", "Maths",        "M. Lefebvre",      60),
        ("jeudi",   "14:00", "Physique",     "M. Hiron-Sirot",   60),
    ],

    # Semaine Pronote 11 — 9 au 14 novembre
    11: [
        ("jeudi",   "14:00", "Maths",        "M. Masselin",      60),
        ("lundi",   "16:00", "Anglais",      "Mme Dufour",       60),
    ],

    # Semaine Pronote 12 — 16 au 21 novembre
    12: [
        ("lundi",   "17:00", "Physique",     "M. Dessup",        60),
        ("mardi",   "13:00", "Informatique", "M. Jacques",      60),
    ],

    # Semaine Pronote 13 — 23 au 28 novembre
    13: [
        ("jeudi",   "15:00", "Maths",        "M. Taviot",         60),
        ("lundi",   "16:30", "Anglais",      "M. Le Bihan",      60),
    ],

    # Semaine Pronote 14 — 30 novembre au 5 décembre
    14: [
        ("jeudi",   "16:00", "Maths",        "M. Brua",           60),
        ("lundi",   "17:30", "Physique",     "M. Kristensen",    60),
    ],

    # Semaine Pronote 15 — 7 au 12 décembre
    15: [
        ("jeudi",   "14:00", "Anglais",      "M. Romanski",      60),
        ("jeudi",   "16:00", "Maths",        "M. Brua",           60),
    ],

    # Semaine Pronote 19 — 4 au 9 janvier
    19: [
        ("jeudi",   "15:00", "Physique",     "M. Le Breton",     60),
        ("mardi",   "13:00", "Informatique", "M. Jacques",       60),
    ],

    # Semaine Pronote 20 — 11 au 16 janvier
    20: [
        ("mardi",   "17:30", "Maths",        "M. Capelle",        60),
        ("jeudi",   "15:00", "Physique",     "M. Le Breton",      60),
        ("jeudi",   "14:00", "Français",     "Mme Glatigny",     60),
    ],

    # Semaine Pronote 21 — 18 au 23 janvier
    21: [
        ("jeudi",   "14:00", "Maths",        "M. Briens",         60),
        ("lundi",   "16:00", "Anglais",      "Mme Lerouilly",    60),
    ],

    # Semaine Pronote 22 — 25 au 30 janvier
    22: [
        ("lundi",   "16:00", "Maths",        "M. Bruyère",        60),
        ("jeudi",   "14:00", "Anglais",      "Mme Thompson",      60),
    ],

    # Semaine Pronote 24 — 8 au 13 février
    24: [
        ("jeudi",   "15:00", "Physique",     "M. Guillon",        60),
        ("vendredi","13:00", "Informatique", "M. Michel",         60),
    ],

    # Semaine Pronote 25 — 15 au 20 février
    25: [
        ("jeudi",   "13:00", "Maths",        "M. Mahé",            60),
        ("jeudi",   "15:00", "Anglais",      "M. Romanski",        60),
    ],

    # Semaine Pronote 28 — 8 au 13 mars
    28: [
        ("mardi",   "17:00", "Maths",        "M. Lefebvre",        60),
        ("jeudi",   "14:00", "Physique",     "M. Hiron-Sirot",     60),
    ],

    # Semaine Pronote 29 — 15 au 20 mars
    29: [
        ("jeudi",   "14:00", "Maths",        "M. Masselin",        60),
        ("lundi",   "16:30", "Anglais",      "M. Le Bihan",        60),
    ],

    # Semaine Pronote 30 — 22 au 27 mars
    30: [
        ("lundi",   "17:00", "Physique",     "M. Dessup",          60),
        ("mardi",   "13:00", "Informatique", "M. Jacques",        60),
    ],
}

# Create a new deck with a unique ID
my_deck_id = 2099400160
my_deck = genanki.Deck(
    my_deck_id,
    'Spé::Physique::Electrocinétique::E1 - Systèmes linéaires / filtrage::Vrai ou Faux'
)

# Add notes (cards) to the deck
for item in cards_data:
    question_text = item[0]
    answer_val = item[1]
    comment_text = item[2]

    # Recto de la carte
    front_content = f"<b>{header}</b><br><br>{question_text}"

    # Verso : Réponse centrée sous l'entête, puis commentaire
    back_content = f"<div style='text-align: center;'><b>{answer_val}</b></div>"
    if comment_text:
        back_content += f"<br><br>{comment_text}"

    note = genanki.Note(
        model=my_model,
        fields=[front_content, back_content]
    )
    my_deck.add_note(note)

# Save the deck to a file
genanki.Package(my_deck).write_to_file('C:/Users/alban/Downloads/physique_e1_vrai_faux.apkg')

print('Fichier physique_e1_vrai_faux.apkg généré avec succès.')