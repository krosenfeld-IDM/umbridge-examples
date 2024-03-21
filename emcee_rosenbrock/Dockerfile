# Use the latest version of Ubuntu as the base image
FROM ubuntu:latest

# Copy the server.py file to the current directory in the container
COPY server.py .

# Update the package lists and install python3-pip package
RUN apt update && \
    DEBIAN_FRONTEND="noninteractive" apt install -y python3-pip

# Install the umbridge and numpy packages using pip3
RUN pip3 install umbridge numpy

# Set the default command to run the server.py file using python3
CMD python3 server.py