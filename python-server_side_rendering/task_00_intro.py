import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            val = attendee.get(key)
            replacement = str(val) if val is not None else "N/A"
            
            processed_template = processed_template.replace(f"{{{key}}}", replacement)

        filename = f"output_{index}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
