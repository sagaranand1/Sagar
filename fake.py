import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from gtts import gTTS
import os

path = 'C:/Users/HP/Desktop/projects/MP2/'
def main()
#if __name__ == "__main__":
     print("Check point")
     aWeight = 0.5
     camera = cv2.VideoCapture(0)
     top, right, bottom, left = 10, 350, 225, 590
     num_frames = 0
     while(True):
            num_frames=num_frames+1
            (grabbed, frame)=camera.read()
            note = frame.copy();  
            gray = cv2.cvtColor(note, cv2.COLOR_BGR2GRAY)  
            num = cv2.cvtColor(note, cv2.COLOR_BGR2GRAY)
            
            _, th1 = cv2.threshold(gray, 0, 256, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  
            
            edges = cv2.Canny(note, 390, 270)
            
            kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]]
                  )

            img_sharpened = cv2.filter2D(edges, -1, kernel)
            
            hist, bins = np.histogram(edges.flatten(), 256, [0, 11])  
            plt.plot(hist, color='b')  
            plt.hist(edges.flatten(), 25, [0, 250], color='r')  

            cdf = hist.cumsum()  
            cdf_normalized = cdf * hist.max() / cdf.max()

            hist, bins = np.histogram(img_sharpened.flatten(), 256, [0, 256])  
            plt.plot(hist, color='b')  
            plt.hist(img_sharpened.flatten(), 256, [0, 256], color='r')  

            cdf = hist.cumsum()  
            cdf_normalized1 = cdf * hist.max() / cdf.max()

            plt.subplot(131)
            plt.plot(cdf_normalized, color='g')  
            plt.hist(edges.flatten(), 25, [0, 250], color='r')  
            plt.xlim([0, 250]), plt.ylim([0, 600000])
            plt.title('without filter')
            plt.legend(('','noise'), loc='lower right')
            plt.subplot(133)
            plt.plot(cdf_normalized1, color='g')  
            plt.hist(img_sharpened.flatten(), 256, [0, 25], color='r') 
            plt.xlim([0, 250]), plt.ylim([0, 600000])
            plt.title('with filter')
            plt.legend((' ','noise'), loc='lower right')

            gray_blur= cv2.GaussianBlur(gray, (15, 15), 0)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            kernel = np.ones((1, 1), np.uint8)
            closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
                                       kernel, iterations=4)
            contours,_= cv2.findContours( closing.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                if  cv2.contourArea(cnt) > 300:
                    ellipse = cv2.fitEllipse(cnt)
                    cv2.ellipse(gray, ellipse, (0, 255, 0), 2)
            cv2.imshow('Contours', gray)
            cv2.waitKey()
            cv2.destroyWindow('Contours')
    
            stats1=pd.read_csv(path +'bank_note_data.csv')

            i=1
            
            stats=pd.read_csv(path +'book'+str(i)+'.csv')
            


            orb = cv2.ORB_create()
            kp1, des1 = orb.detectAndCompute(num, None)
            kp2, des2 = orb.detectAndCompute(num, None)

            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)

            matching_result = cv2.drawMatches(num, kp1, num, kp2, matches[:100], None, flags=2)
            re = cv2.resize(matching_result, (1200, 600))
            
            table=pd.read_csv(path +'table'+str(i)+'.csv')
            
            df=pd.read_csv(path +'table'+str(i)+'.csv') 
            val = df.iloc[:,1].values
            ans=(int(val[0])+int(val[1])+int(val[2])+int(val[3])+int(val[4]))/5;
            final='please try again'
            if ans>=70:
              final='the note is genuine!'
            else:
              final='the note is fake!'
            if num_frames%800==0 and num_frames!=0:
              myobj = gTTS(final,'en') 
              myobj.save("result.mp3") 
              os.system("result.mp3")
            keypress = cv2.waitKey(1) & 0xFF
            if keypress == 27:
                break
     camera.release()
     cv2.destroyAllWindows()
