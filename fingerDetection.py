import cv2
import mediapipe as mp
import pyautogui
import time
import threading
import keyboard

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
oldy = 0
newtime = 0
oldx = 0
threshold = 50
pyautogui.FAILSAFE = False
blink = True
def toggle(test):
    global blink
    if test:
        pyautogui.mouseDown()
        blink = False
    else:
        pyautogui.mouseUp()
        blink = True
arr = []

def mouseMove(x,y):
    pyautogui.moveRel(x,y,_pause=False)

def mouseThread(x,y):
    mouse_thread = threading.Thread(target=mouseMove, args=(x, y), daemon=True)
    mouse_thread.start()

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            currtime = time.time()
            # Access the pointer fingertip (Landmark 8)
            pointer_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            height, width, _ = frame.shape
            x, y = int(pointer_tip.x * width), int(pointer_tip.y * height)
            x1, y1 = int(thumb_tip.x * width), int(thumb_tip.y * height)
            x2, y2 = (int(middle_tip.x * width), int(middle_tip.y * height))
            x3, y3 = int(ring_tip.x * width), int(ring_tip.y * height)
            # Draw circle on the fingertip
            if abs(x-x1) < threshold and abs(y-y1) < threshold:
                pyautogui.moveRel(-.5*(x1-oldx),.5*(y1-oldy))
                color = (0, 0, 255)
            else:
                color = (0, 255, 0)
            if abs(x1 - x2) < threshold and abs(y1 - y2) < threshold:
                pyautogui.click()
                newtime = time.time()
                color = (255, 0, 0)
            if abs(x1 - x3) < threshold and abs(y1 - y3) < threshold:
                toggle(True)
                arr.append([-.5 * (x1 - oldx), .5 * (y1 - oldy)])
                smoothx = (-.5 * (x1 - oldx)) ** (1/3)
                smoothy = (.5 * (y1 - oldy)) ** (1/3)
                mouseThread(smoothx, smoothy)
                color = (255, 0, 0)
                toggle(False)


            cv2.circle(frame, (x, y), 10, color, -1)
            oldx = x1
            oldy = y1


            # Draw circle on the fingertip
            cv2.circle(frame, (x1, y1), 10, color, -1)
            cv2.circle(frame, (x2, y2), 10, color, -1)
            cv2.circle(frame, (x3, y3), 10, color, -1)
            # Draw landmarks
            #mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
