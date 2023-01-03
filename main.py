import cv2

FPS = 60
VIDEO_PATH = 'videos/sample.avi'


# 動画読み込み
cap = cv2.VideoCapture(VIDEO_PATH)
# エラー処理
if (cap.isOpened()== False):  
  print("ビデオファイルを開くとエラーが発生しました") 

# 動画再生開始
while(cap.isOpened()):
    # フレーム取得
    ret, frame = cap.read()
    if ret:
        # フレーム表示
        cv2.imshow("Video", frame)
        # 再生中に押されたキーを取得する
        key = cv2.waitKey(int(1000/FPS))
        if  key & 0xFF == ord('q'): 
            break
    else:
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()