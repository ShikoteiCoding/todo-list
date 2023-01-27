from flask import Flask, jsonify, request
from dotenv import load_dotenv
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    connection = psycopg2.connect(
        host=os.getenv("POSTGRES_EXTERNAL_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB")
    )
    return connection

@app.route("/notes", methods=["GET"])
def get_notes():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title, content, create_date, modify_date FROM notes")
            notes = cursor.fetchall()
            return jsonify([{
                "id": note[0],
                "title": note[1],
                "content": note[2],
                "create_date": note[3],
                "modify_date": note[4]
            } for note in notes])

@app.route("/notes", methods=["POST"])
def create_note():
    title = request.json["title"]
    content = request.json["content"]
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO notes (title, content, create_date, modify_date) VALUES (%s, %s, NOW(), NOW())",
                (title, content)
            )
            connection.commit()
            cursor.execute("SELECT id, title, content, create_date, modify_date FROM notes ORDER BY id DESC LIMIT 1")
            note = cursor.fetchone()
            return jsonify({
                "id": note[0],
                "title": note[1],
                "content": note[2],
                "create_date": note[3],
                "modify_date": note[4]
            }), 201

@app.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):
    title = request.json.get("title")
    content = request.json.get("content")
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE notes SET title = %s, content = %s, modify_date = NOW() WHERE id = %s",
                (title, content, id)
            )
            connection.commit()
            cursor.execute("SELECT id, title, content, create_date, modify_date FROM notes WHERE id = %s", (id,))
            note = cursor.fetchone()
            if not note:
                return jsonify({"error": "Note not found"}), 404
            return jsonify({
                "id": note[0],
                "title": note[1],
                "content": note[2],
                "create_date": note[3],
                "modify_date": note[4]
            })

@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM notes WHERE id = %s", (id,))
            connection.commit()
            if cursor.rowcount == 0:
                return jsonify({"error": "Note not found"}), 404
            return jsonify({"message": "Note deleted"})

if __name__ == "__main__":
    load_dotenv("../.env")
    app.run(host="0.0.0.0", port=8000)
