import subprocess

def run_ssh_commands(ip, username, password, commands, output_file):
    try:
        # Open the SSH connection
        ssh_cmd = f"sshpass -p {password} ssh {username}@{ip}"
        ssh_process = subprocess.Popen(ssh_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ssh_stdin = ssh_process.stdin
        ssh_stdout = ssh_process.stdout
        ssh_stderr = ssh_process.stderr

        # Execute commands
        with open(output_file, 'w') as file:
            for command in commands:
                # Send command to the SSH session
                ssh_stdin.write(f"{command}\n".encode('utf-8'))
                ssh_stdin.flush()

                # Wait for the command to complete
                ssh_process.poll()

                # Read the output
                output_str = ssh_stdout.read().decode('utf-8') if ssh_stdout else ssh_stderr.read().decode('utf-8')

                file.write(f"Command: {command}\n")
                file.write(output_str)
                file.write("\n\n")

        print(f"Output saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        ssh_stdin.close()
        ssh_stdout.close()
        ssh_stderr.close()

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
output_file = "ssh_output_subprocess.txt"

# Run SSH commands using subprocess
run_ssh_commands(ip_address, username, password, commands, output_file)
