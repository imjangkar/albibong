import json
import re

def clean_line(line):
    # Remove comments
    line = line.split("//")[0]
    # Split by ',' and process each part
    parts = line.split(",")
    cleaned_parts = []
    for part in parts:
        # Split by space and take the first word
        word = part.strip().split(" ")[0]
        if word:  # Skip empty words
            cleaned_parts.append(word)
    return cleaned_parts

def to_snake_case(name):
    # Convert CamelCase to SNAKE_CASE
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).upper()

def process_event_codes(input_file, json_output_file, string_output_file):
    event_codes = {}
    string_output = []
    with open(input_file, "r") as file:
        counter = 0
        for line in file:
            cleaned_parts = clean_line(line)
            for part in cleaned_parts:
                snake_case_name = to_snake_case(part)
                event_codes[str(counter)] = snake_case_name
                string_output.append(f"{snake_case_name} = {counter}")
                counter += 1
    
    with open(json_output_file, "w") as json_file:
        json.dump(event_codes, json_file, indent=4)
    
    with open(string_output_file, "w") as string_file:
        string_file.write("\n".join(string_output))

if __name__ == "__main__":
    input_path = "enteredOperationCodesEnums.txt"
    json_output_path = "operation_code.json"
    string_output_path = "operation_code_string.txt"
    process_event_codes(input_path, json_output_path, string_output_path)
    print(f"Processed event codes saved to {json_output_path} and {string_output_path}")
