[//]: # "GeoSight is UNICEF's geospatial web-based business intelligence platform."
[//]: # 
[//]: # "Contact : geosight-no-reply@unicef.org"
[//]: # 
[//]: # ".. note:: This program is free software; you can redistribute it and/or modify"
[//]: # "    it under the terms of the GNU Affero General Public License as published by"
[//]: # "    the Free Software Foundation; either version 3 of the License, or"
[//]: # "    (at your option) any later version."
[//]: # 
[//]: # "__author__ = 'irwan@kartoza.com'"
[//]: # "__date__ = '13/06/2023'"
[//]: # "__copyright__ = ('Copyright 2023, Unicef')"
[//]: # "__copyright__ = ('Copyright 2023, Unicef')"

# GeoSight



GeoSight is a UNICEF’s open-source geospatial web-based data visualization/analysis platform that aims to make geospatial data easily accessible and sharable in support of risk informed programming. This data is displayed utilizing administrative reference datasets from [GeoRepo](https://github.com/unicef-drp/GeoRepo-OS).

## Key Concepts

A **project** (dashboard) is the most important feature of GeoSight. Projects combine different elements (Reference datasets, indicators, and context layers) and enable data visualization/analysis for all end users. 

**Context layers** are geospatial layers used to contextualise the information presented in a project.

**Indicators layers** derive from spreadsheets or other intelligence assets harvested by the platform.

**Widgets** are visual components such as charts generated by performing data analysis on country/regional levels and the indicator data.

## :ballot_box_with_check: Project activity

[![Tests](https://github.com/unicef-drp/GeoSight-OS/workflows/Tests/badge.svg)](https://github.com/unicef-drp/GeoSight-OS/actions/workflows/tests.yaml)
[![Flake8](https://github.com/unicef-drp/GeoSight-OS/workflows/Flake8/badge.svg)](https://github.com/unicef-drp/GeoSight-OS/actions/workflows/flake8.yml)
[![Documentation](https://github.com/unicef-drp/GeoSight-OS/workflows/Documentation/badge.svg)](https://unicef-drp.github.io/GeoSight/)

### Production

```
git clone https://github.com/unicef-drp/GeoSight-OS
cd GeoSight-OS/deployment
docker-compose up -d
```

The web will be available at `http://127.0.0.1/`

To stop containers:

```
docker-compose kill
```

To stop and delete containers:

```
docker-compose down
```

### Development

```
git clone https://github.com/unicef-drp/GeoSight-OS
cd GeoSight-OS/deployment
cp .template.env .env
docker-compose.override.template.yml docker-compose.override.yml
```

After that, do
- open new terminal
- on folder root of project, do
```
make frontend-dev
```
Wait until it is done
when there is sentence "webpack xxx compiled successfully in xxx ms".<br>
After that, don't close the terminal.
If it is accidentally closed, do `make frontend-dev` again

Next step:
- Open new terminal
- Do commands below
```
make up
make dev
```

Wait until it is on.

The web can be accessed using `http://localhost:2000/`

If the web is taking long time to load, restart geosight_dev container.<br>
The sequence should be `make frontend-dev`, after that run or restart geosight_dev. 

# Setup GeoRepo configuration

There are GeoRepo configurations that are needed for geosight.<br>
Go to '/django-admin/core/sitepreferences/1/change/', use admin username/password on .env file (ADMIN_USERNAME and ADMIN_PASSWORD).<br>
Change Georepo url and fill Georepo api key. For Georepo api key, you can ask georepo for the key.

# Building the documentation as a PDF

## Install Dependencies

You need to install these packages:

```bash
pip install mkdocs-with-pdf
pip install mkdocs-material
pip install mdx_gh_links
pip install mkdocs-pdf-export-plugin
```

## Building in a terminal

> Note that whenever you add new sections to nav in the mkdocs.yml
> (used for building the web version), you should apply those same
> edits to mkdocs-pdf.yml if you want those new sections to appear
> in the pdf too.

```bash
cd  docs
./build-docs-pdf.sh
xdg-open TheGeosightHandbook.pdf
```

## Building in VSCode

If you are in VSCode, you can also just run the 'Compile PDF' task. The
generated PDF will be placed in docs/pdfs/.
