pypireg:
	python setup.py register
	python setup.py sdist bdist_egg upload

clean:
	rm -rf build *.egg-info dist sphinxcontrib/*.pyc
