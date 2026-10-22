"""Maren Solis — Night Ground. A Reflex portfolio."""

import reflex as rx

from solis.pages.commission import commission
from solis.pages.home import home
from solis.pages.life import life
from solis.pages.not_found import not_found
from solis.pages.shows import shows
from solis.pages.works import works

app = rx.App(
    html_lang="en",
    stylesheets=["/styles.css"],
    head_components=[
        rx.el.link(rel="icon", href="/favicon.svg", type="image/svg+xml"),
    ],
)

app.add_page(
    home,
    route="/",
    title="Maren Solis — Night Ground",
    description="Portfolio of Maren Solis, a fictional abstract painter working in oil and cold wax on a navy ground in Lisbon.",
    image="/background.jpg",
)
app.add_page(
    works,
    route="/works",
    title="Works — Maren Solis",
    description="Twelve abstract paintings. Filter by color and open a wall label.",
    image="/background.jpg",
)
app.add_page(
    life,
    route="/life",
    title="Life — Maren Solis",
    description="Biography, materials, and the Alcântara studio.",
    image="/background.jpg",
)
app.add_page(
    shows,
    route="/shows",
    title="Shows — Maren Solis",
    description="Exhibitions, upcoming and archived, for the painter Maren Solis.",
    image="/background.jpg",
)
app.add_page(
    commission,
    route="/commission",
    title="Commission — Maren Solis",
    description="Request a canvas. The form validates in the browser session and does not send email.",
    image="/background.jpg",
)
app.add_page(
    not_found,
    route="/404",
    title="Not on this wall — Maren Solis",
    description="That path is not a room in the studio.",
    image="/background.jpg",
)
