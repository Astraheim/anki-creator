from datetime import datetime, timedelta
from uuid import uuid4
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

CALENDAR_NAME = "Khôlles MPI — Groupe 8"
TIMEZONE = "Europe/Paris"

OUTPUT_PATH = Path(
    r"C:\Users\alban\Documents\Prépa\Spé\Autres\ICS Creator"
    r"\Kholles_MPI_Groupe8.ics"
)


# ============================================================
# SEMAINES PRONOTE
#
# IMPORTANT :
# La semaine PRONOTE n°1 est la semaine contenant
# le mardi 1er septembre 2026.
#
# On utilise uniquement les numéros entre parenthèses
# du planning Pronote.
# ============================================================

week_dates = {

    1:  "2026-08-31",
    2:  "2026-09-07",
    3:  "2026-09-14",
    4:  "2026-09-21",
    5:  "2026-09-28",
    6:  "2026-10-05",
    7:  "2026-10-12",

    # Vacances de la Toussaint :
    # semaines 8 et 9

    10: "2026-11-02",
    11: "2026-11-09",
    12: "2026-11-16",
    13: "2026-11-23",
    14: "2026-11-30",
    15: "2026-12-07",

    # Vacances de Noël :
    # semaines 16 à 18

    19: "2027-01-04",
    20: "2027-01-11",
    21: "2027-01-18",
    22: "2027-01-25",

    # Vacances d'hiver :
    # semaine 23

    24: "2027-02-08",
    25: "2027-02-15",

    # Vacances d'hiver :
    # semaines 26 et 27

    28: "2027-03-08",
    29: "2027-03-15",
    30: "2027-03-22",
}


# ============================================================
# KHÔLLES — GROUPE 8
#
# Format :
#
# ("jour", "heure", "matière", "professeur", durée_en_minutes)
#
# ============================================================

