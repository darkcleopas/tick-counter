# tick-counter

## Introduction

Ticks are parasitic arachnids that may be harm some animals, like dairy cattle, horses and so on. Acaricides are used to handle with its infestation.
They are pesticides that kill members of the arachnid subclass Acari, which includes ticks and mites. 

To check the acaricide efficiency, it was take a sample of tick over a paper and apply the product. After a while, it was count the dead and live ticks to get the acaricide accuracy. This process may turn on a manually and boring task. 

Thus, this project uses Image Processing with Python and OpenCV to count the number of ticks in a video and get the acaricide accuracy by identifying the live ticks (moving ticks).

## Methods

The task of get acaricide accuracy was divided into two parts.

### 1. Get the number of ticks in the image
To do this was used this methods in the image:
- Binary Threshold (50, 255) - to avoid noises;
- Canny (0, 50) - for edge detection;
- Dilation (1 iteration) - to connect the edges;
- findContours (RETR_EXTERNAL, CHAIN_APPROX_SIMPLE) - to get the image contours.

### 2. Get the live ticks given a video
This is what was used for:
- Binary Threshold (80, 255) - to avoid noises;
- Background Subtractor MOG2 - to find a mask with not static pixels in the frame;
- findContours (RETR_EXTERNAL, CHAIN_APPROX_SIMPLE) - to get the mask contours.

## Results

### 1. Number of ticks

<table>
  <tr>
    <td>Ticks</td>
    <td>Converted to gray</td>
  </tr>
  <tr>
    <td><img src="https://github.com/darkcleopas/tick-counter/blob/main/images/ticks-2.png"></td>
    <td><img src="https://github.com/darkcleopas/tick-counter/blob/main/images/ticks-gray.png"></td>
  </tr>
  <tr>
    <td>Applied Binary Threshold</td>
    <td>Canny algorithm</td>
  </tr>
  <tr>
    <td><img src="https://github.com/darkcleopas/tick-counter/blob/main/images/ticks-threshed.png"></td>
    <td><img src="https://github.com/darkcleopas/tick-counter/blob/main/images/ticks-canny.png"></td>
  </tr>
  <tr>
    <td>Dilation</td>
    <td>Found ticks</td>
  </tr>
  <tr>
    <td><img src="https://github.com/darkcleopas/tick-counter/blob/main/images/ticks-dilated.png"></td>
    <td><img src="https://github.com/darkcleopas/tick-counter/blob/main/images/ticks-found.png"></td>
  </tr>
 </table>

### 2. Acaricide accuracy

<table>
  <tr>
    <td>Ticks video</td>
    <td>Accaricide accuracy</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/38215548/181861934-2984edde-40c9-4b3f-b1af-52ca099e9921.gif">
    </td>
    <td><img src="https://user-images.githubusercontent.com/38215548/181861950-5c6d814b-e908-41ad-a7d8-2ed9f7d7ba5f.gif">
    </td>
  </tr>
 </table>
 

## Conclusion

The application was able to find and count the live ticks that move over the paper.

The total number of ticks varies depending on the camera stability.
