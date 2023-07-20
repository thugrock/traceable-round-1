# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files into the container
COPY app.py .

# Set the environment variable for Flask to listen on all available IPs (0.0.0.0) and port 5000
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000

# Expose the port your Flask app listens on
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]
