import os

for folder in os.listdir('./Data/genres_original/'):
    for file in os.listdir('./Data/genres_original/' + folder):
        fname = os.path.splitext(file)[0]
        # print(fname)
        fname = fname.replace('.', '_')
        print(fname)
        os.rename('./Data/genres_original/' + folder + '/' + file, './Data/genres_original/' + folder + '/' + folder + '_' + fname + '.wav')