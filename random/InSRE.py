# LinkedIn SRE Prep
# Requests - also see https://www.twilio.com/blog/5-ways-http-requests-python
import requests
import json
import os
import webbrowser

import requests

# Another useful site to tesst Requests with is `httpbin.org`
nasa_api_key = os.environ.get('NASA_API_KEY')
api_url = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(nasa_api_key)

def use_requests(api_url):
    payload = {'key1':4, 'key2':'val2'}  # we can define payload
    response = requests.get(api_url, params=payload, timeout=10)  # and pass it like this
    # for POST requests you can do:
    # requests.post(url, data=payload) <-- this will send data as a post request
    # to get STATUS CODE -> response.status_code, we can also you r.ok to get true/false rather than checking specific code
    # to get text -> response.text (.split('\n'))
    # for basic auth you can do: 
    # requests.get(url, auth=('user','pswd'))
    json_response = json.loads(response.text) # or use response.json()
    photo_url = json_response['url']
    webbrowser.open_new_tab(photo_url)
    # if we needed to download binary content, like images, use `response.content`
    # e.g.
    # with open('image.png','wb) as f:
    #   f.write(response.content)
    return

use_requests(api_url)

# URLLib 3
import json
import os
import webbrowser

import urllib3


nasa_api_key = os.environ.get('NASA_API_KEY')
api_url = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(nasa_api_key)

def use_urllib3(api_url):

    http = urllib3.PoolManager()
    response = http.request('GET', api_url)
    json_response = json.loads(response.data)
    photo_url = json_response['url']
    webbrowser.open_new_tab(photo_url)

    return

use_urllib3(api_url)
"""
in here, Instead of creating a connection directly, You’ll need a PoolManager instance to make requests. This handles connection pooling and thread-safety for you. There is also a ProxyManager object for routing requests through an HTTP/HTTPS proxy Here you can refer to the documentation. example usage :
As mentioned in urrlib3 documentations,urllib3 brings many critical features that are missing from the Python standard libraries.

Thread safety.
Connection pooling.
Client-side SSL/TLS verification.
File uploads with multipart encoding.
Helpers for retrying requests and dealing with HTTP redirects.
Support for gzip and deflate encoding.
Proxy support for HTTP and SOCKS.
100% test coverage.

>>> from urllib3 import PoolManager
>>> manager = PoolManager(10)
>>> r = manager.request('GET', 'http://google.com/')
>>> r.headers['server']
'gws'
>>> r = manager.request('GET', 'http://yahoo.com/')
>>> r.headers['server']
'YTS/1.20.0'
>>> r = manager.request('POST', 'http://google.com/mail')
>>> r = manager.request('HEAD', 'http://google.com/calendar')
>>> len(manager.pools)
2
>>> conn = manager.connection_from_host('google.com')
>>> conn.num_requests
3
"""

# File operations - https://realpython.com/working-with-files-in-python/

with open ('lorem.txt', 'rt') as myfile:  # Open lorem.txt for reading text
    contents = myfile.read()    
""" The mode can be 'r' when the file will only be read, 'w' for 
only writing (an existing file with the same name will be erased),
 and 'a' opens the file for appending; any data written to the file is automatically added to the end. 
'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it's omitted.

Mode	Description
r	Opens a file for reading. (default)
w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Opens a file for exclusive creation. If the file already exists, the operation fails.
a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Opens in text mode. (default)
b	Opens in binary mode.
+	Opens a file for updating (reading and writing)

>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file

>>> f.read()
'This is the entire file.\n'
>>> f.read()
''

>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''

f.write(string) writes the contents of string to the file, returning the number of characters written.

>>> f.write('This is a test\n')
15
To write something other than a string, it needs to be converted to a string first:

>>> value = ('the answer', 42)
>>> s = str(value)
>>> f.write(s)
18

f.tell() returns an integer giving the file object's current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

To change the file object's position, use f.seek(offset, from_what). The position is computed from adding offset to a reference point; the reference point is selected by the from_what argument. A from_what value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.

>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)     # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2) # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'

"""

# To recursively print directory contents
import os

