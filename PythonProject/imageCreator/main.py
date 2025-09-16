import imageio.v2 as iio

filenames = ['test.jpg','test.jpg','test.jpg']

images = []

for filename in filenames:
    images.append(iio.imread(filename))


iio.mimsave('output.gif',images,duration=0.5)


