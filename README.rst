MoonRock
========

MoonRock is a Selenium based web automation testing framework.

Install
-------

pip install -r requirements.txt

To run MoonRock, we provide a fully functional website made with Flask that MoonRock will use for testing. To use MoonRock with this test site, you will need to open two terminals, one for the server of this website and another to run the tests.


Selenium driver
---------------

Download the driver for your Chrome version from https://chromedriver.chromium.org/downloads
Unzip the file, store it in a folder and remember the path, will be used in the next step.
You will need a file called config.py, a sample one is provided, you can mv the sample to config.py:

$ mv localconfig.py.SAMPLE config.py

And edit this file and modify the DRIVER_PATH variable with the path where the Selenium webdriver is installed.


Running the local site
----------------------

Go to the directory of index.py file (in your_installation/moonrock/moonrock/sites/localhost/)

Activate your virtualenv

export FLASK_APP=index.py

(moonrock) $ flask run

Running the tests
-----------------

pytest tests.py