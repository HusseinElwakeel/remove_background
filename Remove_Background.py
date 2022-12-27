from rembg import remove     #to remove background
import cv2                   #for computer vision

input_path ="watch.jpg"               # path for photo want to remove BG
output_path ="watch_without_BG.png"   #path for new photo

input =cv2.imread(input_path)         #use cv to read photo
output =remove(input)                 #to remove BG from input

cv2.imwrite(output_path,output)       #to write output photo without BG

cv2.imshow("w.png",output)            #show photo after remove BG with same name of output_path

if cv2.waitkey(0) & 0Xff==ord("h"):
    cv2.close()
    cv2.destroyAllWindows()
