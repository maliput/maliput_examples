# Maliput Python Examples

## Setup

1. [Install VSCode](https://code.visualstudio.com/docs/setup/linux)
2. Fetch the code

```bash
$ git clone git@github.com:stonier/maliput_examples.git
```

3. Launch the project in the python devcontainer:

```
$ cd maliput_examples
$ code .

# Reopen in Container or CTRL-SHIFT-P
#   Select the python devcontainer from the subsequent drop-down

# Open up a terminal (if it hasn't already)
(docker) zen@python-zen:/workspaces/maliput_examples$

# Switch to the project
$ cd maliput_py_examples
```

4. Install dependencies

```bash
$ poetry install

Installing dependencies from lock file

Package operations: 2 installs, 0 updates, 0 removals

  • Installing maliput (0.1.6)
  • Installing maliput-malidrive (0.1.4)
```

## Run Examples

```bash
$ poetry shell
$ maliput-<TAB><TAB>
  maliput-inertial-to-road
  ...
```

## Visualizing XODRs

Open them in https://odrviewer.io/.
