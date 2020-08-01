import  cv2

img = cv2.imread('cinder.jpeg')
w = img.shape[1]
h = img.shape[0]

divider_x = 4 
divider_y = 3
part_count = 0

for x in range(0, w, w//divider_x):
    for y in range(0, h, h//divider_y):
        img_part = img[y:y+h//divider_y, x:x+w//divider_x]
        img_part = cv2.putText(img_part, str(part_count), (20,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 4)
        part_with_id = (img_part, part_count)
        cv2.imshow('out', img_part)
        cv2.imwrite('part{}.jpg'.format(part_count), img_part)
        cv2.waitKey(1)
        part_count+=1
