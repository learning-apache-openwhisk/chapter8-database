include ../_config.mk
DB=demodb
URL=https://$(CLOUDANT_USER).cloudant.com
AUTH=$(CLOUDANT_USER):$(CLOUDANT_PASS)

deploy: sampleviews.done validate.done

sampleviews.done:
	! test -e sampleviews.done
	curl -su $(AUTH) -X PUT $(URL)/$(DB)/_design/sampleviews \
	-d @sampleviews.json  >sampleviews.done

validate.json: validate.js
	jq -n --rawfile v validate.js \
	'{ "_id" : "_design/validate", "validate_doc_update":$$v}' \
	>validate.json

validate.done: validate.json
	! test -e validate.done
	curl -su $(AUTH) -X PUT $(URL)/$(DB)/_design/validate \
	-d @validate.json  >validate.done

clean:
	curl -u $(AUTH) -X DELETE $(URL)/$(DB)/_design/sampleviews?rev=$(shell jq -r .rev sampleviews.done)
	curl -u $(AUTH) -X DELETE $(URL)/$(DB)/_design/validate?rev=$(shell jq -r .rev validate.done)
	rm sampleviews.done validate.done

.PHONY: clean deploy

include test-views.mk
include test-validate.mk

