import paramiko
import time
import sys
import re

def launch_instances(self,arg1,arg2,arg3):
    """
        Function Name        : launch_instances
        Function Description : Launches an Instance in OpenStack Environment.
        
        Inputs   : 
            arg1                    - Image (imageName) which is mandatory to launch an Instance.
            arg2                    - Flavour to be used to launch an Instance.
            arg3                    - Name of the Instance to be created.
        Outputs  : 
            an Instance is being created with desired Image ,Flavour and Instance Name.
    """
host = '10.53.173.114'                                                    #server Ip Address
username = 'root'                                                       #server User Name
password = 'root123'                                                   #server Password
ssh_obj = paramiko.SSHClient()
ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_obj.connect(host, username=username, password=password, timeout=10)   #SSH to the server.
print "Connected successfully to the Host :",host


stdin, stdout, stderr = ssh_obj.exec_command("virsh define /root/images/vyatta.xml")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print " virsh define /root/images/vyatta.xml Successfully", data
else:
    print 'Failed Define Launch Instance '

stdin, stdout, stderr = ssh_obj.exec_command("virsh list --all")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print " virsh list --all Successfully", data
else:
    print 'Failed Launch Instance '
    
    
stdin, stdout, stderr = ssh_obj.exec_command("virsh start vyatta-1")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "virsh start vyatta-1"
else:
    print 'Failed to display Instances list'
        
stdin, stdout, stderr = ssh_obj.exec_command("virsh console vyatta-1")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "virsh console vyatta-1"
else:
    print 'Failed to display Instances list'

stdin, stdout, stderr = ssh_obj.exec_command("show interfaces")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "show interfaces"
else:
    print 'Failed to show interfaces'
        
stdin, stdout, stderr = ssh_obj.exec_command("configure")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "configure"
else:
    print 'Failed to configure'
    
stdin, stdout, stderr = ssh_obj.exec_command("set interface dataplane dp0s3 address 10.53.173.115/24")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "set interface dataplane dp0s3 address 10.53.173.115/24"
else:
    print 'Failed to set interface dataplane dp0s3 address 10.53.173.115/24'

stdin, stdout, stderr = ssh_obj.exec_command("set protocols static route 0.0.0.0/0 next-hop 10.53.173.254")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "set protocols static route 0.0.0.0/0 next-hop 10.53.173.254"
else:
    print 'failed set protocols static route 0.0.0.0/0 next-hop 10.53.173.254'
        
stdin, stdout, stderr = ssh_obj.exec_command("commit")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "commit"
else:
    print 'Failed to commit'
        
stdin, stdout, stderr = ssh_obj.exec_command("exit")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "exit"
else:
    print 'Failed to exit'
        
stdin, stdout, stderr = ssh_obj.exec_command("show interfaces")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "show interfaces"
else:
    print 'Failed to show interfaces'
        
stdin, stdout, stderr = ssh_obj.exec_command("ping 10.53.173.254")
time.sleep(5)
errout = stderr.read()
if stdout:
    data = stdout.read()
    print "ping 10.53.173.254"
else:
    print 'Failed to ping 10.53.173.254'
    
    
    
if __name__ == "__main__":
    arg1=sys.argv[1]
    arg2=sys.argv[2]
    arg3=sys.argv[3]
    print launch_instances(1,arg1,arg2,arg3)