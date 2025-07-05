def start_v():
    network_addr = input("Enter the network address:")
    prefix = input(" prefix of network: "))
    num_of_sub = int(input("Enter the number of subnets: "))
    return [network_addr, prefix, num_of_sub,max_value_dev]

start_list = start_v()
network_addr = start_list[0]
prefix = int(start_list[1]) 
num_of_sub = start_list[2]
max_value_dev = start_list[3]
    
    def enough_ip():
        needed_ip = num_of_sub *max_value_dev
        haved_ip = 2** (32 - prefix) - 2
        if haved_ip >= needed_ip:
            return haved_ip
        else:
            start_v()
            
        enough_ip()
        
        def rules_ip():
            ip_by_octocat=[]
            
            mask_bin = int(prefix) * "1" + (32 - int(prefix)) * "0"
            mask_bin_list =[]
            for i in range(0, 32, 8):
                mask_bin_list.append(mask_bin[i:i+8])
            print("Enough IPs available")
            return True
        if needed_ip > max_value_dev: