''' pytest_csv_plugins - pytest-csv or pytest-csv-ddt.

They can auto-generate tests from CSV rows with less boilerplate.

 - pip install pytest-csv
 - pytest --csv test_data.csv test_file.py

This works with plugin-provided decorators.

| For beginners | pytest.mark.parametrize + read_csv()
| For advanced | pytest_generate_tests for full dynamic control
| For teams | Use a plugin if you want less custom code
'''