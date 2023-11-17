---
marp: true
backgroundImage: url(https://github.com/ArmandBriere/lunch-and-learn/blob/feat/my-computer-can-see/my-computer-can-see/assets/osedea-background.jpg?raw=true)
color: white
theme: uncover
paginate: true
class: invert
---

<style>
section::after {
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
}
</style>

# My computer can see

*Alternative titles:*

- My computer can C.. but not really sharp
- I love pixels
- I'm sure I can make a model to detect that

---

# Computer vision?

---

# Some use cases...

---

Identification

![width:350px](https://upload.wikimedia.org/wikipedia/en/b/b4/Sharbat_Gula.jpg)


---

Afghan Girl - 1984 portrait

![width:400px](https://www.cl.cam.ac.uk/users/jgd1000/afghanportraits.jpg) ![width:400px](https://www.cl.cam.ac.uk/~jgd1000/youngProcessedR.jpg)

---

Robotics

![width:900px](https://upload.wikimedia.org/wikipedia/commons/a/a4/Perseverance-Selfie-at-Rochette-Horizontal-V2.gif)

---

![width:500px](./assets/spot.jpg)

---

Space


![width:900px](https://siril.readthedocs.io/zh-cn/latest/_images/clahe_inout.png)

---

# Why computer vision?

---

## We are not perfect

![](https://www.researchgate.net/profile/Pawan-Sinha-2/publication/228796924/figure/fig6/AS:300787872878609@1448724825760/Although-this-image-appears-to-be-a-fairly-run-of-the-mill-picture-of-Bill-Clinton-and-Al.png)

Bill Clinton and Al Gore

---

![](https://www.researchgate.net/profile/Pawan-Sinha-2/publication/228796924/figure/fig6/AS:300787872878609@1448724825760/Although-this-image-appears-to-be-a-fairly-run-of-the-mill-picture-of-Bill-Clinton-and-Al.png)

Same person - From Sinha and Poggio, 1996

---

# What is an image?

---

It's a projection on a film

![](https://jalalirs.github.io/Introduction-to-Computer-Vision/L3/imgs/image_formation_1.png)

---

![](https://jalalirs.github.io/Introduction-to-Computer-Vision/L3/imgs/image_formation_2.png)

---

Pinhole Camera

![](https://upload.wikimedia.org/wikipedia/commons/3/3b/Pinhole-camera.svg)

---

# Human VS Machine

---

<style scoped>
section {
  transform: rotate(180deg) scale(1);
}
</style>

![](https://i.pinimg.com/originals/f0/d7/cf/f0d7cf4b07e255d29e353a34cf67b3df.png)


---

![width:550px](https://www.researchgate.net/profile/Ahmed-Ahmed-330/publication/345258613/figure/fig8/AS:953891663388672@1604436903208/RGB-layers-separation-of-best-cover-image.png)

---

# The computer world


---

Lot of numbers

![width:950px](https://www.researchgate.net/publication/330902210/figure/fig1/AS:878026619375622@1586349267376/mage-of-Abraham-Lincoln-as-a-matrix-of-pixel-values.ppm)

---

# Math

---

Who is my neighbour?

![width:300px](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Square_4_connectivity.svg/120px-Square_4_connectivity.svg.png) ![width:300px](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Square_8_connectivity.svg/120px-Square_8_connectivity.svg.png)

---

# OpenCV

---

<!-- _class: invert -->

```bash
# Bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

```python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
```

---

Gaussian filter to reduce artifacts

![width:900px](https://ai.stanford.edu/~syyeung/cvweb/gifs/moving%20average.gif)

---

<!-- _class: invert -->


```py
# Load duck
img = cv.imread("duck.jpg")

# 2D Convolution - 15x15 filter
kernel = np.ones((15, 15), np.float32) / 250
blur = cv.filter2D(img, -1, kernel)
cv.imwrite("duck-2dconv.jpg", blur)

# Default blur - 15x15 filter
blur = cv.blur(img, (15, 15))
cv.imwrite("duck-blur.jpg", blur)

# Gaussian
blur = cv.GaussianBlur(img, (15, 15), 0)
cv.imwrite("duck-gaussian.jpg", blur)
```

---

![width:900px](./src/duck.jpg)

---

2D conv

![width:500px](./src/duck.jpg) ![width:500px](./src/duck-2dconv.jpg)

---

Blur

![width:500px](./src/duck.jpg) ![width:500px](./src/duck-blur.jpg)

---

Gaussian

![width:500px](./src/duck.jpg) ![width:500px](./src/duck-gaussian.jpg)

---

Edge detection with Canny

<!-- _class: invert -->


```py
# Load froge
img = cv.imread("froge.jpg", cv.IMREAD_GRAYSCALE)

# Canny - img, Threshold1,Threshold2
edges = cv.Canny(img, 50, 200)

cv.imwrite("froge-canny.jpg", edges)
```

---

![width:500px](./src/froge.jpg)

---

![width:500px](./src/froge.jpg)![width:500px](./src/froge-canny.jpg)

---

Contrast equalization with CLAHE

<!-- _class: invert -->

```py
# Apply CLAHE on grayscale
img = cv.imread("mountain.jpg", cv.IMREAD_GRAYSCALE)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

cv.imwrite("mountain-clahe-grayscale.jpg", cl1)


# Apply CLAHE on color
img = cv.imread("mountain.jpg", cv.IMREAD_ANYCOLOR)
img = cv.cvtColor(img, cv.COLOR_RGB2Lab)

clahe = cv.createCLAHE(clipLimit=10, tileGridSize=(8, 8))
img[:, :, 0] = clahe.apply(img[:, :, 0])
img = cv.cvtColor(img, cv.COLOR_Lab2RGB)

cv.imwrite("mountain-clahe-rgb.jpg", img)
```

---

![width:1000px](./src/mountain.jpg)

---

![width:560px](./src/mountain.jpg) ![width:560px](./src/mountain-clahe-grayscale.jpg)

---

![width:560px](./src/mountain.jpg) ![width:560px](./src/mountain-clahe-rgb.jpg)

---

Panoramic picture

![width:1100px](https://upload.wikimedia.org/wikipedia/commons/a/a0/Rochester_NY.jpg)

---

# Unblur an image

---
Spectral analysis - Wiener filter

![width:800px](./assets/blur.png)

---

# No AI today...
# maybe next time?

---

# Sources

![bg right:25%](https://photos-professeurs.uqam.ca/images/fiche_professeur/m2/1YXEXw15eJY_.jpg)

Joël Lefebvre
https://professeurs.uqam.ca/professeur/lefebvre.joel/

---

- Afghan girl was Identified https://www.cl.cam.ac.uk/~jgd1000/afghan.html
- Spot https://bostondynamics.com/products/spot/
- Space CLAHE https://siril.readthedocs.io/zh-cn/latest/processing/clahe.html

- Bill Clinton and Al Gore https://www.researchgate.net/figure/Although-this-image-appears-to-be-a-fairly-run-of-the-mill-picture-of-Bill-Clinton-and-Al_fig6_228796924

---

- Pinhole camera https://en.wikipedia.org/wiki/Pinhole_camera
- Canny https://en.wikipedia.org/wiki/Edge_detection
- Clahe https://www.analyticsvidhya.com/blog/2022/08/image-contrast-enhancement-using-clahe/

---

# Questions?

---

![](https://upload.wikimedia.org/wikipedia/commons/2/24/Spot_the_cow.gif)
