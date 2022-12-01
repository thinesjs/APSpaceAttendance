
# APSpaceAttendance

A automation script to automatically scan and update attendance. The program is purely for educational purposes and real usage is not recommended.


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

```json
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

#### Disable timeout or sleep
Disable screen timeouts or sleep due to inactivity because the script will stop working if the computer goes to sleep or hibernation.

#### Increased Battery Consumption
Setting a lower RETRY_INTERVAL in config.ini may increase battery and memory consumption and plugging in is recommended if applicable.

