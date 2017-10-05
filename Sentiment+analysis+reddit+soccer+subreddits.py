
# coding: utf-8

# In[12]:

import requests
import requests.auth
import string
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[13]:

file = open("C:/Users/Darran_K/Documents/posText.txt", "r") 
file2 = open("C:/Users/Darran_K/Documents/negText.txt", "r")


# In[14]:

remove = dict.fromkeys(map(ord, '\n ' + string.punctuation))
posText = []
negText = []
for i in file:    
    posText.append(i.translate(remove))
for i in file2:    
    negText.append(i.translate(remove))


# change user to bot user
# this is the request for Oauth Token
# https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example

# In[15]:

client_auth = requests.auth.HTTPBasicAuth('JM2v20V0nwD5Gw', 'dTPjPXHLCHjufL8pGkXOoEsyKqo')
post_data = {"grant_type": "password", "username": "sentiment_bot12", "password": "26gIDbtk37Et"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
print(response.json())


# In[16]:

headers = {"Authorization": "bearer rv0lnbKdxWobQtva-2vg9yCYZRo", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"}
params = {"t" : "week"}
response = requests.get("https://oauth.reddit.com/r/gunners/top", headers = headers, params = params)
gunners_top = response.json()


# In[17]:

gunners_top_posts = gunners_top["data"]["children"]
print(gunners_top_posts[0]["data"]["id"])
post_ids = []
for i in gunners_top_posts:
    postId = i["data"]["id"]
    post_ids.append(postId)


print(len(post_ids))


# In[18]:

address = "https://oauth.reddit.com/r/gunners/comments/"
allComms = []
for i in range(0,100):
    ad = address + post_ids[i]
    response = requests.get(ad, headers = headers)
    comments = response.json()
    allComms.append(comments)


# In[19]:

comms = []
dataDump = "Start//"
for i in range(0,99):
    comments = allComms[i][1]["data"]["children"]
    for j in range(0, len(comments)-1):
            comms.append(allComms[i][1]["data"]["children"][j]["data"]["body"])
            dataDump = dataDump + " " + allComms[i][1]["data"]["children"][j]["data"]["body"]


# In[20]:

dataList = dataDump.split(" ")


j=0
for i in range(0,len(dataList)):
    dataList[i] = dataList[i].translate(remove)
    


# In[21]:

negScore =0
posScore = 0
neutral = 0
for i in dataList:
    if i in negText:
        negScore +=1
    elif i in posText:
        posScore +=1
    else:
        neutral +=1


# In[31]:

print( negScore)
print(posScore)
print(neutral)

ratioP = posScore/(neutral + posScore + negScore)
ratioN = negScore/(neutral + posScore + negScore)
p2n = posScore/negScore
print(ratioP)
print(ratioN)
print(p2n)
plt.bar([1,2], [ratioP, ratioN], 1, color = "blue")
plt.show()


# Team:
# * Ratio of positive terms/total
# * Ratio of negative terms/total
# * Ratio of positive/Negative
# 
# Gunners:
# * 0.04897
# * 0.02688
# * 1.82214
# 
# Liverpool:
# * 0.04155
# * 0.03834
# * 1.08375
# 
# Chelsea:
# * 0.05006
# * 0.03011
# * 1.66238
# 
# Manchester City:
# * 0.0486
# * 0.0263
# * 1.8494
# 
# Manchester United:
# * 0.0455
# * 0.0284
# * 1.6029
# 
# Findings:
# From the results we can see that most subreddits have a positive "vibe". This is expected as they are fans of their team and is an enjoyable hobby. However we can see that in the subreddits with teams that had "poor" results the ratio of pos/neg drops. 
# Improvements:
#     1. check further down comment tree
#     2. compare to more weeks/team form
#     3. use Match threads/Post match Threads

# Date 02/10/17
# <h3>results:</h3>
#     * Arsenal v Brighton (2-0)
#     * Liverpool v Newcastle (1-1)
#     * Chelsea v Manchester City (0-1)
#     * Manchester City v Chelsea (1-0)
#     * Manchester United v Crystal Palace (4-0)

# In[ ]:



