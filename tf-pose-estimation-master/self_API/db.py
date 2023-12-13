import pymysql

def dbGetConnect():
    
    db = pymysql.connect(host="10.106.128.13",user="root",passwd="",database="fypdb" )
     
    
    cursor = db.cursor()
    
    return db, cursor

def dbGetElderIdByWebcamId(webcamId):
    db, cursor = dbGetConnect()
    elderly_id = 0

    
    sql = "SELECT * FROM webcam where webcam_id=" + str(webcamId)
    try:
       
       cursor.execute(sql)
       
       results = cursor.fetchall()
       for row in results:
          elderly_id = row[1]

    except:
       print ("Error: unable to fetch data")
     
    
    db.close()
    
    return elderly_id
    
def dbGetCareTakerEmailByElderlyId(elderlyId):
    db, cursor = dbGetConnect()
    email = 0
    
    sql = "SELECT * FROM caretaker where elderly_id=" + str(elderlyId)
    try:
       
       cursor.execute(sql)
       
       results = cursor.fetchall()
       for row in results:
          email = row[0]

    except:
       print ("Error: unable to fetch data")
     
    
    db.close()
    
    return email
    
    
def dbAddFallRecord(gif_name, webcam_id, fall_date, fall_count):
    db, cursor = dbGetConnect()
    
    gif_txt =  str(gif_name)
    
    
    sql = """ INSERT INTO fall_record
                          (webcam_id, elderly_id, fall_date, fall_count, fall_gif) VALUES (%s,%s,%s,%s,%s)"""
                          
    try:
        
        elderly_id = dbGetElderIdByWebcamId(webcam_id)

        # Convert data into tuple format
        insert_data = (webcam_id, elderly_id, fall_date, fall_count, gif_txt)
        result = cursor.execute(sql, insert_data)
        db.commit()
    except:
        print ("Error: unable to fetch data")
        
    db.close()
    

    
    

    
    