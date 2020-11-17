from flask import Flask, redirect, url_for, request,make_response
import os
import sys
import cv2

from app.jartesting2 import newjar2


app = Flask(__name__,static_url_path='/static')

@app.route('/success/<name>')
def success(name):
    
    imgpath="/static/newimg.png"
    img = cv2.imread(imgpath)
    retval, buffer = cv2.imencode('.png',img)
    response = make_response(buffer.tobytes())
    response.headers['Content-Type'] = 'image/png'
    return response 


@app.route('/login',methods = ['POST', 'GET'])
def login():
    
    
    imgpath = "/static/jar2.jpg"
    if request.method == 'POST':
        
        player_name=request.form['nm']
        
        
        number_of_balls= request.form.get('nbb',type = int)
        
        
        switcher={"Red":"0","Orange":"1",'Yellow':"2","Green":"3",'Blue':"4",'Indigo':'5','Violet':6}
        
        color_of_balls = request.form.get("rating")
        color_of_balls=int(switcher.get(color_of_balls))
        
        newjar2(number_of_balls,color_of_balls,imgpath)
        
        return redirect(url_for('success',name = player_name))
    else:
        player_name=request.args.get['nm']
        
        number_of_balls= request.args.get('nbb',type=int)
        
        
        switcher={"Red":"0","Orange":"1",'Yellow':"2","Green":"3",'Blue':"4",'Indigo':'5','Violet':6}
        color_of_balls = request.args.get("colour")
        color_of_balls=int(switcher.get(color_of_balls))
        newjar2(number_of_balls,color_of_balls,imgpath)
        return redirect(url_for('success',name = player_name))

if __name__ == '__main__':
    
    app.run(debug = True)
