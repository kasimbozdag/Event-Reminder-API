# Dockerfile
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y netcat-traditional

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Make entrypoint script executable
RUN chmod +x ./docker-entrypoint.sh

# Expose the port (optional)
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["./docker-entrypoint.sh"]
