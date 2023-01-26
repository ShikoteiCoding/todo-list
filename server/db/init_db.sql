CREATE SEQUENCE list_id_pk_seq
    START 1
    INCREMENT 1
    NO MAXVALUE
    CACHE 1;

CREATE TABLE IF NOT EXISTS lists (
    id INT NOT NULL DEFAULT nextval('list_id_pk_seq'),
    title TEXT NOT NULL,
    create_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    modify_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);

CREATE SEQUENCE item_id_pk_seq
    START 1
    INCREMENT 1
    NO MAXVALUE
    CACHE 1;

CREATE TABLE IF NOT EXISTS items (
    id INT NOT NULL DEFAULT nextval('item_id_pk_seq'),
    content TEXT NOT NULL,
    create_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    modify_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    list_id INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_list
        FOREIGN KEY (list_id) 
            REFERENCES lists(id)
);