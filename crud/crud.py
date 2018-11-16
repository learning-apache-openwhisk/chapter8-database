import crud
import rest

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
  a = args["id"].split(":")
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
    query["selector"]["_id"] = id.split(":")[0]
  ret = rest.whisk_invoke("%s/exec-query-find" % db, {"query": query})
  return ret

def test():
    """
    >>> import rest,crud,json
    >>> rest.load_props()
    >>> crud.db = "demodb"
    >>> crud.dtype = "test"
    >>> args = {"name": "Mike", "email":"msciab@gmail.com"}
    >>> x = crud.insert(args)
    >>> res = crud.find()
    >>> fnd = res["docs"][0]
    >>> print(fnd["name"])
    Mike
    >>> id_rev = "%s:%s" % (fnd["_id"], fnd["_rev"])
    >>> args = { "id": id_rev, "name": "Michele", "email": fnd["email"] }
    >>> x = crud.update(args)
    >>> res = crud.find()
    >>> fnd = res["docs"][0]
    >>> print(fnd["name"])
    Michele
    >>> id_rev = "%s:%s" % (fnd["_id"], fnd["_rev"])
    >>> args = {"name":"Miri","email":"miri@sc.com"}
    >>> id = "test-miri"
    >>> x = crud.insert(args, id)
    >>> res = crud.find("test-miri")
    >>> print(res["docs"][0]["name"])
    Miri
    >>> x = crud.delete(res["docs"][0]) 
    >>> x = crud.delete(id_rev)
    >>> res = crud.find()
    >>> print(res["docs"])
    []
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
