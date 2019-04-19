#!/usr/bin/env python
# coding: utf-8

# In[45]:


#作業1:
    #Kobe Bryant Shot Selection
#1. 你選的這組資料為何重要
   #可用以分析球員的出手選擇習慣、命中效率，藉以制定防守、進攻策略以及訓練方針
#2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)
   #stats.nba.com(官方提供)
#3. 蒐集而來的資料型態為何
   #繪製成點狀圖、條狀圖，製作成投球熱點，出場時間點紀錄
#4. 這組資料想解決的問題如何評估
   #製作出圖表可發現許多事:Kobe投球偏好使用右手(慣用手)，不論投球比例跟命中率都高左手一個層級，便可以利用這點做戰術設計   
#作業2:
#自由載客車隊:優勢:相比Uber有更多經營用車，可隨時採點等待
            #劣勢:因為有車子的所有權，必須負擔很重的汽車稅等成本，在淡季時會使車隊有沉重的成本壓力
#1. 核心問題: 
   #提生業績相當於提高淨收入，其中包括提高收入以及減低成本
#2. 資料從何而來:
   #過往的營業紀錄中，可以發現主要的載客地點分布
#3. 蒐集而來的資料型態為何:
  # 可以以點在地圖上做出載客地點的紀錄，製成點狀圖。可單純以一次為一點，亦可將地點分成小區塊，紀錄區塊中的載客次數，
  # 並以點的大小/顏色(例: 載客次越數多，則點越大)紀錄
#4. 你要回答的問題，其如何評估:
  # 可針對較多客源的地點進行蹲點，以增加載客的比例，增加單位營收。放棄部分載客數據較差的地區，僅在數據稍微不差的地點進行設點，
  # 可做到在不大幅提高成本的情況下，保持生意差區域的服務。
  # 評估:檢測車隊的總體淨收入、總體營業區塊(若營業區塊過小，可能造成客人過度外流)、載客人次等
#作業3:

## 練習時間
#### 請寫一個函式用來計算 Mean Square Error
$ MSE = \frac{1}{n}\sum_{i=1}^{n}{(Y_i - \hat{Y}_i)^2} $

### Hint: [如何取平方](https://googoodesign.gitbooks.io/-ezpython/unit-1.html)


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


def mean_absolute_error(y,yp):
    """
    y = 實際值 ; yp = 預測值
    """
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

def mean_squared_error(y, yp):
    return sum((y-yp)**2) / len(y)


# In[46]:


w = 3
b = 0.5

x_lin = np.linspace(0, 100, 101)

y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()


# In[47]:


y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()


# In[48]:


# 執行 Function, 確認有沒有正常執行
MSE = mean_squared_error(y, y_hat)
MAE = mean_absolute_error(y, y_hat)
print("The Mean squared error is %.3f" % (MSE))
print("The Mean absolute error is %.3f" % (MAE))


# In[ ]:





# In[ ]:





# In[ ]:




