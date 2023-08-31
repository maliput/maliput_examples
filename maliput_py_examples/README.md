# Maliput Python Examples

## Setup

* [Install VSCode](https://code.visualstudio.com/docs/setup/linux)
* Launch the project in the devcontainer:

```bash
# Fetch sources
git clone git@github.com:stonier/maliput_ws.git

# Launch VSCode
cd maliput_ws
code .

# Reopen in Container or CTRL-SHIFT-P

# Open up a terminal
(docker) zen@headless:/workspaces/maliput_examples$
```

* Install dependencies

```bash
cd maliput_py_examples
# Install dependencies
poetry install

# Install wheels - this will be be covered by 'poetry install' once
# available on pypi.
poetry shell
pip install wheels/maliput-0.1.5-cp38-cp38-linux_x86_64.whl
pip install wheels/maliput_malidrive-0.1.4-cp38-cp38-linux_x86_64.whl
```

## Run Examples

```bash
poetry shell
maliput-<TAB><TAB>
  maliput-inertial-to-road
  ...
```