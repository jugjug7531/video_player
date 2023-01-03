import cv2

FPS = 60
VIDEO_PATH = 'videos/sample.avi'
PAUSE_IMAGE_PATH = 'img/black.png'
ASCII_SPACEKEY = 32

# 一時停止フラグ
is_playing = False

# 一時停止用画像読み込み
pause_img = cv2.imread(PAUSE_IMAGE_PATH)
# エラー処理
if (pause_img is None):  
  print("画像ファイルを開くとエラーが発生しました") 

# 動画読み込み
cap = cv2.VideoCapture(VIDEO_PATH)
# エラー処理
if (cap.isOpened()== False):  
  print("ビデオファイルを開くとエラーが発生しました") 

# 動画再生開始
is_playing = True
while(cap.isOpened()):
    if is_playing:
        # フレーム取得
        ret, frame = cap.read()
        if ret:
            # フレーム表示
            cv2.imshow("Video", frame)
        else:
            break

    # 再生中に押されたキーを取得する
    key = cv2.waitKey(int(1000/FPS))
    if key & 0xFF == ASCII_SPACEKEY:
        is_playing = not is_playing
        cv2.imshow("Video", pause_img)
    elif key & 0xFF == ord('q'): 
        break

cv2.waitKey(0)

# 終了処理
cap.release()
cv2.destroyAllWindows()