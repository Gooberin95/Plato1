"""Painted canvases made of CSS, plus crops of the shared night-ground image."""

import reflex as rx


def canvas_face(work: dict) -> rx.Component:
    """A single abstract canvas. Crops use the local background painting."""
    layers: list[rx.Component] = []
    crop = work.get("crop")
    if crop:
        layers.append(
            rx.el.div(
                class_name="face-crop",
                background_image='url("/background.jpg")',
                background_size=crop["size"],
                background_position=crop["pos"],
                background_repeat="no-repeat",
            )
        )
    else:
        layers.append(rx.el.div(class_name="face-ground", background=work["ground"]))
        for stroke in work.get("strokes", []):
            layers.append(
                rx.el.div(
                    class_name="stroke",
                    background_color=stroke["color"],
                    top=stroke["top"],
                    left=stroke["left"],
                    width=stroke["width"],
                    height=stroke["height"],
                    transform=f"rotate({stroke['rotate']})",
                    border_radius=stroke.get("radius", "1px"),
                    opacity=stroke.get("opacity", "1"),
                )
            )
        speck = work.get("speck")
        if speck:
            layers.append(rx.el.div(class_name=f"specks specks-{speck}"))
    return rx.el.div(*layers, class_name="work-face")