cur_dir = os.getcwd()
for root, sub_dirs, files in os.walk(cur_dir):
    rel_root = os.path.relpath(root)
    print("Showing entries of %s" % rel_root)
    print("-" * 10)
    for entry in sub_dirs + files:
            print(entry)


file_to_remove = "myFile.txt"

if os.path.exists(file_to_remove):
    os.remove(file_to_remove)


# search all files with *py suffix.

import glob, os

query = "**/*.py"

entries = glob.glob(query, recursive=True)
no_of_entries = len(entries)
if no_of_entries == 0:
    print("No results for query: %s" % query)
else:
    print("Found %s result(s) for query: %s" % (no_of_entries, query))

print("-" * 10)
for entry in entries:
    print(entry)


# Process binary file in python

myBinaryFile = open("myFile.bin", "wb") # wb -> write binary
bytes = bytearray([80, 121, 116, 104, 111, 110])
myBinaryFile.write(bytes)
myBinaryFile.close()

# create and extract from archive
import shutil

output_file = "myArchive"
input_dir = "myFolder"
shutil.make_archive(output_file, "zip", input_dir)

input_file = "myArchive.zip"
output_dir = "myNewFolder"
shutil.unpack_archive(input_file, output_dir)

# copy main.py -> main_copy.py
shutil.copy("main.py", "main_copy.py")
# move (rename) main_copy.py -> main_backup.py 
shutil.move("main_copy.py", "main_backup.py")
# recursive copy myFolder -> myFolder_copy
shutil.copytree("myFolder", "myFolder_copy")
# move (rename) myFolder_copy -> myFolder_backup
# if myFolder_backup exists, source is moved inside folder
shutil.move("myFolder_copy", "myFolder_backup")
print("Done.")


# Process a file: 
def process_file(filename):
    with open(filename, "w+") as myFile: 
    # w+: read/write and create if doesn't exist unlike r+
        # Write content
        myFile.write("Hello Python!")
        print("Cursor position: ", myFile.tell()) # 13
        # Reset internal buffer
        myFile.flush()
        # Set cursor to the beginning
        myFile.seek(0)
        print("Cursor position: ", myFile.tell()) # 0
        # Print new content
        content = myFile.read()
        print(content)
        print("Cursor position: ", myFile.tell()) # 13
file_to_read = "myFile.txt"
try:        
    process_file(file_to_read)
except:
    print("Unable to process file %s " % file_to_read)
else:
    print("Successfully processed %s" % file_to_read)

# json 
"""
If you have an object x, you can view its JSON string representation with a simple line of code:

>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
Another variant of the dumps() function, called dump(), serializes the object to a text file. 
So if f is a text file object opened for writing, we can do this:

json.dump(x, f)
To decode the object again, if f is a text file object which has been opened for reading:

x = json.load(f)
This simple serialization technique can handle lists and dictionaries,
 but serializing arbitrary class instances in JSON requires a bit of extra effort.
  The reference for the json module contains an explanation of this."""

# String Parsing
# https://www.computerhope.com/issues/ch001721.htm
"""
string.rstrip('\n') - strips new lines

print(mylines[1].find("e", 10, 30)) # start and end indices are optional, if not found returns -1

"""
# Regular expressions - https://automatetheboringstuff.com/2e/chapter7/
"""
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn't between the brackets.
"""
import re
str = "Good morning, doctor."
pat = re.compile(r"\bd\w*r\b", re.IGNORECASE)  # compile regex "\bd\w*r\b" to a pattern object
if pat.search(str) != None:     # Search for the pattern. If found,
    print("Found it.")

pattern = re.compile("error", re.IGNORECASE)

Phone_number_regex= r'(\+\d{1,2})?[\s.-]?\d{3}[\s.-]?\d{4}'
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)



# Search a dictionary for words
re.compile(r"\bh\w*pe$", re.IGNORECASE) # word starting with h and end with pe
"""
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
"""


# URLLib
# Linkedin RESTful api calling and recursion
# Take part of a log file, export to CSV

