"""Custom database commands"""
from datetime import datetime
from django.db import connection
from backend.models import ImportCnabTemplate

def custom_sql(sql, fetch=True):
    """Custom SQL function"""
    row = None
    with connection.cursor() as cursor:
        cursor.execute(sql)
        if fetch:
            row = cursor.fetchone()
    return row

def check_table_exists(schema, table_name):
    """Function to check if table exists"""
    sql = f"""
        SELECT EXISTS(
            SELECT *
            FROM information_schema.tables        
            WHERE
            table_schema = '{schema}' AND
            table_name = '{table_name}'
        );
    """
    row = custom_sql(sql)
    return row and row[0]

def create_table(table_name, fields):
    """Create custom table"""
    sql = f"CREATE TABLE {table_name} ("
    sql += ",".join(fields)
    sql += ");"
    custom_sql(sql)

def insert_table(table_name, fields, values):
    """Create custom table"""
    sql = f"INSERT INTO {table_name} ("
    sql += ",".join(fields)
    sql += ") VALUES ('"
    sql += "','".join(values)
    sql += "');"
    return sql


def format_fields(type_format, data_type, line_value):
    """Apply format defined by template"""
    if type_format:
        if data_type == 'date':
            new_date = datetime.strptime(line_value, type_format)
            line_value = new_date.strftime('%Y-%m-%d')
        elif data_type == 'timestamp':
            new_timestamp = datetime.strptime(line_value, type_format)
            line_value = new_timestamp.strftime('%Y-%m-%d %H:%M:%S')
        elif data_type == 'decimal':
            line_value = str(eval(f'{float(line_value)} {type_format}'))
    return line_value

def get_fields(template_id):
    """Get all fields for that format"""
    return ImportCnabTemplate.objects.filter(
                import_template__id=template_id
            ).order_by(
                'order'
            )

def fill_fields(template_id):
    """Fill the fields and fields with type"""
    fields_with_type = []
    fields = []
    for field in get_fields(template_id):
        field_name = field.cnab_template.field_name
        data_type = field.cnab_template.data_type
        fields_with_type.append(f"{field_name} {data_type}")
        fields.append(field_name)
    return fields_with_type, fields

def create_table_if_not_exists(table_name, fields_with_type):
    """Function that verify if table exist then creates it"""
    if not check_table_exists('public', table_name):
        create_table(table_name, fields_with_type)

def do_import_data(file_path, template_id):
    """Function that do the real job of importing the data"""
    import_data = []
    with open(file_path, 'r', encoding='utf-8') as lines:
        for line in lines:
            line_data = []
            for field in get_fields(template_id):
                start = field.cnab_template.start
                end = field.cnab_template.end
                data_type = field.cnab_template.data_type
                type_format = field.cnab_template.type_format
                line_value = format_fields(
                    type_format,
                    data_type,
                    line[start-1:end].replace('\n', '')
                )
                line_data.append(line_value.strip())
            import_data.append(line_data)
    return import_data

def send_it_to_database(import_data, table_name, fields):
    """Send the imported data to database"""
    sql_insert = ""
    for line_data in import_data:
        sql_insert += insert_table(table_name, fields, line_data)
    if sql_insert:
        custom_sql(sql_insert, False)
