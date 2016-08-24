## AgInsight Python-Selenium-SauceLabs Testing Framework
This is the testing framework for AgInsight. It uses Python, Selenium and SauceLabs to run a set of automated UI tests in multiple OS/Browser combinations.

You must have an account in SauceLabs to be able to run these tests. Please contact the Esri Australia Adelaide office for more information.

### Environment Setup - This needs to be completed before running tests.

1. Global Dependencies
    * [Install Python](https://www.python.org/downloads/)
    * Or Install Python with [Homebrew](http://brew.sh/)
    ```
    $ brew install python
    ```
    * Install [pip](https://pip.pypa.io/en/stable/installing/) for package installation

2. Sauce Credentials
    * In the terminal export your Sauce Labs Credentials as environmental variables:
    ```
    $ export SAUCE_USERNAME=<your Sauce Labs username>
    ```
    ```
	$ export SAUCE_ACCESS_KEY=<your Sauce Labs access key>
    ```
3. Project
	* The recommended way to run your tests would be in [virtualenv](https://virtualenv.readthedocs.org/en/latest/). It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.
	```$ pip install virtualenv```
	* Create a virtual environment in your project folder the environment name is arbitrary. You can setup a virtual env in the testFramework folder on your machine, it will not be tracked in source control.
	```$ virtualenv venv```
	* Activate the environment:
	```$ source venv/bin/activate```
	or in Windows, in cmd run the activate.bat file inside the venv/Scripts folder:
	```> venv\Scripts\activate```
	* Install the required packages:
	```$ pip install -r requirements.txt```

### Running Tests:  -n option designates number of parallel tests and -s to disable output capture. On Windows, tests can be run by typing the command below into the cmd window.

Tests in Parallel, note our SauceLabs account only has 2 parallel VMs available:
```$ py.test -s -n 2 tests```

The above command will run all tests inside the tests folder and for each browser combination.

### Notes:

* If py.test is not working, you may need to remove the venv folder and start the whole setup process again.
* If you get errors about .pyc files, remove all .pyc files in the testing folders, including the __pycache__ folder.

[Sauce Labs Dashboard](https://saucelabs.com/beta/dashboard/)

### Kown Issues:
* Test output will be captured in .testlog files as the pytest-xdist plugin has issues with not capturing stdout and stderr. You can use the following commands to output session id's for CI integration and clean up.
```
$ cat *.testlog
$ rm -rf *.testlog
```
