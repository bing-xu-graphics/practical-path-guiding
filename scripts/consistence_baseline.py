
import xml.etree.ElementTree as ET
import os
sceneAPath = "../scenes/cbox/cbox_frame0.xml"
sceneBPath = "../scenes/cbox/cbox_frame2.xml"
numOfImages = 500
numOfFrames = 2
newSceneTmpPath = "../scenes/cbox/cbox_tmp.xml"

def generate_scene_file_with_random_seed(_seed, original_scene):
	tree = ET.parse(original_scene)
	print(original_scene)
	root = tree.getroot()
	for x in root.iter('sampler'):
		# for y in x.iter("integer"):
		# print(x[1].attrib)
		# print(x[1].get("name"))
		# print(x[1].get("value"))
		x[0].set("value", "1")
		x[1].set("value", str(_seed))
		# print(x[1].get("value"))
			# if y.name == "seed":
			# 	print(y.value)
	tree.write(newSceneTmpPath)

def render():
	if not os.path.exists("../scenes/cbox/consistentA/"):
		os.makedirs("../scenes/cbox/consistentA/")
	if not os.path.exists("../scenes/cbox/consistentB/"):
		os.makedirs("../scenes/cbox/consistentB/")	
	for i in range(numOfImages):
		#for scene A
		_seed = 1234+i
		generate_scene_file_with_random_seed(_seed, sceneAPath)
		CMD = "mitsuba -o ../scenes/cbox/consistentA/cbox_frame0_%d_%d %s "%(i, _seed, newSceneTmpPath)
		os.system(CMD)
		#for scene B
		generate_scene_file_with_random_seed(_seed, sceneBPath)
		CMD = "mitsuba -o ../scenes/cbox/consistentB/cbox_frame2_%d_%d %s "%(i, _seed, newSceneTmpPath)
		os.system(CMD)
		



if __name__ == "__main__":
	# generate_scene_file_with_random_seed(0, "/Volumes/projDrive/projects/practical-path-guiding/scenes/cbox/cbox_frame0.xml")
	render()
