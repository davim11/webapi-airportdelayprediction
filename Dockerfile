FROM rust:1.82-slim
WORKDIR /app

# Copy requirements first
COPY requirements-full.txt .

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip \
    && export PATH="/usr/local/cargo/bin:$PATH" \
    && rustc --version && cargo --version \
    && pip3 install --no-cache-dir -r requirements-full.txt --break-system-packages \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY APIcode_task3.py .
COPY test_APIcode_task3.py .

EXPOSE 8000
CMD ["uvicorn", "APIcode_task3:app", "--host", "0.0.0.0", "--port", "8000"]