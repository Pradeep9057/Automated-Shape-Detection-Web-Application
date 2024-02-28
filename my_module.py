import cv2
import numpy as np

def detect_circles(image_path):
    image = cv2.imread(image_path)
    detector = cv2.SimpleBlobDetector_create()

    keypoints = detector.detect(image)

    blank = np.zeros((1,1))
    blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)

    text = "total number of pipes:" + str(len(keypoints))

    cv2.putText(blobs, text, (0,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 10;
    params.maxThreshold = 300;
    params.filterByArea = True
    params.minArea = 400
    params.filterByCircularity = True
    params.minCircularity = 0.4
    params.filterByConvexity = True
    params.minConvexity = 0.8
    params.filterByInertia = True
    params.minInertiaRatio = 0.02

    detector = cv2.SimpleBlobDetector_create(params)

    keypoints = detector.detect(image)
    blank = np.zeros((1,1))
    blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)

    text = "number of pipes:" + str(len(keypoints))
    print(text)
    cv2.putText(blobs, text, (5,40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    #cv2.putText(blobs, text, (5,40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.waitKey()
    cv2.destroyAllWindows()
    return blobs

def detect_rectangles(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 10, 40)

    shape, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rectangles = []

    for shapes in shape:
        perimeter = cv2.arcLength(shapes, True)
        approx = cv2.approxPolyDP(shapes, 0.02 * perimeter, True)

        if len(approx) == 4:
            rectangles.append(approx)

    cv2.drawContours(image, rectangles, -1, (0, 255, 0), 1)

    number_of_rectangles = len(rectangles)
    text = "Number of rectangles: " + str(number_of_rectangles)
    cv2.putText(image, text, (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return image