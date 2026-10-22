import reflex as rx
from reflex.plugins import SitemapPlugin

config = rx.Config(
    app_name="solis",
    plugins=[SitemapPlugin()],
    # A fresh clone has no frontend lockfile. Frozen mode would block `reflex run`.
    frozen_lockfile=False,
    default_color_mode="dark",
    # Keep the designed pages free of the production "Built with Reflex" badge.
    show_built_with_reflex=False,
)
