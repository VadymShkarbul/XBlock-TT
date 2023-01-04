# XBlock Test Task
### XBlock module for the Open edX platform, which will display HTML content in the form of a collapsible block which, upon clicking on the title, will reveal the main content animatedly.
## Installation
#### Clone repository:
```
git clone https://github.com/VadymShkarbul/XBlock-TT.git
cd XBlock-TT
```
#### Create and activate virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
#### Clone the XBlock-SDK:
```
git clone https://github.com/openedx/xblock-sdk.git
```
#### Change directory to SDK directory and install requirements:
```
cd xblock-sdk
pip install -r requirements/base.txt
```
#### Return to project root directory and install newblock:
```
cd ..
pip3 install -e newblock
```
#### Run migration and local server (Note that you should be in sdk-dir):
```
cd xblock-sdk
python3 manage.py migrate
python3 manage.py runserver
```
