import mysql.connector
import uuid

database = "link_shortener"

def mysql_connection():
    return mysql.connector.connect(user='root', password='password123',
                                host='127.0.0.1',
                                database=database,
                                auth_plugin='mysql_native_password')

def fetch_link(shorturl="", id=""):
    connection = mysql_connection()
    cursor = connection.cursor(dictionary=True, buffered=True)

    if shorturl:
        query = (f"SELECT id, name, href, shorturl FROM {database}.link_details WHERE shorturl = %s;")
        cursor.execute(query, (shorturl,))
    else:
        query = (f"SELECT name, href, shorturl FROM {database}.link_details WHERE id = %s;")
        cursor.execute(query, (id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()
    return result

def create_link(link_name, link_href):
    connection = mysql_connection()
    cursor = connection.cursor()

    uuid = random_uuid()

    query = (f"INSERT INTO {database}.link_details (name, href, shorturl) VALUES (%s, %s, %s);")
    cursor.execute(query, (link_name, link_href, uuid))
    connection.commit()

    entered_id = cursor.lastrowid
    shorturl = fetch_link("", entered_id)["shorturl"]

    cursor.close()
    connection.close()
    return shorturl

def random_uuid():
    return str(uuid.uuid4())[:5]
