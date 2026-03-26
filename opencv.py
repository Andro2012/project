import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Ошибка!!! не удалось открыть камеру")
    exit()

print("для выхода нажмите 'q'")


while True:
    ret, frame = cap.read()
    if not ret:
        print("Ошибка!!! не удалось получить кадр")
        break

    cv2.imshow('Наша вебка', frame) #frame это кадры
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()