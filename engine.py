import cv2


class EmotionEngine:
    def __init__(self):
        # Using built-in OpenCV filters (No downloads needed)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    def analyze_frame(self, frame):
        #Convert to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Face coordinates
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            roi_gray = gray[y:y + h, x:x + w]

            #Feature Extraction
            smiles = self.smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
            eyes = self.eye_cascade.detectMultiScale(roi_gray, 1.1, 10)

            # 3. Decision Logic (Heuristic Classifier)
            is_happy = len(smiles) > 0
            eye_count = len(eyes)

            # Default values
            angry = 0
            sad = 0
            neutral = 0

            if is_happy:
                happy = 100
            else:
                happy = 0
                # If eyes are closed/squinted and no smile -> Angry
                if eye_count < 2:
                    angry = 85
                # If eyes are present but low in the face -> Sad
                elif any(e[1] > h * 0.35 for e in eyes):
                    sad = 75
                else:
                    neutral = 100

            return {
                'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h),
                'emotions': {
                    'Happy': happy,
                    'Angry': angry,
                    'Sad': sad,
                    'Neutral': neutral
                }
            }
        return None