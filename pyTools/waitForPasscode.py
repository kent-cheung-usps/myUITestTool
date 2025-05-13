import re
import win32com.client
import pythoncom

class OutlookEventHandler:
    def __init__(self):
        self.passcode = None

    def OnNewMailEx(self, EntryIDCollection):
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        for entry_id in EntryIDCollection.split(','):
            mail_item = outlook.GetItemFromID(entry_id)
            
            # Check if the subject matches "USPS.com Multifactor Authentication"
            if mail_item.Subject == "[EXTERNAL] USPS.com Multifactor Authentication":
                body = mail_item.Body

                # Use regex to extract the passcode
                match = re.search(r"one-time passcode:\s*(\d+)", body, re.IGNORECASE)
                if match:
                    return match.group(1)  # Return the extracted passcode
                else:
                    return "Passcode not found in the email body."
            else:
                return "The latest email does not match the expected subject line."

def wait_for_passcode():
    outlook = win32com.client.DispatchWithEvents("Outlook.Application", OutlookEventHandler)
    print("Waiting for new email...")
    pythoncom.PumpMessages()  # Keeps the script running to listen for new emails

if __name__ == "__main__":
    wait_for_passcode()

