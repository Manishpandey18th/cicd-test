from flask import Flask, jsonify
import os

app = Flask(__name__)

# Get environment configuration
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ENV = os.environ.get('FLASK_ENV', 'production')

@app.route('/')
def hello_world():
    """Home endpoint - returns a simple greeting"""
    return jsonify({
        'message': 'Hello! Welcome to Flask App on AWS Elastic Beanstalk',
        'environment': ENV,
        'status': 'running'
    }), 200

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running'
    }), 200

@app.route('/api/status')
def status():
    """API status endpoint"""
    return jsonify({
        'api_status': 'operational',
        'version': '1.0.0',
        'environment': ENV
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested resource was not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An internal server error occurred'
    }), 500

if __name__ == '__main__':
    # Run the app
    # In production, this is handled by gunicorn via Procfile
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)