CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);

ALTER TABLE public.roles OWNER TO postgres;

INSERT INTO public.roles (id, name) VALUES (1, 'Техническая поддержка');
INSERT INTO public.roles (id, name) VALUES (2, 'SUDO');
INSERT INTO public.roles (id, name) VALUES (3, 'Локальный администратор');
INSERT INTO public.roles (id, name) VALUES (4, 'Менеджер');
INSERT INTO public.roles (id, name) VALUES (5, 'Начальник производства');
INSERT INTO public.roles (id, name) VALUES (6, 'Оператор 3D-принтера');
INSERT INTO public.roles (id, name) VALUES (7, 'Техник');

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);