import math
import numpy as np
import matplotlib.pyplot as plt

# input screen information
Wpx = int(input("Enter horizontal resolution(pixels):"))
Hpx = int(input("Enter vertical resolution(pixels):"))
Dinches = float(input("Enter physical diagonal size(inches):"))

#total pixel count
total_pixels = Wpx*Hpx


#simplified aspect ratio
gcd = math.gcd(Wpx,Hpx)
aspect_width= Wpx // gcd
aspect_height = Hpx // gcd

#calculate diagonal pixel count 
diagonal_pixels = math.sqrt(Wpx ** 2 + Hpx ** 2)

#calculate PPI/DPI
ppi = diagonal_pixels/Dinches

#classify display density 
if ppi < 100:
    density= "Low Density(Standard Monitor)"
elif ppi <= 200:
    density= "Medium Density (HD Display)"
else:
    density = "High Density (Retina / Mobile )"

    # display results 
print("\n--- DISPLAY METRICS ANALYSIS ---")
print("TOTAL PIXEL COUNT : ",F"{total_pixels:,}", "pixels")
print("ASPECT RATIO   : ",F"{aspect_width}:{aspect_height}")
print("Calculated DPI    :",f"{ppi: .2f}","DPI")
print("DENSITY CATEGORY  :",density)

#create a 300* 400 RGB image filled with zeros 
img = np.zeros((300,400,3),dtype=np.uint8)


#fill the four quadrants
img[:150, :200] = [255, 0, 0]    #top-left: Red
img[:150, 200:] = [0, 255, 0]    #top-right: Green
img[150:, :200] = [0, 0, 255]    #bottom-left: Blue
img[150:, 200:] = [255, 255, 255]    #bottom-right: White


#display array information
print("\n--- SYNTHETIC IMAGE MATRIX ---")
print("Shape:", img.shape)
print("Data type:", img.dtype)
print("Total elements:", img.size)
print("Memory usage:", img.nbytes, "bytes")
print("Memory usage:", img.nbytes/1024, "KB")


plt.imshow(img)
plt.axis("off")
plt.title("Synthetic RGB Image")


plt.imsave("sample.jpg", img)

#load sample image
sample = np.array(plt.imread("sample.jpg"))
print("\n--- CHANNEL INFORMATION ---")
print("Original shape:", sample.shape)
R = sample[:, :, 0]
G = sample[:, :, 1]
B = sample[:, :, 2]

print("Red channel shape:", R.shape)
print("Green channel shape:", G.shape)
print("Blue channel shape:", B.shape)

# Create channel-isolated images
red_only = np.zeros_like(sample)
green_only = np.zeros_like(sample)
blue_only = np.zeros_like(sample)

red_only[:, :, 0] = R
green_only[:, :, 1] = G
blue_only[:, :, 2] = B

fig, axes = plt.subplots(2, 3, figsize=(12, 7))

# Top row: isolated color channels
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red Only")

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green Only")

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue Only")

# Bottom row: grayscale intensity maps
axes[1, 0].imshow(R, cmap="gray")
axes[1, 0].set_title("Red Intensity")

axes[1, 1].imshow(G, cmap="gray")
axes[1, 1].set_title("Green Intensity")

axes[1, 2].imshow(B, cmap="gray")
axes[1, 2].set_title("Blue Intensity")

for ax in axes.flat:
    ax.axis("off")

plt.tight_layout()

# Task 4: Spatial Downsampling
N = 8

downsampled = sample[::N, ::N, :]

print("\n--- DOWNSAMPLING ---")
print("Original shape:", sample.shape)
print("Downsampled shape:", downsampled.shape)

# Re-expand the downsampled image
pixelated = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)

print("Pixelated shape:", pixelated.shape)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(sample)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(pixelated)
plt.title("Pixelated Image")
plt.axis("off")

plt.tight_layout()

original_memory = sample.nbytes
downsampled_memory = downsampled.nbytes

reduction = ((original_memory - downsampled_memory) / original_memory) * 100

print("\n--- MEMORY REDUCTION ---")
print("Original memory:", original_memory, "bytes")
print("Downsampled memory:", downsampled_memory, "bytes")
print("Memory reduction:", f"{reduction:.2f}%")

plt.show()