"""Exhibition timeline, with upcoming rooms separated from the archive."""

import reflex as rx

from solis.components.layout import page_intro, shell
from solis.data import SHOW_FILTERS, SHOWS
from solis.state import SiteState


def _filter(value: str, label: str) -> rx.Component:
    current = SiteState.show_filter == value
    return rx.el.button(
        label,
        type="button",
        class_name="chip",
        aria_pressed=current,
        on_click=SiteState.set_show_filter(value),
        background_color=rx.cond(current, "var(--orange)", "transparent"),
        color=rx.cond(current, "#1a0e04", "var(--paper)"),
        border_color=rx.cond(current, "var(--orange)", "rgba(244, 239, 230, 0.28)"),
    )


def _item(show: dict) -> rx.Component:
    visible = (SiteState.show_filter == "All") | (SiteState.show_filter == show["when"])
    kind = "tl-item is-upcoming" if show["when"] == "upcoming" else "tl-item"
    return rx.el.article(
        rx.el.p(show["date"], class_name="tl-date"),
        rx.el.h2(show["title"], class_name="tl-title"),
        rx.el.p(
            show["kind"],
            " · ",
            show["venue"],
            ", ",
            show["city"],
            class_name="meta-sub",
        ),
        rx.el.p(show["note"], class_name="tl-note"),
        class_name=kind,
        display=rx.cond(visible, "block", "none"),
    )


def shows() -> rx.Component:
    return shell(
        page_intro(
            "04  —  Shows",
            "Rooms the paintings have been in.",
            "A short ledger of solos and the group walls that would have them. Upcoming first, then the archive, newest year at the top of what has already closed.",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    *[_filter(value, label) for value, label in SHOW_FILTERS],
                    class_name="chip-row",
                    role="group",
                    aria_label="Filter exhibitions",
                ),
                rx.el.p(SiteState.show_count, " rooms", class_name="count-line"),
                class_name="filter-bar",
            ),
            rx.el.div(*[_item(show) for show in SHOWS], class_name="timeline"),
            class_name="glass panel",
        ),
    )
