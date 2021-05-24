import mysql.connector

def mysql_connection():
    return mysql.connector.connect(user='root', password='password123',
                                host='127.0.0.1',
                                database='link_shortener',
                                auth_plugin='mysql_native_password')

def fetch_link(shorturl):
    connection = mysql_connection()
    cursor = connection.cursor(dictionary=True, buffered=True)

    query = ("SELECT name, href FROM link_shortener.link_details WHERE shorturl = %s;")
    cursor.execute(query, (shorturl,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()
    return result
    
