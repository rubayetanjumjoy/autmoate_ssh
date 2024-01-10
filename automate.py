import paramiko

def run_ssh_commands(ip, username, password, commands, output_file):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the SSH server
        ssh.connect(ip, username=username, password=password)

        # Open a channel
        channel = ssh.invoke_shell()

        # Send commands
        for command in commands:
            channel.send(command + '\n')

        # Wait for the commands to complete
        while not channel.recv_ready():
            pass

        # Read the output
        output = channel.recv(4096).decode('utf-8')

        # Save the output to a file
        with open(output_file, 'w') as file:
            file.write(output)

        print(f"Output saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

# SSH server details
ip_address = "10.21.4.160"
username = "leon.paingheinh"
password = "oXWwe8pZ"

# Commands to be executed
commands = [
    "enable",
    "show version",
    "show running-config",
    "show interface brief",
    "show mac-address-table"
]

# Output file
output_file = "ssh_output.txt"

# Run SSH commands
run_ssh_commands(ip_address, username, password, commands, output_file)
