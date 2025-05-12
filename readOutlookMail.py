import re
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # 6 refers to the Inbox folder
messages = inbox.Items
messages.Sort("[ReceivedTime]", True)  # Sort by received time in descending order
latest_message = messages.GetFirst()  # Get the most recent email

print(latest_message.Subject)
# print(latest_message.Body)

# Check if the subject matches "USPS.com Multifactor Authentication"
if latest_message.Subject == "[EXTERNAL] USPS.com Multifactor Authentication":
    body = latest_message.Body


    # Use regex to extract the passcode
    match = re.search(r"one-time passcode:\s*(\d+)", body, re.IGNORECASE)
    if match:
        passcode = match.group(1)
        print(f"Extracted Passcode: {passcode}")
    else:
        print("Passcode not found in the email body.")
else:
    print("The latest email does not match the expected subject line.")
