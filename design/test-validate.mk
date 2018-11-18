test-contact0: 
	curl -u $(AUTH) $(URL)/$(DB)/test-mike \
	-X PUT -d '{"type":"contact"}'

test-contact1: 
	curl -u $(AUTH) $(URL)/$(DB)/test-mike \
	-X PUT -d '{"type":"contact", "name": "Mike"}'

test-contact2: 
	curl -u $(AUTH) $(URL)/$(DB)/test-mike \
	-X PUT -d '{"type":"contact", "name": "Mike", "email": "mike@home"}'

test-contact3: 
	curl -u $(AUTH) $(URL)/$(DB)/test-mike \
	-X PUT -d '{"type":"contact", "name": "Mike", "email": "michele@sciabarra.com"}'
