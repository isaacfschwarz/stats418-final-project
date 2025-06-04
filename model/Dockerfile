# Use Python 3.12
FROM python:3.12

# Expose port (this is mainly for documentation)
# EXPOSE 8001

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy all application files
COPY . .

# Make sure the model file exists (add a check)
RUN ls -la multi_target_model.joblib || echo "WARNING: Model file not found!"

# Start the application
CMD ["python", "model.py"]