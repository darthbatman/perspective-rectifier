import cv2
import numpy as np
 
if __name__ == '__main__' :
 
    # Read source image.
    im_src = cv2.imread('tilted_flashdrive.jpg')
    # Four corners of the book in source image
    pts_src = np.array([[70, 65], [240, 80], [246, 315],[32, 300]])
 
 
    # Read destination image.
    im_dst = cv2.imread('straight_flashdrive.jpg')
    # Four corners of the book in destination image.
    pts_dst = np.array([[159, 128],[267, 186],[158, 335],[36, 236]])
 
    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
     
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
     
    # Display images
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)
 
    cv2.waitKey(0)