###############################################################################################################################
# Description : launch_instances contains the Library that Launches an Instance in OpenStack Environment.
# Developer   : Kiran Mandal
# Date        : 8th-May,2017
###############################################################################################################################
"""
*launch_instances*  contains the Library that Launches an Instance in OpenStack Environment.
              
"""

import paramiko
import time
import sys
import re
#arg1=imageName
#arg2=flavour
#arg3=instanceName

#arg1=sys.argv[1]
#arg2=sys.argv[2]
#arg3=sys.argv[3]

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
    print "launch_instances"
    host = '10.53.173.114'                                                    #server Ip Address
    username = 'root'                                                       #server User Name
    password = 'root123'                                                   #server Password
    ssh_obj = paramiko.SSHClient()
    ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_obj.connect(host, username=username, password=password, timeout=10)   #SSH to the server.
    print "Connected successfully to the Host :",host
    time.sleep(2)
    print "Launching Instance ",arg3," with Image ",arg1," and Flavour ",arg2
    # Creating Instances.
    stdin, stdout, stderr = ssh_obj.exec_command("source virsh define /root/images/vyatta.xml")
    stdin, stdout, stderr = ssh_obj.exec_command("virsh list --all")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instance ",arg3," Launched Successfully"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to Launch Instance ',arg3,' with Image ',arg1,' and Flavour ',arg2
        #print errout
    '''
    time.sleep(10)
    print "List of Instances:"
    stdin, stdout1, stderr1 = ssh_obj.exec_command("source keystonerc_admin && nova list")   
    time.sleep(5)
    errout = stderr1.read()
    if stdout1:
        print stdout1.read()
        
        #return errout
    else:
        # return stdout.read()
        print errout 
    attaching_ip_address(1,arg3)
    '''
        
    stdin, stdout, stderr = ssh_obj.exec_command("virsh start vyatta-1")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout
        
    stdin, stdout, stderr = ssh_obj.exec_command("virsh console vyatta-1")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout   
    

    stdin, stdout, stderr = ssh_obj.exec_command("show interfaces")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout
        
    stdin, stdout, stderr = ssh_obj.exec_command("configure")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout
        
    stdin, stdout, stderr = ssh_obj.exec_command("set interface dataplane dp0s3 address")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout
        
    stdin, stdout, stderr = ssh_obj.exec_command("set protocols static route 0.0.0.0/0 next-hop 10.53.173.254")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout
        
    stdin, stdout, stderr = ssh_obj.exec_command("commit")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout
        
    stdin, stdout, stderr = ssh_obj.exec_command("exit")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout
        
    stdin, stdout, stderr = ssh_obj.exec_command("show interfaces")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout
        
    stdin, stdout, stderr = ssh_obj.exec_command("ping 10.53.173.254")
    time.sleep(5)
    errout = stderr.read()
    if stdout:
        data = stdout.read()
        print "Instances List"
        #print 'Failed to execute command'
        #print data
        #return errout
    else:
        # return stdout.read()
        #data = stdout.read()
        print 'Failed to display Instances list'
        #print errout

    
    ''' 
    if arg3 in data:
        items=re.findall((arg3+".*$"),data,re.MULTILINE)
    for ip in items:
        #print ip
        ip=ip.split('|')
        #print ip[0]
        #print ip[-2]
        ext_mgmtIP=ip[-2]
        ext_mgmtIP=ext_mgmtIP.split('=')
        ext_mgmtIP=(ext_mgmtIP[-1]).split(" ")
        ext_mgmtIP=str(ext_mgmtIP[0])
        #Copying the Ip address to a file in the server.
        stdin, stdout, stderr = ssh_obj.exec_command("source keystonerc_admin && echo "+"'"+arg3+" "+ext_mgmtIP+"'"+" >>robot_input_openstack.txt")
        print "IP address ",ext_mgmtIP,"is copied to robot_input_openstack.txt "
    '''
    
    #ssh_obj.close()
    

#launch_instances(1,arg1,arg2,arg3)
#attaching_ip_address(1,arg3)
if __name__ == "__main__":
    arg1=sys.argv[1]
    arg2=sys.argv[2]
    arg3=sys.argv[3]
    print launch_instances(1,arg1,arg2,arg3)