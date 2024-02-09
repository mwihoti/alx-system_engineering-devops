# command_line_for_the_win

## Uploading Screenshots to Sandbox Environment via SFTP

This README provides step-by-step instructions on how to upload screenshots of completed levels to the sandbox environment using the SFTP command-line tool.

>
CMD CHALLENGE is a pretty cool game challenging you on Bash skills
## Prerequisites
* Completed levels with screenshots ready for upload.
* Access to a terminal or command prompt on your local machine.
* Hostname, username, and password provided for the sandbox environment.
## Steps:

* Connect to Sandbox Environment:

Use the SFTP command-line tool to establish a connection to the sandbox environment.
```
Copy code
sftp username@hostname
Replace username with your sandbox username and hostname with the provided hostname for the sandbox environment.
```
* Navigate to Destination Directory:

Once connected, navigate to the directory where you want to upload the screenshots.
```
Copy code
cd /path/to/destination_directory
Replace /path/to/destination_directory with the desired directory path on the sandbox environment.
```
* Upload Screenshots:

Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
```
Copy code
put /path/to/local/screenshot.png
Replace /path/to/local/screenshot.png with the path to the screenshot file on your local machine.
```
* Confirm Transfer
