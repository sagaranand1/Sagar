from keras.models import load_model
import cv2
import numpy as np
from gtts import gTTS 
import os

def main():
#if __name__ == "__main__":
    aWeight = 0.5
    camera = cv2.VideoCapture(0)
    top, right, bottom, left = 10, 350, 225, 590
    num_frames = 0
    model = load_model('D:/retrain.h5')

    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
    while(True):
       (grabbed, frame)=camera.read()
       img=frame.copy();
       img = cv2.resize(img,(150,150))
       img = np.reshape(img,[1,150,150,3])
       num_frames=num_frames+1
       classes = model.predict_classes(img)
       note=''
       if classes==[[0]]:
          note='2000'
       else:
           note='500'
       cv2.putText(frame,note, (25,40), cv2.FONT_HERSHEY_SIMPLEX, 2,(51,255,51) ,2)
       cv2.imshow("Video Feed", frame)
       if num_frames%800==0 and num_frames!=0:
          mytext = 'this is a'+note+' rupee note'
          language = 'en'
          myobj = gTTS(text=mytext, lang=language, slow=False) 
          myobj.save("final.mp3") 
          os.system("final.mp3")
       keypress = cv2.waitKey(1) & 0xFF
       if keypress == 27:
          camera.release()  
          break
    camera.release() 
    cv2.destroyAllWindows()
