picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for image in picture: #for every subarray in the picture array 
  for pixel in image: #for every element in the sub array
    if (pixel): #if value is true
      print('*', end ="") #print a * character 
    else:
      print(' ', end ="") # print a space 
  print('')