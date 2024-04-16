# Experimental-Flights-Video-Streaming
Clone this repo on your local machine.

You will need to create a python virtual environment for this. You can do so by running this command in the root directory of the repo:
python -m venv NAME_OF_VIRTUAL_ENVIRONMENT

Usually, you would use some name like .venv for your virtual environment

Then, in order to run your virtual environment, navigate to the Scripts directory inside the virtual environment and run the activate.bat file to activate the virtual environment. This will make it so that the version of python and packages are those in the virtual environment itself. (If you're curious as to how this works, the Scripts directory has its own pip.exe and python.exe files, which are local to the venv. So when you activate the venv, you are telling the terminal to use those versions of pip and python.)

Then, to install the required packages, once you have activated the venv, navigate to the root directory of the repo again. There, you should see a requirements.txt file. Run this command:

pip3 install -r ./requirements.txt

This will install all the packages listed in the requirements.txt file.

After you do this, to actually run the code, navigate into the Files directory. Since setting up a socket requires 2 "machines"/endpoints, you want to run the sender.py file and server.py with separate terminals (they should be separate processes) or by running them on isolated machines. 

You can just run:
python server.py
python sender.py

for the respective files.
