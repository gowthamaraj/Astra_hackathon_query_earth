import cv2
import numpy as np
import matplotlib.pyplot as plt



from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)

client.create_database('network')
client.switch_database('network')




 
cap=cv2.VideoCapture('change.mp4')

old_frame = None
total = 0

while True:

    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if old_frame is not None:
            diff_frame = gray - old_frame
            diff_frame -= diff_frame.min()
            disp_frame = np.uint8(255.0*diff_frame/float(diff_frame.max()))
            retval, threshold = cv2.threshold(disp_frame, 127, 255, cv2.THRESH_BINARY)
            cv2.imshow('diff_frame',threshold)
            disp_frame = cv2.resize(disp_frame,(100,100))
            x,y = disp_frame.shape
            for i in range(x):
                for j in range(y):
                    if disp_frame[i][j]==disp_frame.max():
                        total = total +1;
                        
            json_body = [
            {
            "measurement": "astra",
            "tags": {
            "user": "impact",
            },
            "fields": {
            "tot": total,    
            }
            }
            ]
            client.write_points(json_body)           
                        
                        
                        
            
        old_frame = gray
        
        print(total)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        print('over')
        break

cap.release()
cv2.destroyAllWindows()

