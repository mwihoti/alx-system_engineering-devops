# 0x0E. Web stack debugging #1

## Author Details :-
```
Mwihoti
```
## What is Debugging
```
the process of finding and fixing errors or bugs in the source code of any software.
```

## Test and verify your assumptions
The idea is to ask a set of questions until you find the issue.
```
* Is the web server started? - You can check using the service manager, also double check by checking process list.
* On what port should it listen? - Check your web server configuration
* Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
* It is listening on the correct server IP? - netstat is also your friend here
* Is there a firewall enabled?
* Have you looked at logs?  usually in /var/log and tail -f is your friend
* Can I connect to the HTTP port from the location I am browsing from? - curl is your friend
```
