import paramiko

# SSH connection parameters
hostname = '10.21.4.160'
port = 22
username = 'leon.paingheinh'
password = 'oXWwe8pZ'

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the SSH server
    ssh.connect(hostname, port=port, username=username, password=password)

    # List of commands to execute
    commands = [
        'enable',
        'show version',
        'show running-config',
        'show interface brief',
        'show mac-address-table',
    ]

    # Execute commands and save output to a text file
    with open('ssh_commands_output.txt', 'w') as output_file:
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode('utf-8')
            output_file.write(f"\n===== {command} =====\n{output}\n")

    print("Commands executed successfully. Output saved to ssh_commands_output.txt")

finally:
    # Close the SSH connection
    ssh.close()
