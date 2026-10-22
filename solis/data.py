"""Catalog, exhibitions, and the night palette for Maren Solis."""

NAV = [
    ("01", "Studio", "/"),
    ("02", "Works", "/works"),
    ("03", "Life", "/life"),
    ("04", "Shows", "/shows"),
    ("05", "Commission", "/commission"),
]

FAMILIES = ["All", "Ember", "Tide", "Verdant", "Crimson", "Gilt"]

PIGMENT_ORDER = ["Ground", "Ember", "Tide", "Verdant", "Crimson", "Gilt"]

PIGMENTS = {
    "Ground": (
        "The ground is not black. Prussian blue, bone black, and a thread of "
        "alizarin are rolled into the linen until it reads as evening."
    ),
    "Ember": (
        "Cadmium orange, in short loaded bars. It is the last light on the "
        "warehouse brick, and she stops before it explains itself."
    ),
    "Tide": (
        "Cobalt, with a deeper ultramarine underneath. The river, only the "
        "part that refuses the streetlamps."
    ),
    "Verdant": (
        "Viridian, never nudged toward yellow. She wants the green to feel "
        "manufactured and alive in the same stroke."
    ),
    "Crimson": (
        "Alizarin beside a hotter naphthol red. Used the way a siren is used: "
        "rarely, and from a street or two away."
    ),
    "Gilt": (
        "Chrome yellow, sometimes a nickel-bright strip. The color that is "
        "still there after the others have receded."
    ),
}

PIGMENT_COLORS = {
    "Ground": "#0c1836",
    "Ember": "#ff9f1c",
    "Tide": "#3c7dff",
    "Verdant": "#2fbf5a",
    "Crimson": "#e23b4a",
    "Gilt": "#f2d04b",
}

SCALES = [
    ("Study", "30 × 30 cm"),
    ("Chamber", "80 × 60 cm"),
    ("Wall", "140 × 110 cm"),
    ("Field", "200 × 160 cm"),
]

PALETTES = ["Ember", "Tide", "Verdant", "Crimson", "Gilt"]

SHOW_FILTERS = [
    ("All", "All rooms"),
    ("upcoming", "Upcoming"),
    ("archive", "Archive"),
]

SHOWS = [
    {
        "when": "upcoming",
        "date": "November 2026",
        "title": "Night Ground",
        "kind": "Solo",
        "venue": "Galeria Lume",
        "city": "Lisbon",
        "note": (
            "Twelve canvases from the Alcântara warehouse, hung low. "
            "Harbor, Unnamed and The Yellow That Stayed are in the first room."
        ),
    },
    {
        "when": "upcoming",
        "date": "March 2027",
        "title": "Field Notes",
        "kind": "Group, one wall",
        "venue": "Hall Nord",
        "city": "Antwerp",
        "note": "Three studies and a single wall-scale canvas. She is not traveling with them.",
    },
    {
        "when": "archive",
        "date": "June 2026",
        "title": "Pigment, After Dark",
        "kind": "Solo",
        "venue": "Salle Basse",
        "city": "Marseille",
        "note": "The first time the night ground was shown without daylight in the room.",
    },
    {
        "when": "archive",
        "date": "September 2025",
        "title": "Twelve Rivers",
        "kind": "Group",
        "venue": "The Low Room",
        "city": "Glasgow",
        "note": "Two tide paintings. The cobalt read colder there, which she kept in mind.",
    },
    {
        "when": "archive",
        "date": "March 2024",
        "title": "Cold Wax Studies",
        "kind": "Solo",
        "venue": "Galeria Lume",
        "city": "Lisbon",
        "note": "Smaller canvases, the knife still visible. The wax was the subject.",
    },
    {
        "when": "archive",
        "date": "November 2023",
        "title": "Index of Reds",
        "kind": "Group",
        "venue": "Casa do Azulejo",
        "city": "Porto",
        "note": "A return to the city she left. One crimson, hung opposite a window of tiles.",
    },
    {
        "when": "archive",
        "date": "May 2022",
        "title": "Ember Index",
        "kind": "Solo",
        "venue": "Warehouse 4",
        "city": "Athens",
        "note": "Orange, almost only orange, on grounds that were still too black.",
    },
    {
        "when": "archive",
        "date": "September 2020",
        "title": "First Ground",
        "kind": "Solo",
        "venue": "Galeria Lume",
        "city": "Lisbon",
        "note": "Debut. Eight paintings and a wall label that just said the hour she starts.",
    },
]

