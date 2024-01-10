import subprocess

def run_ssh_commands(ip, username, password, commands, output_file):
    try:
        # Open the SSH connection and execute commands
        with open(output_file, 'w') as file:
            for command in commands:
                full_command = f"sshpass -p {password} ssh {username}@{ip} {command}"
                result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                # Decode the byte output to a string
                output_str = result.stdout.decode('utf-8') if result.stdout else result.stderr.decode('utf-8')
                
                file.write(f"Command: {command}\n")
                file.write(output_str)
                file.write("\n\n")

        print(f"Output saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

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
