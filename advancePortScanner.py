import optparse
from socket import *
from threading import *


def connScan(tgtHost,tgtPort):
    #check weather the port is connected or not 
    try:
        #creating object of socket 
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect(tgtHost,tgtPort)
        print('[+]%d/tcp Open' % tgtPort)
        print('\n')
    except:
        print('[-]%d/tcp Closed' % tgtPort)
        print('\n')
    finally:
        #close the socket object
        sock.close()

#scan all the ports of the HostName
def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Unknown Host %s' %tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan Results for: ' + tgtName[0])
    except:
        print('[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in  tgtPorts:
        t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()

def main():
    #this is use to take input as command line
    parser = optparse.OptionParser('Usade of program: ' + '-H <target host> -p <target port>' )
    #example -H 104.26.6.164 -p 135,443,22,445
    # agrParse options
    parser.add_option('-H',dest='tgtHost',type='string' ,help='specify target host')
    parser.add_option('-p',dest='tgtPort',type='string' ,help='specify target ports specified by comma')
    (options,args) = parser.parse_args()
    #assign value to the variables
    tgtHost =options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if(tgtHost == None) | (tgtPorts[0]==None):
        print (parser.usage)
        exit(0)
    
    portScan(tgtHost,tgtPorts)


if __name__ == '__main__':
    main()

