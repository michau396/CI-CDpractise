build_distribution:
	python3 setup.py sdist bdist_wheel

upload_to_testpypi:
	twine upload --repository testpypi dist/* --verbose

upload_to_pypi:
	twine upload dist/*
