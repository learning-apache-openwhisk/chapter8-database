include ../_config.mk
DB=demodb
URL=https://$(CLOUDANT_USER).cloudant.com
AUTH=$(CLOUDANT_USER):$(CLOUDANT_PASS)
JSON=

deploy: sampleview.done

sampleview.done:
	! test -e sampleviews.done
	curl -su $(AUTH) -X PUT $(URL)/$(DB)/_design/sampleviews \
	-d @sampleviews.json  >sampleviews.done

clean:
	curl -u $(AUTH) -X DELETE $(URL)/$(DB)/_design/sampleviews?rev=$(shell jq -r .rev sampleviews.done)
	rm sampleviews.done

test-count: 
	curl -su $(AUTH) $(URL)/$(DB)/_design/sampleviews/_view/count

test-count2: 
	curl -su $(AUTH) $(URL)/$(DB)/_design/sampleviews/_view/count2

test-names: 
	curl -su $(AUTH) $(URL)/$(DB)/_design/sampleviews/_view/names

test-persons: 
	curl -su $(AUTH) $(URL)/$(DB)/_design/sampleviews/_view/persons

test-stats: 
	curl -su $(AUTH) $(URL)/$(DB)/_design/sampleviews/_view/stats

test-join: 
	curl -su $(AUTH) "$(URL)/$(DB)/_design/sampleviews/_view/join?include_docs=true" | jq .

test-join-mike:
	curl -su $(AUTH) '$(URL)/$(DB)/_design/sampleviews/_view/join?include_docs=true&key="mike"' | jq .

test-join2: 
	curl -su $(AUTH) "$(URL)/$(DB)/_design/sampleviews/_view/join2?include_docs=true" | jq .

test-join2-mike:
	curl -su $(AUTH) '$(URL)/$(DB)/_design/sampleviews/_view/join2?include_docs=true&key="mike"' | jq .

.PHONY: clean deploy