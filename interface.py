import cv2


class Dashboard:
    def __init__(self):
        self.color_main = (0, 255, 0)  #Dahsboard at the top of box will be Green
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def draw(self, frame, result):
        # If no face, show scanning status
        if not result:
            cv2.putText(frame, "STATUS: SEARCHING...", (20, 40), self.font, 0.6, (0, 0, 255), 2)
            return frame

        x, y, w, h = result['x'], result['y'], result['w'], result['h']

        # 1. Draw Corners
        t = 100  # thickness
        cv2.line(frame, (x, y), (x + 40, y), self.color_main, 2)
        cv2.line(frame, (x, y), (x, y + 40), self.color_main, 2)
        cv2.line(frame, (x + w, y), (x + w - 40, y), self.color_main, 2)
        cv2.line(frame, (x + w, y), (x + w, y + 40), self.color_main, 2)

        # 2. Draw Emotion Bars on the left
        y_pos = 60
        for emotion, value in result['emotions'].items():
            # Bar Background
            cv2.rectangle(frame, (20, y_pos), (140, y_pos + 15), (40, 40, 40), -1)
            # Bar Fill
            bar_w = int((value / 100) * 120)
            cv2.rectangle(frame, (20, y_pos), (20 + bar_w, y_pos + 15), self.color_main, -1)
            # Label
            cv2.putText(frame, f"{emotion}", (20, y_pos - 5), self.font, 0.5, (255, 255, 255), 1)
            y_pos += 45

        # 3. Scanning line effect
        line_y = y + (int(cv2.getTickCount() / 1000000) % h)
        cv2.line(frame, (x, line_y), (x + w, line_y), (0, 255, 0), 1)

        return frame