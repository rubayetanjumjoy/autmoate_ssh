FROM python:3.8

# Install Paramiko
RUN pip install paramiko

# Copy your script into the container
COPY automate.py /app/automate.py

# Set the working directory
WORKDIR /app

# Run the script
CMD ["python", "automate.py"]
