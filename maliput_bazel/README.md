# Maliput CC Examples <!-- omit from toc -->

This is an exemplar bzlmod package that depends on the bzlmodded maliput family.

- [Setup](#setup)
- [Usage](#usage)
  - [Examples](#examples)
  - [Tools](#tools)

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
(docker) zen@bazel-zen:/workspaces/maliput_examples$

# Switch to the project
$ cd maliput_cc_examples
```

4. Build

```bash
$ bazel build //...
```

## Usage

### Examples

```sh
# Extract z-values from the road surface
bazel run :superelevation
```

### Tools

Use https://odrviewer.io/ to view xodr files.

```
$ bazel run @maliput_malidrive//:xodr_query ${PWD}/resources/onramp.xodr FindLargestGap

Largest Gap between Geometries in the XODR: 0.000500386
Located at RoadHaderId: 91, Geometry Indexes: [5,6]

$ bazel run @maliput_malidrive//:xodr_query -- ${PWD}/resources/GapInElevationNonDrivableRoad.xodr FindLargestElevationGap

Largest Gap between elevation functions in the XODR: 2
Located at RoadHaderId: 1, elevation indexes: [0,1]
```
