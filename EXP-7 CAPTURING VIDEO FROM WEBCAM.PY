import cv2
def adjust_speed(frame, factor):
    return cv2.resize(frame, None, fx=factor, fy=factor, interpolation=cv2.INTER_LINEAR)
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break
        cv2.imshow("Original", frame)
        slow_frame = adjust_speed(frame, 0.5) 
        cv2.imshow("Slow Motion", slow_frame)
        fast_frame = adjust_speed(frame, 2.0)  
        cv2.imshow("Fast Motion", fast_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
