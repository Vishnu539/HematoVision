# Base image with Python 3.9
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the app files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Streamlit or Flask runs on
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]
