# Maliput Python Examples

## Setup

* [Install VSCode](https://code.visualstudio.com/docs/setup/linux)
* Launch the project in a devcontainer

```
# Fetch sources
git clone git@github.com:stonier/maliput_ws.git

# Launch VSCode
cd maliput_ws
code .

# Reopen in Container or CTRL-SHIFT-P

# Open up a terminal
(docker) zen@headless:/workspaces/maliput_ws$
```

* Install wheels (this step will be removed later once it's available on pypi)

```
cd maliput_py_examples
pip install --user maliput-0.1.5-cp38-cp38-linux_x86_64.whl
pip install --user maliput_malidrive-0.1.4-cp38-cp38-linux_x86_64.whl
```

## Usage

```bash
python3 test_maliput.py
```