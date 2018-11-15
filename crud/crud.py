import crud
import rest
import website

empty = {
  "op": "save",
  "name": "",
  "email": ""
}

db = "demodb"
dtype = "contact"

def delete(id_rev):
  params = {}
  if type(id_rev) is str:
    a = id_rev.split(":")
    params = {
      "docid": a[0],
      "docrev": a[1]
    }
  if type(id_rev) is dict:
    params = {
      "docid": id_rev["_id"],
      "docrev": id_rev["_rev"]
    }
  ret = rest.whisk_invoke("%s/delete-document" % db, params)
  return ret

def update(args):
  a = args["_id_rev"].split(":")
  doc = {
    "_id": a[0],
    "_rev": a[1],
    "name": args["name"],
    "email": args["email"],
    "type": dtype
  }
  ret = rest.whisk_invoke("%s/update-document" % db, {"doc": doc})
  return ret

def insert(args, id=None):
  doc = {"name": args["name"], "email": args["email"], "type": dtype}
  if id:
    doc["_id"] = id
  ret = rest.whisk_invoke("%s/create-document" % db, {"doc": doc})
  return ret

def find(id=None):
  query = { "selector": {"type": dtype} }
  if id:
    query["selector"]["_id"] = id
  ret = rest.whisk_invoke("%s/exec-query-find" % db, {"query": query})
  return ret

    