import time
from functools import wraps
import yaml
import os

def load_yaml_data(file_name="data.yaml"):
    path = os.path.join("config", file_name)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def retry(retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def timing(func):
    """Perform a timing function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    return wrapper
