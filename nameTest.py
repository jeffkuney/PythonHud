import json

# Function to save input to a JSON file
def save_input_to_json():
    # Get user input
    user_input = input("Enter something to save to JSON: ")

    # Create a dictionary with the input
    data = {"user_input": user_input}

    # Save to a JSON file
    with open("user_input.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Your input has been saved to 'user_input.json'.")

# Call the function
if __name__ == "__main__":
    save_input_to_json()