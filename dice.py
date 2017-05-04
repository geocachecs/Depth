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
	
		

# this function will take an image or a SECTION of an image and create a list of of average colors of its segents
def dice(image,squareSize=100,rect=None):
	
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
	
	iterationsAcross = croppedSize[0]/squareSize+1
	iterationsDown = croppedSize[1]/squareSize+1
	width = squareSize
	height = squareSize
	output = []
	
	for i in range(0,iterationsAcross):
		for j in range(0,iterationsDown):
			if(squareSize+i*squareSize > croppedSize[0]):
				width = croppedSize[0] - i*squareSize
			else:
				width = squareSize
			if(squareSize+j*squareSize > croppedSize[1]):
				height = croppedSize[1] - j*squareSize
			else:
				height = squareSize
			if(width>0 and height>0):
				tempCropped = cropped.crop( (i*squareSize,j*squareSize,width+i*squareSize,height+j*squareSize) )
			
				output.append( ( (i*squareSize,j*squareSize,width+i*squareSize,height+j*squareSize),averageColor(tempCropped) ) ) 
	
	return output




