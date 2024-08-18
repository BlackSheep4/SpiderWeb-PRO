# Use a base Python image
FROM python:3.12-slim AS base

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary files to install dependencies first
COPY requirements.txt .

# Install necessary system dependencies, including ncurses
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    ncurses-term \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set the TERM environment variable to xterm (helps in headless environments)
ENV TERM=xterm

# Default command to run your script
CMD ["python", "test.py"]
