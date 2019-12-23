import cv2
import matplotlib.pyplot as plt

image = cv2.imread('../Crawling/img/lena1.png') # 이미지를 불러온다

edges = cv2.Canny(image, 200, 100)  # Canny 알고리즘을 사용해 edges를 검출한다

plt.figure(figsize=(8,5))
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(image[:,:,[2,1,0]])
plt.subplot(122)
plt.axis('off')
plt.title('edges')
plt.imshow(edges, cmap='gray')
plt.tight_layout()
plt.show()