import csv
data = ["This", "is", "a", "Test"]
with open('example.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)

import csv
# 1. step
with open('example.csv', 'w', encoding="UTF8") as file:
    # 2. step
    writer = csv.writer(file)
    # 3. step
    data = ["This", "is", "a", "Test"]
    writer.writerow(data)  # use writerows() for multiline data

# write to CSV file
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# Questions on file-system traversal, log processing and APIs.

# apache web logs - 
"""
you can access Apache logs from var/log/log_type. For example, you can access Apache logs from the Apache Unix/Linux server by looking in the following directories:

/var/log/apache/access.log
/var/log/apache2/access.log
/etc/httpd/log/access_log (on MacOS)
/var/log/apache2/error.log
"""
# apache webserver directory location and structure
"""
/etc/apache2/apache2.conf
This file can also be named httpd.conf on older installs. If it's not there, it's likely in one of the following places:

/etc/httpd/httpd.conf
/etc/httpd/conf/httpd.conf


Html dir : /var/www/html 
DocumentRoot "/var/www/html"
or
DocumentRoot "/var/mywebsite/html"

"""
# Describe what happens when you do "curl"?
# -> Answer: bash searches for executable "curl" in directories from PATH env var, 
# once found it forks a process passing in the arg "www.google.com". After that, a call 
# to the kernel is made to handle requests to the network. The network stack is used (TCP/IP) 
# to arbitrate for access to the resources, the request gets broken down into muliple packets 
# onto the network, first to DNS for address translation to IP, then out to the internet and back with muliple packets. 
# When arrived it gets checksumed and re-ordered and sent back to the application


# You type ssh . Can you talk for 30 minutes about what is going on between you hit Enter and you get the login prompt?
"""
Upon receiving a connection request, the server sends the client a set of
supported encryption protocols. The server uses the public key as the authentication method.
The client compares the protocols to its own set. If there are matching protocols, the machines agree to use one to establish the connection.
The client compares the server's public key to the stored private key stored 
in its system on the first connection attempt. 
If the keys match, the client and the server agree to use symmetric encryption to 
communicate during the SSH session. For this purpose, they communicate using an asymmetrically 
encrypted process that employs the Diffie-Hellman (DH) key exchange algorithm.

The DH algorithm enables machines to work together and securely create a cryptographic key over a public network. To generate a key, the machines perform the following steps:

The machines agree on two numbers: a modulus and a base number. To prevent brute force key decryption, the chosen modulus is a prime number of at least 600 digits.
The machines separately choose one number and apply it to the equation involving the two public numbers.
The server and the client exchange the calculated values.
Each machine now performs a calculation using the result received from the other.

Symmetric Encryption
Symmetric encryption generates a single key that two machines exchange. Then, the machines use the key for both encryption and decryption. 
This method is quick, it is not resource-intensive, and SSH uses it for each session.

Whenever the client and the server negotiate which algorithm to use for an SSH session, they always choose the first algorithm on the client's 
list that the server supports.

Asymmetric Encryption
Data is asymmetrically encrypted when machines use two different but mathematically related keys, public and private, to perform the encryption.
The client machine that participated in setting up the encryption can decrypt the information using the private key.

SSH uses temporal asymmetric keys to exchange symmetric keys, such as during the user authentication process.

Hashing
SSH uses hashing to validate if the data packets come from the source they appear to come from. Hashing algorithms used
 to produce hashes in SSH are Message Authentication Code (MAC) and Hashed Message Authentication Code (HMAC).

A hashing algorithm uses a data packet to create a unique hash string. The machine sending the packet always sends the packet together with the hash value.

The receiving machine knows the algorithm used to create the hash and can apply it to the data. The purpose is to see if 
the calculated hash value will be the same. If the obtained hash value differs from the sender's hash, the data got corrupted during the transfer.

sudo vim /etc/ssh/sshd_config  <-- Server config
~/.ssh/config  <-- client config
e.g. content
Host fedora25
        HostName 192.168.56.15
        Port 22
        ForwardX11 no

Host centos7
        HostName 192.168.56.10
        Port 22
        ForwardX11 no

Host ubuntu
        HostName 192.168.56.5
        Port 2222
        ForwardX11 yes

Host *
        User tecmint
        IdentityFile ~/.ssh/id_rsa
        Protocol 2
        Compression yes
        ServerAliveInterval 60
        ServerAliveCountMax 20
        LogLevel INFO



SSH auth failures are logged here /var/log/auth.log

journalctl -t sshd
journalctl -u ssh where -u == unit
journalctl -t sshd -b0
journalctl -t sshd -b0 -r


"""

# https://www.glassdoor.com/Interview/You-need-to-distribute-a-terabyte-of-data-from-a-single-server-to-10-000-nodes-and-then-keep-that-data-up-to-date-It-take-QTN_533809.htm

# How HTTPS works
"""
Server sends certificate - can be seen as public key from server, then you use that to ecnrypt your Symmetric key and send it to server.
Only server can open this and retrieve the key you sent to the server, using it own unique private key. Now that server has your symmetric key
both you and server can use it to encrypt and decrypt the content on the either side. Your key was safely delivered to the server and no one else
can read your communication now as the comm is encrypted and they don't have the key."""

# detailing the steps of an ssh connection
"""
- Initiate ssh request, resolve the IP or hostname and make request on port 22 to the server
- If server has sshd running and it is listening on port 22(as that can be changed) then you start negotiating
  a protocol for authentication that both server and client supports.
- Client sends the public key to server and server checks if it has a matching private key in the authorized keys to complete authentication
- Then once client is authenticated, both of them can agree on a protocol/algorithm to use symmetric encryption during the session lifetime, and every time they communicate
  they will use the encryption and decrypt the received data and also check hash of the data,  The machine sending the packet always sends the packet together with the hash value.

The receiving machine knows the algorithm used to create the hash and can apply it to the data. The purpose is to see if 
the calculated hash value will be the same. If the obtained hash value differs from the sender's hash, the data got corrupted during the transfer.


0 
Operation was successful 
1 
Generic error, usually because invalid command line options or malformed configuration 
2 
Connection failed 
65 
Host not allowed to connect 
66 
General error in ssh protocol 
67 
Key exchange failed 
68 
Reserved 
69 
MAC error 
70 
Compression error 
71 
Service not available 
72 
Protocol version not supported 
73 
Host key not verifiable 
74 
Connection failed 
75 
Disconnected by application 
76 
Too many connections 
77 
Authentication cancelled by user 
78 
No more authentication methods available 
79 
Invalid user name 
"""
# host name resolution details
"""
Client may also check /etc/hosts file before doing dns lookup
Client needs to know where is the DNS server, in linus it could be at /etc/resolv.conf , this file has `search directives` as well as DNS server names
as nameserver directive.
Request goes to first nameserver and it does recursive query- first DNS server may contact other DNS servers unless it has that info in cache.
Top level root zone, first DNS response will say ask nameserver for `.com` domain and provides the nameserver name/ip. 


"""

# http, fork, process priority, runlevel, init
"""
The fork() Function

The fork() function is used to create a new process by duplicating the existing process from which it is called. 
The existing process from which this function is called becomes the parent process and the newly created process
 becomes the child process. As already stated that child is a duplicate copy of the parent but there are some exceptions to it.

The child has a unique PID like any other process running in the operating system.
The child has a parent process ID which is same as the PID of the process that created it.
Resource utilization and CPU time counters are reset to zero in child process.
Set of pending signals in child is empty.
Child does not inherit any timers from its parent
Fork() has an interesting behavior while returning to the calling method. If the fork() function is successful 
then it returns twice. Once it returns in the child process with return value '0' and then it returns in the parent process with child's PID as return value. 
This behavior is because of the fact that once the fork is called, child process is  created and since the child process  shares the text segment with parent 
process and continues execution from the next statement in the same text segment so fork returns twice (once in parent and once in child).
fork() bomb is defined as follows:

:(){
 :|:&
};:
:|: – Next it will call itself using programming technique called recursion and pipes the output to another call of the function ‘:’. The worst part is function get called two times to bomb your system.

& – Puts the function call in the background so child cannot die at all and start eating system resources.

; – Terminate the function definition.

: – Call (run) the function aka set the fork() bomb.
Here is more human readable code:
The number 128038 indicates that you can run 128038 processes. 
To protect your Linux system from a fork bomb, you need to lower that number. To limit your session to 5000 processes, use the following command
ulimit -S -u 5000


# Process priority

Now that we have enough context, let’s dive into the specifics.
Priority value — The priority value is the process’s actual priority which is used by the Linux kernel to schedule a task.
In Linux system priorities are 0 to 139 in which 0 to 99 for real-time and 100 to 139 for users.
Nice value — Nice values are user-space values that we can use to control the priority of a process. The nice value range is -20 to +19 where -20 is highest, 0 default and +19 is lowest.
The relation between nice value and priority is as such -
Priority_value = Nice_value + 20

Start the process with the nice value in the command as 
nice -n nice_val [command] 
Change the nice value of a running process using its PID using renice as 
renice -n nice_val -p [pid] 


# Run levels
he standard LINUX kernel supports these seven different runlevels :

0 – System halt i.e the system can be safely powered off with no activity.
1 – Single user mode.
2 – Multiple user mode with no NFS(network file system).
3 – Multiple user mode under the command line interface and not under the graphical user interface.
4 – User-definable.
5 – Multiple user mode under GUI (graphical user interface) and this is the standard runlevel for most of the LINUX based systems.
6 – Reboot which is used to restart the system.


# Init process and Bootup Sequence


1) BIOS - Executes Master Boot Record
Performs some system integrity checks
Searches, loads, and executes the boot loader program.
It looks for boot loader in floppy, cd-rom, or hard drive. You can press a key
 (typically F12 of F2, but it depends on your system) during the BIOS startup to change the boot sequence.
Once the boot loader program is detected and loaded into the memory, BIOS gives the control to it.
So, in simple terms BIOS loads and executes the MBR boot loader


2) MBR - Executes Grand Unified Bootloader
It is located in the 1st sector of the bootable disk. Typically /dev/hda, or /dev/sda
MBR is less than 512 bytes in size. This has three components 
    1) primary boot loader info in 1st 446 bytes 
    2) partition table info in next 64 bytes 
    3) mbr validation check in last 2 bytes.
It contains information about GRUB (or LILO in old systems).

3) GRUB - Executes Kernel
If you have multiple kernel images installed on your system, you can choose which one to be executed.
GRUB displays a splash screen, waits for few seconds, if you don’t enter anything, it loads the default kernel image as specified in the grub configuration file.
GRUB has the knowledge of the filesystem (the older Linux loader LILO didn’t understand filesystem).
Grub configuration file is /boot/grub/grub.conf (/etc/grub.conf is a link to this). The following is sample grub.conf of CentOS.

    #boot=/dev/sda
    default=0
    timeout=5
    splashimage=(hd0,0)/boot/grub/splash.xpm.gz
    hiddenmenu
    title CentOS (2.6.18-194.el5PAE)
            root (hd0,0)
            kernel /boot/vmlinuz-2.6.18-194.el5PAE ro root=LABEL=/
            initrd /boot/initrd-2.6.18-194.el5PAE.img

As you notice from the above info, it contains kernel and initrd image.



4) Kernel - Executes /sbin/init
Mounts the root file system as specified in the “root=” in grub.conf
Kernel executes the /sbin/init program
Since init was the 1st program to be executed by Linux Kernel, it has the process id (PID) of 1. Do a ‘ps -ef | grep init’ and check the pid.
initrd stands for Initial RAM Disk.
initrd is used by kernel as temporary root file system until kernel is booted and
 the real root file system is mounted. It also contains necessary drivers compiled inside, which helps it to access the hard drive partitions, and other hardware.


5) Init - Executes runlevel
Looks at the /etc/inittab file to decide the Linux run level.
Following are the available run levels
0 – halt
1 – Single user mode
2 – Multiuser, without NFS
3 – Full multiuser mode
4 – unused
5 – X11
6 – reboot
Init identifies the default initlevel from /etc/inittab and uses that to load all appropriate program.
Execute ‘grep initdefault /etc/inittab’ on your system to identify the default run level
If you want to get into trouble, you can set the default run level to 0 or 6. Since you know what 0 and 6 means, probably you might not do that.
Typically you would set the default run level to either 3 or 5.

6) Runlevel - Executes programs from /etc/rc.d/rc*.d/
When the Linux system is booting up, you might see various services getting started. For example, it might say “starting sendmail …. OK”. Those are the runlevel programs, executed from the run level directory as defined by your run level.
Depending on your default init level setting, the system will execute the programs from one of the following directories.
Run level 0 – /etc/rc.d/rc0.d/
Run level 1 – /etc/rc.d/rc1.d/
Run level 2 – /etc/rc.d/rc2.d/
Run level 3 – /etc/rc.d/rc3.d/
Run level 4 – /etc/rc.d/rc4.d/
Run level 5 – /etc/rc.d/rc5.d/
Run level 6 – /etc/rc.d/rc6.d/

Ref: https://www.thegeekstuff.com/2011/02/linux-boot-process/


"""
# If you have an executable program (a binary) and you made a copy of that program, and
#  then changed permissions on the copy, would a diff show that the file had been changed?
"""
It won't show the diff.
❯ diff /bin/ls ./ls

~
❯ ls -la /bin/ls ./ls
-rwxr-xr-x@ 1 kedarvijayk  staff  187040 Jul 19 15:03 ./ls
-rwxr-xr-x  1 root         wheel  187040 Mar 26 03:21 /bin/ls

~
❯ chmod -x ./ls

~
❯ ls -la /bin/ls ./ls
-rw-r--r--@ 1 kedarvijayk  staff  187040 Jul 19 15:03 ./ls
-rwxr-xr-x  1 root         wheel  187040 Mar 26 03:21 /bin/ls

~
❯ diff /bin/ls ./ls

"""

# When you run a program from the shell, why doesn't the program log you out when it's done running? If you wanted this behavior, how would you run the program?
"""
 (answer: exec)

Whenever we run any command in a Bash shell, a subshell is created by default, and a new child process is spawned (forked) to execute the command. 
When using exec, however, the command following exec replaces the current shell. This means no subshell is created and the current process is replaced with this new command.
"""
# What protocol(s) do/does DNS use when you run an nslookup. 
"""(answer: normally UDP, but TCP is used for zone transfers and if a record is too long to be returned via UDP)"""

# Describe the difference between TCP and UDP, advantages and disadvantages of both.
"""
TCP

Not lightweight as it has more features
Connection oriented
Data called as Segments
Reliable, has error recovery
Windowing(flow control)
Ordered Data transfer using sequence numbers
Uses Source and Dest ports, ports enable multiplexing, so many applications can use the network at same time. 
If we receive two different network communications, we can't figure out which process owns it
 until we know what Port it is going to. Because IP and MAC addresses are same in both the case.

Three Way Handshakes:

Client sends Empty TCP header with SYN, uses SYN flag for synchronous conversation, Window value is also set.
Server sends Empty header with SYN/ACK- Says I acknowldge you and let's have synchronous communication
Client sends Empty TCP header with ACK flag set. Random sequence number is used in all 3 packets above. 
First is selected random and next two will be incrementing that random sequence number.
Graceful Termination:

Dev1 sends FIN/ACK, Dev2 says ACK
Dev2 Sends FIN/ACK, and Dev1 says ACK These are required because when initial FIN/ACK is received, the application may need little time to send FIN/ACK of its own.
Abrupt Termination:

RST(Reset) message is used to close connection if there is error in the connection
UDP

Lightweight
Connection less
Data called as Datagrams
Does not care about data sequencing
Unreliable, doesn't care about missing packets or errors(useful in audio/video data)
Uses Source and Dest ports, ports enable multiplexing, so many applications can use the network at same time. 
If we receive two different network communications, we can't figure out which process owns it until we know what Port it is going to. 
Because IP and MAC addresses are same in both the case.

"""


# Write a program that reverses the contents of a file, byte for byte.
# Open the file in write mode
f1 = open("output1.txt", "w")
  
# Open the input file and get 
# the content into a variable data
with open("file.txt", "r") as myfile:
    data = myfile.read()
  
# For Full Reversing we will store the 
# value of data into new variable data_1 
# in a reverse order using [start: end: step],
# where step when passed -1 will reverse 
# the string
data_1 = data[::-1]
  
# Now we will write the fully reverse 
# data in the output1 file using 
# following command
f1.write(data_1)
  
f1.close()

# Write a program that descends through a directory tree and prints all files. (hint: recursion is your friend here.)
#!/usr/bin/python

import os

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("./random"):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)

