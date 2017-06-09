# PiRobot Notebooks

Examples and exercises for a mobile robot built with Lego components,
and controlled by a [Raspberry Pi](https://www.raspberrypi.org/) + [BrickPi interface board](https://www.dexterindustries.com/brickpi/).

The code consists of [Jupyter notebooks](http://jupyter.org/) 
running in a laptop or desktop computer, 
which communicates with the robots via WiFi.

## Prerequisites

See [BrickPi Tutorials and Documentation](https://www.dexterindustries.com/brickpi3-tutorials-documentation/).

### OpenCV

`cd ~/Desktop/BrickPi+/Software/BrickPi_Python/Project/openCV`

`sudo ./install.sh`

### Jupyter

`pip install --user --upgrade pip`

`sudo pip install jupyter`

## Usage

In the Raspberry, launch:

`jupyter notebook --NotebookApp.token= --no-browser --ip=’*’`

In the computer, open your favourite browser and connect to the URL:

`http://<IP of your robot>:8888`

## Try-a-Bot: an open source guide for robot programming

Developed by:
[![Robotic Intelligence Lab @ UJI](img/logo/robinlab.png "Robotic Intelligence Lab @ UJI")](http://robinlab.uji.es)

Sponsored by:
<table>
<tr>
<td style="border:1px solid #ffffff ;"><a href="http://www.ieee-ras.org"><img src="img/logo/ras.png"></a></td>
<td style="border:1px solid #ffffff ;"><a href="http://www.cyberbotics.com"><img src="img/logo/cyberbotics.png"></a></td>
<td style="border:1px solid #ffffff ;"><a href="http://www.theconstructsim.com"><img src="img/logo/theconstruct.png"></a></td>
</tr>
</table>

Follow us:
<table>
<tr>
<td style="border:1px solid #ffffff ;"><a href="https://www.facebook.com/RobotProgrammingNetwork"><img src="img/logo/facebook.png"></a></td>
<td style="border:1px solid #ffffff ;"><a href="https://www.youtube.com/user/robotprogrammingnet"><img src="img/logo/youtube.png"></a></td>
</tr>
</table>
