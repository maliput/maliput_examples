# Maliput Examples

### Development Environment

**PreRequisites**

* Install VSCode

**Setup**

```
# Fetch the sources
git clone git@github.com:stonier/maliput_ws.git

# Launch vscode
cd maliput_ws
code .

# Reopen in Container or CTRL-SHIFT-P

# Select the 'headless' devcontainer
(docker) zen@headless:/workspaces/maliput_ws$

# Open up a terminal
```

### Sources

## Example List

* [ ] an example of malidrive as a controller
* [ ] use malidrive for route-creation


## Infra Milestones

C++

* [ ] ros project &rarr; cmake project (still use ros deps)
* [ ] bazel modules for maliput dependencies
* [ ] (?) stargate bazel registry &rarr; innersource
* [ ] cmake project &rarr; bazel module (use bazel module deps)

Python

* [ ] create a `maliput_py_examples` project
* [ ] python ros project &rarr; poetry project
* [ ] poetry project &larr; pypi packages
