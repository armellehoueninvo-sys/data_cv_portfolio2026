# OpenCV Basics - Week 1
# Test OpenCV installation and basic image operations

import cv2
import numpy as np

print("✓ OpenCV version:", cv2.__version__)

# Create a simple image (blue rectangle with text)
image = np.zeros((300, 400, 3), dtype=np.uint8)

# Draw rectangle (BGR format: Blue, Green, Red)
cv2.rectangle(image, (50, 50), (350, 250), (255, 0, 0), 3)

# Add text
cv2.putText(image, 'OpenCV Works!', (100, 150), 
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

# Save image
cv2.imwrite('output.jpg', image)

print("✓ Image created and saved as output.jpg")
```

**Clique "Commit new file"**

---

## ✅ Après avoir créé les 2 fichiers

Clique le logo GitHub pour voir la structure complète

Tu dois avoir :
```
📁 data-analyst/
   ├── README.md ✓
   └── sql-queries/
       └── queries.sql ✓

📁 computer-vision/
   ├── README.md ✓
   └── scripts/
       └── openCV_basics.py ✓
