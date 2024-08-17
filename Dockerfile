# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /Users/anthonylieu/Projects/AlgoTrader-v2

# Copy the current directory contents into the container at /Users/anthonylieu/Projects/AlgoTrader-v2
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make sure python-dotenv is installed
RUN pip install python-dotenv

# Make the .env file available to Docker
COPY .env .env

# Run the Python script
CMD ["python", "./trading.py"]