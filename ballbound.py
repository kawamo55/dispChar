#!/usr/bin/python3

import os
import time as tm

# スクリーン用配列
scr=[]
# X方向の枠
xline=''

# スクリーンとして使う配列を作成する
def initscr(x,y):
    global scr,xline
    # スクリーン用配列の初期化
    scr=[]
    # １行分のデータとX方向枠線を作る
    line=''
    for l in range(x):
        line += '　'
        xline += 'ー'
    # スクリーンデータを初期化する
    for l in range(y):
        scr.append(line)

# スクリーンを表示する
def dispScreen():
    global scr,xline
    # 'clear' はLinux用の画面クリアコマンド
    # Windowsコマンドプロンプトでは 'clear' を 'cls' に変更する
    os.system('clear')
    l = len(scr)
    print('+'+xline+'+')
    for y in range(l):
        print('|'+scr[y]+'|')
    print('+'+xline+'+')

# スクリーンにキャラクタをセットする
def setChar(x,y,c):
    global scr
    scr[y]=scr[y][:x]+c+scr[y][x+1:]
    
# スタート位置座標
px, py = (8,2)
# 動かす幅
mx, my = (1,1)
# スクリーンサイズ
wx, wy = (30, 20)
initscr(wx, wy)

#  ボールを動かす
while True:
    cx,cy = (px,py)
    setChar(px,py,'●')
    dispScreen( )
    print(px,py)
    px += mx
    py += my
    setChar(cx,cy,'　')
    if px >= wx-1:
        mx *= -1
    if py >= wy-1:
        my *= -1
    if px < 1:
        mx *= -1
    if py < 1:
        my *= -1
    tm.sleep(0.1)

