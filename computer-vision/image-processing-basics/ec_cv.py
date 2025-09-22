import numpy as np
# To convert an RGBA image array that represents data with floating point numbers from 0 to 1 into the RGB integer format from 0 to 255, we need to change 4 things:

# 1) Get rid of the A channel
# 2) Multiply by 255
# 3) Round the resulting values
# 4) Ensure values are between 0 and 255
# 5) Convert data to 8-bit integers

# Let's define a function for this:

def adapt_PNG(the_PNG):
    the_PNG = the_PNG[:,:,:3] # Step 1
    the_PNG = the_PNG * 255   # Step 2
    the_PNG = adapt_image(the_PNG) # Steps 3, 4, 5
    return the_PNG

# The following function will be useful to perform steps 3, 4, 5 for RGB images in the 0-255 range, which are undergoing operations that may result in floating point numbers.

def adapt_image(the_img):
    return np.uint8(np.clip(the_img.round(), 0, 255)) # steps 3, 4, 5