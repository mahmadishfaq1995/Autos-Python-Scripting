import MySQLdb
db = MySQLdb.connect(host="inspection-pro-stage.cs1it6yrzvdt.ap-southeast-1.rds.amazonaws.com"
                     ,user="mahmad",db="inspection_pro_stage",passwd="gK9dgljAd7hHyw") #port=3306

with db:
    cur = db.cursor()
    cur.execute("select * from leads")
    rows = cur.fetchone()
    first_column_content=rows[0]
    print(first_column_content)