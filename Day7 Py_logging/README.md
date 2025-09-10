# Python Logging Notes

## Part 1: Logging Basics

### 1. Importing Logging Module
```python
import logging
```
2. Basic Logging Configuration

```python
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
level=logging.DEBUG → capture DEBUG and above

format → time, logger name, level, and message

Handlers: FileHandler → file, StreamHandler → console
```
3. Creating Logger Instance
```python

logger = logging.getLogger("arithmetic_app")
4. Logging in Functions
python
Copy code
def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Error: Division by zero when dividing {a} by {b}")
        return None
```
5. Function Calls Example
```python

add(10, 15)
subtract(15, 10)
multiply(10, 20)
divide(20, 10)
divide(20, 0)  # Triggers error log
Part 2: Logs & Execution
Running the Script
bash
Copy code
python app.py
Example Log Output
ruby
Copy code
YYYY-MM-DD HH:MM:SS - arithmetic_app - DEBUG - Adding 10 + 15 = 25
YYYY-MM-DD HH:MM:SS - arithmetic_app - DEBUG - Subtracting 15 - 10 = 5
YYYY-MM-DD HH:MM:SS - arithmetic_app - DEBUG - Multiplying 10 * 20 = 200
YYYY-MM-DD HH:MM:SS - arithmetic_app - DEBUG - Dividing 20 / 10 = 2.0
YYYY-MM-DD HH:MM:SS - arithmetic_app - ERROR - Error: Division by zero when dividing 20 by 0
DEBUG → Successful operations

ERROR → Critical issues (like division by zero)

Logs stored in app1.log and displayed in console
```
Part 3: Logging with Multiple Loggers
1. Creating Multiple Loggers
```python

# Logger for Module One
logger_one = logging.getLogger("module_one")
logger_one.setLevel(logging.DEBUG)

# Logger for Module Two
logger_two = logging.getLogger("module_two")
logger_two.setLevel(logging.WARNING)
2. Basic Config (applies globally)
python
Copy code
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
3. Logging with Different Loggers
python
Copy code
logger_one.debug("This is a debug message for module one")

logger_two.warning("This is a warning message for module two")
logger_two.error("This is an error message for module two")
```

###Benefits
Clear identification by logger name

Different log levels for different modules

Easier debugging and monitoring
