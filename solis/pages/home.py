"""Studio landing: hero, night palette, and a few paintings on the wall."""

import reflex as rx

from solis.components.canvas import canvas_face
from solis.data import FEATURED_IDS, PIGMENT_COLORS, PIGMENT_ORDER, SHOWS, work_by_id
from solis.components.layout import shell, site_link
from solis.state import SiteState


def _swatch(name: str) -> rx.Component:
    current = SiteState.pigment == name
    return rx.el.button(
        rx.el.span(
            class_name="swatch",
            style={"background": PIGMENT_COLORS[name]},
            aria_hidden="true",
        ),
        rx.el.span(name, class_name="swatch-name"),
        type="button",
        class_name="swatch-btn",
        aria_pressed=current,
        on_click=SiteState.choose_pigment(name),
        border_color=rx.cond(current, "var(--orange)", "transparent"),
    )


def _feature(work_id: str) -> rx.Component:
    work = work_by_id(work_id)
    return rx.el.button(
        canvas_face(work),
        rx.el.div(
            rx.el.p(work["family"], class_name="meta-family"),
            rx.el.p(work["title"], class_name="meta-title"),
            rx.el.p(work["year"], " · ", work["size"], class_name="meta-sub"),
            class_name="work-meta",
        ),
        type="button",
        class_name="work-card",
        aria_label=f"Open {work['title']}",
        on_click=SiteState.open_work(work["id"]),
    )


def home() -> rx.Component:
    nxt = SHOWS[0]
    return shell(
        rx.el.section(
            rx.el.div(
                rx.el.p("01  —  Alcântara  ·  oil and cold wax", class_name="kicker"),
                rx.el.h1(
                    rx.el.span("Color, held", class_name="title-line"),
                    rx.el.span("against the dark.", class_name="title-line"),
                    class_name="hero-title",
                ),
                rx.el.p(
                    "Maren Solis paints on a navy ground, after the light goes. "
                    "The strokes are short, loaded, and few. Orange, cobalt, "
                    "viridian, crimson, chrome yellow — harbor colors, kept.",
                    class_name="deck",
                ),
                rx.el.div(
                    site_link("Enter the studio", href="/works", class_name="btn-solid"),
                    site_link(
                        "Commission a canvas",
                        href="/commission",
                        class_name="btn-ghost",
                    ),
                    class_name="hero-actions",
                ),
                class_name="hero-copy",
            ),
            rx.el.div(
                rx.el.button(
                    canvas_face(work_by_id("harbor")),
                    type="button",
                    class_name="hero-canvas-btn",
                    aria_label="Open Harbor, Unnamed",
                    on_click=SiteState.open_work("harbor"),
                ),
                rx.el.p(
                    rx.el.span("№ 2025"),
                    rx.el.span("Harbor, Unnamed"),
                    rx.el.span("140 × 110 cm"),
                    class_name="wall-label",
                ),
                class_name="hero-aside",
            ),
            class_name="glass panel hero",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.p("The night palette", class_name="kicker"),
                rx.el.h2("Five colors, and the ground they sit on.", class_name="section-title"),
                rx.el.p(
                    "Choose a pigment. The studio note changes with it.",
                    class_name="deck",
                ),
            ),
            rx.el.div(
                *[_swatch(name) for name in PIGMENT_ORDER],
                class_name="pigment-row",
                role="group",
                aria_label="Night palette",
            ),
            rx.el.p(SiteState.pigment_line, class_name="pigment-line"),
            class_name="glass panel",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.p("On the wall now", class_name="kicker"),
                    rx.el.h2("Three from the studio.", class_name="section-title"),
                ),
                site_link("All paintings", href="/works", class_name="text-link"),
                class_name="section-head",
            ),
            rx.el.div(
                *[_feature(work_id) for work_id in FEATURED_IDS],
                class_name="feature-grid",
            ),
            class_name="glass panel",
        ),
        rx.el.section(
            rx.el.blockquote(
                "I am not painting objects. I am painting the moment a color decides to stay.",
                class_name="quote-text",
            ),
            rx.el.p("Studio note, 2024", class_name="meta-sub"),
            rx.el.div(
                rx.el.p("Next room", class_name="kicker"),
                rx.el.h2(nxt["title"], class_name="section-title"),
                rx.el.p(
                    nxt["date"],
                    " · ",
                    nxt["venue"],
                    ", ",
                    nxt["city"],
                    class_name="deck",
                ),
                site_link("The exhibitions", href="/shows", class_name="text-link"),
                class_name="next-show",
            ),
            class_name="glass panel quote-panel",
        ),
    )
