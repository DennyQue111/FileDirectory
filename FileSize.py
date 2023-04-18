import os

basedir = "/Users/749vfx_2/Desktop/2048x1426"
names = os.listdir(basedir)

paths = [os.path.join(basedir, name) for name in names]

sizes = [(path, os.stat(path).st_size) for path in paths]
print sizes
