import cv2
import numpy as np

selected_points = []
tracking_points = None
prev_gray = None

def select_points(event, x, y, flags, param):
    """Mouse callback function to select four points."""
    global selected_points
    if event == cv2.EVENT_LBUTTONDOWN and len(selected_points) < 4:
        selected_points.append((x, y))

def compute_homography(frame, points):
    """Compute homography to warp selected rectangle to a fixed size."""
    # destination points for the warped image (200x200)
    dest_points = np.array([[0, 0], [200, 0], [200, 200], [0, 200]], dtype=np.float32)
    # homography matrix
    h_matrix, _ = cv2.findHomography(np.array(points, dtype=np.float32), dest_points)
    # img warping
    warped = cv2.warpPerspective(frame, h_matrix, (200, 200))
    return warped



# initialize webcam -- live
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", select_points)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # cvt to grayscale for optical flow
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for point in selected_points:
        cv2.circle(frame, point, 5, (0, 255, 0), -1)

    if len(selected_points) == 4:
        if tracking_points is None:
            # init tracking points
            tracking_points = np.array(selected_points, dtype=np.float32).reshape(-1, 1, 2)
        else:
            # use optical flow tracking
            new_points, status, _ = cv2.calcOpticalFlowPyrLK(prev_gray, gray, tracking_points, None)
            if status.sum() == len(status): 
                tracking_points = new_points
            else:
                print("Tracking failed. Resetting points.")
                selected_points = []
                tracking_points = None

        # draw tracked rectangle
        if tracking_points is not None:
            for i in range(4):
                start_point = tuple(tracking_points[i][0].astype(int))
                end_point = tuple(tracking_points[(i + 1) % 4][0].astype(int))
                cv2.line(frame, start_point, end_point, (0, 255, 0), 2)

            # compute homography and display the warped view
            warped = compute_homography(frame, tracking_points.reshape(-1, 2))
            cv2.imshow("Warped View", warped)


    prev_gray = gray.copy()


    cv2.imshow("Webcam", frame)

    # exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
