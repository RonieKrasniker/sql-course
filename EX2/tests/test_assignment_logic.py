import unittest
from unittest.mock import MagicMock, patch
import os
import sys
import re

# Path to submission folder
SUBMISSION_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'submission')

class TestAssignmentLogic(unittest.TestCase):

    def setUp(self):
        # Create a mock for mysql.connector
        self.mock_mysql_connector = MagicMock()
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        
        self.mock_mysql_connector.connect.return_value = self.mock_conn
        self.mock_conn.cursor.return_value = self.mock_cursor
        
        # Setup fetchall to return empty list by default
        self.mock_cursor.fetchall.return_value = []

        # Create a mock for the 'mysql' package
        self.mock_mysql_package = MagicMock()
        # Ensure mysql.connector refers to our connector mock
        self.mock_mysql_package.connector = self.mock_mysql_connector

        # Patch sys.modules
        self.patcher = patch.dict(sys.modules, {
            'mysql': self.mock_mysql_package,
            'mysql.connector': self.mock_mysql_connector
        })
        self.patcher.start()

        # Also need to update self.mock_mysql for the tests to use
        self.mock_mysql = self.mock_mysql_connector

    def tearDown(self):
        self.patcher.stop()

    def run_script(self, filename):
        filepath = os.path.join(SUBMISSION_DIR, filename)
        if not os.path.exists(filepath):
            self.fail(f"File {filename} not found")

        with open(filepath, 'r') as f:
            script_content = f.read()

        # Execute the script in a separate namespace
        # We set __name__ to '__main__' to trigger the execution block
        global_vars = {'__name__': '__main__'}
        try:
            exec(script_content, global_vars)
        except Exception as e:
            self.fail(f"Script {filename} raised exception: {e}")

        # Collect all executed SQL queries
        queries = []
        for call in self.mock_cursor.execute.call_args_list:
            args, _ = call
            if args:
                queries.append(args[0].strip())
        
        return queries

    def assertSqlMatchesRegex(self, query, pattern, msg=None):
        # Normalize whitespace in query and pattern
        query_norm = ' '.join(query.split())
        # We don't normalize pattern because it's a regex, but we assume the user writes regex that handles spaces
        if not re.search(pattern, query_norm, re.IGNORECASE):
            self.fail(msg or f"Query '{query_norm}' does not match pattern '{pattern}'")

    # --- Tests ---

    def test_q1_create_db(self):
        queries = self.run_script('q1.py')
        self.assertTrue(queries, "No queries executed in q1.py")
        self.assertSqlMatchesRegex(queries[0], r"CREATE DATABASE\s+biu_shoes")

    def test_q2_1_create_shoe_table(self):
        queries = self.run_script('q2_1.py')
        self.assertTrue(queries)
        self.assertSqlMatchesRegex(queries[0], r"CREATE TABLE\s+shoe.*shoe_id\s+INT.*shoe_name\s+VARCHAR.*price\s+SMALLINT")

    def test_q2_7_create_customer_table(self):
        queries = self.run_script('q2_7.py')
        self.assertTrue(queries)
        # Check for table creation and the CHECK constraint
        self.assertSqlMatchesRegex(queries[0], r"CREATE TABLE\s+customer")
        self.assertSqlMatchesRegex(queries[0], r"CHECK\s*\(\s*LENGTH\s*\(\s*customer_id\s*\)\s*=\s*9\s*\)")

    def test_q3_inserts(self):
        # Spot check one insert file
        queries = self.run_script('q3_1.py')
        self.assertTrue(queries)
        self.assertSqlMatchesRegex(queries[0], r"INSERT INTO\s+shoe.*VALUES")

    def test_q4_alter_size(self):
        queries = self.run_script('q4.py')
        self.assertTrue(queries)
        self.assertSqlMatchesRegex(queries[0], r"ALTER TABLE\s+size\s+ADD\s+(COLUMN\s+)?uk_number\s+TINYINT")

    def test_q5_alter_upcoming(self):
        queries = self.run_script('q5.py')
        self.assertTrue(queries)
        self.assertSqlMatchesRegex(queries[0], r"ALTER TABLE\s+upcoming\s+ADD\s+(COLUMN\s+)?pre_order_available\s+BIT(\(1\))?\s+DEFAULT\s+0")

    def test_q6_updates(self):
        queries = self.run_script('q6_1.py')
        self.assertTrue(queries)
        self.assertSqlMatchesRegex(queries[0], r"UPDATE\s+size\s+SET\s+uk_number\s*=\s*5\s+WHERE\s+european_number\s*=\s*38")

    def test_q7_revenue_query(self):
        queries = self.run_script('q7.py')
        self.assertTrue(queries)
        q = queries[0]
        self.assertSqlMatchesRegex(q, r"SELECT.*SUM\(.*price\).*FROM\s+customer")
        self.assertSqlMatchesRegex(q, r"JOIN\s+order_customer")
        self.assertSqlMatchesRegex(q, r"GROUP BY")

    def test_q8_price_analysis(self):
        queries = self.run_script('q8.py')
        self.assertTrue(queries)
        q = queries[0]
        self.assertSqlMatchesRegex(q, r"SELECT.*AVG\(.*price\).*FROM\s+size")
        self.assertSqlMatchesRegex(q, r"ORDER BY.*DESC")

    def test_q9_shoe_availability(self):
        queries = self.run_script('q9.py')
        self.assertTrue(queries)
        q = queries[0]
        self.assertSqlMatchesRegex(q, r"SELECT.*COUNT\(.*size_id\).*FROM\s+shoe")
        self.assertSqlMatchesRegex(q, r"LEFT JOIN\s+shoe_size")

    def test_q10_union(self):
        queries = self.run_script('q10.py')
        self.assertTrue(queries)
        q = queries[0]
        self.assertSqlMatchesRegex(q, r"SELECT.*FROM\s+shoe.*UNION.*SELECT.*FROM\s+upcoming")

    def test_q11_view(self):
        # q11_1 creates view
        queries1 = self.run_script('q11_1.py')
        self.assertTrue(queries1)
        self.assertSqlMatchesRegex(queries1[0], r"CREATE VIEW\s+total_sales_per_shoe\s+AS\s+SELECT")
        
        # Reset mock to clear history for the next script in this test
        self.mock_cursor.reset_mock()

        # q11_2 selects from view
        queries2 = self.run_script('q11_2.py')
        self.assertTrue(queries2)
        self.assertSqlMatchesRegex(queries2[0], r"SELECT\s+\*\s+FROM\s+total_sales_per_shoe")

    def test_q12_unsold(self):
        queries = self.run_script('q12.py')
        self.assertTrue(queries)
        q = queries[0]
        self.assertSqlMatchesRegex(q, r"SELECT.*FROM\s+shoe")
        self.assertSqlMatchesRegex(q, r"LEFT JOIN\s+order_shoe")
        self.assertSqlMatchesRegex(q, r"WHERE.*IS NULL")

if __name__ == '__main__':
    unittest.main()
