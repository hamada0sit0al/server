import datetime
import csv
from flask import Flask, request, render_template
name = './' + str(datetime.date.today())
file_path = name + '.csv'

app = Flask(__name__) 

my_port = 16082 
 
@app.route('/', methods=['GET']) 
def get_html():   
    return render_template('./index.html')    

@app.route('/second', methods=['POST']) 
def update_second():   
    time = request.form["time"]   
    second = request.form["second"]
    print(second)   
    try:     
        f = open(file_path, 'a')     
        f.write(time + "," + second + "\n")     
        return "succeeded to write"   
    except Exception as e:
        print(e)     
        return "failed to write"   
    finally:     
        f.close() 
 
@app.route('/second', methods=['GET']) 
def get_second():   
    try:     
        f = open(file_path, 'r')     
        for row in f:        
            second = row[17:]
        print(type(second))
        temp = int(second) / 3600
        hour = str(int(temp))
        temp = (int(second) / 60) - int(hour)*60 
        minute = str(int(temp))
        date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
        data = date + " 現在<br>計 " + hour + " 時間 " + minute + " 分在席"    
        return data   
    except Exception as e:     
        print(e)     
        return e   
    finally:     
        f.close() 
 
if __name__ == '__main__':     
    app.run(debug=True, host='0.0.0.0', port=my_port)