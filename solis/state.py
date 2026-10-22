"""Session state: navigation, gallery, palette, exhibitions, and the commission form."""

import re
from typing import Any

import reflex as rx

from solis.data import PIGMENTS, SHOWS, WORKS

_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _clean(value: object) -> str:
    return str(value or "").strip()


class SiteState(rx.State):
    """One state tree for the whole studio site."""

    menu_open: bool = False
    active_filter: str = "All"
    open_id: str = ""
    open_title: str = ""
    open_year: str = ""
    open_medium: str = ""
    open_size: str = ""
    open_family: str = ""
    open_note: str = ""

    pigment: str = "Ground"
    show_filter: str = "All"

    name: str = ""
    email: str = ""
    city: str = ""
    scale: str = ""
    palette: str = ""
    message: str = ""
    error_name: str = ""
    error_email: str = ""
    error_scale: str = ""
    error_palette: str = ""
    error_message: str = ""
    submitted: bool = False

    @rx.event
    def toggle_menu(self):
        self.menu_open = not self.menu_open

    @rx.event
    def close_menu(self):
        self.menu_open = False

    @rx.event
    def set_filter(self, family: str):
        self.active_filter = family

    @rx.event
    def open_work(self, work_id: str):
        for work in WORKS:
            if work["id"] == work_id:
                self.menu_open = False
                self.open_id = work["id"]
                self.open_title = work["title"]
                self.open_year = work["year"]
                self.open_medium = work["medium"]
                self.open_size = work["size"]
                self.open_family = work["family"]
                self.open_note = work["note"]
                return

    @rx.event
    def close_work(self):
        self.open_id = ""

    @rx.event
    def choose_pigment(self, name: str):
        self.pigment = name

    @rx.event
    def set_show_filter(self, value: str):
        self.show_filter = value

    @rx.event
    def choose_scale(self, value: str):
        self.scale = value
        self.error_scale = ""

    @rx.event
    def choose_palette(self, value: str):
        self.palette = value
        self.error_palette = ""

    @rx.event
    def submit_request(self, form_data: dict[str, Any]):
        """Validate the commission note and keep it in this session."""
        self.name = _clean(form_data.get("name"))
        self.email = _clean(form_data.get("email"))
        self.city = _clean(form_data.get("city"))
        self.message = _clean(form_data.get("message"))
        self.error_name = ""
        self.error_email = ""
        self.error_scale = ""
        self.error_palette = ""
        self.error_message = ""
        ok = True
        if len(self.name) < 2:
            self.error_name = "A name, even a short one. The note is addressed with it."
            ok = False
        if _EMAIL.match(self.email) is None:
            self.error_email = "That does not look like an email the studio can answer."
            ok = False
        if self.scale == "":
            self.error_scale = "Choose a scale so the note is about a wall, not a guess."
            ok = False
        if self.palette == "":
            self.error_palette = "Pick the color family you want the canvas to lean toward."
            ok = False
        if len(self.message) < 20:
            self.error_message = (
                "Say a little more: where it will hang, and what you want the color to do. "
                "Twenty characters at least."
            )
            ok = False
        self.submitted = ok

    @rx.event
    def reset_form(self):
        self.submitted = False
        self.name = ""
        self.email = ""
        self.city = ""
        self.scale = ""
        self.palette = ""
        self.message = ""
        self.error_name = ""
        self.error_email = ""
        self.error_scale = ""
        self.error_palette = ""
        self.error_message = ""

    @rx.var
    def visible_count(self) -> int:
        if self.active_filter == "All":
            return len(WORKS)
        return sum(1 for work in WORKS if work["family"] == self.active_filter)

    @rx.var
    def pigment_line(self) -> str:
        return PIGMENTS[self.pigment]

    @rx.var
    def show_count(self) -> int:
        if self.show_filter == "All":
            return len(SHOWS)
        return sum(1 for show in SHOWS if show["when"] == self.show_filter)

    @rx.var
    def scale_detail(self) -> str:
        details = {
            "Study": "30 × 30 cm",
            "Chamber": "80 × 60 cm",
            "Wall": "140 × 110 cm",
            "Field": "200 × 160 cm",
        }
        return details.get(self.scale, "")
