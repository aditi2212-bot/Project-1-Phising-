import json
from datetime import datetime
import dateutil.parser

def convert_format_1(time_str):
    """Convert ISO time string to timestamp using datetime.strptime (data-1 logic)."""
    date = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    timestamp = (date - datetime(1970, 1, 1)).total_seconds() * 1000
    return int(timestamp)

def convert_format_2(time_str):
    """Convert ISO time string to timestamp using dateutil.parser (data-2 logic)."""
    parsed_time = dateutil.parser.parse(time_str)
    timestamp = parsed_time.timestamp() * 1000
    return int(timestamp)

def convert_to_unified_format(time_str):
    """Convert any ISO timestamp to target unified format."""
    # Using Python 3.11+ fromisoformat won't work directly with 'Z'
    if time_str.endswith("Z"):
        time_str = time_str.replace("Z", "+00:00")  # Convert to offset format

    s_since_epoch = datetime.fromisoformat(time_str).timestamp()
    ms_since_epoch = int(s_since_epoch * 1000)

    return {
        "timestamp": ms_since_epoch
    }

if __name__ == "__main__":
    # Example ISO timestamp string (same in all formats)
    time_input = "2020-02-25T00:02:43.000Z"

    # Apply the transformations
    result_format_1 = convert_format_1(time_input)
    result_format_2 = convert_format_2(time_input)
    result_target = convert_to_unified_format(time_input)

    # Save all three to files for comparison
    with open("result-data-1.json", "w") as f1:
        json.dump({"timestamp": result_format_1}, f1, indent=2)

    with open("result-data-2.json", "w") as f2:
        json.dump({"timestamp": result_format_2}, f2, indent=2)

    with open("data-result.json", "w") as f3:
        json.dump(result_target, f3, indent=2)

    print("All timestamps converted and saved successfully.")

