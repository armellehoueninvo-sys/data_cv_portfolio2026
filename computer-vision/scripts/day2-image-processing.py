# Day 2 - Image Processing with OpenCV
# Grayscale, Blur, Edge Detection

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

print("✓ Day 2 - Image Processing")

# Create sample image
image = np.random.randint(0, 256, (300, 400, 3), dtype=np.uint8)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Edge detection (Canny)
edges = cv2.Canny(gray, 100, 200)

print("✓ Grayscale created")
print("✓ Blur applied")
print("✓ Edges detected")

# Display
cv2_imshow("Original", image)
cv2_imshow("Grayscale", gray)
cv2_imshow("Blurred", blurred)
cv2_imshow("Edges", edges)
```

5. Clique **"Commit new file"**

---

## 📊 ÇA DONNE QUOI APRÈS?

Ton repo ressemblera à ça :
```
📁 data-analyst/
   ├── README.md
   └── sql-queries/
       ├── queries.sql (Day 1)
       └── day2-groupby.sql (Day 2) ← NOUVEAU

📁 computer-vision/
   ├── README.md
   └── scripts/
       ├── openCV_basics.py (Day 1)
       └── day2-image-processing.py (Day 2) ← NOUVEAU
