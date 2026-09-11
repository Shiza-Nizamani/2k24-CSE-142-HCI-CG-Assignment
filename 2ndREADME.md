# LAB 1: Display Density Metrics & Image Array Mechanics in NumPy

## Lab Objectives

- Calculate display resolution, total pixels, aspect ratio, and PPI/DPI.
- Set up a Python environment for visual graphics.
- Create and inspect 3D image arrays using NumPy.
- Perform RGB channel extraction and isolation.
- Perform spatial downsampling and pixelation.

## Task 1: Display Pixel Density (PPI/DPI) Calculator

### Desktop Monitor
- Resolution: 1920 × 1080
- Physical diagonal: 24 inches
- Total pixels: 2,073,600
- Aspect ratio: 16:9
- Calculated DPI: 91.79
- Density: Low Density (Standard Monitor)

### Smartphone
- Resolution: 1170 × 2532
- Physical diagonal: 6.1 inches
- Total pixels: 2,962,440
- Aspect ratio: 195:422
- Calculated DPI: 457.25
- Density: High Density (Retina / Mobile)

## Task 2: Environment Setup & Synthetic Image Matrix

A 300 × 400 × 3 RGB image array was created using NumPy with `uint8` data type.

The image was divided into four colored quadrants:
- Top-left: Red
- Top-right: Green
- Bottom-left: Blue
- Bottom-right: White

## Task 3: Channel Slicing & Isolation

The Red, Green, and Blue channels were extracted from the image array.

Each channel was isolated separately and grayscale intensity maps were also generated using Matplotlib.

## Task 4: Spatial Downsampling & Pixelation

A downsampling factor of 8 was used to reduce the image resolution.

- Original shape: 300 × 400 × 3
- Downsampled shape: 38 × 50 × 3
- Pixelated shape: 304 × 400 × 3
- Original memory: 360000 bytes
- Downsampled memory: 5700 bytes
- Memory reduction: 98.42%

The original and pixelated images were compared using Matplotlib.

## Short Answer

### Why does adding an Alpha channel (RGBA) increase an image array’s memory consumption by 33% compared to standard RGB?

RGB images contain three channels: Red, Green, and Blue. With `uint8`, each channel uses 1 byte per pixel, so RGB requires 3 bytes per pixel.

RGBA adds a fourth channel called Alpha, which stores transparency information. Therefore, RGBA requires 4 bytes per pixel.

The increase in memory is:

(4 - 3) / 3 × 100 = 33.33%

Therefore, RGBA uses approximately 33% more memory than RGB for the same image resolution.
