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
* maliput_cc_examples - coming soon

## Backlog

Python

* [ ] create a `maliput_py_examples` project
* [ ] manually install wheels and prove it works with a demo
* [ ] fetch wheels from pypi and use in a poetry project

C++

* [ ] ros project &rarr; cmake project (still use ros deps)
* [ ] bazel modules for maliput dependencies
* [ ] (?) stargate bazel registry &rarr; innersource
* [ ] cmake project &rarr; bazel module (use bazel module deps)

Examples

* [ ] get superelevation
