# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port (important for Hugging Face)
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]
