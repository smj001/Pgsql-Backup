FROM iran-registry.itsmj.ir/python:3.8-slim-buster

# Install PostgreSQL client tools
RUN apt-get update && \
    apt-get install -y postgresql-client-15 && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Run the backup script
CMD ["python", "app.py"]
