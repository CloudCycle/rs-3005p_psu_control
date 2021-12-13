:: Create the virtual environment for Python 3.8 and install all the requirements
py -3.8 -m venv .venv
.\.venv\Scripts\pip3 install --upgrade pip
.\.venv\Scripts\pip3 install -r .\requirements.txt
echo Press key to open Visual Studio Code
timeout /t 30
code .
