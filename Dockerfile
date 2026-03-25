# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install flask redis

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "flaskapp.py"]