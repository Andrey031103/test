import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect("game.db")
        self.cur = self.con.cursor()

        create_table_sql="""
            create table if not exists score (
                score integer primary key               
            );

        """
        self.cur.execute(create_table_sql)
        self.con.commit()

    def insert(self, score):
        insert_sql = f"""
            insert into score (score) values ({score});
        """
        self.cur.execute(insert_sql)
        self.con.commit()

    def select(self):
        select_sql = """
            select * from score order by score desc limit 3;
        """
        return self.cur.execute(select_sql).fetchall()

db = DB()




