CREATE SEQUENCE note_id_pk_seq
    START 1
    INCREMENT 1
    NO MAXVALUE
    CACHE 1;

CREATE TABLE IF NOT EXISTS notes (
    id INT NOT NULL DEFAULT nextval('note_id_pk_seq'),
    title TEXT NOT NULL,
    content TEXT,
    create_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    modify_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    deleted BOOLEAN,
    PRIMARY KEY (id)
);