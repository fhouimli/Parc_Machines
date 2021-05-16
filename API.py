import parcMachines
from flask import Flask, jsonify,request



########### API #############

app = Flask(__name__)

@app.route("/machine",methods=["GET"])
def getAllAPI():
  return parcMachines.listAllMachines("listMachines.txt")

@app.route("/machine/<hostname>", methods=["GET"])
def getByIdAPI(hostname):
    #print('hostname ======' +hostname)
    m1 =parcMachines.listMachineByHostname(hostname)
    return (m1)

@app.route('/machine/addorupdate', methods=['POST'])
def createAPI():
   data = request.get_json()
   nom= data.get('nom', '')
   ip= data.get('ip', '')
   cpu= data.get('cpu', '')
   ram= data.get('ram', '')
   ddr= data.get('ddr', '')
   os= data.get('os', '')
   m1 = parcMachines.Machines(nom,ip,cpu,ram,ddr,os)
   parcMachines.createOrUpdate(m1)
   return "Creation de l'hote "+nom+" est enregistré avec succès !!"

@app.route('/machine/del/<host>', methods=['DELETE'])
def deleteApi(host):
  parcMachines.delete(host)
  return "le host "+host+" est supprimé avec succès !!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')