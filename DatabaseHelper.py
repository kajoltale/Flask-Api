import mysql.connector
import json

dataPoints = ['id', 'user_name', 'email', 'company', 'country', 'age', 'highest_education']

def connection():
    db = mysql.connector.connect(host='localhost', database='UserInfo', user='admin', password='admin4321')
    return db

def getUserInfo(request):
    db = connection()
    limit = '10'
    page = '0'

    try:
        limit = request.args.get('limit')
        if (limit == None):
            limit = '10'
    except:
         limit = '10'

    try:
        page = request.args.get('page')
        if (page == None):
            page = '0'
        else:
            page = int(page) - 1
            if (page <= 0):
                page = 0
            page = str(page)

    except:
        page = '0'

    query = 'SELECT id,user_name ,email,company,country,age,highest_education FROM userDetails'

    query = query + " limit " + page + "," + limit

    result = {}
    cur = db.cursor()
    count = 0
    cur.execute(query)

    for row in cur.fetchall():
        result[count] = {dataPoints[0]: row[0], dataPoints[1]: row[1], dataPoints[2]: row[2], dataPoints[3]: row[3],
                         dataPoints[4]: row[4], dataPoints[5]: row[5], dataPoints[6]: row[6]}
        count = count + 1

    db.close()
    result['Status'] = 200
    result = json.dumps(result)
    return result

def createUser(request):
    jsonV = request.get_json()
    dictonary = {}
    response = {}

    for field in dataPoints:
        try:
            dictonary[field] = jsonV[field]
        except:
            dictonary[field] = None

    mustPresent = ['user_name', 'email']
    for field in mustPresent:
        if (dictonary[field] == None):
            response['ErrorMessage'] = field + "Should Be Present"
            response['ErrorCode'] = 500
            return json.dumps(response)

    fields = '('
    values = '('
    for field in dataPoints:
        if field == 'id':
            continue
        fields = fields + "" + field + ","
        if dictonary[field] == None:
            values = values + " NULL ,"
        else:
            values = values + "'" + str(dictonary[field]) + "',"

    values = values[:-1]
    fields = fields[:-1]
    values = values + ')'
    fields = fields + ')'

    try:
        db = connection()
        query = 'INSERT IGNORE INTO userDetails ' + fields + ' VALUES ' + values
        cur = db.cursor()
        result = cur.execute(query)
        db.commit()
        db.close()
        response['Status'] = 200
        return json.dumps(response)
    except:
        response['ErrorMessage'] = "Internal Server Error"
        response['ErrorCode'] = 500
        return json.dumps(response)

def getUser(id):
    db = connection()
    result = {}
    cur = db.cursor()
    query = 'SELECT id,user_name ,email,company,country,age,highest_education FROM userDetails WHERE id =' + id
    count = 0
    cur.execute(query)

    for row in cur.fetchall():
        result[count] = {dataPoints[0]: row[0], dataPoints[1]: row[1], dataPoints[2]: row[2], dataPoints[3]: row[3],
                         dataPoints[4]: row[4], dataPoints[5]: row[5], dataPoints[6]: row[6]}
        count = count + 1

    db.close()
    result['Status'] = 200
    result = json.dumps(result)
    return result

def alterUser(id, request):
    jsonV = request.get_json()
    dictonary = {}

    for field in dataPoints:
        try:
            dictonary[field] = jsonV[field]
        except:
            dictonary[field] = None

    values = ''
    for field in dataPoints:
        if (dictonary[field] == None):
            continue
        values = values + ' ' + field + ' = "' + str(dictonary[field]) + '",'
    values = values[:-1]
    values = values + ''

    response = {}
    try:
        db = connection()
        query = 'UPDATE `userDetails` SET  ' + values + ' WHERE id = ' + id
        print(query)
        cur = db.cursor()
        cur.execute(query)
        db.commit()
        db.close()
        response["code"] = 200
        return json.dumps(response)
    except:
        response['ErrorMessage'] = "Internal Server Error"
        response['ErrorCode'] = 500

        return json.dumps(response)

def deleteUser(id):
    response = {}
    try:
        db = connection()
        cur = db.cursor()
        query = 'DELETE FROM `userDetails` WHERE id = ' + id
        cur.execute(query)
        db.commit()
        db.close()
        response["code"] = 200
        return json.dumps(response)
    except:
        response['ErrorMessage'] = "Internal Server Error"
        response['ErrorCode'] = 500
        return json.dumps(response)
