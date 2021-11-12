# manim_projects
### Overview:
Take the math I learn in classes and turn them into animations to help me visualize the concepts and gain a greater understanding. Also make math look cool and get me excited to learn new things (*"How can I show concept **X** in a video later?"*).
---
### Instillation (mac)
To install all required dependencies for installing Manim (namely: ffmpeg, Python, and some required Python packages), run:

`brew install py3cairo ffmpeg`

On Apple Silicon based machines (i.e., devices with the M1 chip or similar; if you are unsure which processor you have check by opening the Apple menu, select About This Mac and check the entry next to Chip), some additional dependencies are required, namely:

`brew install cmake pango scipy`

After all required dependencies are installed, simply run:

`pip3 install manim`

to install Manim.

### Instillation (windows)
Manim can be installed via Chocolatey simply by running:

`choco install manimce`

That’s it, no further steps required.

### Instillation (linux)

To first update your sources, and then install Cairo, Pango, and FFmpeg simply run:

`sudo apt update`

`sudo apt install libcairo2-dev libpango1.0-dev ffmpeg`

If you don’t have python3-pip installed, install it via:

`sudo apt install python3-pip`

Then, to install Manim, run:

`pip3 install manim`

---
# Running Files
Navigate to the manim_projects folder once you have cloned it and run the following command on the python `file.py` that the scene you want is in and using the class's `function name` to specificy which scene you want to run. ex:

`manim -pql main.py LinearTransform`
