"""Page shell. The night-ground painting is applied once, here, on the root."""

import reflex as rx
from reflex_components_core.react_router.dom import ReactRouterLink

from solis.components.canvas import canvas_face
from solis.data import NAV, WORKS
from solis.state import SiteState


def site_link(*children, href: str, **props) -> rx.Component:
    """Client-side link without the Radix theme stylesheet."""
    return ReactRouterLink.create(*children, href=href, **props)


def _is_current(href: str):
    path = SiteState.router.page.path
    if href == "/":
        return (path == "/") | (path == "")
    return path == href


def nav_link(index: str, label: str, href: str, large: bool = False) -> rx.Component:
    current = _is_current(href)
    return site_link(
        rx.el.span(index, class_name="nav-index"),
        rx.el.span(label, class_name="nav-label"),
        href=href,
        on_click=SiteState.close_menu,
        class_name="nav-link nav-link-large" if large else "nav-link",
        aria_current=rx.cond(current, "page", "false"),
        color=rx.cond(current, "var(--paper)", "var(--muted)"),
        border_left_color=rx.cond(current, "var(--orange)", "transparent"),
    )


def spine() -> rx.Component:
    return rx.el.aside(
        site_link(
            rx.el.span("MS", class_name="mark"),
            href="/",
            class_name="mark-link",
            aria_label="Maren Solis, studio",
            on_click=SiteState.close_menu,
        ),
        rx.el.p("Maren Solis", class_name="spine-name"),
        rx.el.nav(
            *[nav_link(index, label, href) for index, label, href in NAV],
            aria_label="Sections",
            class_name="spine-nav",
        ),
        rx.el.div(
            rx.el.p("Night ground", class_name="spine-caption"),
            class_name="spine-foot",
        ),
        class_name="spine",
    )


def topbar() -> rx.Component:
    return rx.el.header(
        site_link(
            rx.el.span("MS", class_name="mark mark-small"),
            rx.el.span("Maren Solis", class_name="topbar-name"),
            href="/",
            class_name="topbar-brand",
            on_click=SiteState.close_menu,
        ),
        rx.el.button(
            rx.cond(SiteState.menu_open, "Close", "Menu"),
            type="button",
            class_name="menu-toggle",
            aria_expanded=SiteState.menu_open,
            aria_controls="mobile-menu",
            on_click=SiteState.toggle_menu,
        ),
        class_name="topbar",
    )


def mobile_menu() -> rx.Component:
    return rx.cond(
        SiteState.menu_open,
        rx.el.nav(
            *[nav_link(index, label, href, large=True) for index, label, href in NAV],
            id="mobile-menu",
            aria_label="Sections",
            class_name="mobile-menu",
        ),
    )


def lightbox() -> rx.Component:
    return rx.cond(
        SiteState.open_id != "",
        rx.el.div(
            rx.el.button(
                "",
                type="button",
                class_name="lightbox-backdrop",
                aria_label="Close the painting",
                on_click=SiteState.close_work,
            ),
            rx.el.div(
                rx.el.div(
                    *[
                        rx.el.div(
                            canvas_face(work),
                            class_name="lightbox-face",
                            display=rx.cond(
                                SiteState.open_id == work["id"],
                                "block",
                                "none",
                            ),
                        )
                        for work in WORKS
                    ],
                    class_name="lightbox-stage",
                ),
                rx.el.div(
                    rx.el.p(SiteState.open_family, class_name="kicker"),
                    rx.el.h2(SiteState.open_title, class_name="lightbox-title"),
                    rx.el.p(
                        SiteState.open_year,
                        " · ",
                        SiteState.open_size,
                        class_name="meta-sub",
                    ),
                    rx.el.p(SiteState.open_medium, class_name="lightbox-medium"),
                    rx.el.p(SiteState.open_note, class_name="lightbox-note"),
                    rx.el.button(
                        "Close",
                        type="button",
                        class_name="btn-ghost",
                        on_click=SiteState.close_work,
                    ),
                    class_name="lightbox-copy",
                ),
                class_name="lightbox-panel",
                role="dialog",
                aria_modal="true",
                aria_label=SiteState.open_title,
            ),
            class_name="lightbox",
        ),
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.p("Maren Solis", class_name="footer-name"),
                rx.el.p("Alcântara, Lisbon", class_name="footer-line"),
                rx.el.a(
                    "studio@marensolis.studio",
                    href="mailto:studio@marensolis.studio",
                    class_name="footer-line footer-mail",
                ),
            ),
            rx.el.nav(
                *[
                    site_link(
                        label,
                        href=href,
                        class_name="footer-link",
                        on_click=SiteState.close_menu,
                    )
                    for _, label, href in NAV
                ],
                aria_label="Footer",
                class_name="footer-nav",
            ),
            class_name="footer-grid",
        ),
        rx.el.p(
            "Fictional studio. The commission form stays in this browser session and does not send email.",
            class_name="footer-note",
        ),
        class_name="glass panel footer",
    )


def shell(*children: rx.Component) -> rx.Component:
    """Root for every page. The painting is fixed to the viewport here, once."""
    return rx.el.div(
        rx.el.a("Skip to content", href="#content", class_name="skip-link"),
        spine(),
        topbar(),
        mobile_menu(),
        rx.el.main(
            rx.el.div(*children, footer(), class_name="page-wrap"),
            id="content",
            class_name="page-offset",
        ),
        lightbox(),
        class_name=rx.cond(
            SiteState.menu_open | (SiteState.open_id != ""),
            "site-root lock",
            "site-root",
        ),
        background_image='url("/background.jpg")',
        background_size="cover",
        background_position="center",
        background_attachment="fixed",
        background_repeat="no-repeat",
        background_color="#070b16",
        min_height="100vh",
    )


def page_intro(index: str, title: str, deck: str) -> rx.Component:
    return rx.el.header(
        rx.el.p(index, class_name="kicker"),
        rx.el.h1(title, class_name="page-title"),
        rx.el.p(deck, class_name="deck"),
        class_name="glass panel intro",
    )
