import subprocess

def getNodeStats(ip):
    print 1
    subprocess.call(["./exe/jormungandr"])



# if __name__ == "__main__":
print "Welcome to the node stress tester."
print "Using IP form nodeIP.txt"

f = open("nodeIP.txt", "r")
if f:
    ip = f.readline()
    print ip
else:
    ip = raw_input("nodeIP.txt not found. Enter ip of the node.")

