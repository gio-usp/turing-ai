import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration class."""
    ENV = 'base'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///default.db')

class DevelopmentConfig(Config):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True
    DATABASE_URI = os.environ.get('DATABASE_URI', "mongodb+srv://root:passwd@clusterturing.g6gpfgy.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTuring")
    PORT = os.environ.get('PORT', 8080)

class TestingConfig(Config):
    """Testing configuration."""
    ENV = 'testing'
    TESTING = True
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///test.db')
    PORT = os.environ.get('PORT', 8081)

class ProductionConfig(Config):
    """Production configuration."""
    ENV = 'production'
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///prod.db')
    PORT = os.environ.get('PORT', 80)

def getConfig():
    """Get the appropriate configuration based on the environment variable."""
    env = os.environ.get('ENV')
    if env == 'development':
        return DevelopmentConfig()
    elif env == 'testing':
        return TestingConfig()
    elif env == 'production':
        return ProductionConfig()
    else:
        return Config()  # Default to base config if no valid ENV is set