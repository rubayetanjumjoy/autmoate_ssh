import paramiko

# Server details
ip_address = "10.21.4.160"
username = "leon.paingheinh"
password = "oXWwe8pZ"

# Command to be executed
command = "ls"

try:
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    ssh_client.connect(ip_address, username=username, password=password)

    # Execute the command
    stdin, stdout, stderr = ssh_client.exec_command(command)

    # Read the output
    result = stdout.read().decode('utf-8')

    # Print command output
    print(result)

    # Save result to a file
    with open("ls_output.txt", "w") as file:
        file.write(result)

    print("Command executed successfully.")

except paramiko.AuthenticationException:
    print("Authentication failed.")
except paramiko.SSHException as e:
    print(f"Unable to establish SSH connection: {e}")
except Exception as e:
    print(f"Error executing command: {e}")

finally:
    # Close the SSH connection
    if ssh_client:
        ssh_client.close()
