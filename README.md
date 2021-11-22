# tinder_bot_edit
Editing a Tinder bot created by [@frederikme](https://github.com/frederikme)

## Steps for Using the Bot to Automatically Like `n` number of times
1. Download the code as a zip or clone the repository from https://github.com/frederikme/TinderBotz
2. Setup a [virtual environment](https://docs.python.org/3/library/venv.html) by writing `$ python -m venv \path\to\your\virtual\environment`
3. Move the folders and files inside the **TinderBotz-Master** folder to the venv folder ![Imgur](https://imgur.com/ZDZMiHW.jpg)
4. Activate the virtual environment `$ ./my_venv/Scripts/Activate.ps1` ![Imgur](https://imgur.com/WpKXp5p.jpg)<br>
*Note: I'm using PowerShell on Windows*
5. Change directory into the venv `$ cd .\my_venv\` <br> ![Imgur](https://imgur.com/vjIJtzH.jpg)
6. Download all required Python libraries by running `$ pip install -r requirements.txt` ![Imgur](https://imgur.com/JZpB56G.jpg)
7. Log in to Tinder on Google Chrome then exit Chrome <br>
*Note: The script will open Chrome for you*
9. Run my modified version of `quickstart.py` for the easiest start <br>
*Note: For more functionality, please read Frederik's GitHub repository*
9. Once the script has finished, the stats should appear on your terminal and Chrome will be closed <br> ![Imgur](https://imgur.com/w6HWVpV.jpg)
10. To get out of the virtual environment, run `$ deactivate` <br> ![Imgur](https://imgur.com/6BTnak0.jpg)
11. **FYI** - This function is called on exit of the script <br> ![Imgur](https://imgur.com/WmzBaMr.jpg)
