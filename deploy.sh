#!/usr/bin/env bash
rsync -a --delete --exclude 'data' --exclude 'venv' . io.lan:/home/kyle/crib-detect
