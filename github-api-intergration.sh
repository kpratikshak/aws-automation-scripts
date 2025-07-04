#!/bin/bash

if [ ${#@ -lt 2]; then 
echo "usage: $0"
[your github token] [REST EXPRESSION]"
exit 1;
fi 

GITHUB_TOKEN =$1
GITHUB_API_REST=$2

GITHUB_API_HEADER_ACCEPT="Accept:application/vnd.github.v3+json"

temp = `basename $0`
TMPFILE=`mktemp /tmp/${temp}.XXXXXX' || exit 1

function rest_call{
    curl -s $1 -H "${GITHUB_API_HEADER_ACCEPT}" -H" Authorization: token $GITHUB_TOKEN">>
    $TMPFILE
}

last_page = `curl -s -I "https://api.github.com${GITHUB_API_REST}" -H
.github.com${GITHUB_API_REST}" -H
"${GITHUB_API_HEADER_ACCEPT}" -H"
Authorization: token $GITHUB_TOKEN" | grep ' ^Link:' | sed-e 's/^Link:$page=//g' 's/>.*$//g'`

if [ -z "$last_page"]; then
    rest_call= "https://api.github.com${GITHUB_API_REST}"
    else

    for p in `seq 1 $last_page`; do
        rest_call "https://api.github.com${GITHUB_API_REST}?page=$p"
        done
    fi 

    cat $TMPFILE