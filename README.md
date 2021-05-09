# ScreenPen

## Description

Screen annotation software which allows drawing directly on the screen. It is a free and multiplatform (all systems that support Python) alternative for tools such as Epic Pen. Supported shapes:
* line,
* rectangle,
* chart (using matplotlib).

The behavior of he programs depends on the OS you use:
* For Linux transparent background is used (you can see a video playing in the background).
* For Windows, the screenshot is taken, and the user draws on the captured image (you see a static image of the screen).

### Controls
* Left mouse button - drawing.
* Right mouse button - quit.
* Keyboard shortcuts:
    * `Ctrl+Z` - undo,
    * `Ctrl+Y` - redo,
    * hold `Shift` - change mouse cursor icon to arrrow.

### Demo (video)

https://user-images.githubusercontent.com/19404835/116938635-5e63a980-ac6b-11eb-818d-7723967e1d94.mp4?s=100


*Note: The app is created ad-hoc only for my use case. It may contain bugs, and the code definitely is not clean.*


## Usage

Tu run the program:

```bash
pip install screenpen
screenpen
```

