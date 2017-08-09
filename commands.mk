check-json:
	python -m json.tool < .zenodo.json >> /dev/null && exit 0 || echo "NOT valid JSON"; exit 1
