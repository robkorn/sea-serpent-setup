import subprocess, time, random, argparse

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
    elif choice == "4":
        performChoice(str(random.randint(1,4)))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="Either 'a' for automatic or 'm' for manual.")
    args = parser.parse_args()
    print args.mode

    if args.mode == 'a':
        delay = 0.000001
        choice = "4"

    elif args.mode == 'm':
        print "Welcome to the node stress tester."
        choice = raw_input("Choose:\n(1) Node Stats\n(2) Whole UTXO\n(3) Block Tip\n(4) Random\n")
        delay = input("Enter the delay you wish to use in seconds(can be fractional): ")

    else:
        print "Please enter a correct mode (a/m)"
        quit()

    ip = getIP()
    while 1:
        performChoice(choice)
        time.sleep(delay)
