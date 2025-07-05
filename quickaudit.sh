
#!/bin/bash

get_user_names(){
    nopass=`passwd -${1}a | grep -o "^.* NP"`

    for i in ${nopass/ /_}
    {
        nopass="${nopassnames:-} $i"
    }
}

if [["$OSTYPE"== *linux-gnu*]]; then
    get_user_names S
elif [["$OSTYPE" ==*sunos*]]; then
    get_user_names s
fi 

if [ -z "$nopassnames"]
    then 
    echo "
Goof -All user accounts have a password"
else 
    echo "Error:The users listed below have no password set:""
    \"
    ${nopassnames//_NP/}" 1>&2 
    exit 1
fi