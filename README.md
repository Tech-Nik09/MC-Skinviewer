# MC - Skinviewer by Niklas Maroldt



## About this project
This is the repository for my minecraft skinviewer project.  
My Skinviewer app is a clean and easy to use  web-application which I made with just a few lines of [Python](https://www.python.org/) code and [Streamlit](https://streamlit.io/). After entering a valid minecraft gamertag, the app shows you the player's UUID and skin. By using the elements in the "Properties" section you are able to:
1. toggle the shadow casted by the player.
2. toggle the visibility of the player's cape.
3. toggle whether the second layer of the head should be shown.
4. toggle whether the second layer of the body should be shown.
5. rotate the skin to view it from a different perspective.

You can download the player's skin as a [64 x 64 px PNG image](https://de.minecraft.wiki/w/Skin#Overlays) to use it in minecraft. Additionally you can also downlad the current skin preview as a PNG image.



## Where can I find the Skinviewer app?
You can use the following links to open the app or to visit my Streamlit profile.
* [NM-Skinviewer app](https://nm-skinviewer.streamlit.app/)
* [My Streamlit profile](https://share.streamlit.io/user/tech-nik09)



## How does the app work?
Basically the app works by requesting information about the player (UUID and skin image) from the [public Mojang API](https://minecraft.wiki/w/Mojang_API).
To show the preview of the skin I decided to use the  [VZGE (SurgePlay Visage) API](https://vzge.me/). Everytime you enter another gamertag or change on of the settings in the "Properties" section, a new request is send to  VZGE. After recieving the API response form VZGE the image changes in the app.



## Requirements / Installation
Here you can find everything about how to install and run the app at your own system.
### 1. Make sure that Python 3.13.5 is installed:
* *Notice: Other versions of Python may also work but I just tried it with version 3.13.5!*
* Download and install Python from the [official website](https://www.python.org/).
* If you have Python already installed you can check the version with this command.
```
python --version
```
### 2. Clone the repository:
* Run the following command to clone the repository to the current directory of your local machine.
```
git clone https://github.com/Tech-Nik09/MC-Skinviewer.git
```
### 3. Create a virtuel environment (venv) inside the new directory:
* *Notice: Run all following commands inside the local repository `./MC-Skinviewer`*
* Run this command to create a new venv.
```
python -m venv .venv
```
* Then start the venv by executing the "activate" file (`./.venv/Scripts/activate`).
* If you are using bash, you could run this command. Otherwise see [THIS](https://docs.python.org/3/library/venv.html) documentation for help.
```bash
source ./.venv/Scripts/activate
```
### 4. Install all required Python packages:
* Install all required packages from the `requirements.txt` file by running this command.
```
pip install -r requirements.txt
```
### 5. Configure User-Agent header for [VZGE (SurgePlay Visage) API](https://vzge.me/)
* *Notice: The VZGE API now requires to use a custom User-Agent header. Otherwise all requests will fail with a 400 error. On thier website they say:*
> If your VZGE client is not using a custom UA, all requests to VZGE will now fail with a 400 error, returning a short explanatory text. You must ensure you use a reasonable User-Agent header in all requests to VZGE, preferably including a link to your website and your email address should you need to be contacted if you are misusing VZGE. An example of such a UA is MyProgramName/2.0 (+https://my.website/myprogramname.html; <me@my.website>).
* To set up your User-Agent you have to create a `secrets.toml` file inside the `.streamlit` directory.
* You can do it manually by pasting the following text into the `secrets.toml` file. Or by running the command given below.
* Please make sure to replace the URL and email address with your own.

Content of `secrets.toml`:
```toml
[VZGE]
user_agent = "MyProgramName/2.0 (+https://my.website/myprogramname.html; <me@my.website>)"
```
Bash command to create the `secrets.toml` file with its content
```bash
echo -e '[VZGE]\nuser_agent = "MyProgramName/2.0 (+https://my.website/myprogramname.html; <me@my.website>)"' > ./.streamlit/secrets.toml
```
### 6. Execute the application.
* *Notice: Every time before executing the app make sure that the venv is active!*
* Run the app with this command.
```
streamlit run ./skinviewer/app.py
```
* Now a new tab in your browser should open with the app.
* You can stop the app by closing the command prompt or by interrupting the process. (Mostly CRTL + C)



## Important / Notice
* Please do not spam rendering requests to the VZGE API.  
On thier website they say:
> I run VZGE for free! Please be respectful of that. If you're bulk-requesting renders, wait at least a second between subsequent requests.
* If you encounter any bugs please open an issue and report it.
* Feel also free to let me know your ideas about how I could improve the skinviewer app. (Please use the "discussion" section of this repository.)
