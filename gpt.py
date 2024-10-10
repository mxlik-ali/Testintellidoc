import sqlite3  # Using SQLite for simplicity; you can switch to MySQL or PostgreSQL.
from dbconfig1 import dbconfig
import sys
from rich import print as printc
from rich.console import Console
console = Console()

def checkConfig():
	db = dbconfig()
	cursor = db.cursor()
	query = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA  WHERE SCHEMA_NAME = 'sim card'"
	cursor.execute(query)
	results = cursor.fetchall()
	db.close()
	if len(results)!=0:
		return True
	return False

def db_init():
    try:
        if not checkConfig():
            """
            Initialize the database by creating the required tables for SIM card activation.
            """
            try:
                # Step 1: Establish connection to the database
                db = dbconfig()
                cur = db.cursor()

                # Step 2: Create the 'sim_cards' table to store SIM information
                try:
                    query = """
                    CREATE TABLE IF NOT EXISTS sim_cards (
                        sim_number TEXT PRIMARY KEY,  -- Unique identifier for each SIM card
                        phone_number TEXT NOT NULL UNIQUE,  -- Associated phone number
                        status TEXT CHECK(status IN ('active', 'inactive')) NOT NULL DEFAULT 'inactive',  -- Status: active/inactive
                        activation_date TIMESTAMP  -- Activation date (NULL until activated)
                    )
                    """
                    cur.execute(query)
                    console.print("[green][+][/green] Table 'sim_cards' created successfully.")
                except Exception as e:
                    console.print("[red][!] An error occurred while creating 'sim_cards' table.")
                    console.print_exception(show_locals=True)
                    sys.exit(1)

                # Step 3: Commit the changes and close the connection
                db.commit()
                db.close()
                console.print("[green][+][/green] Database setup complete.")

            except Exception as e:
                console.print("[red][!] An unexpected error occurred during database initialization.")
                console.print_exception(show_locals=True)
                sys.exit(1)

    except Exception as e:
        #printc(f'[red]Error initializing database: {e}[/red]')
        print(e)

if __name__ == "__main__":
    db_init()  # Run the DB initialization
