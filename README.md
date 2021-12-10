# Contrast-Normalization

## Introduction

Basic python implementation that applies local contrast normalization with the use of order filters. The idea is to use the intensity distribution only in the vicinity of the pixel being processed, and not the entire image. Therefore, the process becomes local and no longer global. A portuguese article was written analyzing the results. The article can be found in the folder: <i>docs</i>

<b>Second project of digital image processing</b>


## How it works

Basically, a neighborhood region is centered on a pixel x in the input image, from where the intensity values will be extracted and then applied with the global method. The result is applied at the x position of the output image. This neighborhood region is shifted pixel by pixel so that all pixels in the input image are processed. For a more efficient implementation, the <a href="https://scikit-image.org/"> scikit-image</a> library was used, functions such as <a href="https://scikit-image.org/docs/dev/api/skimage.filters.rank.html#skimage.filters.rank.maximum"><i>skimage.filters.rank.maximum</i></a> and <a href="https://scikit-image.org/docs/dev/api/skimage.filters.rank.html#skimage.filters.rank.minimum"><i>skimage.filters.rank.minimum</i></a>, which are two rank statistics filters.

### Input & output

## How to use

The application will look for images in the same directory as the source code (accepting jpeg, png and tif formats), asking which image do you wanna load.
