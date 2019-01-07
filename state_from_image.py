from PIL import Image, ImageStat
import numpy as np

grid_dims = (38,11)
img = Image.open('ggg.png').convert('L').resize(grid_dims)
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

with open('Loadfiles/GosperGliderGun.txt', 'w') as f:
    for x in [list(row) for row in gridarr.astype(str)]:
        f.write(''.join(x) + '\n')


