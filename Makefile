init:
	pip install -r requirements-dev.txt
publish:
	rm -f -r pypuyo.egg-info/* dist/*
	python3 -m build
	twine upload dist/*
	rm -f -r pypuyo.egg-info/* dist/*
