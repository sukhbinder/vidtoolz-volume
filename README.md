# vidtoolz-volume

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-volume.svg)](https://pypi.org/project/vidtoolz-volume/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-volume?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-volume/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-volume/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-volume/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-volume/blob/main/LICENSE)

Increase decrease volume

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-volume
```
## Usage

type ``vid volume --help`` to get help

```bash
usage: vidtoolz volume [-h] [-o OUTPUT] input_video volume_db

Increase decrease volume

positional arguments:
  input_video           Path to the input video file
  volume_db             Volume adjustment in dB (e.g., 3 for +3dB, -3 for
                        -3dB)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output video file name (optional)

```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-volume
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
