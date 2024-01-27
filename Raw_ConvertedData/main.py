import json

def process_quotes_from_text(filename, convert_to_json=False):
    """Reads quotes from a text file, extracts them, and optionally converts them to JSON."""

    quotes = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # Assuming quotes are enclosed in double quotes, adjust if needed
            quote = line.strip().strip('"')  # Remove leading/trailing spaces and quotes
            if quote:  # Skip empty lines
                quotes.append({"quotes": quote})

    if convert_to_json:
        formatted_json = json.dumps(quotes, indent=4)
        with open("reformatted_quotes_Shawshank.json", "w") as file:
            file.write(formatted_json)

    return quotes

# Example usage:
quotes = process_quotes_from_text("test.txt")  # Read quotes from text file
print(quotes)  # Print the extracted quotes

# If you want to convert them to JSON:
process_quotes_from_text("test.txt", convert_to_json=True)  # Save as JSON
