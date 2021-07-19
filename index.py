import psycopg
from search_in_current_db import SearchInCurrentDb
from utils import clean_string, string_to_date

fusionpbxDb = SearchInCurrentDb("fusionpbx", "postgres", "127.0.0.1", "11223344", "5432")

tuple_of_json = fusionpbxDb.search()
list_of_json = []

for json_file in tuple_of_json:
  list_of_json.extend(json_file)
  
conn = psycopg.connect(
  dbname = "allowdb",
  user = "postgres",
  host = "127.0.0.1",
  password = "11223344",
  port = "5432"
)

cur = conn.cursor()

for data in list_of_json:
  call_uuid = data["variables"].get("call_uuid", None)
  domain_uuid = data["variables"].get("domain_uuid", None)
  domain_name = data["variables"].get("domain_name", None)
  call_direction = data["variables"].get("call_direction", None)
  last_bridge_hangup_cause = data["variables"].get("last_bridge_hangup_cause", None)
  caller_id_name = data["variables"].get("caller_id_name", None)
  caller_destination = data["variables"].get("caller_destination", None)
  origination_callee_id_name = data["variables"].get("origination_callee_id_name", None)
  last_sent_callee_id_number = data["variables"].get("last_sent_callee_id_number", None)

  str_start_stamp = clean_string(data["variables"].get("start_stamp", None))
  start_stamp = string_to_date(str_start_stamp)

  str_end_stamp = clean_string(data["variables"].get("end_stamp", None))
  end_stamp = string_to_date(str_end_stamp)

  str_voicemail_answer_stamp = clean_string(data["variables"].get("voicemail_answer_stamp", None))
  voicemail_answer_stamp = string_to_date(str_voicemail_answer_stamp)

  billsec = data["variables"].get("billsec", None)
  dialstatus = data["variables"].get("dialstatus", None)
  hangup_cause = data["variables"].get("hangup_cause", None)
  intercept = data["variables"].get("intercept", None)
  read_result = data["variables"].get("read_result", None)

  cur.execute("INSERT INTO cdr (call_uuid, domain_uuid, domain_name, call_direction, last_bridge_hangup_cause, caller_id_name, caller_destination, origination_callee_id_name, last_sent_callee_id_number, start_stamp, end_stamp, voicemail_answer_stamp, billsec, dialstatus, hangup_cause, intercept, read_result) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(call_uuid, domain_uuid, domain_name, call_direction, last_bridge_hangup_cause, caller_id_name, caller_destination, origination_callee_id_name, last_sent_callee_id_number, start_stamp, end_stamp, voicemail_answer_stamp, billsec, dialstatus, hangup_cause, intercept, read_result))

conn.commit()

cur.close()
conn.close()
