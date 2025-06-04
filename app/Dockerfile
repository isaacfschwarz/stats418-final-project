# Use Python 3.12
FROM python:3.12-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create a non-root user
RUN useradd --create-home --shell /bin/bash app
RUN chown -R app:app /app
USER app

# Start the Streamlit application
# Cloud Run will set PORT environment variable
CMD ["sh", "-c", "streamlit run streamlit_app_v2.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true"]