from flask import Flask, redirect, url_for, render_template, request, flash, send_file
app = Flask('app')
@app.route('/')
def home():
  ip_address = request.remote_addr
  print(ip_address)
  return send_file('rckrl.gif', mimetype = 'image/gif')
app.run(host='0.0.0.0', port=8080)
