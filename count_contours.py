import cv2

from config import *


def get_contours_number(image, save_img=False, show_img=False):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, threshed = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    canny = cv2.Canny(threshed, 0, 50, 3)
    dilated = cv2.dilate(canny, (1, 1), iterations=1)
    
    (cnt, hierarchy) = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours_number = len(cnt)

    if save_img or show_img:
        cv2.drawContours(image, cnt, -1, DRAW_COLOR, DRAW_THICK)
        cv2.putText(image, f"Total number: {contours_number}", (30, 40), FONT_TYPE, FONT_SIZE, FONT_COLOR, FONT_THICK)
    
        if save_img:
            cv2.imwrite(f"{IMAGE_DIR}/ticks-gray.png", gray)
            cv2.imwrite(f"{IMAGE_DIR}/ticks-threshed.png", threshed)
            cv2.imwrite(f"{IMAGE_DIR}/ticks-canny.png", canny)
            cv2.imwrite(f"{IMAGE_DIR}/ticks-dilated.png", dilated)
            cv2.imwrite(f"{IMAGE_DIR}/ticks-found.png", image)
        
        if show_img:
            cv2.imshow("Gray", gray)
            cv2.imshow("Threshed", threshed)
            cv2.imshow("Canny", canny)
            cv2.imshow("Dilated", dilated)
            cv2.imshow("RGB", image)
            cv2.waitKey()

    return contours_number

if __name__ == "__main__":
    image_name = "ticks-2.png"
    image = cv2.imread(f"{IMAGE_DIR}/{image_name}")
    cnt = get_contours_number(image, save_img=True, show_img=True)
    print(cnt)
