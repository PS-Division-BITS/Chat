#!/bin/sh

git fetch upstream master
git rebase upstream/master
git push upstream master