import crud

def wrap(body):
    return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8"> 
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" 
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script 
     src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"
     ></script>
    <script 
     src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
     ></script>
  </head>
  <body>
   <div class="container">
      %s
   </div>
  </body>
</html>
""" % body

def rows(docs):
  res = ""
  for row in docs:
    res += """
<tr>
  <td scope="row">
   <input name="id" value="%s:%s" type="radio">
  </td>
  <td>%s</td>
  <td>%s</td>
</tr>
    """ % (row["_id"], row["_rev"], row["name"], row["email"])
  return res

def table(data):
    res = """
<form method="get">
 <table class="table">
  <thead>
    <tr>
     <th scope="col">#</th>
     <th scope="col">Name</th>
     <th scope="col">Email</th>
    </tr>
  </thead>
 <tbody>"""

    res += rows(data)

    res += """
    <tr>
     <td colspan="4" align="center">  
       <button name="op" value="new" type="submit" class="btn btn-default">New Contact</button>
       <button name="op" value="edit" type="submit" class="btn btn-default">Edit Contact</button>
       <button name="op" value="delete" type="submit" class="btn btn-default">Delete Contact</button>
     </td>
   <tr>
 </tbody>
 </table>
</form>
"""    
    return res

def form(args):
    id = ""
    if "_id" in args and "_rev" in args:
      id = """<input type="hidden" name="id" value="%s:%s">""" % (args["_id"], args["_rev"])
    return """<form method="get">%s
  <input type="hidden" name="op" value="save">
  <div class="form-group">
    <label for="usr">Name:</label>
    <input type="text" class="form-control" 
     id="name" name="name" value="%s">
  </div>
  <div class="form-group">
    <label for="email">Email address:</label>
    <input type="email" class="form-control" 
     id="email" name="email" value="%s">
  </div>
  <button type="submit" class="btn btn-default">Save</button>
</form>    
    """ % (id, args["name"], args["email"])

empty = {
  "op": "save",
  "name": "",
  "email": ""
}

def main(args):
    if "db" in args:
      crud.db = args["db"]
    op = args.get("op")
    if  op == "new":
        return { "body": wrap(form(empty)) }
    if op == "edit":
      rec = crud.find(args["id"])
      return { "body": wrap(form(rec["docs"][0])) }
    if op == "save":
      if "id" in args:
        crud.update(args)
      else:
        crud.insert(args)
    if op == "delete":
        crud.delete(args["id"])
    data = crud.find()["docs"]
    return { "body": wrap(table(data)) }