# Given an Apache log file, print the timestamp hour, minute, and second, followed by the number of times any log entry occurs during that time. (hint: if you're programming in perl, a hashed array works great here.)

# What is difference between tcp/udp, which one is used in live streaming and paid subscriptions
"""
HTTP Live Streaming (HLS)
Live TV may use UDP but for on-demand content may be using TCP.
"""

# CareerCup and the Unix and Linux System Administration Handbook by Evi Nemeth were invaluable
# https://github.com/krishnaramb/FB_Prep/blob/master/glassdoor_questions.md


# Goat Latin - https://leetcode.com/problems/goat-latin/
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        words = sentence.split(' ')
        for i, item in enumerate(words):
            if item[0].lower() in "aeiou":
                words[i] = item + 'ma' + 'a'* (i+1)
            else:
                words[i] = item[1:] + item[0] + 'ma' + 'a'* (i+1)
        return ' '.join(words)



# Find wordcount from a file using Linux command line

"""
tr -s ' \011' '\012' < /var/log/McAfeeSecurity.log | sort | uniq -c | sort -rn | head -20
"""
# Re to find INFO/ERROR logs from file, line by line
lines ="""
Jan 31 00:21:30 ubuntu.local ticky: ERROR: The ticket was modified while updating (breee)
Jan 31 00:21:30 ubuntu.local ticky: ERROR: The ticket was modified while updating (sam)
Jan 31 00:21:30 ubuntu.local ticky: INFO: The ticket was successful (breee)
"""
for line in lines.split('\n'):
    # ?P<> is used to name the groups
    info = re.findall(r"ticky: (?P<logtype>INFO|ERROR): (?P<logmessage>[\w].*)? \((?P<username>[\w]*)\)$", line, re.MULTILINE)
    print(info)



