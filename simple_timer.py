import time

def simple_timer(duration):
    print(f"Timer started for {duration} seconds.")
    for remaining in range(duration, 0, -1):
        print(f"Time remaining: {remaining} seconds", end="\r")
        time.sleep(1)
    print("\nTimer finished!")

# Example usage
simple_timer(10)  # Timer for 10 seconds