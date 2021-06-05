import h5py
import numpy as np
from plot_result.color_dict import color_dict
import matplotlib.pyplot as plt


def h5_data_loader(data_dir):
    with h5py.File(data_dir, 'r') as f:
        data = f['data'][:]
        label = f['label'][:]

    return data, label


def labelmap_2_img(color_list, label_map):
    h, w = label_map.shape
    img = np.zeros((h, w, 3))
    for i in range(h):
        for j in range(w):
            R,G,B = color_list[str(label_map[i, j])]
            img[i,j] = [R, G, B]
    return np.array(img, np.uint8)


data_set = 'PaviaU'
data_root  = '/data/data2/zhk218/data/HSIs/h5'
#
# data_dir = data_root + '/{}.h5'.format(data_set)
# data, label_map = h5_data_loader(data_dir)
# color_map = labelmap_2_img(color_dict[data_set], label_map)
code_map = []
for i in range(9):
    code_map.append(np.zeros((60, 60))+i+1)
code_map=np.array(np.vstack(code_map), np.int)
code_map = labelmap_2_img(color_dict[data_set], code_map)
plt.imshow(code_map); plt.show()

print('done')
