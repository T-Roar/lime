# Stage 1: Build the Python environment
FROM python:3.11.6-bullseye AS builder
WORKDIR /app

# Copy just the requirements file to work directory
COPY app/requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt

# Stage 2: Create the final lightweight image
FROM python:3.11-slim-bullseye
WORKDIR /app

# Copy the virtual environment and the app
COPY --from=builder /app/venv venv
COPY app/ .

# Expose the port your app runs on
EXPOSE 80

# Run the application
CMD ["venv/bin/python", "app.py"]