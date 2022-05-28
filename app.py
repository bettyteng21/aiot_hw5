from flask import Flask
from flask import render_template
import pymysql

app = Flask(__name__)
@app.route('/')
def index():
  # 連結database
  conn = pymysql.connect(host='localhost',user='test123',password='test123',db='aiotdb')
  cur = conn.cursor()

  # 從資料庫撈我要的值，並執行 SQL 指令
  sql = "SELECT `id`,`time`,`value`,`temp`,`humi`,`status` FROM sensors"
  try:
    cur.execute(sql)
    data = cur.fetchall() # 取出全部的資料
  except:
    print("Error: unable to fetch data")

  # 關閉 SQL 連線
  conn.close()
  return render_template('index.html',data=data)

if __name__ == '__main__':
  app.debug = True
  app.run(port=8003)