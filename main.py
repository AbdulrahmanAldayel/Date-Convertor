"""Main entry point for the Hijri Date Converter application."""

import sys
import os
import logging

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.ui.main_window import DateConverterUI
from src.utils.logger import setup_logging


def main():
    """Main application entry point."""
    # Setup logging
    setup_logging(log_level="INFO", log_file="logs/app.log")
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Starting Hijri Date Converter application")
        
        # Create and run the application
        app = DateConverterUI()
        app.run()
        
    except Exception as e:
        logger.error(f"Application error: {e}")
        sys.exit(1)
    finally:
        logger.info("Application shutdown")


if __name__ == "__main__":
    main()
