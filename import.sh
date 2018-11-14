#!/bin/bash
for i in data/*.json ;\
do wsk action invoke demodb/create-document \
   -p doc "$(cat $i)"
done  
