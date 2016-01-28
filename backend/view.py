from uuid import uuid4
from flask import jsonify
from flask.ext.cors import cross_origin
from pydoop import hdfs
from wsgi import app

__author__ = 'an'

@app.route('/')
@cross_origin()
def index():
	n = 'NongNghiep.mp4'
	d = str(uuid4())

	hdfs.get('/video/{}'.format(n), '/usr/share/nginx/html/ver2/video/{}/{}'.format(d, n))
	data = {
		'directory': 'video/{}/{}'.format(d, n)
	}
	return jsonify(data)