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

test-join2-mac:
	curl -su $(AUTH) '$(URL)/$(DB)/_design/sampleviews/_view/join2?include_docs=true&key="mac"' | jq .


