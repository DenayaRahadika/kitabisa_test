from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.postgres_operator import PostgresOperator

# ##### Problem Assumptions: ##### # 
# Assume that we have a database named "json_table" that store raw data in json format with the respective created date time
# (note: "json_table" is assumed to be given)
# We would like to transform the database to a better format (columnar) and do this daily with the help of Airflow scheduler
# We save the transformed data in "donut_table"

default_args = {
    'dag_id': 'donut_etl',
    'start_date': datetime(2020, 10, 7),
    'schedule_interval': "@daily",
}

#  Assume that we have (given) all the json files saved in this table with schema; id:int, json_file:json, and the created_at:timestamp
input_table_name = "json_table"

# This table will store all of the transformed json data
output_table_name = "donut_table"

# DAG main code
with DAG("donut_etl", default_args=default_args) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        database="kitabisa",
        postgres_conn_id="postgres_kb",
        sql='''
        CREATE TABLE IF NOT EXISTS public.{output}(
            id integer, 
            type text,
            name text,
            ppu float,
            batter text,
            topping text
        );'''.format(output=output_table_name)
    )

    insert_row = PostgresOperator(
        task_id='insert_row',
        database="kitabisa",
        postgres_conn_id="postgres_kb",
        sql='''
            WITH 
                json_files AS (SELECT json_file FROM public.{input} WHERE created_at BETWEEN CURRENT_DATE - 1 AND CURRENT_DATE),
                json_arrays AS (SELECT json_agg(elems) AS json_array FROM json_files, json_array_elements(json_file) AS elems),
                data AS (SELECT id, type, name, ppu, batters, topping FROM json_arrays, json_to_recordset(json_arrays.json_array) 
                    AS x("id" int, "type" text, "name" text, "ppu" float, "batters" jsonb, "topping" jsonb[]))
            INSERT INTO {output}
                SELECT data.id, data.type, data.name, data.ppu, specs.type as batter, unnest(data.topping)->>'type' AS topping
                FROM data, jsonb_to_recordset(data.batters -> 'batter') AS specs(id int, type text)	
            '''.format(input=input_table_name, output=output_table_name), 
    )

create_table >> insert_row