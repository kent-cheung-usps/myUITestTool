# myUITestTool
Quick RAD Tools: Design and execute specific in Windows Environment.

## Summary of extractPasscode.py
This Python script retrieves a one-time passcode (OTP) from the latest email in Classic Outlook via COM object if it matches the subject "[EXTERNAL] USPS.com Multifactor Authentication".

* Connects to Outlook via win32com.client to access the inbox.
* Retrieves and sorts emails by received time, extracting the latest one.
* Checks if the subject matches "[EXTERNAL] USPS.com Multifactor Authentication."
* If matched, uses regex to find the passcode in the email body and returns it as a string.
* If no match or passcode is not found, returns descriptive error messages.

### Prerequisites
1. Desktop version 16 Microsoft Outlook with enabled COM object. ([Download here](https://usps365.sharepoint.com/:u:/r/sites/PPCOnboardingTool/Shared%20Documents/General/Misc_))
2. JDK 17
3. Python 3
4. Win32 COM Python library (pip install pywin32)
5. Windows Environment ONLY

### Usage
```
python extractPasscode.py
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
