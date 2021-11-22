# tinder_bot_edit
Editing a Tinder bot created by [@frederikme](https://github.com/frederikme)

## Table of Contents

- [Basic Swipe Usage](#basic-swipe-usage)


## Basic Swipe Usage
- Download the code as a zip or clone the repository from https://github.com/frederikme/TinderBotz
- Setup a [virtual environment](https://docs.python.org/3/library/venv.html) by writing `$ python -m venv \path\to\your\virtual\environment`
- Move the folders and files inside the **TinderBotz-Master** folder to the venv folder ![Imgur](https://imgur.com/ZDZMiHW.jpg)
- Activate the virtual environment `$ ./my_venv/Scripts/Activate.ps1` ![Imgur](https://imgur.com/WpKXp5p.jpg)<br>
*Note: I'm using PowerShell on Windows*
- Change directory into the venv `$ cd .\my_venv\` <br> ![Imgur](https://imgur.com/vjIJtzH.jpg)
- Download all required Python libraries by running `$ pip install -r requirements.txt` ![Imgur](https://imgur.com/JZpB56G.jpg)
- Log in to Tinder on Google Chrome then exit Chrome <br>
*Note: The script will open Chrome for you*
- Run my modified version of `quickstart.py` for the easiest start <br>
```python
from tinderbotz.session import Session

if __name__ == "__main__":
    session = Session()                              # Instance of the Session Class                
    session.like(amount=25, ratio="84.5%", sleep=3)  # Edit these arguments to your liking
```
*Note: For more functionality, please read Frederik's GitHub repository* <br>
- Once the script has finished, the stats should appear on your terminal and Chrome will be closed <br> ![Imgur](https://imgur.com/w6HWVpV.jpg) <br>
- To get out of the virtual environment, run `$ deactivate` <br> ![Imgur](https://imgur.com/6BTnak0.jpg) <br>
- **FYI** - This function is called on exit of the script <br> ![Imgur](https://imgur.com/WmzBaMr.jpg)
