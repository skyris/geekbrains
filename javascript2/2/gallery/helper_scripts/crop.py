files = ["pexels-photo-101472.jpeg", 
"pexels-photo-157053.jpeg",
"pexels-photo-227507.jpeg",
"pexels-photo-247576.jpeg",
"pexels-photo-265957.jpeg",
"pexels-photo-290013.jpeg",
"pexels-photo-313702.jpeg",
"pexels-photo-420332.jpeg",
"pexels-photo-424154.jpeg",
"pexels-photo-434203.jpeg",
"pexels-photo-457878.jpeg",
"pexels-photo-459799.jpeg",
"pexels-photo-464311.jpeg",
"pexels-photo-569202.jpeg",
"pexels-photo-571171.jpeg",
"pexels-photo-572741.jpeg",
"pexels-photo-583677.jpeg",
"pexels-photo-583837.jpeg",
"pexels-photo-583845.jpeg",
"pexels-photo-585039.jpeg",
"pexels-photo-589819.jpeg"]

from PIL import Image

sizes = [(300, 200), (1200, 800)]
for i, image in enumerate(files):
    print(image)
    for size in sizes:
        try:
            im = Image.open(image)
            im.thumbnail(size)
            im.save("img{:03}_{}_{}.jpeg".format(i+1, size[0], size[1]), "JPEG")

        except:
            print("Fail to create: {}".format(image))
