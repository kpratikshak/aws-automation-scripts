#!/usr/bin/env bash
PIDFILE =""
# about "kill -0 <pid>", see man 2 kill

if test -s ${PIDFILE}; then
    if !kill -0 "$(cat ${PIDFILE})">/dev/null 2 >&1; then 
         echo xxx
    fi
    else 
        echo "PID File could not be found!"
        exit
    fi