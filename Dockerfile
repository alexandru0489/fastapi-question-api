# Use the official PYthon image from the Docker Hub
FROM python:3.11-slim

# Set the working directory
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt .



# Install the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the app
EXPOSE 8000


# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