# count number of times each timestamp occured in a log file


from collections import Counter

def read_logs(filename):
    with open(filename) as log_file:
         for line in log_file:
             timestamp = datetime.datetime.strptime(
                     line.strip(),
                     '[%d/%b/%Y:%H:%M:%S %z]')
             yield timestamp.hour


def count_access(log_filename):
    return Counter(read_logs(log_filename))


if __name__ == '__main__':
    print(count_access('/path/to/logs/'))


line = "Feb  3 13:34:03 j4-be02 sshd[672]: Failed password for root from 85.17.188.70 port 47613 ssh"

re.search("Failed password for (?P<user>.+?) from (?P<ip>\S+)", line).group('user')
'root'

re.search("Failed password for (?P<user>.+?) from (?P<ip>\S+)", line).group('ip')
'85.17.188.70'

re.search(r"(?P<date>[A-Z][a-z]{2}\s{2}\d{1,2}\s\d+:\d+:\d+).+Failed password for (?P<user>.+?) from (?P<ip>\S+)", line).groups()
Out[24]: ('Feb  14 13:34:03', 'root', '85.17.188.70')


res = re.search(r"(?P<date>[A-Z][a-z]{2}\s{2}\d{1,2}\s\d+:\d+:\d+).+Failed password for (?P<user>.+?) from (?P<ip>\S+)", line)

