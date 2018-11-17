deploy: crud.zip crud.done validate.done
	wsk action update crud/main crud.zip -p db demodb --kind python:3 --web true
	wsk action get crud/main --url

crud.done:
	wsk package create crud
	touch crud.done

crud.zip: *.py
	zip crud.zip *.py

validate.done:
	wsk action invoke demodb/create-document \
   -P validate.json -r | \
   sed -e 's/"id"/"docid"/' -e 's/"rev"/"docrev"/' \
   >validate.done

clean:
	wsk action invoke demodb/delete-document -P validate.done -r
	wsk action delete crud/main 
	rm validate.done

test: deploy
	wsk action invoke crud/main -r
