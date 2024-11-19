from plyer import notification
from datetime import datetime

def notfiy_user(is_successful: bool):
    if is_successful:
        notification.notify(
            title="Screenshots organizer",
            message="Screenshot was taken successfully",
            timeout=1
        )
        return
    
    notification.notify(
        title="Screenshots organizer",
        message="Screenshot was not taken becuase of an error, the error can be found in logs",
        timeout=1

    )
   
def format_window_title(window_title: str, root_app_name: str):
    window_title = window_title.replace(root_app_name, "").replace("-", "").strip()

    invalid_chars = '<>:"/\\|?*'
    new_title = window_title[0] if window_title[0] not in invalid_chars else ""

    for i in range(1, len(window_title)):
        if window_title[i] not in invalid_chars and window_title[i] != " ":
            new_title += window_title[i]
        
        if window_title[i] == " " and new_title[-1] != " ":
            new_title += " "

    return new_title


def write_to_logs(error):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    error_template = f"""
-------------------- {formatted_datetime} --------------------

{error}

-------------------- [END OF THIS ERROR] --------------------
"""

    with open("./logs.txt", "a") as logs:
        logs.write(error_template)

