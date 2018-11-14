import crud
import website

empty = {
  "op": "save",
  "name": "",
  "email": ""
}

def main(args):
    op = args.get("op")
    if  op == "new":
        return { "body": website.wrap(website.form(empty)) }
    return { "body": website.wrap(website.table()) }
    