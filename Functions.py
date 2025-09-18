
import json
import os
import re


# Define prompt function
def response_func (llm, model, prompt,instructions, reasoning_effort, reasoning_summary):
    response = llm.responses.create(
        input = prompt,
        model = model,
        instructions = instructions,
        reasoning={
            "effort": reasoning_effort,
            "summary": reasoning_summary
        }
    )
    return response

# Build instructions function
# Note to LXD: We can extend the list of instructions we want to give with our prompt 

def build_instructions(role, context):
    instructions = [
    "ROLE", f"- {role}",
    "\nCONTEXT", *[f"- {g}" for g in context]
    ]
    return "\n".join(instructions)


#function to get the next serial number from a json file
def get_next_serial(file_name: str) -> str:
    """
    Returns the next ID from a JSON file in the same directory.
    - If IDs have a prefix (e.g. "TC-5"), it preserves the prefix.
    - If IDs are numeric (e.g. "5"), returns the next number.
    - If the file is empty or contains an empty list, returns "1".
    """
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    # Handle empty file
    if os.path.getsize(file_path) == 0:
        return "1"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:  # empty JSON list
        return "1"

    ids = []
    for item in data:
        raw_id = str(item.get("id", ""))
        match = re.match(r"^([^\d]*)(\d+)$", raw_id)  # prefix + number
        if match:
            prefix, number = match.groups()
            width = len(number)               
            ids.append((prefix, int(number), width)) 

    if not ids:  # no valid IDs found
        return "1"

    # Find prefix/number with the largest numeric value
    prefix, max_num, width = max(ids, key=lambda x: x[1])
    next_num = str(max_num + 1).zfill(width)      #preserve zero padding
    return f"{prefix}{next_num}"      

