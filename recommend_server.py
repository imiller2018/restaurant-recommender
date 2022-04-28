import socket, time
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
serverSocket.bind(("192.168.168.129",9090))
print(serverSocket.getsockname()[0])
serverSocket.listen()
received = []

while(len(received) < 1):

    (clientConnected, clientAddress) = serverSocket.accept()
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))

    dataFromClient = clientConnected.recv(1024)
    data_decode = dataFromClient.decode()
    print(data_decode)
    data_split = data_decode.split(',')
    print(data_split)
    received.append(data_split)

    clientConnected.send("Received.".encode())
"""
serverSocket.shutdown('SHUT_RDWR')
serverSocket.close()
""" 
location_ratings = {
    "McDonald's":[],
    "Wendy's":[],
    "Rathskeller Eatery":[],
    "Hardee's":[],
    "Outback Steakhouse":[],
    "Longhorns":[],
    "Mustard's Last Stand":[],
    "Chipotle":[],
    "Rain-Bo Island":[],
    "Panda Express":[],
    "Panera Bread":[],
    "Subway":[],
    "Amazing Food Place":[],
    "McDonald's but Expensive":[],
}

for user in received:
    data = user
    iter = 0
    for location in location_ratings:
        location_ratings[location].append(int(data[iter]))
        iter += 1

print(location_ratings)

location_satisfaction = {}

data_in_order = [
    "McDonald's",
    "Wendy's",
    "Rathskeller Eatery",
    "Hardee's",
    "Outback Steakhouse",
    "Longhorns",
    "Mustard's Last Stand",
    "Chipotle",
    "Rain-Bo Island",
    "Panda Express",
    "Panera Bread",
    "Subway",
    "Amazing Food Place",
    "McDonald's but Expensive",
]

'''
import pandas as pd
filename = "Restaurant Decision Maker (Responses) - Form Responses 1.csv"
df = pd.read_csv(filename)
print(df)
titles = [col_name for col_name in df.columns]
print(titles)

flagged = 0

for item in titles:
    if flagged:
        satis = [{"Yes":1, "No":0}[i] for i in df[item]]
        location_satisfaction[flagged] = satis
        flagged = 0
        print(satis)
    if item in location_ratings:
        ratings = [i for i in df[item]]
        location_ratings[item] = ratings
        print(ratings)
        flagged = item
'''

location_stats = { # stars, $s, time
    "McDonald's":[2.6, 1, 6],
    "Wendy's":[3.4, 1, 7],
    "Rathskeller Eatery":[3.7, 1, 2],
    "Hardee's":[4.4, 1, 4],
    "Outback Steakhouse":[4.2, 2, 7],
    "Longhorns":[4.0, 2, 14],
    "Mustard's Last Stand":[4.6, 1, 5],
    "Chipotle":[3.6, 1, 8],
    "Rain-Bo Island":[4.4, 1, 4],
    "Panda Express":[4.0, 1, 12],
    "Panera Bread":[4.1, 2, 13],
    "Subway":[4.0, 1, 8],
    "Amazing Food Place":[4, 8, 1],
    "McDonald's but Expensive":[4, 5, 5],
}

location_score = {}

def average_algorithm():
    location_score = {}
    for loc in location_ratings:
        location_score[loc] = sum(location_ratings[loc]) / len(location_ratings[loc])
    
    return location_score

def max_min():
    location_score = {}
    for loc in location_ratings:
        location_score[loc] = min(location_ratings[loc])
    return location_score

import numpy as np
from sklearn.linear_model import LinearRegression

reg_places = {}
res_places = {}
for iter in range(1):
    for name in location_ratings:
        value = location_stats[name]
        reg_places[name] = value
        value = [location_ratings[name][iter]]
        res_places[name] = value

x_data = [reg_places[name] for name in reg_places]
y_data = [res_places[name] for name in res_places]

print(x_data)
print(y_data)

# y = 1 * x_0 + 2 * x_1 + 3
X = np.array(x_data)
y = np.array(y_data)

reg = LinearRegression().fit(X, y)
print(reg.predict(np.array([[3, 1, 7]])))

def rank(scores):
    ranking = {}
    target = len(scores)
    while len(ranking) < target:
        max_value = max(scores, key=scores.get)
        ranking[max_value] = round(scores[max_value], 2)
        scores.pop(max_value)
    return ranking

print("\nScores with averaging:")
best = None
dict = rank(average_algorithm())
for k in dict:
    if best == None:
        best = k
    print(k, dict[k], " |  ")#, sum(location_satisfaction[k]), "/ 6")
    
print("\nScores with the highest lowest score:")
dict = rank(max_min())
for k in dict:
    print(k, dict[k], " |  ")#, sum(location_satisfaction[k]), "/ 6")
    
for user in received:
    ip = user[14]
    data = data_in_order.index(best)
    #print(data)
    str_data = str(data)
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    clientSocket.connect((ip, 9090))
    clientSocket.send(str_data.encode())
    dataFromServer = clientSocket.recv(1024)

    #print(dataFromServer.decode());
