# Maliput CC Examples <!-- omit from toc -->

This is an exemplar bzlmod package that depends on the bzlmodded maliput family.

- [Setup](#setup)
- [Usage](#usage)
  - [Examples](#examples)
  - [Tools](#tools)
- [Errata](#errata)

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

```
bazel run :superelevation
```

### Tools

```
bazel query @maliput_malidirve/...
```


## Errata

This is using a temporary fork of the bazel central registry until
`tinyxml2`, `yaml-cpp`, `maliput` and `maliput_malidrive` are fully
registered there.

* https://github.com/maliput/maliput/issues/576
* https://github.com/stonier/bazel-central-registry/tree/maliput_releases
