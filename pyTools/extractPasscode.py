import re
import win32com.client

def get_passcode():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 refers to the Inbox folder
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)  # Sort by received time in descending order
    latest_message = messages.GetFirst()  # Get the most recent email

    # Check if the subject matches "USPS.com Multifactor Authentication"
    if latest_message.Subject == "[EXTERNAL] USPS.com Multifactor Authentication":
        body = latest_message.Body

        # Use regex to extract the passcode
        match = re.search(r"one-time passcode:\s*(\d+)", body, re.IGNORECASE)
        if match:
            return match.group(1)  # Return the extracted passcode
        else:
            return "Passcode not found in the email body."
    else:
        return "The latest email does not match the expected subject line."

# If this script is run directly, print the passcode
if __name__ == "__main__":
    print(get_passcode())