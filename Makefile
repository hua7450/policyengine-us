all: build
format:
	uv run ruff format .
	uv run ruff check .
install:
	pip install -e .[dev]
test:
	pytest policyengine_us/tests/ --maxfail=0
	coverage run -a --branch -m policyengine_core.scripts.policyengine_command test policyengine_us/tests/policy/ -c policyengine_us
	coverage xml -i
test-yaml-structural:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib --exclude states
test-yaml-structural-heavy:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/states --batches 1
test-yaml-structural-reform:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/ctc/ctc_additional_bracket.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/ctc/ctc_minimum_refundable_amount.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/ctc/ctc_older_child_supplement.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/ctc/ctc_per_child_phase_in.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/ctc/ctc_per_child_phase_out.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/ctc/integration.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/crfb/agi_surtax.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/crfb/non_refundable_ss_credit.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/crfb/senior_deduction_extension.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/crfb/tax_employer_all_payroll_tax.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/crfb/tax_employer_medicare_tax.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/crfb/tax_employer_payroll_tax_percentage.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/crfb/tax_employer_social_security_tax.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/ubi_center --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/federal --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/harris --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib/treasury --batches 1
test-yaml-structural-other:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/contrib --exclude states,ctc,ubi_center,federal,harris,treasury,crfb
test-yaml-variables:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/variables --batches 1
test-yaml-no-structural-states:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/states --batches 4 --exclude ny
	$(MAKE) test-yaml-no-structural-states-ny
test-yaml-no-structural-states-ny:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/states/ny/tax/income/credits --batches 3
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/states/ny/tax/income/taxable_income --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/states/ny/tax/income --exclude credits,taxable_income --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/states/ny/hhs --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/states/ny/nyserda --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/states/ny/otda --batches 1
test-yaml-no-structural-other:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline --batches 2 --exclude states
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/household --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/contrib --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/reform --batches 1
test-yaml-no-structural-other-irs:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/credits --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/income --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/tax --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/deductions --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/integration --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/payroll --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/self_employment --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/social_security --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/tax_unit --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/tce --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/vita --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/irs_gross_income.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/irs/tax_unit_is_filer.yaml --batches 1
test-yaml-no-structural-other-household:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/household --batches 2
test-yaml-no-structural-other-irs-household: test-yaml-no-structural-other-irs test-yaml-no-structural-other-household
test-yaml-no-structural-other-contrib:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/contrib/biden --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/contrib/states --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/contrib/ubi_center/basic_income.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/contrib/ubi_center/basic_income_before_phase_out.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/contrib/ubi_center/basic_income_eligible.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/contrib/ubi_center/basic_income_phase_in.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/contrib/ubi_center/basic_income_phase_out.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/reform --batches 1
test-yaml-no-structural-other-ssa:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/ssa/revenue --batches 2
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/ssa/social_security --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/ssa/ss --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/ssa/ssi --batches 1
test-yaml-no-structural-other-rest:
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/hhs --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/usda --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/simulation --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/local --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/territories --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/aca --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/ed --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/hud --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/fcc --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/doe --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/abolitions.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/gov/test_categorical_eligibility_vectorization.yaml --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/calcfunctions --batches 1
	python policyengine_us/tests/test_batched.py policyengine_us/tests/policy/baseline/income --batches 1
test-other:
	pytest policyengine_us/tests/ --maxfail=0
coverage:
	coverage combine
	coverage xml -i
documentation:
	jb clean docs
	jb build docs
	python policyengine_us/tools/add_plotly_to_book.py docs/_build
build:
	rm policyengine_us/data/storage/*.h5 | true
	python -m build
changelog:
	python .github/bump_version.py
	towncrier build --yes --version $$(python -c "import re; print(re.search(r'version = \"(.+?)\"', open('pyproject.toml').read()).group(1))")
dashboard:
	python policyengine_us/data/datasets/cps/enhanced_cps/update_dashboard.py
calibration:
	python policyengine_us/data/datasets/cps/enhanced_cps/run_calibration.py
clear-storage:
	rm -f policyengine_us/data/storage/*.h5
	rm -f policyengine_us/data/storage/*.csv.gz
	rm -rf policyengine_us/data/storage/*cache

# Run tests only for changed files
test-changed:
	@echo "Running tests for changed files..."
	@python policyengine_us/tests/run_selective_tests.py --verbose --debug