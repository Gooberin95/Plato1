"""Commission request. Validation runs in Reflex state; nothing is emailed."""

import reflex as rx

from solis.components.layout import page_intro, shell
from solis.data import PALETTES, PIGMENT_COLORS, SCALES
from solis.state import SiteState


def _error(message: rx.Var) -> rx.Component:
    return rx.cond(
        message != "",
        rx.el.p(message, class_name="error", role="alert"),
    )


def _choice(value: str, detail: str, selected, handler) -> rx.Component:
    current = selected == value
    return rx.el.button(
        rx.el.span(value, class_name="choice-name"),
        rx.el.span(detail, class_name="choice-detail"),
        type="button",
        class_name="choice",
        aria_pressed=current,
        on_click=handler(value),
        background_color=rx.cond(current, "var(--orange)", "transparent"),
        color=rx.cond(current, "#1a0e04", "var(--paper)"),
        border_color=rx.cond(current, "var(--orange)", "rgba(244, 239, 230, 0.28)"),
    )


def _palette(name: str) -> rx.Component:
    current = SiteState.palette == name
    return rx.el.button(
        rx.el.span(
            class_name="choice-dot",
            style={"background": PIGMENT_COLORS[name]},
            aria_hidden="true",
        ),
        name,
        type="button",
        class_name="choice choice-inline",
        aria_pressed=current,
        on_click=SiteState.choose_palette(name),
        background_color=rx.cond(current, "var(--orange)", "transparent"),
        color=rx.cond(current, "#1a0e04", "var(--paper)"),
        border_color=rx.cond(current, "var(--orange)", "rgba(244, 239, 230, 0.28)"),
    )


def _form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.label("Name", html_for="commission-name", class_name="label"),
            rx.el.input(
                id="commission-name",
                name="name",
                type="text",
                placeholder="The name the note should use",
                auto_complete="name",
                class_name="field",
                aria_invalid=SiteState.error_name != "",
            ),
            _error(SiteState.error_name),
            class_name="field-block",
        ),
        rx.el.div(
            rx.el.label("Email", html_for="commission-email", class_name="label"),
            rx.el.input(
                id="commission-email",
                name="email",
                type="email",
                placeholder="you@example.com",
                auto_complete="email",
                class_name="field",
                aria_invalid=SiteState.error_email != "",
            ),
            _error(SiteState.error_email),
            class_name="field-block",
        ),
        rx.el.div(
            rx.el.label("City", html_for="commission-city", class_name="label"),
            rx.el.input(
                id="commission-city",
                name="city",
                type="text",
                placeholder="Optional. Where the painting would live.",
                auto_complete="address-level2",
                class_name="field",
            ),
            class_name="field-block",
        ),
        rx.el.fieldset(
            rx.el.legend("Scale", class_name="label"),
            rx.el.div(
                *[
                    _choice(value, detail, SiteState.scale, SiteState.choose_scale)
                    for value, detail in SCALES
                ],
                class_name="choice-row",
            ),
            _error(SiteState.error_scale),
            class_name="field-block",
        ),
        rx.el.fieldset(
            rx.el.legend("Palette", class_name="label"),
            rx.el.div(
                *[_palette(name) for name in PALETTES],
                class_name="choice-row",
            ),
            _error(SiteState.error_palette),
            class_name="field-block",
        ),
        rx.el.div(
            rx.el.label("The room", html_for="commission-message", class_name="label"),
            rx.el.textarea(
                id="commission-message",
                name="message",
                placeholder="Where it will hang, the light in the evening, and what you want the color to do.",
                class_name="field field-area",
                rows="6",
                aria_invalid=SiteState.error_message != "",
            ),
            _error(SiteState.error_message),
            class_name="field-block",
        ),
        rx.el.div(
            rx.el.button("Hold this note", type="submit", class_name="btn-solid"),
            rx.el.p(
                "Checked in the session. Not emailed.",
                class_name="fine-print",
            ),
            class_name="form-actions",
        ),
        class_name="commission-form",
        no_validate=True,
        on_submit=SiteState.submit_request,
    )


def _success() -> rx.Component:
    return rx.el.div(
        rx.el.p("Held", class_name="kicker"),
        rx.el.h2("The note is on this page.", class_name="section-title"),
        rx.el.p(
            SiteState.name,
            ", the studio can read this back while the tab is open. It has not been sent anywhere.",
            class_name="deck",
        ),
        rx.el.dl(
            rx.el.div(
                rx.el.dt("Scale", class_name="fact-label"),
                rx.el.dd(
                    SiteState.scale,
                    " — ",
                    SiteState.scale_detail,
                    class_name="fact-value",
                ),
                class_name="fact-row",
            ),
            rx.el.div(
                rx.el.dt("Palette", class_name="fact-label"),
                rx.el.dd(SiteState.palette, class_name="fact-value"),
                class_name="fact-row",
            ),
            rx.cond(
                SiteState.city != "",
                rx.el.div(
                    rx.el.dt("City", class_name="fact-label"),
                    rx.el.dd(SiteState.city, class_name="fact-value"),
                    class_name="fact-row",
                ),
            ),
            rx.el.div(
                rx.el.dt("Email", class_name="fact-label"),
                rx.el.dd(SiteState.email, class_name="fact-value"),
                class_name="fact-row",
            ),
            class_name="facts success-facts",
        ),
        rx.el.blockquote(SiteState.message, class_name="held-message"),
        rx.el.p(
            "To ask a person, copy the same words to studio@marensolis.studio. That address belongs to this fiction.",
            class_name="fine-print",
        ),
        rx.el.button(
            "Write another note",
            type="button",
            class_name="btn-ghost",
            on_click=SiteState.reset_form,
        ),
        class_name="success",
    )


def commission() -> rx.Component:
    return shell(
        page_intro(
            "05  —  Commission",
            "A canvas for a room with evening light.",
            "The studio takes a small number of commissions each year. Most are a single painting. Say the wall, the scale, and the color you want to remain.",
        ),
        rx.el.section(
            rx.el.aside(
                rx.el.p("Before you write", class_name="kicker"),
                rx.el.ul(
                    rx.el.li("About twelve weeks from a yes to a crated painting."),
                    rx.el.li("A deposit of forty percent. The rest when it leaves Lisbon."),
                    rx.el.li("Ships crated from Alcântara. The studio does not install."),
                    rx.el.li("Studies are sometimes available sooner. Fields take the season."),
                    class_name="materials",
                ),
                class_name="form-aside",
            ),
            rx.cond(SiteState.submitted, _success(), _form()),
            class_name="glass panel form-grid",
        ),
    )
