RUNNER=cwl-runner

## unittest-examples: run unit tests for the examples
unittest-examples:
	cd _includes/cwl; cwltest --test=conformance-test.yml --tool=${RUNNER}
check-json:
	python -m json.tool < .zenodo.json >> /dev/null && exit 0 || echo "NOT valid JSON"; exit 1
