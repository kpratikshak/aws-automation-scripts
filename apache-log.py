import re 
import csv 
import argparse 
from collections import Counter

IP_REGEX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

parser = argparse.ArgumentParser(description="Reading the log file")
parser.add_argument("--l","--logfile",
                    help="Please enter the logfile to parse",
                    type="logfile",
                    type=argparse.FileType('r'),
                    required=True)

def extract_ips(logfile):
    """Extracts all IP addresses from the given logfile""
    required=True)
    
    def extract_ips(logfile):
    """Extracts all IP addresses from the given logfile""
    required=True)
    
    def extract_ips(logfile):
    """Extracts all IP addresses from the given logfile""
    required=True)
    try:
        with open(logfile,"r") as f:
            log = f.read()
    except Exception as e:
        print(f"Error: {e}")
        return  []
        
    return re.findall(IP_REGEX,log)
    
    def count_ips(ip_list):
        """
        return counter(ip_list)
    
    def write_csv(counter):
        with open("ipnewcount.csv","w") as f:
            writer = csv.Dictwriter(f,fieldness=["IP_Addresses","Count"])
            writer.writeheader()
            for item, count in counter.items():
                writer.writerow({"IP_Addresses":item,"Count":count})
    except Exception as e:
        print(f"Error: {e}")
        
    def main():
        args = parser.parse_args()
        ip_list = extract_ips(args.logfile)
        counter = count_ips(ip_list)
        write_csv(counter)
        
        if __name__ == "_main_":
            main()
                    
                    
    list_top_memory_consuming_processes(){
        top_five_memory_processes(){
        
        if command -v iotop >/dev/null 2>&1; then 
            echo "iotop command is present"
        else 
        echo "iotio command is not present.Installing.."
        if [-f/etc/centos-release]; then 
            sudo yum install -y epel-release  
            sudo yum install -y iotop
        elif [ -f /etc/lsb-release ]; then
        else  [ -f /etc/lsb-release ]; then
        sudo apt-get update
        sudo apt-get install -y iotop 
    else 
            echo "Unsupported operating system"
            exit 1
    fi 
  fi 
  
  list_top_io_consuming_processes(){
      top_five_io_processes=$(sudo iotop -o -b -n 5)
      
      echo "####################"
      echo "Top 5 IO consuming processes"
      echo "####################"
      echo "$top_five_io_processes"
  }
  
  if command -v iftop >/dev/null 2>&1; then 
      echo "iftop command is present"
  else 
      echo "iftop command is not present.Installing.."
      if [-f/etc/centos-release]; then 
          sudo yum install -y epel-release  
          sudo yum install -y iftop
      elif [ -f /etc/lsb-release ]; then
      else  [ -f /etc/lsb-release ]; then
          sudo apt-get update
          sudo apt-get install -y iftop 
      else 
          echo "Unsupported operating system"
          exit 1
      fi 
  fi
  
  list_top_network_consuming_processes(){
      top_five_network_processes=$(sudo iftop -P -n -t -s 5) 
      echo "####################"
      echo "Top 5 Network consuming processes"
      echo "####################"
      echo "$top_five_network_processes"
  }
  
  main(){
      list_top_cpu_consuming_processes
      list_top_memory_consuming_processes
      list_top_io_consuming_processes
      list_top_network_consuming_processes
  }
  
  main()
