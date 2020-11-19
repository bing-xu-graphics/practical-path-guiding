# import imp
# imp.find_module("OpenEXR")
# imp.load_source("openexr", "/usr/local/Cellar/")
# import OpenEXR, Imath
import pyexr
import numpy as np
import os

I_PRE_EDIT_SAMPLE = 10
K_POST_EDIT_SAMPLE = 0
J_CORRECTION_SAMPLE = 0

def compute_L_pre():
	total_radiance = None
	for i in range(I_PRE_EDIT_SAMPLE):
		_seed = 1234+i
		path_sceneA = "../scenes/cbox/consistentA/cbox_frame0_%d_%d.exr"%(i, _seed)
		img = loadEXR2matrix(path_sceneA)
		if total_radiance is None:
			total_radiance = img
		else:
			total_radiance += img
	L_pre = total_radiance/float(I_PRE_EDIT_SAMPLE)
	if not os.path.exists("../scenes/cbox/consistent_simu/"):
		os.makedirs("../scenes/cbox/consistent_simu/")
	saveEXRfromMatrix("../scenes/cbox/consistent_simu/L_pre.exr", img)


def compute_old_and_new():
	pass

def compute_mask():
	pass

def compute_L_post():
	total_radiance = None
	for i in range(I_PRE_EDIT_SAMPLE+J_CORRECTION_SAMPLE, I_PRE_EDIT_SAMPLE+J_CORRECTION_SAMPLE+K_POST_EDIT_SAMPLE):
		_seed = 1234+i
		path_sceneB = "../scenes/cbox/consistentB/cbox_frame0_%d_%d.exr"%(i, _seed)
		img = loadEXR2matrix(path_sceneB)
		if not total_radiance:
			total_radiance = img
		else:
			total_radiance += img
	L_pre = total_radiance/float(K_POST_EDIT_SAMPLE)
	if not os.path.exists("../scenes/cbox/consistent_simu/"):
		os.makedirs("../scenes/cbox/consistent_simu/")
	saveEXRfromMatrix("../scenes/cbox/consistent_simu/L_post.exr", img)

def simulate_consistent():
	L_pre = compute_L_pre()
	L_old, L_new = compute_old_and_new()
	L_diff = L_new - L_old
	M = compute_mask()
	L_post = compute_L_post()
	L_repair = (1-M) * ( I/(I+K)*L_pre + I/(I+K)*L_diff + K/(I+K)*L_post ) + M* 1/(J+K)



#util functions
def loadEXR2matrix(path, channel=4):
	col = pyexr.read(path, "default")
	return col
# def loadEXR2matrix(path,channel=3):
#     image = OpenEXR.InputFile(path)
#     dataWindow = image.header()['dataWindow']
#     # print(image.header())
#     size = (dataWindow.max.x - dataWindow.min.x + 1, dataWindow.max.y - dataWindow.min.y + 1)
#     FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
#     if channel == 3:
#         data = np.array([np.fromstring(image.channel(c, FLOAT), dtype=np.float32) for c in 'BGR'])
#     elif channel == 4:
#         data = np.array([np.fromstring(image.channel(c, FLOAT), dtype=np.float32) for c in 'BGRA'])
#     data = np.moveaxis(data, 0, -1)
#     data = data.reshape(size[1], size[0], channel) #(600,800,3)
#     return data,size
def saveEXRfromMatrix(file, data):
	pyexr.write(file, data)

# def saveEXRfromMatrix(file,data,size):
#     output = OpenEXR.OutputFile(file, OpenEXR.Header(*size))
#     data = np.moveaxis(data, -1, 0)
#     output.writePixels({
#         "B": data[0].tostring(),
#         "G": data[1].tostring(),
#         "R": data[2].tostring(),
#     #    "A": data[3].tostring()
#     })


if __name__ == "__main__":
	# simulate_consistent()
	compute_L_pre()
