"""Unknown paths, still on the night ground."""

import reflex as rx

from solis.components.layout import shell, site_link


def not_found() -> rx.Component:
    return shell(
        rx.el.section(
            rx.el.p("404", class_name="kicker"),
            rx.el.h1("Not on this wall.", class_name="page-title"),
            rx.el.p(
                "That path is not a room in the studio. The paintings are still where they were.",
                class_name="deck",
            ),
            site_link("Back to the studio", href="/", class_name="btn-solid"),
            class_name="glass panel intro",
        ),
    )
