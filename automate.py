import subprocess

# Specify the file name where you want to save the ls command output
output_file = 'ls_output.txt'

# Using subprocess to run the ls command and capture the output
try:
    # Run the ls command with subprocess and capture the output
    ls_output = subprocess.check_output(['ls'], text=True)

    # Write the output to the specified file
    with open(output_file, 'w') as file:
        file.write(ls_output)

    print(f"ls command output successfully written to {output_file}")

except subprocess.CalledProcessError as e:
    print(f"Error while running ls command: {e}")
except IOError as e:
    print(f"Error writing to file {output_file}: {e}")
