# Contrast-Normalization

## Introduction

Basic python implementation that applies local contrast normalization with the use of order filters. The idea is to use the intensity distribution only in the vicinity of the pixel being processed, and not the entire image. Therefore, the process becomes local and no longer global.


## How it works

Basically, a neighborhood region is centered on a pixel x in the input image, from where the intensity values will be extracted and then applied with the global method. The result is applied at the x position of the output image. This neighborhood region is shifted pixel by pixel so that all pixels in the input image are processed.

### Input and output

## How to use
