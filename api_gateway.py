from flask import Flask,jsonify
from sqllib import cek_ruangan, input_data,cek_data,update_data

app = Flask(__name__)


@app.route('/indoor/input/data/<uuid>/<suhu>/<detak_jtg>/<saturasi>/<ruangan>',methods=['POST'])
def data_input(uuid,suhu,detak_jtg,saturasi,ruangan):
    cek = cek_data(uuid)
    if cek==False:
        cek_posisi = cek_ruangan(uuid,ruangan)
        if cek_posisi == False:
            status = "Forbiddden"
            input_data(uuid,suhu,detak_jtg,saturasi,ruangan,status)
            result = {"message":status}
            resp = jsonify(result)
            return resp,203
        else:
            status = "Allow"
            input_data(uuid,suhu,detak_jtg,saturasi,ruangan,status)
            result = {"message":status}
            resp = jsonify(result)
            return resp,200
    else:
        cek_posisi = cek_ruangan(uuid,ruangan)
        if cek_posisi == False:
            status = "Forbiddden"
            update_data(suhu,detak_jtg,saturasi,ruangan,status,uuid)
            result = {"message":status}
            resp = jsonify(result)
            return resp,203
        else:
            status = "Allow"
            update_data(suhu,detak_jtg,saturasi,ruangan,status,uuid)
            result = {"message":status}
            resp = jsonify(result)
            return resp,200


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=2001)
    app.run(port=2001, debug=True,host="0.0.0.0")