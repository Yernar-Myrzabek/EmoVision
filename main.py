import cv2
from engine import EmotionEngine
from interface import Dashboard


def main():
    # Initialize Camera
    cap = cv2.VideoCapture(0)

    # Initialize our Modules
    engine = EmotionEngine()
    interface = Dashboard()

    print("--- EmotionSentiment AI Active ---")
    print("Press 'q' to exit the system.")

    while True:
        ret, frame = cap.read()#Readnsingle frame from the camera
        if not ret:
            break

        # Flip frame for a "mirror" effect
        frame = cv2.flip(frame, 1)

        #Run AI Logic
        result = engine.analyze_frame(frame)

        #Run UI Rendering
        frame = interface.draw(frame, result)

        #Show Window
        cv2.imshow('EmotionSentiment AI Terminal', frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()