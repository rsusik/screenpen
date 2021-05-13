compileone:
	pyinstaller --onefile -F --add-data "./utils/*:utils" screenpen.pyw

clean:
	rm -rf dist build screenpen.egg-info

setup: clean
	python setup.py sdist bdist_wheel 

pipinstall:
	rm -rf screenpen.egg-info && python -m pip install -e .

pipwheel:
	rm -rf screenpen.egg-info && python -m pip wheel install -e . -w wheels

setuppip: clean
	rm -rf dist build  && python setup.py sdist bdist_wheel && twine upload dist/*
