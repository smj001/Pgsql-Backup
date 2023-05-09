FROM iran-registry.itsmj.ir/postgres:15.1

RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Run the backup script
CMD ["python", "app.py"]