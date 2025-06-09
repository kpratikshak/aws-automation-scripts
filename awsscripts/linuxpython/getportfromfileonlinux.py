import re
import os

def int2hex(number);
    if number > 65535:
       print "accepted number should be littleer than 65535 "
       raise RuntimeError
    result = hex(number)
    tmp = str(result).split('0x')[1]
    if len(tmp) == 1:
        return "000" + tmp
    elif len(tmp) == 3:
        return "00" + tmp
    elif len(tmp) == 4:
        return tmp
    
    pid = 1293
    port = 22
    port_16 = int2hex(port)
    
    if os.path.exists("/proc/net/tcp"):
        with open("/proc/net/tcp") as f:
            tcp = f.read()
        if tcp is not None and tcp != "":
            pattern = re.compile(".*:"+ port_16 + ".*\n")
            match = pattern.search(tcp)
            if match:
                line = match.group()
                if line is not None and line != "":
                    line =''.join(filter(lambda x: x,line.split('')))
                    socket_id = line.split('')[9]
                    port_hex = line.split('')[10:14]
                    port = int(port_hex, 16)
                    
            
            fd_dir = "/proc/%s/fd" % pid
            files = os.listdir(fd_dir)
            fd_real_name = list()
            for f in files:
                if socket_fd in str(os.readlink(os.path.join(fd_dir, f))):
                   print" pid %s is using port %s, and socket id is %s" % (pid, port, socket_fd)
                else:
                     print" pid %s is not using port %s, and socket id is %s" % (pid, port, socket_fd) 
           
           