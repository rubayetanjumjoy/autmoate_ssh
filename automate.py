import subprocess

# Server details
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

try:
    # Spawn an SSH process
    ssh_process = subprocess.Popen(
        f'ssh {username}@{ip_address}', 
        shell=True, 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    # Provide the password
    ssh_process.stdin.write(password + '\n')
    ssh_process.stdin.flush()
    print("successfully ssh in the server")
    for command in commands:
        # Send each command
        ssh_process.stdin.write(command + '\n')
        ssh_process.stdin.flush()
        print(command)
        # Wait for the command to complete
        ssh_process.wait()

        # Save result only for 'show mac-address-table'
        if command.startswith("show mac-address-table"):
            with open("mac_address_table.txt", "a") as file:
                file.write(f"\nCommand: {command}\n")
                file.write(ssh_process.stdout.read())

    print("Commands executed successfully.")

except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")

finally:
    # Close the SSH process
    if ssh_process:
        ssh_process.communicate()
