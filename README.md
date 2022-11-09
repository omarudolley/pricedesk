# MarketRateLiberia

MarketRateLiberia aims to provide accurate and up-to-date information about the prices of basis
commodities in Liberia.

GitHub Actions are used to automatically download latest data and rebuild the site.

The generated site is hosted on GitHub Pages at
[https://omarudolley.github.io/pricedesk/](https://omarudolley.github.io/pricedesk/)

## Project setup

### Install prerequisites

Install `poetry` to manage Python dependencies:
[https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

Install `pre-commit` to do automatic code analysis and formatting before committing changes:
[https://pre-commit.com/#install](https://pre-commit.com/#install)

### Get/update data from Google drive

After cloning the repository, you will need to download the latest data from Google Drive.

```bash
poetry install
poetry run download
```

### Install front-end dependencies

```bash
cd frontend/
pnpm install
```

### Compiles and hot-reloads for development

```bash
pnpm run dev
```

### Compiles and minifies for production

```bash
pnpm run build
```

# How to contribute?

If you have a suggestion about something that could be improved or wish to help with the technical
development, please take a look here: https://github.com/omarudolley/pricedesk/issues

All suggestions and ideas are welcome. Please feel free to fork the project, raise new issues, or
make pull requests.

# License and data information

This repository is maintained as an open source project and released under an
[MIT license](LICENSE).
