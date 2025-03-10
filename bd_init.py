import sqlite3


def init_db():
    conn = sqlite3.connect("agents.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestep INTEGER,
            agent_id INTEGER,
            param_1 REAL,
            param_2 REAL,
            param_3 REAL,
            param_4 REAL,
            param_5 REAL,
            param_6 REAL,
            param_7 REAL,
            param_8 REAL,
            param_9 REAL,
            param_10 REAL
        )
    """
    )

    conn.commit()
    conn.close()


init_db()
