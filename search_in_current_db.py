import psycopg

class SearchInCurrentDb:
  def __init__(self, dbname, user, host, password, port):
    self.__dbname = dbname
    self.__user = user
    self.__host = host
    self.__password = password
    self.__port = port

  def search(self):
    conn = psycopg.connect(
      dbname = self.__dbname,
      user = self.__user,
      host = self.__host,
      password = self.__password,
      port = self.__port
    )
    
    cur = conn.cursor()
    cur.execute("SELECT domain_name FROM v_domains")
    
    domains = cur.fetchall()
    list_of_domains = []

    for domain_name in domains:
      list_of_domains.extend(domain_name)
    
    data = []

    for domain in list_of_domains:
      cur.execute("SELECT json FROM v_xml_cdr WHERE domain_name = '{}' AND start_stamp BETWEEN CURRENT_DATE - INTERVAL '1 DAY' AND CURRENT_DATE - INTERVAL '1 DAY' + '23:59:59'".format(domain))

      data.extend(cur.fetchall())

    cur.close()
    conn.close()
    
    return data
