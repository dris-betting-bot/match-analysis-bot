"""
Configuration Module
Loads and manages bot configuration
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # Telegram Configuration
    TELEGRAM_TOKEN = os.getenv(
        'TELEGRAM_TOKEN',
        '8834948528:AAGYNH4TQZE2ve3bSw007QaXNoxCJYpJr-o'
    )
    
    # Football Data API Configuration
    FOOTBALL_API_KEY = os.getenv(
        'FOOTBALL_API_KEY',
        'ba15271bc79f4a01a4ddae95a017ad72'
    )
    FOOTBALL_API_BASE = 'https://api.football-data.org/v4'
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Bot Configuration
    BOT_NAME = 'Match Analysis Bot'
    BOT_VERSION = '1.0.0'
    BOT_TIMEOUT = 30
    
    # Cache Configuration
    CACHE_TTL = 3600  # 1 hour
    
    # API Rate Limiting
    API_RATE_LIMIT = 10  # requests per minute
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        if not cls.TELEGRAM_TOKEN:
            raise ValueError("TELEGRAM_TOKEN not set")
        if not cls.FOOTBALL_API_KEY:
            raise ValueError("FOOTBALL_API_KEY not set")
        
        return True

# Development Configuration
class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

# Production Configuration
class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    LOG_LEVEL = 'INFO'

# Select configuration based on environment
ENV = os.getenv('ENVIRONMENT', 'development')
if ENV == 'production':
    config = ProductionConfig()
else:
    config = DevelopmentConfig()

# Validate configuration
config.validate()