WORKS = [
    {
        "id": "harbor",
        "title": "Harbor, Unnamed",
        "year": "2025",
        "medium": "Oil and cold wax on linen",
        "size": "140 × 110 cm",
        "family": "Tide",
        "span": "wide",
        "speck": "a",
        "note": (
            "A cobalt bar crosses a field of near-black the way the river cuts "
            "the city after rain. The orange is a lamp, not a sun."
        ),
        "ground": "linear-gradient(165deg, #071428 0%, #0a1c44 48%, #06101c 100%)",
        "strokes": [
            {"color": "#3c7dff", "top": "16%", "left": "-6%", "width": "68%", "height": "15%", "rotate": "-8deg"},
            {"color": "#2450c8", "top": "30%", "left": "8%", "width": "40%", "height": "9%", "rotate": "-8deg", "opacity": "0.85"},
            {"color": "#ff9f1c", "top": "58%", "left": "42%", "width": "28%", "height": "16%", "rotate": "6deg"},
            {"color": "#f2d04b", "top": "18%", "left": "62%", "width": "18%", "height": "11%", "rotate": "-16deg"},
            {"color": "#e23b4a", "top": "74%", "left": "6%", "width": "14%", "height": "12%", "rotate": "3deg"},
        ],
    },
    {
        "id": "yellow-stayed",
        "title": "The Yellow That Stayed",
        "year": "2026",
        "medium": "Oil and cold wax on linen",
        "size": "80 × 100 cm",
        "family": "Gilt",
        "span": "",
        "speck": "b",
        "note": "Chrome yellow laid down last, and then left alone. Everything else is there so the yellow has somewhere to remain.",
        "ground": "linear-gradient(180deg, #0b0e16 0%, #14120c 100%)",
        "strokes": [
            {"color": "#f2d04b", "top": "58%", "left": "-4%", "width": "86%", "height": "18%", "rotate": "-3deg"},
            {"color": "#ffe56a", "top": "62%", "left": "18%", "width": "34%", "height": "8%", "rotate": "-3deg", "opacity": "0.9"},
            {"color": "#3c7dff", "top": "22%", "left": "12%", "width": "26%", "height": "14%", "rotate": "8deg"},
            {"color": "#2fbf5a", "top": "18%", "left": "78%", "width": "10%", "height": "46%", "rotate": "4deg"},
        ],
    },
    {
        "id": "siren",
        "title": "Alcântara, After the Siren",
        "year": "2024",
        "medium": "Oil and cold wax on linen",
        "size": "160 × 130 cm",
        "family": "Ember",
        "span": "tall",
        "speck": "c",
        "note": "Stacked orange, the shape of shutters. A blue crosses them once, the way a siren crosses a street and is gone.",
        "ground": "linear-gradient(195deg, #120c0a 0%, #1a0d08 55%, #0c1018 100%)",
        "strokes": [
            {"color": "#ff9f1c", "top": "14%", "left": "18%", "width": "46%", "height": "16%", "rotate": "-4deg"},
            {"color": "#f27b16", "top": "34%", "left": "8%", "width": "58%", "height": "18%", "rotate": "3deg"},
            {"color": "#ffb703", "top": "56%", "left": "22%", "width": "50%", "height": "14%", "rotate": "-2deg"},
            {"color": "#3c7dff", "top": "40%", "left": "28%", "width": "48%", "height": "18%", "rotate": "-12deg", "radius": "40%"},
            {"color": "#e23b4a", "top": "78%", "left": "64%", "width": "16%", "height": "10%", "rotate": "8deg"},
        ],
    },
    {
        "id": "viridian",
        "title": "Viridian Ledger",
        "year": "2025",
        "medium": "Oil and cold wax on linen",
        "size": "90 × 90 cm",
        "family": "Verdant",
        "span": "",
        "speck": "b",
        "note": "Two greens that do not match, on purpose. The yellow stroke is the only accounting.",
        "ground": "linear-gradient(150deg, #07140f 0%, #0c1a12 100%)",
        "strokes": [
            {"color": "#1e8f45", "top": "18%", "left": "10%", "width": "48%", "height": "42%", "rotate": "-6deg"},
            {"color": "#2fbf5a", "top": "40%", "left": "36%", "width": "46%", "height": "28%", "rotate": "4deg"},
            {"color": "#c6e34a", "top": "28%", "left": "-8%", "width": "70%", "height": "10%", "rotate": "-18deg"},
            {"color": "#ff9f1c", "top": "72%", "left": "18%", "width": "22%", "height": "16%", "rotate": "2deg"},
        ],
    },
    {
        "id": "crimson-kept",
        "title": "Crimson, Kept",
        "year": "2023",
        "medium": "Oil and cold wax on linen",
        "size": "120 × 90 cm",
        "family": "Crimson",
        "span": "",
        "speck": "c",
        "note": "The red is large and then stopped. She scraped the right edge back to the ground so the color would not take the whole night.",
        "ground": "linear-gradient(180deg, #14080c 0%, #1a0a10 40%, #0c101c 100%)",
        "strokes": [
            {"color": "#8e1d32", "top": "48%", "left": "8%", "width": "70%", "height": "34%", "rotate": "-2deg"},
            {"color": "#e23b4a", "top": "54%", "left": "20%", "width": "42%", "height": "18%", "rotate": "2deg"},
            {"color": "#ff9f1c", "top": "22%", "left": "14%", "width": "36%", "height": "14%", "rotate": "-7deg"},
            {"color": "#3c7dff", "top": "18%", "left": "62%", "width": "22%", "height": "20%", "rotate": "10deg"},
        ],
    },
    {
        "id": "two-blues",
        "title": "Two Blues and a Window",
        "year": "2026",
        "medium": "Oil and cold wax on linen",
        "size": "70 × 90 cm",
        "family": "Tide",
        "span": "",
        "note": "A window cut from the same night the studio wall is painted with. Blue over yellow, then a small orange that got left in the room.",
        "crop": {"pos": "12% 18%", "size": "280%"},
    },
    {
        "id": "chrome-4",
        "title": "Chrome Study No. 4",
        "year": "2022",
        "medium": "Oil and cold wax on linen",
        "size": "40 × 40 cm",
        "family": "Gilt",
        "span": "",
        "speck": "a",
        "note": "One of the early squares. The yellow is thinner than she uses now, and the ground is still a little too black.",
        "ground": "linear-gradient(160deg, #10131c 0%, #0a0c12 100%)",
        "strokes": [
            {"color": "#f2d04b", "top": "22%", "left": "8%", "width": "72%", "height": "22%", "rotate": "-8deg"},
            {"color": "#ff9f1c", "top": "48%", "left": "18%", "width": "64%", "height": "20%", "rotate": "7deg"},
            {"color": "#3c7dff", "top": "66%", "left": "10%", "width": "28%", "height": "16%", "rotate": "-2deg"},
        ],
    },
    {
        "id": "warehouse",
        "title": "The Warehouse Door",
        "year": "2024",
        "medium": "Oil and cold wax on linen",
        "size": "150 × 120 cm",
        "family": "Ember",
        "span": "wide",
        "note": "The door is a stack of orange. This one is taken from the painting that also grounds the site, cropped to the passage.",
        "crop": {"pos": "46% 68%", "size": "250%"},
    },
    {
        "id": "orchard",
        "title": "Night Orchard",
        "year": "2025",
        "medium": "Oil and cold wax on linen",
        "size": "110 × 140 cm",
        "family": "Verdant",
        "span": "tall",
        "speck": "a",
        "note": "A green field with yellow dragged across it, the memory of a lit window in trees. Not fruit. Not a landscape. Just the green staying.",
        "ground": "linear-gradient(180deg, #070b16 0%, #0a1020 100%)",
        "strokes": [
            {"color": "#1e8f45", "top": "16%", "left": "14%", "width": "70%", "height": "58%", "rotate": "2deg"},
            {"color": "#2fbf5a", "top": "24%", "left": "22%", "width": "52%", "height": "36%", "rotate": "-3deg", "opacity": "0.92"},
            {"color": "#c6e34a", "top": "30%", "left": "-6%", "width": "84%", "height": "9%", "rotate": "-14deg"},
            {"color": "#f2d04b", "top": "48%", "left": "8%", "width": "64%", "height": "8%", "rotate": "8deg"},
            {"color": "#ff9f1c", "top": "78%", "left": "58%", "width": "24%", "height": "12%", "rotate": "-4deg"},
        ],
    },
    {
        "id": "red-river",
        "title": "Red Against the River",
        "year": "2021",
        "medium": "Oil and cold wax on linen",
        "size": "100 × 80 cm",
        "family": "Crimson",
        "span": "",
        "note": "The lower right of the night ground, where the red finally takes the corner. An early decision she still stands by.",
        "crop": {"pos": "96% 92%", "size": "270%"},
    },
    {
        "id": "lisbon-gilt",
        "title": "Lisbon Gilt",
        "year": "2026",
        "medium": "Oil and cold wax on linen",
        "size": "60 × 80 cm",
        "family": "Gilt",
        "span": "",
        "speck": "b",
        "note": "Yellow crossing orange, cobalt kept underneath like a curb seen from a tram. Made in an afternoon that ran into night.",
        "ground": "linear-gradient(200deg, #0c1018 0%, #16120c 100%)",
        "strokes": [
            {"color": "#2450c8", "top": "36%", "left": "6%", "width": "78%", "height": "22%", "rotate": "-5deg"},
            {"color": "#ff9f1c", "top": "28%", "left": "20%", "width": "34%", "height": "40%", "rotate": "8deg"},
            {"color": "#f2d04b", "top": "22%", "left": "8%", "width": "54%", "height": "14%", "rotate": "-12deg"},
            {"color": "#2fbf5a", "top": "70%", "left": "62%", "width": "22%", "height": "14%", "rotate": "3deg"},
        ],
    },
    {
        "id": "cobalt",
        "title": "Cobalt, Interrupted",
        "year": "2023",
        "medium": "Oil and cold wax on linen",
        "size": "130 × 100 cm",
        "family": "Tide",
        "span": "tall",
        "speck": "c",
        "note": "The blue was going to be the whole painting. An orange bar was the interruption, and then it was the painting.",
        "ground": "linear-gradient(180deg, #06101f 0%, #102652 55%, #071018 100%)",
        "strokes": [
            {"color": "#3c7dff", "top": "8%", "left": "12%", "width": "62%", "height": "74%", "rotate": "-2deg", "radius": "46% 46% 8% 8%"},
            {"color": "#7aa2ff", "top": "18%", "left": "22%", "width": "36%", "height": "28%", "rotate": "4deg", "opacity": "0.75"},
            {"color": "#ff9f1c", "top": "46%", "left": "-8%", "width": "92%", "height": "14%", "rotate": "-6deg"},
            {"color": "#e23b4a", "top": "78%", "left": "18%", "width": "18%", "height": "10%", "rotate": "5deg"},
        ],
    },
]

