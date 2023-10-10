import docker
import psycopg2
import time


class TestSuit:
    def __init__(self, container_name, db_name, db_user, db_password):
        self.container_name = container_name
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

    def create_container(self, image_name):
        client = docker.from_env()
        try:
            container = client.containers.run(
                image=image_name,
                name=self.container_name,
                detach=True,
                environment={
                    "POSTGRES_DB": self.db_name,
                    "POSTGRES_USER": self.db_user,
                    "POSTGRES_PASSWORD": self.db_password,
                },
                ports={"5432/tcp": 5432},
            )
            return container
        except docker.errors.APIError as e:
            print(f"Error creating container: {e}")
            return None

    def connect_to_db(self, host="localhost", port=5432):
        try:
            connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=host,
                port=port,
            )
            return connection
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")
            return None

    def update_db(self, connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            connection.rollback()
            return None

    def stop_and_remove_container(self):
        client = docker.from_env()
        try:
            container = client.containers.get(self.container_name)
            container.stop()
            container.remove()
        except docker.errors.NotFound:
            print(f"Container '{self.container_name}' not found.")


if __name__ == "__main__":
    container_name = "test_db_container"
    db_name = "database"
    db_user = "4aika"
    db_password = "4aika"

    image_name = "test_db_image"

    test_suit = TestSuit(container_name, db_name, db_user, db_password)
    container = test_suit.create_container(image_name)

    if container:
        try:
            time.sleep(5)
            connection = test_suit.connect_to_db()
            update_query = "INSERT INTO users_test_table (name, birthdate) VALUES ('John Doe', '1990-5-15')"
            test_suit.update_db(connection, update_query)
            result = test_suit.update_db(connection, "SELECT * FROM users_test_table")
            if result:
                for row in result:
                    print(row)
            else:
                print("Failed to update data")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            test_suit.stop_and_remove_container()