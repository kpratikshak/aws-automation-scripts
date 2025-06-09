 import os 
 
 def list_top_cpu_consuming_processes():
    top_five_cpu_processes = os.popen("ps aux | sort -nrk 3,3 | head -n 6").read()
    
    print("###############################")
    print("Top 5 CPU consuming processes")
    print(top_five_cpu_processes)
    
    def list_top_cpu_consuming_processes():
    top_five_memory_processes = os.popen("ps -eo pmem, pid,user,args| sort -k 1 -r| head -n 6").read()
    
    print("###############################")
    print("Top 5 CPU consuming processes")
    print(top_five_cpu_processes)
    
    if os.system("command -v iotop >/dev/null 2>&1") == 0:
        print("iotop command is present")
    else:
        print("iotop is not present.Installing")
    if os.path.isfile("/etc/lsb-release"):
        os.system("sudo apt-get update ")
        os.system("sudo apt-get install iotop")
    else:
        print("Unsupported operating system")
        exit(1)
        
    def list_top_cpu_consuming_process():
        top_five_io_processes = os.popen("iotop -b -n 1 | head -n 6").read()
        
        print("###############################")
        print("Top 5 I/O consuming processes:")
        print("iftop command is present")
        
    else:
        print("iftop is not present.Installing")
    if os.path.isfile("/etc/centos-release"):
        #Centos
        os.system("sudo yum install -y iftop")
    elif os.path.isfile("/etc/lsb-release"):
        os.system("sudo apt-get update ")
        os.system("sudo apt-get install-yiftop")
    else:
        print("Unsupported operating system")
        exit(1)
        
    def list_top_network_consuming_processes():
        top_five_network_processes = os.popen("iftop -i eth0 -b -n 1 | head -n 6").read()
        
        print("###############################")
        print("Top 5 Network consuming processes:")
        print(top_five_network_processes)
        
    def main():
        list_top_cpu_consuming_processes()
        list_top_memory_consuming_processes()
        list_top_io_consuming_processes()
        list_top_network_consuming_processes()
        
        if __name__ == "__main__":
            main()