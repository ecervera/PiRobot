# PiRobot Notebooks

Examples and exercises for a mobile robot built with Lego components,
and controlled by a [Raspberry Pi](https://www.raspberrypi.org/) + [BrickPi interface board](https://www.dexterindustries.com/brickpi/).

The code consists of [Jupyter notebooks](http://jupyter.org/) 
running in a laptop or desktop computer, 
which communicates with the robots via WiFi.

## Prerequisites

See [BrickPi Tutorials and Documentation](https://www.dexterindustries.com/brickpi3-tutorials-documentation/).

### OpenCV

`cd ~/Desktop/BrickPi+/Software/BrickPi_Python/Project/openCV
sudo ./install.sh`

### Jupyter

`pip install --user --upgrade pip
sudo pip install jupyter`

## Usage

In the Raspberry, launch:

`jupyter notebook --NotebookApp.token= --no-browser --ip=’*’`

In the computer, open your favourite browser and connect to the URL:

`http://<IP of your robot>:8888`
