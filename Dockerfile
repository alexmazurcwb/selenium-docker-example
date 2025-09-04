FROM python:3.12-slim

# Install Chrome and required tools
RUN apt-get update && apt-get install -y wget gnupg2 curl unzip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-linux-signing-keyring.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/google-linux-signing-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

# Download ChromeDriver compatible with Chrome 140
RUN wget -q "https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.41/linux64/chromedriver-linux64.zip" && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf chromedriver-linux64 chromedriver-linux64.zip

# Create screenshots and cache directories with correct permissions
RUN mkdir -p /screenshots
RUN mkdir -p /.cache/selenium && chmod -R 777 /.cache

# Set environment variables for Selenium to avoid permission errors
ENV XDG_CACHE_HOME=/tmp/.cache

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Selenium scripts
COPY . /app
WORKDIR /app

# Default command
CMD ["python", "test.py"]