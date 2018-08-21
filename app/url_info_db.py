import MySQLdb

db = MySQLdb.connect("localhost", "root", "root")

def getURLInfo(url):
    cursor = db.cursor()
    query = "SELECT malware_info from dev.url_infos where url = %s"
    cursor.execute(query, (url,))

    result = cursor.fetchone()

    if (not result):
        return None

    malware_info = result[0]
    print("Got malware_info : "+malware_info +" , for url : "+url)
    return malware_info

if __name__=="__main__":
    # Testing the code
    info = getURLInfo("http://google.com")
    print (info)









