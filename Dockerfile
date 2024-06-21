# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the lommeregner.py script into the container
COPY lommeregner.py ./

# Run the Python script
CMD ["python", "./lommeregner.py"]
