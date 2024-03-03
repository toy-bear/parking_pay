寒假小作，整理一下分享。
使用paddleocr超轻量级模型"ch_pp-ocrv3"https://github.com/PaddlePaddle/PaddleOCR模型识别汽车牌照，通过记录相同牌照进出时间，计算停车费用。付费模块因为付费授权原因没有加入。时间关系，记录显示格式也没有调整。
进场和出场图片保存在D:/paizhao目录下，时间戳作为文件名。付款二维码保存在D:/paizhao下，文件名qrcode.jpg，实时刷新。模型处理完图片存放在D:/ocr下，包含置信度。
提供一个demo运行视频。
环境
torch 2.0.0
paddleaddle 2.6.0
python 3.8.18
win11 cpu