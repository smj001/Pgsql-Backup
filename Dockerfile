FROM iran-registry.itsmj.ir/python:3.8-slim-buster

# Add PostgreSQL Apt Repository
RUN apt-get update \
    && apt-get install -y curl \
    && curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list

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
