from PIL import Image,ImageOps


class Rect(object):
	def __init__(self,x,y,w,h):
		self.x = x
		self.y = y 
		self.w = w
		self.h = h

# returns the average color of the input image #
def averageColor(image):
	size = image.size
	count = 0
	red = 0
	green = 0
	blue = 0
	tempRed=0
	tempGreen=0
	tempBlue=0
	pixels = image.load()
	for i in range(0,size[0]):
		for j in range(0,size[1]):
			tempRed,tempGreen,tempBlue = pixels[i,j]
			red += tempRed
			green += tempGreen
			blue +=tempBlue
			count+=1
	if(count==0):
		raise Exception("Image does not seem to have any pixels")
	else:
		red = red/count
		green = green/count
		blue = blue/count
		return(red,green,blue)
	
		

# this function will take a SECTION of an image and create a list of of average colors of its segents
def splice(image,rect=None,segments = 16):
	
	if(pow(segments,.5)%1!=0):
		raise Exception("ERROR: segments should be a perfect square")
		return
	
	size = image.size
	
	if rect == None:
		rect = Rect(0,0,size[0],size[1])
	elif(not isinstance(rect,Rect)):
		if(len(rect)!=4):
			raise Exception("ERROR: rect arguement should be of type Rect")
			return
		else:
			rect = Rect(rect)
	
	if(rect.x+rect.w>size[0] or rect.y+rect.h > size[1]):
		raise Exception("ERROR: rect out of range")
		return
	
	cropped = image.crop((rect.x,rect.y,rect.w,rect.h))
	croppedSize = cropped.size
	
	segment_width = croppedSize[0]/pow(segments,.5)
	segment_height = croppedSize[1]/pow(segments,.5)
	#print croppedSize
	output = []
	
	for i in range(0,int(pow(segments,.5))):
		for j in range(0,int(pow(segments,.5))):
			tempCropped = cropped.crop( (int(i*segment_width),int(j*segment_height),int(segment_width)+int(i*segment_width),int(segment_height)+int(j*segment_height)) )
			
			#print (int(i*segment_width),int(j*segment_height),int(segment_width)+int(i*segment_width),int(segment_height)+int(j*segment_height))
			
			#tempCropped.show()
			output.append( ((int(i*segment_width),int(j*segment_height),int(segment_width)+int(i*segment_width),int(segment_height)+int(j*segment_height)),averageColor(tempCropped)) )
	
	return output




