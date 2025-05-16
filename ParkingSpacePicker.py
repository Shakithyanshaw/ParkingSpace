import cv2
import pickle

# Define standard dimensions for a single parking space
width, height = 107, 48

# Try to load saved parking positions from a file using pickle
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)  # Load list of parking space positions
except:
    posList = []  # If file not found or any error, initialize empty list

# Function to handle mouse events on the image
def mouseClick(events, x, y, flags, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i) 

# Save updated parking positions to file
with open('CarParkPos', 'wb') as f:
    pickle.dump(posList, f)

# Infinite loop to display the image and handle mouse clicks
while True:
    img = cv2.imread('carParkImg.png')  

    # Draw rectangles over the image to show defined parking spaces
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 2)

    cv2.imshow("image", img) 
    cv2.setMouseCallback("image", mouseClick)  
    key = cv2.waitKey(1)  