In [28]: res.groups()
Out[28]: ('Feb  14 13:34:03', 'root', '85.17.188.70')

In [30]: res.group('date')
Out[30]: 'Feb  14 13:34:03'


Regex_for_http_byte_and_status_codes = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - .*?HTTP/1.1" (\d+) (\d+)'


Rather than using multiple regular expressions making multiple passes through the log, this solution uses one regular expression to pull out all the relevant values in one pass.

Function process_log is passed the text of the log as a single string. In the following demo program, a test string is used. An actual implementation would call this function with the results of reading the actual log file.

To keep track of IP addresses/status pairs, a defaultdict using a list as the default_factory is used. The number of items in the list counts the number of times the IP address/status combination has been seen and each list item is the number of bytes transferred for that HTTP request. For example, an key/value pair of the ip_status dictionary might be:

key: ('123.12.11.9', '200')  value: [6213, 9876, 376]
The interpretation of the above is that there were 3 instances of status code '200' for ip address '123.12.11.9' discovered. The bytes transferred for these 3 instances were 6213, 9876 and 376.

Explanation of the regex:

(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - .*?HTTP/1.1" (\d+) (\d+)
(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - This is essentially the regex used by the OP to recognize an IP address so it shouldn't require much of an explanation. I have followed it with - - to provide additional following context just in case there are other instances of similar looking strings. The IP address is captured in Capture Group 1.
.*? This will match non-greedily 0 or more non-newline characters until the following.
HTTP/1.1" Matches the string HTTP/1.1" to provide left-hand context for the following.
(\d+) Matches one or more digit in Capture Group 2 (the status).
 Matches a single space.
(\d+) Matches one or more digit in Capture Group 3 (the transferred bytes).
See Regex Demo

In other words, I just want to make sure I am picking up the right fields from the right place by matching what I expect to find next to the fields I am looking for. When your regex returns multiple groups, finditer is often more convenient then findall. finditer returns an iterator yielding a match object for each iteration. I have added code to produce statistics for both ip/status code/transferred bytes and just status code. You need only one or another depending on what the user wants.

The code:

import re
from collections import defaultdict

def process_log(log):
    ip_counter = defaultdict(list)
    status_counter = defaultdict(int)
    total_count = 0
    for m in re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - .*?HTTP/1.1" (\d+) (\d+)', log):
        total_count += 1
        ip = m[1]
        status = m[2]
        bytes = int(m[3])
        ip_counter[(ip, status)].append(bytes)
        status_counter[status] += 1
    for k, v in ip_counter.items():
        count = len(v)
        percentage = count/total_count
        total_bytes = sum(v)
        ip = k[0]
        status = k[1]
        print(f"IP Address => {ip}, status => {status}, Count => {count}, Percentage => {percentage}, Total Bytes Transferred => {total_bytes}")
    for k, v in status_counter.items():
        count = v
        percentage = count/total_count
        print(f"Status Code => {k}, Percentage => {percentage}")




log = """93.114.45.13 - - [17/May/2015:10:05:17 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 6146 "http://www.semicomplete.com/articles/dynamic-dns-with-dhcp/" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
93.114.45.13 - - [17/May/2015:10:05:21 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/style2.css" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
66.249.73.135 - - [17/May/2015:10:05:40 +0000] "GET /blog/tags/ipv6 HTTP/1.1" 200 12251 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1;
+http://www.google.com/bot.html)"83.149.9.216 - - [17/May/2015:10:05:25 +0000] "GET /presentations/logstash-monitorama-2013/images/elasticsearch.png HTTP/1.1" 200 8026 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
83.149.9.216 - - [17/May/2015:10:05:59 +0000] "GET /presentations/logstash-monitorama-2013/images/logstashbook.png HTTP/1.1" 200 54662 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
"""

process_log(log)
Prints:

IP Address => 93.114.45.13, status => 200, Count => 2, Percentage => 0.4, Total Bytes Transferred => 58461
IP Address => 66.249.73.135, status => 200, Count => 1, Percentage => 0.2, Total Bytes Transferred => 12251
IP Address => 83.149.9.216, status => 200, Count => 2, Percentage => 0.4, Total Bytes Transferred => 62688
Status Code => 200, Percentage => 1.0



# nohup command in linux allows you to logout without interrupting process you started.