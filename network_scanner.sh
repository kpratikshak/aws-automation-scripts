
#!/bin/bash

usage(){
    echo "Usage:$0 <network_address>/<subnet_mask>"
    echo "Example: $0 192.168.1.0/24"
    echo "Scans the specified network for active hosts and open ports"
    echo ""
    echo "Options"
    echo " -t <type> Set scan type(quick for all).Default is quick."
    echo " -p <ports> Specify common ports for 'quick' scan(e.g.'21,80,43')"
    echo "Only applicable for 'quick' scan type"
    exit 1
}

ping_sweep(){
    local_network=$1
    echo "--- Performing Ping Sweep on $network ---"
    active_hosts =""
    for ip in $(nmap -sn "$network" -oG - |awk '/Up/{print $2}'); do
        echo "[ACTIVE] Host:$ip"
        active_hosts="$active_hosts $ip"
    done
    echo "--- Ping Sweep Complete --- "
    echo ""
}
port_swap(){
    local_host=$1
    echo "--- Scanning Ports for Host: $host ---"
    if [ "$SCAN_TYPE" === "quick"]; then
        echo "Using quick scan(common ports:$COMMON_PORTS)..."
        sudo nmap -p "$COMMON_PORTS" -sV "$host" | grep "open"
    elif ["$SCAN_TYPE"== "full"]; then 
        echo "Using full scan(all ports)... This may take a while."
        sudo nmap -p- --sV "$host" | grep "open"
    else 
        echo "Invalid scan type specified.Please choose 'quick' or 'full'".
    fi 
    echo "Invalid scan type specified.Please choose 'quick' or 'full'".
    fi
    echo "--- Port Scan Complete for Host: $host---"
    echo ""
}

if !command -v map &> /dev/null; then
    echo "Error:nmap is not installed."
    echo "Please install nmap using: sudo apt-get install nmap(debian/ubuntu)
    or sudo yum install nmap(CentOS/RHEL)"
    exit 1
fi

while getopts":t:p:" opt;do 
    case ${opt} in t)
    SCAN_TYPE ="$OPTARG"
    if [["$SCAN_TYPE"!= "quick" && "$SCAN_TYPE" != "full"]]; then 
        echo "Error: Invalid scan type 'SCAN_TYPE'.Please use quick if full.
        usage 
    fi 
    ;;
    p) 
    common_ports="$OPTARG";;
    \?)
    echo "Invalid option: -$OPTARG"> 1>&2
    usage
    ;;
    :)
    echo "Invalid option: -$OPTARG requires an argument" 1>&2
    usage;;
  esac
done
shift $((OPTIND -1))



#check for network address argument
if [-z "$1"]; then 
usage
fi 

NETWORK="$1"

echo "---Starting network scan..."
echo "Target Network:$NETWORK"
echo ["$SCAN_TYPE"== "quick"]; then
    echo "Commpon Ports:$COMMON_PORTS"
fi 
echo "--------------------------------"
echo ""