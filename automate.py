import paramiko
from paramiko import AuthenticationException, SSHException
import time
import re
def clean_text(output):
    # Remove control characters and escape sequences
    cleaned_output = re.sub(r'\x1b\[[0-9;]*[mK]', '', output)
    output=output.replace("....press ENTER to next line, CTRL_C to quit, other key to next page....","")
    return output
 
    
def connect_send_command_and_save(hostname, port, username, password, commands, output_file):
    try:
        # Create an SSH client
        with paramiko.SSHClient() as client:
            # Automatically add the host key (this is insecure; see below)
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the network switch
            client.connect(hostname, port, username, password)

            print(f"Connected to {hostname}.")

            # Open a shell session
            with client.invoke_shell() as shell:
                # Read the initial output to detect the password prompt
                output = shell.recv(65535).decode('utf-8')
                print(output)

                # Check if the output contains a password prompt
                if 'Password' in output:
                    # Send the password
                    shell.send(password + '\n')
                    print(f"Sent password to {hostname}.")

                # Iterate through the list of commands
                for command in commands:
                    # Send the current command
                    shell.send(command + '\n')
                    print(f"Sent command to {hostname}: {command}")

                    # Wait for a short time to ensure the command has been executed
                    time.sleep(2)

                    # Receive and print the command output
                    output = shell.recv(65535).decode('utf-8')
                    print("Command Output:")
                    print(output)
                    if '....press ENTER to next line, CTRL_C to quit, other key to next page....' not in output:
                        with open(output_file, 'a') as file:
                                file.write(f": {command}\n")
                                file.write(f"=================\n\n\n")
                                file.write(clean_text(output))
                                
                                file.write("\n\n")
                                
                        

                    # Handle pagination
                    while '....press ENTER to next line, CTRL_C to quit, other key to next page....' in output:
                        shell.send('\n')
                        time.sleep(2)
                        new_output = shell.recv(65535).decode('utf-8')

                        # Exclude the specific string from the output
                        new_output = clean_text(new_output)

                        output += new_output
                        print(new_output)
 

                        # Check for a prompt indicating the end of the command output
                        if 'fs-cag-sw1#' in new_output:
                            after_clean = output.replace("....press ENTER to next line, CTRL_C to quit, other key to next page....", "")
                            clear_terminal=clean_text(after_clean)
                            # Save the new output to the file with a headline
                            with open(output_file, 'a') as file:
                                file.write(f": {command}\n")
                                file.write(f"=================\n\n\n")
                                file.write(clear_terminal)
                                print(after_clean)
                                file.write("\n\n")
                            break

                    print(f"Saved command output to {output_file}.")

    except AuthenticationException:
        print("Authentication failed. Please check your username and password.")
    except SSHException as e:
        print(f"Error connecting to {hostname}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the SSH connection parameters
hostname = '10.21.4.160'
port = 22
username = 'leon.paingheinh'
password = 'oXWwe8pZ'
commands = [
    'enable',
    # 'show version',
    'show running-config',
    # 'show interface brief',
    # 'show mac-address-table',
    
]
output_file = 'fs-cag-sw1.txt'

# Open the file in write mode to clear its content
with open(output_file, 'w') as file:
    file.truncate(0)


print(f"Text in {output_file} cleared.")
# Attempt to connect to the network switch, execute the commands, and save the outputs
connect_send_command_and_save(hostname, port, username, password, commands, output_file)



# Read the file content
with open(output_file, 'r') as file:
    content = file.read()

# Remove the specified sequence
content = content.replace('\033[72D\033[K', '')

# Write the modified content back to the file
with open(output_file, 'w') as file:
    file.write(content)
