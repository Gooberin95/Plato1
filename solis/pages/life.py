"""Biography, materials, and a studio wall that is not a likeness."""

import reflex as rx

from solis.components.canvas import canvas_face
from solis.components.layout import page_intro, shell
from solis.data import STUDIO_WALL

FACTS = [
    ("Born", "1986, Porto"),
    ("Works", "Alcântara, Lisbon"),
    ("Ground", "Prussian blue, bone black, alizarin"),
    ("Medium", "Oil and cold wax on linen"),
    ("Rooms", "Galeria Lume, Lisbon · Salle Basse, Marseille"),
    ("Hour", "She starts when the light fails"),
]

MATERIALS = [
    "Belgian linen, double-primed, then covered again with the night ground.",
    "Cold wax medium, enough that the stroke keeps the mark of the knife.",
    "Cadmium orange, cobalt blue, viridian, alizarin crimson, chrome yellow.",
    "Acrylic ink, flicked, for the small interruptions.",
    "No varnish. The wax is the surface.",
]


def life() -> rx.Component:
    return shell(
        page_intro(
            "03  —  Life",
            "Porto, then the warehouse.",
            "A short life of the painter. The rectangle beside the text is the studio wall in late 2025, not a portrait.",
        ),
        rx.el.section(
            rx.el.div(
                canvas_face(STUDIO_WALL),
                rx.el.p(
                    "Studio wall, Alcântara, late 2025. Not a likeness.",
                    class_name="meta-sub portrait-caption",
                ),
                class_name="portrait",
            ),
            rx.el.div(
                rx.el.p(
                    "Maren Solis was born in Porto in 1986, on the side of the river the postcards crop out. She painted the water as a child and was told to lighten it. She has been darkening grounds ever since.",
                    class_name="prose",
                ),
                rx.el.p(
                    "She studied painting at the Faculty of Fine Arts in Lisbon, then spent a year in a rented room in Lyon grinding pigment for other people and keeping the evenings for herself. The night ground — Prussian, bone black, a thread of alizarin — was settled there, on a canvas leaned against a wardrobe.",
                    class_name="prose",
                ),
                rx.el.p(
                    "Since 2016 the studio has been a former tile warehouse in Alcântara. The windows face west. She does not paint into the sunset. She waits until the brick goes dull, rolls the ground if it needs another day, and puts down five or six strokes. Some evenings that is the painting. Some evenings she scrapes it back and the scrape is the painting.",
                    class_name="prose",
                ),
                rx.el.p(
                    "Galeria Lume on Rua das Gaivotas has shown her since the debut in 2020. Salle Basse, a low room in Marseille, took the 2026 solo. She ships crated, and she does not attend every opening. The work is the visit.",
                    class_name="prose",
                ),
                class_name="bio-copy",
            ),
            class_name="glass panel bio-grid",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.p("Facts", class_name="kicker"),
                rx.el.dl(
                    *[
                        rx.el.div(
                            rx.el.dt(label, class_name="fact-label"),
                            rx.el.dd(value, class_name="fact-value"),
                            class_name="fact-row",
                        )
                        for label, value in FACTS
                    ],
                    class_name="facts",
                ),
                class_name="facts-col",
            ),
            rx.el.div(
                rx.el.p("On the table", class_name="kicker"),
                rx.el.ul(
                    *[rx.el.li(item) for item in MATERIALS],
                    class_name="materials",
                ),
                class_name="materials-col",
            ),
            class_name="glass panel split",
        ),
    )
