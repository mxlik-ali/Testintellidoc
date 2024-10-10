from dbconfig1 import dbconfig
from rich import print as printc
from rich.console import Console
import sys
console = Console()

def checkConfig():
	db = dbconfig()
	cursor = db.cursor()
	query = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA  WHERE SCHEMA_NAME = 'sim_card'"
	cursor.execute(query)
	results = cursor.fetchall()
	db.close()
	if len(results)!=0:
		return True
	return False

def delete():
    printc("[green][-][/green] Deleting config")

    if not checkConfig():
        printc("[yellow][-][/yellow] No configuration exists to delete!")
        return

    success = True
    try:
        db = dbconfig()
        cursor = db.cursor()
        query = "DROP DATABASE sim_card"
        cursor.execute(query)
        db.commit()
        db.close()
    except Exception as e:
        print(f"Error deleting config: {e}")
        success = False
    if success:
        printc("[green][+] Config deleted![/green]")
    sys.exit()

def db__init__():
    try:
        if not checkConfig():
            db = dbconfig()  # Assuming dbconfig() establishes the database connection
            cur = db.cursor()
            try:
                cur.execute("CREATE DATABASE sim_card")
            except Exception as e:
                printc("[red][!] An error occured while creating a database")
                console.print_exception(show_locals = True)
                sys.exit(0)
            printc("[green][+][/green] Database 'sim_card created")

            query = """
                   CREATE TABLE IF NOT EXISTS sim_card.info (
                        sim_number INTEGER PRIMARY KEY UNIQUE,  -- Unique identifier for each SIM card
                        phone_number INTEGER NOT NULL UNIQUE,  -- Associated phone number, must be unique
                        status TEXT CHECK(status IN ('active', 'inactive')) NOT NULL ,  -- Status of the SIM card
                        activation_date TIMESTAMP  -- Date the SIM card was activated, can be NULL before activation
                    );
                    """
            res = cur.execute(query)
            printc("[green][+][/green]Tables sim info created")

            
            db.commit()
            db.close()

            
            printc('[green]Database initialized successfully[/green]')
        else:
            printc('[yellow]Database already initialized[/yellow]')

    except Exception as e:
        printc(f'[red]Error initializing database: {e}[/red]')

if __name__ == "__main__":
    #delete()
    db__init__()  # Run the DB initialization