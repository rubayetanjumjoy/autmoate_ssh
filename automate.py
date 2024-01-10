import subprocess

# Run the 'ls' command
result = subprocess.run(['ls'], stdout=subprocess.PIPE, text=True)

# Save the output to a text file
with open('ls_output.txt', 'w') as file:
    file.write(result.stdout)

print("ls command output has been saved to ls_output.txt")