FEATURED_IDS = ["harbor", "yellow-stayed", "warehouse"]

STUDIO_WALL = {
    "ground": "linear-gradient(165deg, #070b16 0%, #12101a 55%, #0c121c 100%)",
    "speck": "a",
    "strokes": [
        {"color": "#c6e34a", "top": "10%", "left": "6%", "width": "34%", "height": "14%", "rotate": "-8deg"},
        {"color": "#3c7dff", "top": "18%", "left": "28%", "width": "36%", "height": "16%", "rotate": "2deg"},
        {"color": "#ff9f1c", "top": "32%", "left": "8%", "width": "28%", "height": "14%", "rotate": "-4deg"},
        {"color": "#2fbf5a", "top": "28%", "left": "48%", "width": "42%", "height": "30%", "rotate": "3deg"},
        {"color": "#f2d04b", "top": "36%", "left": "52%", "width": "30%", "height": "8%", "rotate": "-16deg"},
        {"color": "#e23b4a", "top": "62%", "left": "18%", "width": "22%", "height": "18%", "rotate": "4deg"},
        {"color": "#ff9f1c", "top": "70%", "left": "40%", "width": "18%", "height": "22%", "rotate": "-2deg"},
        {"color": "#3c7dff", "top": "74%", "left": "62%", "width": "24%", "height": "14%", "rotate": "8deg", "radius": "40%"},
        {"color": "#f2d04b", "top": "84%", "left": "8%", "width": "30%", "height": "8%", "rotate": "-6deg"},
    ],
}


def work_by_id(work_id: str) -> dict:
    """Return one catalog record by its id."""
    for work in WORKS:
        if work["id"] == work_id:
            return work
    raise KeyError(work_id)
