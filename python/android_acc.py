
#import pygame_sdl2

# Pyjniusを利用して、JavaのクラスをPythonのオブジェクトとして取り出す
from  jnius import autoclass

# センサーなどのハードウェア関係の機能を利用する
# (org.renpy.android.Hardwareクラスの取得)
hw = autoclass('org.renpy.android.Hardware')

# 加速度センサーを利用可能にする
hw.accelerometerEnable(True)

# 0.5秒待つ
import time
time.sleep(0.5)

# 加速度の取得
a = []
t = []
step = 0.01
for i in range(100):
	ax, ay, az = hw.accelerometerReading()
	a.append([ax,ay,az])
	time.sleep(step)
	t.append( len(t) )

# ファイルに保存
with open('test.txt', 'w') as f:
	for ax, ay, az in a:
		f.write('{0},{1},{2}\n'.format(ax,ay,az))
	
	import numpy as np
	ave = np.average(np.array(a),axis=0)
	f.write('\n')
	f.write('{0},{1},{2}\n'.format(ave[0],ave[1],ave[2]))


# グラフ化
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(2,1,1)

nt = np.array(t)
na = np.array(a)
ax.plot(nt, na)
#ax.set_ylim([0,15])

ax2 = fig.add_subplot(2,1,2)
norm = []
for ax, ay, az in a:
	norm.append(np.sqrt(ax**2+ay**2+az**2))
ax2.plot(nt, np.array(norm))
#ax2.set_ylim([0,15])

fig.savefig('test.png')
fig.clf()
plt.close(fig)
