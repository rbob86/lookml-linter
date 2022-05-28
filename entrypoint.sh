#!/usr/bin/env bash

ALPINE_VERSION=$1

docker build -t docker-action \
             -f ./docker-action/Dockerfile \
             --build-arg alpine_version="$ALPINE_VERSION" \
             ./docker-action

PROJECT_NAME="$(basename ${GITHUB_REPOSITORY})"
WORKSPACE="${RUNNER_WORKSPACE}/${PROJECT_NAME}"

docker run --workdir=$GITHUB_WORKSPACE \
           -v $WORKSPACE:$GITHUB_WORKSPACE \
           docker-action "$@"


# python -m linter.main config.example.yaml
