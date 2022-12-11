# Animated Heart using Qt with python and PyQt

My wife and I watched the Lighter & Princess (点燃我，温暖你) Chinese Drama in December of 2022. The show featured an ultra smart programmer, and he coded an animated heart (Episode 5 @ 31:43). My wife challenged me to replicate the animated heart. This is my attempt. I thought it would be fun to do it in Qt and Python.

This is my first Qt program, and I kind of hacked this together until it looked kind of similar.

I have to give credit to the following:

* [A javascript implementation](https://qqqqqcy.github.io/heart_beat/#) - I only took the colours from it. Implemented my own logic and algorithm.
* Used the third formula offered in this [article by Saanvi Gutta](https://blogs.lcps.org/academiesonline/2021/02/13/the-equation-of-the-heart/)

![Heart Formulaes](https://blogs.lcps.org/academiesonline/files/2021/02/new-hearts.jpg)

* Learned a lot about Qt Animation and PyQt5 from this [article by Salem Al Bream](https://www.pythonguis.com/tutorials/qpropertyanimation/)
* Learned how to draw on QPixmap and QPainter from this [article by Martin Fitzpatrick](https://www.pythonguis.com/tutorials/bitmap-graphics/)

Thanks to the above references, I was able to hack this together.

I tested on:

  * macOS Ventura
  * Ubuntu 22.04 LTS (Desktop)
  * Windows 10

# Installation
Use the following command line instructions on Ubuntu and macOS.

Use equivalents on Windows 10.

```
git clone https://github.com/kanglu/heart.git

cd heart

python3.10 -m venv env

source env/bin/activate

pip install -r requirements.txt

# If you are doing this on Linux or Ubuntu you may need to update your library dependencies
#
# sudo apt install '^libxcb.*-dev'

python ./heart.py

```
