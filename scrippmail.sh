#!/bin/sh

git filter-branch --env-filter '
OLD_EMAIL="pi@raspberrypi.(none)"
OLD_EMAIL2=""
OLD_EMAIL3=""
OLD_NAME=""
OLD_NAME2=""
OLD_NAME3=""

CORRECT_NAME="IAL-bot"
CORRECT_EMAIL="ialcentral0000@gmail.com"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
