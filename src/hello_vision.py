import cv2

# print(cv2.__version__)
img = cv2.imread(r"../images/laotie.jpeg")

if img is not None:
    # print(img.shape)
    # print(help(img))
    out_path = r"F:\workspace\vision01\output\laotie_copy.jpeg"
    cv2.imwrite(out_path, img)
else:
    print("读取图片失败")
