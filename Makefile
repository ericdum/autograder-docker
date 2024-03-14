reqs:
	pipreqs --ignore tests/target .

test:
	pytest tests