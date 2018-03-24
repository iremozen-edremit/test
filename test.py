from cloudant.client import Cloudant
import pandas as pd
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

import plotly
plotly.tools.set_credentials_file(username='iremoze', api_key='N0pN2Vqt1NphEV7q8jLC')
import plotly.plotly as py
import plotly.graph_objs as go

serviceUsername = "7c8a4f57-32eb-4b8d-8d03-511763000d12-bluemix"
servicePassword = "8e2867d38e698bda88f1b7176688143719cf1fab09e11693a11c20993a50aef6"
serviceURL = "https://7c8a4f57-32eb-4b8d-8d03-511763000d12-bluemix:8e2867d38e698bda88f1b7176688143719cf1fab09e11693a11c20993a50aef6@7c8a4f57-32eb-4b8d-8d03-511763000d12-bluemix.cloudant.com"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

my_database1 = client['wunder']
#my_database3 = client['test']
#my_database2 = client.create_database('comfort2')
#my_database2 = client['comfort2']

databaseName = "test"
my_database3 = client.create_database(databaseName)

if my_database3.exists():
    print('SUCCESS!!')

for x in my_database1:
    print(x)

for item in my_database1:
    if (item['tempature'] == 13.2 ):
         item = {
            'tempature' : item['tempature'],
             '_id': item['_id'],
             '_rev' : item['_rev'],
             'weather': item['weather']

         }
         print('aa',item)
         #my_database2 = json.dumps (data)
         #print(item['tempature'])
         #print(item['_id'])
         #print(item)
         newDocument = my_database3.create_document(item)


print('SA!!')
for document in my_database3:
    print(document)


columns= list(my_database3)
print('ses', columns[1])

column_names = [col['tempature'] for col in columns]
print(column_names)


good_columns = [
    "tempature",
    "weather",
    "_rev",
    "_id"
]

#stops = pd.DataFrame(data1, columns=column_names)
#stops["color"].value_counts()

trace1 = go.Scatter(
    y = column_names,
    x=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
)
trace2 = go.Bar(
    x=[0, 1, 2, 3, 4, 5],
    y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
)

data = [trace1, trace2]
py.plot(data, filename='bar-line')