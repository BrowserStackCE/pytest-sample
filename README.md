# Python-Pytest-Selenium


## Prerequisites

1. Install pip and python.

```
sudo apt install python-pip
sudo apt install python
```

2. The recommended way to run your tests would be in virtualenv. It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.

```
pip install virtualenv
```

## Steps to Run your First Test

Step 1. Clone the Python-Pytest-Selenium Repository.
git@github.com:BrowserStackCE/pytest-sample.git


Step 2. Next we create and Activate the virtual environment in the Python-Pytest-Selenium folder.

For Linux/MacOS
```
virtualenv venv
source venv/bin/activate
```

For Windows
```
python -m virtualenv venv
venv\Scripts\activate.bat
```

Step 3. Then install required packages.

```
pip install -r requirements.txt
```

Step 4. Inside Python-Pytest-Selenium folder, export the Browserstack Credentials. You can get these from your automation dashboard.

<p align="center">
   <b>For Linux/macOS:</b>
   
```
export BROWSERSTACK_USERNAME="YOUR_USERNAME"
export BROWSERSTACK_ACCESS_KEY="YOUR ACCESS KEY"
```
<p align="center">
   <b>For Windows:</b>
   
```
set BROWSERSTACK_USERNAME="YOUR_USERNAME"
set BROWSERSTACK_ACCESS_KEY="YOUR ACCESS KEY"
```
   
Step 5. To run your first test from the root folder
```
pytest ./tests/single.py

Step 6. To run the tests in parallel
install xdist using below command 
pip3 install pytest-xdist
execute the testcases using below command mentioning the no. of parallel threads.
pytest ./tests/parallel.py -s -v -n=no. of parallel threads
```

