class User(object):
    __id = None
    username = None
    __hashed_password = None
    email = None

    @property
    def id(self):
        return self.__id

    def save(self, cursor):
        if self.__id is None:
            query = f"""
            INSERT INTO "User"(username, hashed_password, email)
	        VALUES ('{self.username}','{self.__hashed_password}','{self.email}')
	        RETURNING id;
            """
            cursor.execute(query)
            id = cursor.fetchone()[0]
            self.__id = id
        else:
            query = f"""
            UPDATE public."User"
            SET username='{self.username}', 
                hashed_password='{self.__hashed_password}', 
                email='{self.email}'
            WHERE id={self.__id}
            """
            cursor.execute(query)

    @staticmethod
    def get_item_by_id(id, cursor):
        query = f"""
            SELECT username, hashed_password, email
	        FROM "User" WHERE id = {id};
        """
        cursor.execute(query)
        item = cursor.fetchone()
        u = User()
        u._User__id = id
        u.username = item[0]
        u._User__hashed_password = item[1]
        u.email = item[2]
        return u

    @staticmethod
    def get_create_sql():
        return """
            CREATE TABLE "User" (
            id serial,
            username varchar(200),
            hashed_password varchar(200),
            email varchar(200),
            PRIMARY KEY (id)
        );
        """

    def __str__(self):
        return f"{self.username}, {self.__hashed_password}, {self.email}"


class Message:

    def __init__(self):
        self.id = None
        self.body = None
        self.from_user = None
        self.to_user = None

    @staticmethod
    def get_create_sql():
        return """
            CREATE TABLE "Message" (
                id serial,
                body varchar(200),
                from_user integer,
                to_user  integer,
                PRIMARY KEY (id),
                FOREIGN KEY (from_user) references "User"(id),
                FOREIGN KEY (to_user) references "User"(id)
        );
        """

if __name__ == "__main__":
    from connection import get_connection

    c = get_connection()
    u = User.get_item_by_id(1,c.cursor())
    u.username = "Jagoda"
    u.save(c.cursor())
    print (u)
    # u = User()
    # u.username = 'SLAWEK'
    # u.email = 'slawek@jest.super'
    #
    # cursor = c.cursor()
    # u.save(cursor)
    # u.username = "Agnieszka"
    # u.save(cursor)
    # print(u.id)

    c.close()
