#how to run a python app on host 0.0.0.0
flask run --host=0.0.0.0 
but this is after you have added cors to your flask application
make sure all your fetch requests are made using the actual ip address of the host computer not just localhost. this is because when you run on another system, if you used localhost, it defaults to the localhost of that system and hence an error. but if you use the id address of the host computer, then it sends the request to the said host
