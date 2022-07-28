import cv2

from config import *
from count_contours import get_contours_number

video_name = "video-3.mp4"

cap = cv2.VideoCapture(f"{VIDEO_DIR}/{video_name}")

object_detector = cv2.createBackgroundSubtractorMOG2()

while True:
	ret, frame = cap.read()
	if ret: 
		H, W = frame.shape[0], frame.shape[1]

		# cut the edges of the video 
		frame = frame[H_CUT_SIZE:H-H_CUT_SIZE, W_CUT_SIZE:W-W_CUT_SIZE]

		# get the contour amount given a frame
		amount = get_contours_number(frame, False)		

		# convert to gray scale and apply threshold binary 
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		ret, gray_frame = cv2.threshold(gray_frame, 80, 255, cv2.THRESH_BINARY)

		# create the mask 
		mask = object_detector.apply(gray_frame)
		
		# get the contours in the mask 
		contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		# count the amount of contours found in the mask given a certain area
		live_ticks = 0
		for cnt in contours:
			area = cv2.contourArea(cnt)
			if area > TH_CONTOUR_AREA:
				x, y, w, h = cv2.boundingRect(cnt)
				cv2.rectangle(frame, (x, y), (x + w, y + h), DRAW_COLOR, DRAW_THICK)
				live_ticks += 1	

		dead_ticks = amount - live_ticks
		acc = (dead_ticks / amount) * 100

		# put legend in the frame
		cv2.putText(frame, f"Total number of ticks: {amount}", (30, 40), FONT_TYPE, FONT_SIZE, FONT_COLOR, FONT_THICK)
		cv2.putText(frame, f"Live ticks: {live_ticks}", (30, 70), FONT_TYPE, FONT_SIZE, FONT_COLOR, FONT_THICK)
		cv2.putText(frame, f"Acaricide accuracy: {round(acc, 2)} %", (30, 100), FONT_TYPE, FONT_SIZE, FONT_COLOR, FONT_THICK)
		
		# show the frame
		cv2.imshow("Threshold", gray_frame)
		cv2.imshow("Mask", mask)
		cv2.imshow("Frame", frame)

		print("Total number of ticks:", amount)
		print("Number of live ticks:", live_ticks)
		print("Number of dead ticks:", dead_ticks)

		key = cv2.waitKey(30)
		if key == 27:
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()