import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch secrets from App Service environment variables
    db_conn = os.environ.get("DatabaseConnectionString", "Not Found")
    mongo_uri = os.environ.get("MONGOURI", "Not Found")
    oauth_token = os.environ.get("OAuthToken", "Not Found")

    return f"""
    <h2>Hello, Azure! Here are the secrets from App Service environment variables:</h2>
    <p><b>DatabaseConnectionString:</b> {db_conn}</p>
    <p><b>MONGOURI:</b> {mongo_uri}</p>
    <p><b>OAuthToken:</b> {oauth_token}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
