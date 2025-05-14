# Disclaimer
**Use at Your Own Risk** – These scripts are provided without warranties and are intended for informational and experimental use only. The author assumes no responsibility for any issues, including but not limited to errors, data loss, security risks, or unintended consequences resulting from their use. Users should exercise due diligence, test thoroughly, and ensure compatibility with their own environments before implementation.

### Prerequisites
1. Desktop version 16 Microsoft Outlook with enabled COM object. ([Download here](https://usps365.sharepoint.com/:u:/r/sites/PPCOnboardingTool/Shared%20Documents/General/Misc_))
2. JDK 17
3. Python 3
4. Win32 COM Python library (pip install pywin32)
5. Windows Environment ONLY

## Summary of extractPasscode.py
This Python script retrieves a one-time passcode (OTP) from the latest email in Classic Outlook via COM object if it matches the subject "[EXTERNAL] USPS.com Multifactor Authentication".

* Connects to Outlook via win32com.client to access the inbox.
* Retrieves and sorts emails by received time, extracting the latest one.
* Checks if the subject contains "USPS.com Multifactor Authentication."
* If matched, uses regex to find the passcode in the email body and returns it as a string.
* If no match or passcode is not found, returns descriptive error messages.

### Usage
```
python extractPasscode.py
```

## Summary of extractValidationLink.py
This Python script retrieves a validation link from the latest email in Classic Outlook via COM object if it matches the subject "Validate Your Email to Complete Your USPS Online Account".

* Connects to Outlook via win32com.client to access the inbox.
* Retrieves and sorts emails by received time, extracting the latest one.
* Checks if the subject matches "Validate Your Email to Complete Your USPS Online Account."
* If matched, uses regex to find the validation link in the email body and returns it as a string.
* If no match or validation link is not found, returns descriptive error messages.

### Usage
```
python extractValidationLink.py
```
   
## Summary of App.java
This Java example demonstrates how to invoke the extractPasscode.py script from within Java code.

* Executes the Python script using Runtime.getRuntime().exec().
* Captures and prints the script's output line-by-line.
* Waits for the process to complete and checks its exit code.
* Handles errors and exceptions with a try-catch block.

## Build and Run

1. Clone the project
   ```
   git clone https://github.com/kent-cheung-usps/myUITestTool.git
   ```
2. Build the java example
   ```
   mvn clean install
   ```
3. Run the java example
   ```
   java -jar target/demo-1.0-SNAPSHOT-jar-with-dependencies.jar
   ```
