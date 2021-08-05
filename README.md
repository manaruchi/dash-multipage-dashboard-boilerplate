# Multipage Dashboard App using Plotly Dash

This repository contains the source code files to make a multipage dashboard app as shown below. The app has been created using Plotly Dash framework and is written in Python. This boilerplate code is free to use and free to distribute. (Acknowledging this repository will always be appreciated but not necessary to do so. ;-))

<img src="https://github.com/manaruchi/dash-multipage-dashboard-boilerplate/raw/main/app.gif" style="zoom:80%;" />

## Running the App

Make sure you have installed Python 3.x and have pip available. You have to install the following python libraries.

```
dash==1.20.0
dash_bootstrap_components==0.10.7
```

A Requirements.txt file is added in this repository. You can install all the required libraries from the file using, 

```bash
pip install -r requirements.txt
```

Then simply run the app using,

```bash
python app.py
```



## Files Used

The main python script is in `app.py`. The images used in this app are saved in base64 string in `figures.py`. A great tool to convert your images to base64 string is https://codebeautify.org/image-to-base64-converter. The CSS files are in `assets` folder. 

> Alongside the required CSS files for the page, a CSS file to style the scrollbars of the page is available in assets folder called `scrollbar.css`. Also a CSS file `preloader.css` file contains CSS styling to override the default 'Loading...' text in Dash with a cool spinner animation.



### Queries/Questions

Drop me a mail regarding questions/opinions/any random stuff at manaruchimohapatra@gmail.com. Also visit my page at https://manaruchi.github.io/. 

