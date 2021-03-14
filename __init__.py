from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
from modules.core.props import Property
import httplib2
from flask import request
import base64

@cbpi.actor
class TasmotaSocket(ActorBase):

    host = Property.Text("IP or DNS Name", configurable=True, default_value="10.0.2.153")
    # Command so swtich wifi socket on
    onCommand = "On"
    # Command so swtich wifi socket off
    offCommand = "Off"

    def send(self,  command):
        try:
            h = httplib2.Http()
            ## Sending http command ""
            content = h.request("http://%s/cm?cmnd=Power%20%s" % (self.host, command), "GET")[1]
        except Exception as e:
            self.api.app.logger.error("FAIELD to switch Tasmota socket %s Command: %s" % (self.host, command))

    def on(self, power=100):
        self.send(self.onCommand)

    def off(self):
        self.send(self.offCommand)


