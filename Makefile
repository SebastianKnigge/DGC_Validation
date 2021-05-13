create-aws-lambda-function:
	cd env/lib/python3.7/site-packages/
	zip -r9 ../../../../function.zip .
	cd ../../../../
	zip -g ./function.zip -r app