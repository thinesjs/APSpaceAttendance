
# APSpaceAttendance

A automation script to automatically scan and update attendance. The program is purely for educational purposes and real usage is not recommended.
Supports Windows and Mac OS X.


## Prerequisites

Install dependencies.

```python
pip install -r requirements.txt
```
or
```python
pip3 install -r requirements.txt
```

Add your APSpace credentials in config.ini.

```
[APKEY]
APKey: tp000000
APKeyPassword: Tp000000@1234
```


## Usage

Run the program and follow the onscreen instructions.

```bash
py run.py
```
or
```bash
python3 run.py
```
## How to Use

The programs needs to be running and Microsoft Teams needs to be open and visible in the foreground. 
The program will not detect the attendance QR if Microsoft Teams is minimised or hidden behind other application.

#### Code Fetching
The lecturer has to share their screen which displays a QR code. If ONLY the 3 digit code is displayed WITHOUT the QR code or the QR code is not FULLY visible on screen, the program will not update the attendance. The program does not scan for 'digits' but only QR codes. 

#### Disable timeout or sleep
Disable screen timeouts or sleep due to inactivity because the script will stop working if the computer goes to sleep or hibernation.

#### Increased Battery Consumption
Setting a lower RETRY_INTERVAL in config.ini may increase battery and memory consumption and plugging in is recommended if applicable.

#### Auto Shutdown
The program can be configured to automatically shut down the system after successfully updating the attendance by changing ON_COMPLETION to shutdown.

```
ON_COMPLETION : shutdown
```
Any unsaved or open applications will be forcefully closed and will not be saved. Make sure to save any word documents or important applications to avoid file corruptions.
