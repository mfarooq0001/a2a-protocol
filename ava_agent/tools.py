# Tools for Ava's scheduling agent

# Dummy data representing Ava's availability
AVA_AVAILABILITY = {
    "2026-02-03": "Available from 9:00 AM to 11:00 AM",
    "2026-02-04": "Available from 2:00 PM to 5:00 PM",
    "2026-02-05": "Available all morning (8:30 AM – 12:00 PM)",
    "2026-02-06": "Busy all day",
    "2026-02-07": "Available from 10:00 AM to 1:00 PM",
}

def check_ava_availability(date_str: str) -> dict[str, str]:
    """Check Ava's availability for a given date.

    Args:
        date_str (str): The date to check in 'YYYY-MM-DD' format.
    
    Returns:
        dict[str, str]: A dictionary with the date and Ava's availability.
    """

    if not date_str:
        return {"status": "error": "No date provided."}

    availability = AVA_AVAILABILITY.get(date_str)

    if availability:
        return {
            "status": "success",
            "message": f"Ava's availability on {date_str}: {availability}"
        }
    
    return {
        "status": "input_required",
        "message": f"No availability information found for {date_str}. Please provide a different date."
    }