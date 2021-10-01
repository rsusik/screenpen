<p align="center">
    <img src="https://github.com/rsusik/screenpen/raw/master/screenpen.png" alt="ScreenPen" />
</p>
<p align="center">
    <em>Multiplatform screen annotation software that allows drawing directly on the screen.</em>
</p>
<p align="center">
<a href="https://pypi.org/project/screenpen" target="_blank">
    <img src="https://img.shields.io/pypi/v/screenpen?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://github.com/rsusik/screenpen/blob/master/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/rsusik/screenpen" alt="License">
</a>
<a href="https://pepy.tech/project/screenpen" target="_blank">
    <img src="https://static.pepy.tech/personalized-badge/screenpen?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads" alt="Number of downloads">
</a>
<a href="https://pepy.tech/project/screenpen" target="_blank">
    <img src="https://static.pepy.tech/personalized-badge/screenpen?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads/month">
</a>
</p>

## Description

Screen annotation software which allows drawing directly on the screen. 
It is an open source and multiplatform 
(all systems that support Python) 
alternative to tools such as Epic Pen. 
Supported shapes:
* line,
* rectangle,
* chart (using matplotlib).

The behavior of the program depends on the OS you use:
* in Linux, a transparent background is used (you can see a video playing in the background),
* and in Windows, the screenshot is taken, and the user draws on the captured image (you see a static image of the screen).



### Demo (video)

https://user-images.githubusercontent.com/19404835/130215780-705e4eb9-330b-4a91-bd1f-b9ec3843556e.mp4


*Note: The app is created ad-hoc only for my use case. It may contain bugs, and the code definitely is not clean.*


## Usage

### Installation and execution

Tu run the program you need to have Python installed and execute following:

```bash
pip install screenpen
screenpen                # or python -m screenpen
```

### Controls
* Left mouse button - drawing.
* Right mouse button - quit.
* Keyboard shortcuts:
    * `Ctrl+Z` - undo,
    * `Ctrl+Y` - redo,
    * hold `Shift` - change mouse cursor icon to arrrow.

### TODO

- [ ] Better Matplotlib charts support.
