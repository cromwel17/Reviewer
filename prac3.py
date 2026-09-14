import logging

class AllAttempsFailedError(Exception):
    pass

def process_file():

    import random

    if random.choice([True, False]):
        raise FileNotFoundError("File not found.")
    return "File processed successfully."

def safe_process(process_func, max_retries=3):
    attempts = 0
    while attempts < max_retries:
        try:
            result = process_func()
            return result

        except FileNotFoundError as e:
            logging.warning(
                f"attempt {attempts} failed: {e}. Retrying..."
            ) 


logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s: %(message)s"
)

try:
    result = safe_process(process_file, max_retries=3)
    print(result)

except AllAttempsFailedError as e:
    print(f"All attempts failed: {e}")

def always_fail():
    raise FileNotFoundError("This function always fails.")

try:
    safe_process(always_fail, max_retries=3)
except AllAttempsFailedError as e:
    print(f"All attempts failed: {e}")

    
