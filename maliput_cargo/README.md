# Maliput Cargo Examples <!-- omit from toc -->

This is an example cargo package that depends on the cargo-released maliput family.

- [Setup](#setup)
- [Usage](#usage)
  - [Examples](#examples)

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
#   Select the rust devcontainer from the subsequent drop-down

# Open up a terminal (if it hasn't already)
(docker) zen@rust-zen:/workspaces/maliput_examples$

# Switch to the project
$ cd maliput_cargo
```

4. Build

```bash
$ cargo build
```

## Usage

### Examples

```sh
cargo run --bin road_geometry
```
