# Maliput Examples

This repo exemplifies usage of [maliput](https://github.com/orgs/maliput/repositories)
(specifically [maliput](https://github.com/maliput/maliput),
[maliput_malidrive](https://github.com/maliput/maliput_malidrive)
and [maliput_py](https://github.com/maliput/maliput_py)) as a dependency for
integration into a simulator (c++ and python). It also includes code demonstrating
how to use the maliput api for
specific purposes.

## Requirements

The requirements are very light:

* Python - Ubuntu 20.04, python3, pip3
* C++ - Bazel 6.0 or greater

The repo uses devcontainers to simplify the development environment setup,
but you could work directly on an Ubuntu system just as easily - parse the 
[Dockerfile](./.devcontainer/Dockerfile) to discover the build machinery that
needs to be installed and configured.

## Usage

See the individual projects in subdirectories for detailed
setup and usage instructions.

* [maliput_py_examples](./maliput_py_examples/README.md)
* [maliput_cpp_examples](./maliput_cpp_examples/README.md)

## Backlog

Python

* [x] create a `maliput_py_examples` project
* [x] manually install wheels and prove it works with a demo
* [~] fetch wheels from pypi and use in a poetry project

C++

* [x] `yaml-cpp` bazel module
* [~] upstream bzlmod PR to yaml-cpp
* [x] `maliput` bazel module
* [ ] eliminate dependency on `unsupported/Eigen`
* [ ] `maliput_drake` decomposition
* [ ] `maliput_malidrive` bazel module
* [ ] eliminate dependency on `fmt`
* [ ] upstream all bzlmod related PRs to maliput family
* [ ] upstream module PRs bazel-central-registry

Examples

* [x] python - superelevation
* [ ] ...
