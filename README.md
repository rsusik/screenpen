# Simple pen

## Description

Super simple screen annotation software which allows drawing:
* line,
* rectangle,
* charts (using matplotlib).

Right mouse click stops the program.

The application allows writing directly on the screen.
* For Linux transparent background is used.
* For Windows, the screenshot is taken, and the user draws on the captured image.

Screenshot:

<img src="screenshot_1.png" height="300px" />

*Note: The app is created ad-hoc only for my use case. It may contain bugs, and the code definitely is not clean.*

## Usage

Tu run the program:

### Pip

```bash
pip install -r requirements.txt
python screenpen.pyw
```

### Conda

Once virtual env is activated:
```bash
conda install --file requirements.txt
python screenpen.pyw
```
