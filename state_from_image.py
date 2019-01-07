from PIL import Image, ImageStat
import numpy as np

#           (width, height)
grid_dims = (11,18)
img = Image.open('Loadfiles/Loadimages/pentadecathlon.png').convert('L').resize(grid_dims)
meanL = ImageStat.Stat(img).mean[0]
pixels = np.array(img)
gridarr = np.zeros(pixels.shape, dtype = int)
for y in range(len(pixels)):
    for x in range(len(pixels[y])):
        if pixels[y,x] > meanL:
            gridarr[y,x] = 0
        else:
            gridarr[y,x] = 1
#ugly but it works for now

with open('Loadfiles/pentadecathlon.txt', 'w') as f:
    for x in [list(row) for row in gridarr.astype(str)]:
        f.write(''.join(x) + '\n')
