import dice
from PIL import Image,ImageDraw


def comparePixels(pixel1,pixel2):
	red = pixel1[1][0]-pixel2[0][0]
	green = pixel1[1][1]-pixel2[0][1]
	blue = pixel1[1][2]-pixel2[1][2]
	distance = pow( pow(red,2)+pow(green,2)+pow(blue,2) , 0.5 )
	return distance
	
def findMatchingPixel(pixel1,image2Pixels):
	
	currentClosestMatch = None
	currentClosestDist = -1
	tempDist = 0
	for pixel2 in image2Pixels:
		tempDist = comparePixels(pixel1,pixel2)
		if(currentClosestDist == -1 or currentClosestDist > tempDist):
			currentClosestDist = tempDist
			currentClosestMatch = pixel2
	return currentClosestMatch

	
def getDist(pixel1,pixel2):
	x1 = (pixel1[0][2]+pixel1[0][0])/2
	y1 = (pixel1[0][1]+pixel1[0][3])/2
	x2 = (pixel2[0][2]+pixel2[0][0])/2
	y2 = (pixel2[0][1]+pixel2[0][3])/2
	
	x1 = pixel1[0][0]
	y1 = pixel1[0][1]
	x2 = pixel2[0][0]
	y2 = pixel2[0][1]
	
	dist = pow(pow(x1-x2,2)+pow(y1-y2,2),0.5)
	return dist
	
def compareImages(image1,image2):
	
	newImage = Image.new('L',image1.size,120)
	newDraw = ImageDraw.Draw(newImage)
	image1Pixels = dice(image1,squareSize = 50) # using 100 right now, but have to find a better way to determine squareSize
	image2Pixels = dice(image2,squareSize = 50)
	match = -1
	dist = -1
	color = 120
	
	for pixel1 in image1Pixels:
		match = findMatchingPixel(pixel1,image2Pixels)

		dist = getDist(pixel1,match)
		color = 255*dist/pow(image1.size[0]*image2.size[1],0.5)
		#print(color)
		newDraw.rectangle(pixel1[0],int(color) )
		
	newImage.show()
	
	
	
	
	