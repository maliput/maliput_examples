# Maliput Cargo Examples <!-- omit from toc -->

This is an example cargo package that depends on the cargo-released maliput family.

- [Setup](#setup)
- [Usage](#usage)
  - [Examples](#examples)
    - [RoadGeometry](#roadgeometry)
    - [TrafficLights](#trafficlights)

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

#### RoadGeometry

```sh
cargo run --bin road_geometry
```

Use _--help_ for getting the help message.

```sh
cargo run --bin road_geometry -- --help
```

```sh
Load an OpenDRIVE file and exercise the RoadGeometry API via ToRoadPosition query

Usage: road_geometry [OPTIONS]

Options:
  -m, --xodr-map-name <XODR_MAP_NAME>  Name of the OpenDRIVE file to load [default: TShapeRoad]
  -x, --i-pos-x <I_POS_X>              Inertial position x-coordinate [default: -0.5]
  -y, --i-pos-y <I_POS_Y>              Inertial position y-coordinate [default: 0]
  -z, --i-pos-z <I_POS_Z>              Inertial position z-coordinate [default: 1]
  -h, --help                           Print help
  -V, --version                        Print version
```

Use _--xodr-map-name_ (or _-m_) to indicate the OpenDRIVE file to load.
You can also can indicate the Inertial Position that will be used for the ToRoadPosition query.
```sh
cargo run --bin road_geometry -- --xodr-map-name=SpiralRoad -x 1 -y 1 -z 1
```

#### TrafficLights

```sh
cargo run --bin traffic_lights
```
