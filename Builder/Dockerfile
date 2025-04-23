# Use official Python image
FROM python:3.13

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install mysqlclient

# Copy full Django project
COPY . /app/

# Copy and set permissions on the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose port for Django
EXPOSE 8000

# Use custom entrypoint to wait for DB, migrate, then start server
ENTRYPOINT ["/app/entrypoint.sh"]
