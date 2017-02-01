import os, time
d = {}
try:
    while True:
    	  info = os.popen("ps -eo pcpu,pmem,pid,user,args | grep \"\\sdwblair\\s\" | grep \"phant\"").read()
        data = info.strip().split()
        d['cpu'] = data[0]
        d['mem'] = data[1]
        d['pid'] = data[2]
        print(d)
        time.sleep(10)
except KeyboardInterrupt:
    print("exiting...")
