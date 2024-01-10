import subprocess

# Server details
ip_address = "10.21.4.160"
username = "leon.paingheinh"
password = "oXWwe8pZ"

# Command to be executed
command = "ls"

try:
    # Spawn an SSH process
    ssh_process = subprocess.Popen(
        f'ssh {username}@{ip_address} "{command}"', 
        shell=True, 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    # Provide the password
    ssh_process.stdin.write(password + '\n')
    ssh_process.stdin.flush()
    print("Successfully SSHed into the server")

    # Read the output
    result = ssh_process.stdout.read()

    # Print command output
    print(result)

    # Save result to a file
    with open("ls_output.txt", "w") as file:
        file.write(result)

    print("Command executed successfully.")

except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")

finally:
    # Close the SSH process
    if ssh_process:
        ssh_process.communicate()
