import psycopg2
# Function to create a table
def db_connection():
    try:
        connection = psycopg2.connect(
            user= "postgres",
            password= "postgres",
            host= "localhost",
            port= "5432",
            database= "duilal"
        )
        return connection

        # create_table_query = '''
        #     CREATE TABLE IF NOT EXISTS student (
        #         id SERIAL PRIMARY KEY,
        #         name VARCHAR(50),
        #         class VARCHAR(50),
        #         rollno VARCHAR(50)
        #     )
        #     '''
        # cursor.execute(create_table_query)
        # connection.commit()
        # print("Table created successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