colles_by_week = {

    # --------------------------------------------------------
    # SEMAINE PRONOTE 3
    # 14 → 19 septembre
    # --------------------------------------------------------

    3: [
        ("lundi", "16:00", "Anglais", "Mme Lerouilly", 60),
        ("mardi", "17:30", "Maths", "M. Capelle", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 4
    # 21 → 26 septembre
    # --------------------------------------------------------
    # Français ajouté ici comme demandé.
    # --------------------------------------------------------

    4: [
        ("mardi", "13:00", "Physique", "Mme Najid", 60),
        ("jeudi", "14:00", "Maths", "M. Briens", 60),
        ("jeudi", "15:30", "Français", "Mme Glatigny", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 5
    # 28 septembre → 3 octobre
    # --------------------------------------------------------

    5: [
        ("lundi", "16:00", "Maths", "M. Bruyère", 60),
        ("jeudi", "14:00", "Anglais", "Mme Thompson", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 6
    # 5 → 10 octobre
    # --------------------------------------------------------

    6: [
        ("jeudi", "15:00", "Physique", "M. Guillon", 60),
        ("vendredi", "13:00", "Informatique", "M. Michel", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 7
    # 12 → 17 octobre
    # --------------------------------------------------------

    7: [
        ("jeudi", "13:00", "Maths", "M. Mahé", 60),
        ("jeudi", "15:00", "Anglais", "M. Romanski", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 10
    # 2 → 7 novembre
    # --------------------------------------------------------

    10: [
        ("mardi", "17:00", "Maths", "M. Lefebvre", 60),
        ("jeudi", "14:00", "Physique", "M. Hiron-Sirot", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 11
    # 9 → 14 novembre
    # --------------------------------------------------------

    11: [
        ("lundi", "16:00", "Anglais", "Mme Dufour", 60),
        ("jeudi", "14:00", "Maths", "M. Masselin", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 12
    # 16 → 21 novembre
    # --------------------------------------------------------

    12: [
        ("lundi", "17:00", "Physique", "M. Dessup", 60),
        ("mardi", "13:00", "Informatique", "M. Jacques", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 13
    # 23 → 28 novembre
    # --------------------------------------------------------

    13: [
        ("lundi", "16:30", "Anglais", "M. Le Bihan", 60),
        ("jeudi", "15:00", "Maths", "M. Taviot", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 14
    # 30 novembre → 5 décembre
    # --------------------------------------------------------

    14: [
        ("lundi", "17:30", "Physique", "M. Kristensen", 60),
        ("jeudi", "16:00", "Maths", "M. Brua", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 15
    # 7 → 12 décembre
    # --------------------------------------------------------

    15: [
        ("jeudi", "14:00", "Anglais", "M. Romanski", 60),
        ("jeudi", "16:00", "Maths", "M. Brua", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 19
    # 4 → 9 janvier
    # --------------------------------------------------------

    19: [
        ("jeudi", "15:00", "Physique", "M. Le Breton", 60),
        ("mardi", "13:00", "Informatique", "M. Jacques", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 20
    # 11 → 16 janvier
    # --------------------------------------------------------
    # Français ajouté ici comme demandé.
    # --------------------------------------------------------

    20: [
        ("mardi", "17:30", "Maths", "M. Capelle", 60),
        ("jeudi", "14:00", "Français", "Mme Glatigny", 60),
        ("jeudi", "15:00", "Physique", "M. Le Breton", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 21
    # 18 → 23 janvier
    # --------------------------------------------------------

    21: [
        ("lundi", "16:00", "Anglais", "Mme Lerouilly", 60),
        ("jeudi", "14:00", "Maths", "M. Briens", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 22
    # 25 → 30 janvier
    # --------------------------------------------------------

    22: [
        ("lundi", "16:00", "Maths", "M. Bruyère", 60),
        ("jeudi", "14:00", "Anglais", "Mme Thompson", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 24
    # 8 → 13 février
    # --------------------------------------------------------

    24: [
        ("jeudi", "15:00", "Physique", "M. Guillon", 60),
        ("vendredi", "13:00", "Informatique", "M. Michel", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 25
    # 15 → 20 février
    # --------------------------------------------------------

    25: [
        ("jeudi", "13:00", "Maths", "M. Mahé", 60),
        ("jeudi", "15:00", "Anglais", "M. Romanski", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 28
    # 8 → 13 mars
    # --------------------------------------------------------

    28: [
        ("mardi", "17:00", "Maths", "M. Lefebvre", 60),
        ("jeudi", "14:00", "Physique", "M. Hiron-Sirot", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 29
    # 15 → 20 mars
    # --------------------------------------------------------

    29: [
        ("lundi", "16:30", "Anglais", "M. Le Bihan", 60),
        ("jeudi", "14:00", "Maths", "M. Masselin", 60),
    ],


    # --------------------------------------------------------
    # SEMAINE PRONOTE 30
    # 22 → 27 mars
    # --------------------------------------------------------

    30: [
        ("lundi", "17:00", "Physique", "M. Dessup", 60),
        ("mardi", "13:00", "Informatique", "M. Jacques", 60),
    ],
}


# ============================================================
# JOURS
# ============================================================

days = {
    "lundi": 0,
    "mardi": 1,
    "mercredi": 2,
    "jeudi": 3,
    "vendredi": 4,
}


# ============================================================
# FONCTIONS
# ============================================================

def make_datetime(week_number, day_name, time_str):

    if week_number not in week_dates:
        raise ValueError(
            f"Semaine Pronote inconnue : {week_number}"
        )

    if day_name not in days:
        raise ValueError(
            f"Jour invalide : {day_name}"
        )

    monday = datetime.strptime(
        week_dates[week_number],
        "%Y-%m-%d"
    )

    hour, minute = map(
        int,
        time_str.split(":")
    )

    return (
        monday
        + timedelta(days=days[day_name])
        + timedelta(hours=hour, minutes=minute)
    )


def fmt(dt):
    return dt.strftime("%Y%m%dT%H%M%S")


def escape_ics(text):

    return (
        text
        .replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


# ============================================================
# VÉRIFICATION
# ============================================================

print()
print("=" * 70)
print("        VÉRIFICATION — KHÔLLES GROUPE 8")
print("=" * 70)
print()

total = 0
errors = 0

for week in sorted(week_dates):

    colles = colles_by_week.get(week, [])
    count = len(colles)

    total += count

    # 3 khôlles uniquement en semaines 4 et 20
    if week in (4, 20):

        if count == 3:
            status = "OK — 3 khôlles (Français)"
        else:
            status = "⚠ ERREUR — attendu : 3"
            errors += 1

    else:

        if count == 2:
            status = "OK — 2 khôlles"
        elif count == 0:
            status = "— aucune khôlle"
        else:
            status = f"⚠ À VÉRIFIER — {count}"
            errors += 1

    print(
        f"Semaine Pronote {week:2d} : "
        f"{count} khôlle(s) → {status}"
    )

    for day, time, subject, teacher, duration in colles:

        start = make_datetime(
            week,
            day,
            time
        )

        end = start + timedelta(
            minutes=duration
        )

        print(
            f"    {start.strftime('%d/%m/%Y')} "
            f"{start.strftime('%H:%M')}–"
            f"{end.strftime('%H:%M')} | "
            f"{subject} | {teacher}"
        )

    print()


print("-" * 70)
print(f"TOTAL : {total} khôlles")

if errors == 0:
    print("VÉRIFICATION : OK")
else:
    print(
        f"VÉRIFICATION : {errors} semaine(s) à contrôler"
    )

print("=" * 70)
print()


# ============================================================
# GÉNÉRATION DU FICHIER ICS
# ============================================================

lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//OpenAI//Kholles MPI Groupe 8//FR",
    "CALSCALE:GREGORIAN",
    f"X-WR-CALNAME:{escape_ics(CALENDAR_NAME)}",
    f"X-WR-TIMEZONE:{TIMEZONE}",
]


timestamp = datetime.utcnow().strftime(
    "%Y%m%dT%H%M%SZ"
)


for week in sorted(colles_by_week):

    for (
        day,
        time,
        subject,
        teacher,
        duration
    ) in colles_by_week[week]:

        start = make_datetime(
            week,
            day,
            time
        )

        end = start + timedelta(
            minutes=duration
        )

        summary = (
            f"Khôlle {subject} — {teacher}"
        )

        description = (
            f"Khôlle {subject} du groupe 8.\\n"
            f"Professeur : {teacher}\\n"
            f"Semaine Pronote : {week}"
        )

        lines.extend([
            "BEGIN:VEVENT",

            f"UID:{uuid4()}",

            f"DTSTAMP:{timestamp}",

            f"DTSTART;TZID={TIMEZONE}:{fmt(start)}",

            f"DTEND;TZID={TIMEZONE}:{fmt(end)}",

            f"SUMMARY:{escape_ics(summary)}",

            f"DESCRIPTION:{escape_ics(description)}",

            "END:VEVENT",
        ])


lines.append("END:VCALENDAR")


# ============================================================
# ÉCRITURE
# ============================================================

OUTPUT_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_PATH.write_text(
    "\r\n".join(lines),
    encoding="utf-8"
)


print(
    f"Fichier ICS généré :\n{OUTPUT_PATH}"
)

print("DONE")