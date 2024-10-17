import os
import logging
import logging.config
from app.commands import add, subtract, multiply, divide

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set up logging
logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')

def main():
    logger.info('Starting the calculator app')

    # Example calculator operations
    a, b = 10, 5
    result_add = add(a, b)
    result_sub = subtract(a, b)
    result_mul = multiply(a, b)
    result_div = divide(a, b)

    logger.info(f"Results - Add: {result_add}, Subtract: {result_sub}, Multiply: {result_mul}, Divide: {result_div}")

if __name__ == "__main__":
    main()
