cd package
zip -r9 ${OLDPWD}/function.zip .
cd $OLDPWD
zip -g function.zip change_link_rules.py
aws lambda update-function-code --function-name change_link_rules --zip-file fileb://function.zip