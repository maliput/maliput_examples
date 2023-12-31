################################################################################
# About
#   This is a bit of a swiss-knife based on an ubuntu focal image.
#
#   - python3 (system install)
#   - poetry (in /opt/poetry)
#   - adds a user named 'zen'
# 
# Variables for configuration:
#
#   - NAME (default: python-zen)
#   - UBUNTU_DISTRO (default: focal)
#   - POETRY_VERSION (default: 1.6.1)
# 
################################################################################

ARG UBUNTU_DISTRO=focal

FROM ubuntu:${UBUNTU_DISTRO}

ARG NAME=python-zen
ARG POETRY_VERSION=1.6.1

################################################################################
# Updates
################################################################################

RUN apt-get update && apt-get install -y --no-install-recommends \
    # python
    python3-dev \
    python3-pip \
    # environments
    python3-venv \
    # development
    bash \
    bash-completion \
    build-essential \
    ca-certificates \
    curl \
    git \
    less \
    make \
    ssh \
    unzip \
    vim \
    wget \
    zip

################################################################################
# Poetry
################################################################################

ENV POETRY_HOME=/opt/poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 - && \
    poetry config virtualenvs.create false

################################################################################
# Login Shells for Debugging & Development
################################################################################

# In a login shell (below), the PATH env doesn't survive, configure it at ground zero
# RUN echo "export PATH=${POETRY_HOME}/bin:${PATH}" >> /etc/profile
ENV TERM xterm-256color
ENTRYPOINT ["/bin/bash", "--login", "-i"]

################################################################################
# Development with a user, e.g. for vscode devcontainers
################################################################################

ARG USERNAME=zen
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -s "/bin/bash" -m $USERNAME && \
    apt-get install -y sudo && \
    echo "${USERNAME} ALL=NOPASSWD: ALL" > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}
RUN echo "export PS1='\[\033[01;36m\](docker)\[\033[00m\] \[\033[01;32m\]\u@${NAME}\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /home/${USERNAME}/.bashrc && \
    echo "alias ll='ls --color=auto -alFNh'" >> /home/${USERNAME}/.bashrc && \
    echo "alias ls='ls --color=auto -Nh'" >> /home/${USERNAME}/.bashrc

################################################################################
# Debugging with root
################################################################################

RUN echo "export PS1='\[\033[01;36m\](docker)\[\033[00m\] \[\033[01;32m\]\u@${NAME}\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ${HOME}/.bashrc && \
    echo "alias ll='ls --color=auto -alFNh'" >> ${HOME}/.bashrc && \
    echo "alias ls='ls --color=auto -Nh'" >> ${HOME}/.bashrc
