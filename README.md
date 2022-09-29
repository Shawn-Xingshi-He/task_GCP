### This task is to simulate the registration process on a website which composed of 3 different sub tasks:

1. The "server" script (Server.py) which is automated on a Virtual Machine in GCP.
2. The "client" script (Client.py) to send a message to the server script running on the VM.
3. A GCP Function (GCPFunction.py) which sends an email to the client's email, triggered by the server script.

#### Client.py should be executed via command line: `python client.py {Email address} {Email subject} {Email content}`

This script will send the message to the VM server.

#### Server.py `python Server.py`

It should receive the message from the client and forward it to the GCP function. You may consider running this script in `tmux`.

#### GCP function script

This procedural script running on a GCP function will simply take the three arguments (address/subject/content), and utilize a python library of choice (smtplib), to send an email to the client's email.

### Restrictions/Clarifications:

• The client script is able to externally access the "server" running on the VM, that is from outside GCP.
• You need to setup a Gmail account and "Enable Third-Party Access" to programmatically send emails in the GCP Function
• You should consider HTTP triggers.
