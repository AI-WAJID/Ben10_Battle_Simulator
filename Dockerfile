# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install system dependencies for building Python packages (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (backend + frontend)
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r backend/requirements.txt && \
    pip install -r frontend/requirements.txt && \
    pip install supervisor

# Expose the default Render port (or 8501 for Streamlit)
EXPOSE 10000

# Add supervisord config file
COPY supervisord.conf /etc/supervisord.conf

# Start supervisor (which manages both services)
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]
