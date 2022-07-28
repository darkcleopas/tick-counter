# tick-counter

Ticks are parasitic arachnids that may be harm some animals, like dairy cattle, horses and so on. Acaricides are used to handle with its infestation.
They are pesticides that kill members of the arachnid subclass Acari, which includes ticks and mites. 

To check the acaricide efficiency, it was take a sample of tick over a paper and apply the product. After a while, it was count the dead and live ticks to get the acaricide accuracy.
This process may turn on a manually and boring task. 

Thus, this project uses Image Processing with Python and OpenCV to count the number of ticks in a video and get the acaricide accuracy by identifying the live ticks (moving ticks).

The task of get acaricide accuracy was divided into two parts.

The first one is to get all the ticks given an image. To do this was used this methods in the image:
- Binary Threshold (50, 255) - to avoid noises;
- Canny (0, 50) - for edge detection;
- Dilation (1 iteration) - to connect the edges;
- findContours (RETR_EXTERNAL, CHAIN_APPROX_SIMPLE) - to get the image contours.


Original tick image            |  Found ticks
:-------------------------:|:-------------------------:
![](https://github.com/darkcleopas/tick-counter/blob/main/images/ticks-2.png)  |  ![](https://github.com/darkcleopas/tick-counter/blob/main/images/ticks-found.png)


The second part is to get a video frame and do some methods in order to get the live ticks. This is what was used for:
- Binary Threshold (80, 255) - to avoid noises;
- Background Subtractor MOG2 - to find a mask with not static pixels in the frame;
- findContours (RETR_EXTERNAL, CHAIN_APPROX_SIMPLE) - to get the mask contours.
