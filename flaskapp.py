from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis setup: use environment variables if available, fallback to defaults
redis_host = os.getenv("REDIS_HOST", "redis")  # Docker container name or localhost
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Home page
@app.route('/')
def home():
    return 'Welcome to my flask-redis app!<br>Visit http://localhost:5000/count to see how many times you have visited this page.'

# Count page
@app.route('/count')
def count():
    try:
        # Increment visit count in Redis and return a simple message
        visits = r.incr('count')
        print(f"Visit count: {visits}")  # Optional: shows in terminal
        return f"You have visited this page {visits} times."
    except redis.exceptions.ConnectionError:
        return "Redis connection failed. Please make sure Redis is running.", 500

if __name__ == "__main__":
    # Flask server accessible outside container, default port 5000
    app.run(host="0.0.0.0", port=5000)