import cv2
import numpy as np
import pyautogui

template_paths = ['assets/safe_zone.png', 'assets/safe_zone_out.jpg']
top_y = 840
bottom_y = 960
threshold = 0.6

while True:
    screenshot = pyautogui.screenshot(region=(0, top_y, pyautogui.size().width, bottom_y - top_y))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    for template_path in template_paths:
        template = cv2.imread(template_path, cv2.IMREAD_COLOR)
        if template is None:
            continue

        template_height, template_width = template.shape[:2]
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        if len(locations) > 0:
            for loc in locations:
                center_x = loc[0] + template_width // 2
                center_y = loc[1] + template_height // 2 + top_y
                print(f"Match at x={center_x}, y={center_y}")