import subprocess, time

def getNodeStats(ip):
    subprocess.call(["./jcli", "rest", "v0", "node", "stats", "get", "-h", ip])

def getUTXO(ip):
    subprocess.call(["./jcli", "rest", "v0", "utxo", "get", "-h", ip])

def getTip(ip):
    subprocess.call(["./jcli", "rest", "v0", "tip", "get", "-h", ip])

def getIP():
    f = open("nodeIP.txt", "r")
    if f:
        print "Using IP from nodeIP.txt"
        ip = f.readline().strip() 
        ip = "http://" + ip + "/api"
        print ip
    else:
        ip = raw_input("nodeIP.txt not found. Enter ip of the node.")
    return ip

def performChoice(choice):
    if choice == "1":
        getNodeStats(ip)
    elif choice == "2":
        getUTXO(ip)
    elif choice == "3":
        getTip(ip)



# if __name__ == "__main__":
print "Welcome to the node stress tester."
ip = getIP()

choice = raw_input("Choose:\n(1) Node Stats\n(2) Whole UTXO\n(3) Block Tip\n")
delay = input("Enter the delay you wish to use in seconds(can be fractional): ")

while 1:
    performChoice(choice)
    time.sleep(delay)
