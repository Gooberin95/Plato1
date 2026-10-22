"""Filterable gallery. Each card opens a wall label in the lightbox."""

import reflex as rx

from solis.components.canvas import canvas_face
from solis.components.layout import page_intro, shell
from solis.data import FAMILIES, WORKS
from solis.state import SiteState


def _chip(family: str) -> rx.Component:
    current = SiteState.active_filter == family
    return rx.el.button(
        family,
        type="button",
        class_name="chip",
        aria_pressed=current,
        on_click=SiteState.set_filter(family),
        background_color=rx.cond(current, "var(--orange)", "transparent"),
        color=rx.cond(current, "#1a0e04", "var(--paper)"),
        border_color=rx.cond(current, "var(--orange)", "rgba(244, 239, 230, 0.28)"),
    )


def _card(work: dict) -> rx.Component:
    span = work["span"]
    span_class = f" span-{span}" if span else ""
    visible = (SiteState.active_filter == "All") | (
        SiteState.active_filter == work["family"]
    )
    return rx.el.button(
        canvas_face(work),
        rx.el.div(
            rx.el.p(work["family"], class_name="meta-family"),
            rx.el.p(work["title"], class_name="meta-title"),
            rx.el.p(work["year"], " · ", work["size"], class_name="meta-sub"),
            class_name="work-meta",
        ),
        type="button",
        class_name=f"work-card{span_class}",
        aria_label=f"Open {work['title']}",
        on_click=SiteState.open_work(work["id"]),
        display=rx.cond(visible, "flex", "none"),
    )


def works() -> rx.Component:
    return shell(
        page_intro(
            "02  —  Works",
            "The paintings.",
            "Twelve canvases. Filter by the color that leads, then open one for the wall label. "
            "Nothing here is fetched from another site: the faces are painted in CSS, or cropped from the ground behind this page.",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    *[_chip(family) for family in FAMILIES],
                    class_name="chip-row",
                    role="group",
                    aria_label="Filter by color family",
                ),
                rx.el.p(
                    rx.cond(
                        SiteState.active_filter == "All",
                        rx.el.span(SiteState.visible_count, " paintings"),
                        rx.el.span(
                            SiteState.visible_count,
                            " in ",
                            SiteState.active_filter,
                        ),
                    ),
                    class_name="count-line",
                ),
                class_name="filter-bar",
            ),
            rx.el.div(*[_card(work) for work in WORKS], class_name="gallery-grid"),
            rx.cond(
                SiteState.visible_count == 0,
                rx.el.p(
                    "Nothing in that family is on the wall.",
                    class_name="deck",
                ),
            ),
            class_name="glass panel",
        ),
    )
