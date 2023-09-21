import logging

logger = logging.getLogger(__name__)

def setup_logger():
    """Set up the logger for the application."""
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.DEBUG)
 
