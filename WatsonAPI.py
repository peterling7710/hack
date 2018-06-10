import ibmiotf.application

#File or array for options
'''
options = ibmiotf.application.ParseConfigFile(configFilePath)
options = options = {
    "org": "w2r0su",
    "id": "1",
    "auth-method": myEventCallback,
    "auth-key": username,
    "auth-token": password,
    "clean-session": True
  }


username = "a-w2rosu-ypnrx9rtvj"
password = "_SLVi(v*rwEKTQF9YU"
'''

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
#url = "https://<w2r0su>.internetofthings.ibmcloud.com/api/v0002"
#res = request.get(url)
#data = res.json()
'''
client = ibmiotf.application.Client(options)
client.connect()
client.deviceEventCallback = myEventCallback
client.subscribeToDeviceEvents()
#lights.append(light)

#Pick One
def myEventCallback(event):
  str = "%s event '%s' received from device [%s]: %s"
  print(str % (event.format, event.event, event.device, json.dumps(event.data)))

def myEventCallback(event):
    data = event.data
    ret(data)
'''
