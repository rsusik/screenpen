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

The behavior of the program depends on the Window System you use:
* if the system supports "live transparency then a transparent background is used (you can see a video playing in the background),
* if not then the screenshot is taken, and the user draws on the captured image (you see a static image of the screen),
* sometimes your WM may be detected as not supporting "live transparency". In that case try running with `-t` parameter to force it._


### Demo (video)

https://user-images.githubusercontent.com/19404835/130215780-705e4eb9-330b-4a91-bd1f-b9ec3843556e.mp4


*Note: The app is created ad-hoc only for my use case. It may contain bugs...*


## Usage

### Installation and execution

Tu run the program you need to have Python installed and execute following:

```bash
pip install screenpen
screenpen                # or python -m screenpen
```

**NOTE: Your WM may be detected as not supporting "live transparency". In that case try running with `-t` parameter:**

```bash
screenpen -t
```

### Controls
* Left mouse button - drawing.
* Right mouse button - quit.
* Keyboard shortcuts:
    * `Ctrl+Z` - undo,
    * `Ctrl+Y` - redo,
    * hold `Shift` - change mouse cursor icon to arrrow.


### Configuration
There are a few configuration options that can be set using config file:
* `icon_size` - size of the icons (default: 50)
* `hidden_menus` - to hide menus on start (default: False)

The config should look like below:
```ini
[screenpen]
; Possible values for areas: topToolBarArea, bottomToolBarArea, leftToolBarArea, rightToolBarArea
penbar_area = topToolBarArea
boardbar_area = topToolBarArea
actionbar_area = leftToolBarArea
hidden_menus = False
icon_size = 50
sc_undo = Ctrl+Z
sc_redo = Ctrl+Y
sc_toggle_menus = Ctrl+1
exit_mouse_button = right
exit_shortcut = Escape
drawing_history = 500
```
(more options will be added in the future...)

### TODO

- [ ] Better Matplotlib charts support.
- [ ] Better wayland support.
- [ ] Add "paste image" feature.
- [ ] Add ellipse shape.
- [ ] Keyboard shortcuts for changing colors.

### Compatilibity notes

Screenpen (from 0.2 version) is compatible with PyQt5 and PyQt6, nevertheless the PyQt5 is currently in the requirements and recommended.
It is possible to run it using PyQt6 by running:
```
pip install matplotlib>=3.2 numpy>=1.8 PyQt6
pip install screenpen --no-deps
```

### Wayland support

Screenpen works in some Wayland compositors, but it is not perfect.
There are issues with windows positioning and transparency.
In case the window opens on wrong monitor (which I noticed on Sway WM) you can move it using `Win+Shift+Arrows` (or `Alt+Shift+Arrows`) shortcuts to a desired monitor.
I have no plans to fix it in near future, but I will accept PRs.
