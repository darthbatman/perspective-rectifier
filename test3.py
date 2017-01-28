import cv2
import numpy as np

sourcePoints = []
destinationPoints = []
im_src = cv2.imread('tilted_flashdrive.jpg')

def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print str(x) + "," + str(y)
        if len(sourcePoints) < 4:
            sourcePoints.append([x, y])
            if len(sourcePoints) == 4:
                black_image = cv2.imread("straight_flashdrive.jpg")
                cv2.namedWindow("black_image")
                cv2.setMouseCallback('black_image', mouse)
                cv2.imshow("black_image", black_image)
        elif len(destinationPoints) < 4:
            destinationPoints.append([x, y])
            if len(destinationPoints) == 4:
                pts_src = np.array(sourcePoints)
                pts_dst = np.array(destinationPoints)
                h, status = cv2.findHomography(pts_src, pts_dst)
                im_out = cv2.warpPerspective(im_src, h, (im_src.shape[1], im_src.shape[0]))
                cv2.imshow("output_image", im_out)


if __name__ == '__main__' :

    cv2.namedWindow("source_image")
    cv2.setMouseCallback('source_image', mouse)
    cv2.imshow("source_image", im_src)
 
    cv2.waitKey(0)