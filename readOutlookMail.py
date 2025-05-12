import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # 6 refers to the Inbox folder
messages = inbox.Items
messages.Sort("[ReceivedTime]", True)  # Sort by received time in descending order
latest_message = messages.GetFirst()  # Get the most recent email

print(latest_message.Subject)
print(latest_message.Body)
