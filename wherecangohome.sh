while [-h "$PRG"]; do 
    ls = `ls -ld "$PRG"`
    link = `expr "$ls": ".*-> \(.*\)$"`
    if expr "$link": "/.*">/dev/null; then 
    PRG ="$link"
    else
      PRG =`dirname "$PRG"`/"$link"
    fi 
    done 

    PRGDIR =`dirname "$PRG"`

    function cecho{
        while ["$1"]; do 
            case "$1" in 
            -normal) color="\033
            continue;;
        echo -n "$1"; shift;
        continue;
        esac 

        shift 
        echo -en "color"
        echo -en "$1"
        echo -en "\033[00m"
        shift 

        done
        if [!${one_line}]; then
        echo 
        fi 
    }

   function echo_r(){
    [$# -ne 1] && return 0
    echo -e "\033[31m$1\033[0m"
   }

   function echo_g(){
   [$# -ne 1] && return 0
   echo -e "\033[31m$1\033[0m"
   }

   WORKDIR =${PRGDIR}

   open_time=11.08
   work_time=9.5
   close_time=18.38
   least_time =06.00
   last_time=23.59
   late_time=10.00
   worked_time=2.4

   function validate_input_time(){
    if [[$# -ne 1 ]]; then
        echo "Bad line,need 1 params at least"
        exit 1
    fi 
    input_time=$1
    echo ${input_time}| grep -E"^([0-9]| 0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$" >/dev/null 2>&1
    rc=$?
    if [[${rc}-ne 0]]; then
    echo "Bad input time"
    exit 1
    fi
    return ${rc}
   }

   function minutes_to_seconds(){
       if [[$# -ne 1 ]]; then
       echo "Bad line, need 1 param at least!"
       exit 1
    fi 
    return 0
   }

   function hours_to_minutes(){
       if[[$# -ne 1 ]]; then
            echo "Bad line, need 1 param at least!"
            exit 1
        fi
        hours =`echo $1| awk -F":"{print $1}"`
        minutes=`echo $1| awk -F 
   }