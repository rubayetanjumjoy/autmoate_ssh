import subprocess

def run_ssh_commands(ip, username, password, commands, output_file):
    try:
        # Open the SSH connection and execute commands
        with open(output_file, 'w') as file:
            for command in commands:
                full_command = f"sshpass -p {password} ssh {username}@{ip} {command}"
                result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE)
                
                # Decode the byte output to a string
                output_str = result.stdout.decode('utf-8')
                
                file.write(f"Command: {command}\n")
                file.write(output_str)
                file.write("\n\n")

        print(f"Output saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

# Rest of the code remains unchanged
