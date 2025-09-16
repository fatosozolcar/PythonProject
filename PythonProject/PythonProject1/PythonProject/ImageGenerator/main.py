# import library
import imageio.v3 as iio

# create an image object
images = iio.imread('test.gif')
print(images.shape)

# read frames one-by-one instead
for i in range(16):
    img = iio-imread('test.gif', index=i)
    # Each frame is a numpy matrix
    print(img.shape)