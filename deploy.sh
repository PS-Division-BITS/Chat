#!/bin/sh

git fetch upstream
git rebase upstream/master
git push upstream master