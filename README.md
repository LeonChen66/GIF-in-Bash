# GIF-in-Bash
### Present GIF in Bash

#### Demo

##### Run " python GIF_bash.py -f 'GIF/sim.gif' " in bash
##### &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;GIF in bash     &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Original GIF
<p align="center"> 
    <img src="https://i.imgur.com/QaXuaUF.gif" width="200" height="200">
        <img src="https://media.tenor.com/images/0a1652de311806ce55820a7115993853/tenor.gif">
</p>

#### There are 3 parameters to set.
###### -s set GIF size (default = 54)
###### -t set threshold (0~255) (default = 128)
###### -q set frequency (default = 0.2 sec)

(1) Size of the images (GIF). The image is needed to be resized in order to show in bash.

(2) Threshold. The color are transformed from RGB (2^24 colors) to 8 colors (Colors in bash). As shown in the following figure, we have to determine the edge properly.

<p align="center"> 
    <img src="https://github.com/LeonChen66/GIF-in-Bash/blob/master/images/colors.png?raw=true">
</p>

(3) Frequency between each frame. 

