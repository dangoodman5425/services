from . import Aws
import os


class Athena(Aws):
    def __init__(self, db, default_bucket=None, profile_name=None, **kwargs):
        super().__init__("lambda", profile_name, **kwargs)
        self.db = db
        self.output_location = "{default_bucket}/athena/".format(
            default_bucket=os.getenv("ATHENA_BUCKET")) if not default_bucket else default_bucket

    def create_query(self, name, sql_file):
        with open(sql_file, "r") as f:
            query_string = f.read()
        res = self.client.create_named_query(Name=name, Database=self.db, QueryString=query_string)
        return res["NamedQueryId"]

    def delete_query(self, query_id):
        self.client.delete_named_query(query_id)

    def list_queries(self):
        return self.client.list_named_queries()["NamedQueryIds"]

    def run_query(self, query, output_location=None):
        output_location = output_location if output_location else self.output_location
        res = self.client.start_query_execution(QueryString=query, QueryExecutionContext={"Database": self.db},
                                                ResultConfiguration={"OutputLocation": output_location})
        return res["QueryExecutionId"]

    def get_query(self, query_id):
        return self.client.get_named_query(NamedQueryId=query_id)

    def drop_table(self, table_name, output_location=None):
        query = "DROP TABLE {}".format(table_name)
        output_location = output_location if output_location else self.output_location
        res = self.client.start_query_execution(QueryString=query, QueryExecutionContext={"Database": self.db},
                                                ResultConfiguration={"OutputLocation": output_location})
        return res["QueryExecutionId"]
