PGDMP  0    "                |            chicken    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    25405    chicken    DATABASE     ~   CREATE DATABASE chicken WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE chicken;
                postgres    false            �            1259    25437    cajas    TABLE     o   CREATE TABLE public.cajas (
    box_id integer NOT NULL,
    name character varying(80),
    amount integer
);
    DROP TABLE public.cajas;
       public         heap    postgres    false            �            1259    25448    cajas_box_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cajas_box_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.cajas_box_id_seq;
       public          postgres    false    215            �           0    0    cajas_box_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.cajas_box_id_seq OWNED BY public.cajas.box_id;
          public          postgres    false    216                       2604    25449    cajas box_id    DEFAULT     l   ALTER TABLE ONLY public.cajas ALTER COLUMN box_id SET DEFAULT nextval('public.cajas_box_id_seq'::regclass);
 ;   ALTER TABLE public.cajas ALTER COLUMN box_id DROP DEFAULT;
       public          postgres    false    216    215            �          0    25437    cajas 
   TABLE DATA           5   COPY public.cajas (box_id, name, amount) FROM stdin;
    public          postgres    false    215   W
       �           0    0    cajas_box_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.cajas_box_id_seq', 25, true);
          public          postgres    false    216                       2606    25451    cajas cajas_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.cajas
    ADD CONSTRAINT cajas_pkey PRIMARY KEY (box_id);
 :   ALTER TABLE ONLY public.cajas DROP CONSTRAINT cajas_pkey;
       public            postgres    false    215            �   K  x���MN�0���)|Ԥ�[��+B��ΐ��=�N���3N[�Vq��7�7��j���QZ��A�4 ?��(��;#mё��_�,8ȕ���!��1z.�@�g��d�5�Ȇ�x��͓翪O�X�B�{� `���ɚ�h>`���.'7JO|�q9�o���jD�G�r*^��C��\Nf�ӹ�hG��_��i��W���\�ֺͼ�N���i��G���J`���bk�F:��
/�����x$�^2��*o�?û*VbK���Xs��<6=}Y��x���04��=4f����(8	vJ�v���đ��նW��P�7z��     