# Maren Solis — Night Ground

A portfolio for **Maren Solis**, a fictional abstract painter working in oil and cold wax on a navy ground in a warehouse studio in Alcântara, Lisbon. The site is a [Reflex](https://reflex.dev) app: pages, gallery, and the commission form are Python.

The whole site sits on one painting. `assets/background.jpg` is that canvas — orange, cobalt, viridian, crimson, and chrome yellow on a dark navy ground — applied once on the page root with `background_size="cover"`, `background_position="center"`, and `background_attachment="fixed"`. It stays put while the page scrolls. Sections are translucent dark panels so the painting shows through.

## Python

**This project targets Python 3.14.4.**

[Reflex 0.10.0](https://pypi.org/project/reflex/0.10.0/) (pinned in `requirements.txt`) requires Python `>=3.11, <4`. Python 3.14 has been supported since Reflex 0.8.15. It was installed and checked here with CPython **3.14.4**. Any later 3.14 patch also satisfies Reflex. `.python-version` records `3.14.4`.

## Run it on Ubuntu

Install Python 3.14.4 if `python3.14` is not already on your `PATH`. [uv](https://docs.astral.sh/uv/) can fetch that exact interpreter:

```bash
sudo apt-get update
sudo apt-get install -y curl ca-certificates
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv python install 3.14.4
python3.14 --version
```

`python3.14 --version` should print `Python 3.14.4`.

Then clone and run:

```bash
git clone https://github.com/Gooberin95/Plato1.git
cd Plato1
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
# The app is already initialized (rxconfig.py and the solis package).
# Only run init if that file is missing — do not run it over this repo.
if [ ! -f rxconfig.py ]; then reflex init; fi
reflex run
```

Open **[http://localhost:3000](http://localhost:3000)**.

The first `reflex run` downloads the frontend toolchain and needs a network connection. It can take a few minutes. Leave that terminal open. Reflex also listens on port 8000 for the backend; the site itself is port 3000. If 3000 is taken, Reflex prints the next free port — open the URL it prints.

Stop the server with Ctrl+C.

## Deploy

The GitHub Actions workflow builds this site on every push to `main`. Deploying to Azure App Service is described in [DEPLOY.md](DEPLOY.md). Those deploy jobs stay skipped until an Azure subscription exists and the variable `AZURE_DEPLOY_ENABLED` is set to `true`.

## What is in the studio

- **Studio** (`/`) — hero, a pigment index you can switch, and three paintings.
- **Works** (`/works`) — gallery filtered by color family. Open a canvas for its wall label.
- **Life** (`/life`) — biography and materials.
- **Shows** (`/shows`) — exhibition timeline, upcoming or archive.
- **Commission** (`/commission`) — a request form. Name, email, scale, palette, and a short note are checked in Reflex state. A valid note is held in the browser session and read back on the page. **It does not send email.**

The painter, the galleries, and `studio@marensolis.studio` are fictional.

Navigation is a fixed index along the left edge on a wide screen, and a menu button on a narrow one. Type is Fraunces and Outfit, both SIL Open Font License, shipped in `assets/fonts/` (see the license files there).

## Layout

```
rxconfig.py
requirements.txt
.python-version
assets/background.jpg
assets/styles.css
solis/solis.py
solis/state.py
solis/data.py
solis/components/
solis/pages/
```
