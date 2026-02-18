# Dockerfile

# 1. Use official Python base image
FROM python:3.12-slim

# 2. Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 3. Set working directory
WORKDIR /app

# 4. Copy requirements first for caching
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the project
COPY . .

# 7. Expose port for FastAPI
EXPOSE 8000

# 8. Run the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
