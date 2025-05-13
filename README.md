# myUITestTool
Quick RAD Tools: Design and execute specific in Windows Environment.

## Summary of extractPasscode.py
This Python script retrieves a one-time passcode (OTP) from the latest email in Classic Outlook via COM object if it matches the subject "[EXTERNAL] USPS.com Multifactor Authentication".

* Connects to Outlook via win32com.client to access the inbox.
* Retrieves and sorts emails by time, extracting the latest one.
* Uses regex to find the passcode in the email body and returns it as a string.
* If no match, returns appropriate error messages.
* Prints the passcode if executed directly.

## Summary of App.java
This is Java example to embed the extractPasscode.py script and displays its output.

* Executes the Python script using Runtime.getRuntime().exec().
* Captures and prints the script's output line-by-line.
* Waits for the process to complete and checks its exit code.
* Handles errors and exceptions with a try-catch block.

## Build

1. Clone the project
   ```
   git clone https://github.com/kent-cheung-usps/myUITestTool.git
   ```
3. Build the java example
   ```
   mvn clean install
   ```
## Execute
### Prerequisities
1. Desktop version 16 Microsoft Outlook with enabled COM object.
2. JDK 17
3. Python 3
4. Windows Environment
### Run
```
java -jar target

## References:

* Download and install Microsoft Outlook Desktop Version 16.X https://usps365.sharepoint.com/:u:/r/sites/PPCOnboardingTool/Shared%20Documents/General/Misc_Tools/OfficeSetup.exe?csf=1&web=1&e=djkoKy
