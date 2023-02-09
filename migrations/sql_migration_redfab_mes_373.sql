--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6
-- Dumped by pg_dump version 14.6

-- Started on 2023-02-09 11:43:23

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 904 (class 1247 OID 26380)
-- Name: sensorDataType; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public."sensorDataType" AS ENUM (
    'int',
    'string',
    'boolean'
);


ALTER TYPE public."sensorDataType" OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 26387)
-- Name: clusters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clusters (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "markingDeletion" boolean
);


ALTER TABLE public.clusters OWNER TO postgres;

--
-- TOC entry 3776 (class 0 OID 0)
-- Dependencies: 209
-- Name: TABLE clusters; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.clusters IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-88/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%9A%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D1%8B---clusters';


--
-- TOC entry 210 (class 1259 OID 26390)
-- Name: clusters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clusters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clusters_id_seq OWNER TO postgres;

--
-- TOC entry 3777 (class 0 OID 0)
-- Dependencies: 210
-- Name: clusters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clusters_id_seq OWNED BY public.clusters.id;


--
-- TOC entry 211 (class 1259 OID 26391)
-- Name: colors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.colors (
    id integer NOT NULL,
    name character varying(16),
    "additionalCleaning" smallint,
    composite boolean,
    "colorMaterialRGB" character varying(6),
    "colorPointRGB" character varying(6),
    "markingDeletion" boolean
);


ALTER TABLE public.colors OWNER TO postgres;

--
-- TOC entry 3778 (class 0 OID 0)
-- Dependencies: 211
-- Name: TABLE colors; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.colors IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-114/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%A6%D0%B2%D0%B5%D1%82%D0%B0-%D0%BC%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2---colors';


--
-- TOC entry 212 (class 1259 OID 26394)
-- Name: colors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.colors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.colors_id_seq OWNER TO postgres;

--
-- TOC entry 3779 (class 0 OID 0)
-- Dependencies: 212
-- Name: colors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.colors_id_seq OWNED BY public.colors.id;


--
-- TOC entry 213 (class 1259 OID 26395)
-- Name: currentPrinterStatuses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."currentPrinterStatuses" (
    id integer NOT NULL,
    "printerId" integer NOT NULL,
    online boolean NOT NULL,
    "idPrinterStatus" integer NOT NULL,
    update timestamp with time zone NOT NULL
);


ALTER TABLE public."currentPrinterStatuses" OWNER TO postgres;

--
-- TOC entry 3780 (class 0 OID 0)
-- Dependencies: 213
-- Name: TABLE "currentPrinterStatuses"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."currentPrinterStatuses" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-126/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%A2%D0%B5%D0%BA%D1%83%D1%89%D0%B8%D0%B9-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81-%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B0---currentPrinterPtatuses';


--
-- TOC entry 214 (class 1259 OID 26398)
-- Name: currentPrinterStatuses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."currentPrinterStatuses_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."currentPrinterStatuses_id_seq" OWNER TO postgres;

--
-- TOC entry 3781 (class 0 OID 0)
-- Dependencies: 214
-- Name: currentPrinterStatuses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."currentPrinterStatuses_id_seq" OWNED BY public."currentPrinterStatuses".id;


--
-- TOC entry 215 (class 1259 OID 26399)
-- Name: errorTriggers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."errorTriggers" (
    id bigint NOT NULL,
    code character varying(6) NOT NULL,
    "idPrinterStatus" integer NOT NULL,
    "booleanValue" boolean,
    "valueFrom" numeric(7,3),
    "valueTo" numeric(7,3),
    "idErrorType" integer,
    "errorText" character varying(255),
    "allowedHide" boolean,
    "idServiceOperation" integer,
    "automaticServiceOperation" boolean,
    "allowedIgnoreServiceOperation" boolean,
    "idSensor" integer
);


ALTER TABLE public."errorTriggers" OWNER TO postgres;

--
-- TOC entry 3782 (class 0 OID 0)
-- Dependencies: 215
-- Name: TABLE "errorTriggers"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."errorTriggers" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-145/%5B%D0%9E%D0%BF%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%5D-%D0%A2%D1%80%D0%B8%D0%B3%D0%B3%D0%B5%D1%80%D1%8B-%D0%BE%D1%88%D0%B8%D0%B1%D0%BE%D0%BA---errorTriggers';


--
-- TOC entry 216 (class 1259 OID 26402)
-- Name: errorTriggers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."errorTriggers_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."errorTriggers_id_seq" OWNER TO postgres;

--
-- TOC entry 3783 (class 0 OID 0)
-- Dependencies: 216
-- Name: errorTriggers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."errorTriggers_id_seq" OWNED BY public."errorTriggers".id;


--
-- TOC entry 217 (class 1259 OID 26403)
-- Name: errorTypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."errorTypes" (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public."errorTypes" OWNER TO postgres;

--
-- TOC entry 3784 (class 0 OID 0)
-- Dependencies: 217
-- Name: TABLE "errorTypes"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."errorTypes" IS 'документация https://yt.omegafuture.ru/articles/RedFabMES-A-146/%5B%D0%9E%D0%BF%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%5D-%D0%92%D0%B8%D0%B4%D1%8B-%D0%BE%D1%88%D0%B8%D0%B1%D0%BE%D0%BA---errorTypes';


--
-- TOC entry 218 (class 1259 OID 26406)
-- Name: errorTypes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."errorTypes_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."errorTypes_id_seq" OWNER TO postgres;

--
-- TOC entry 3785 (class 0 OID 0)
-- Dependencies: 218
-- Name: errorTypes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."errorTypes_id_seq" OWNED BY public."errorTypes".id;


--
-- TOC entry 219 (class 1259 OID 26407)
-- Name: extruders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.extruders (
    id integer NOT NULL,
    name character varying(16) NOT NULL,
    "serialNumber" character varying(255) NOT NULL
);


ALTER TABLE public.extruders OWNER TO postgres;

--
-- TOC entry 3786 (class 0 OID 0)
-- Dependencies: 219
-- Name: TABLE extruders; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.extruders IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-104/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%AD%D0%BA%D1%81%D1%82%D1%80%D1%83%D0%B4%D0%B5%D1%80%D1%8B---extruders';


--
-- TOC entry 220 (class 1259 OID 26410)
-- Name: extrudersInPrinters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."extrudersInPrinters" (
    id integer NOT NULL,
    "idPrinter" integer NOT NULL,
    "idExtruder" integer NOT NULL,
    main boolean
);


ALTER TABLE public."extrudersInPrinters" OWNER TO postgres;

--
-- TOC entry 3787 (class 0 OID 0)
-- Dependencies: 220
-- Name: TABLE "extrudersInPrinters"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."extrudersInPrinters" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-116/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%A1%D0%BE%D0%BE%D1%82%D0%BD%D0%B5%D1%81%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BE%D0%B2-%D1%81-%D1%8D%D0%BA%D1%81%D1%82%D1%80%D1%83%D0%B4%D0%B5%D1%80%D0%B0%D0%BC%D0%B8---extrudersInPrinters';


--
-- TOC entry 221 (class 1259 OID 26413)
-- Name: extrudersInPrinters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."extrudersInPrinters_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."extrudersInPrinters_id_seq" OWNER TO postgres;

--
-- TOC entry 3788 (class 0 OID 0)
-- Dependencies: 221
-- Name: extrudersInPrinters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."extrudersInPrinters_id_seq" OWNED BY public."extrudersInPrinters".id;


--
-- TOC entry 222 (class 1259 OID 26414)
-- Name: extruders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.extruders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.extruders_id_seq OWNER TO postgres;

--
-- TOC entry 3789 (class 0 OID 0)
-- Dependencies: 222
-- Name: extruders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.extruders_id_seq OWNED BY public.extruders.id;


--
-- TOC entry 223 (class 1259 OID 26415)
-- Name: makers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.makers (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "markingDeletion" boolean
);


ALTER TABLE public.makers OWNER TO postgres;

--
-- TOC entry 3790 (class 0 OID 0)
-- Dependencies: 223
-- Name: TABLE makers; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.makers IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-112/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%9F%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D0%B8---makers';


--
-- TOC entry 224 (class 1259 OID 26418)
-- Name: makers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.makers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.makers_id_seq OWNER TO postgres;

--
-- TOC entry 3791 (class 0 OID 0)
-- Dependencies: 224
-- Name: makers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.makers_id_seq OWNED BY public.makers.id;


--
-- TOC entry 225 (class 1259 OID 26419)
-- Name: materials; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.materials (
    id integer NOT NULL,
    name character varying NOT NULL,
    "idPolymerBase" integer NOT NULL,
    composite boolean,
    "idMaker" integer,
    density numeric(3,2) NOT NULL,
    "printingTemp" smallint NOT NULL,
    "maxRadiatorTemp" smallint NOT NULL,
    "tableTemp" smallint NOT NULL,
    "blowingParts" smallint NOT NULL,
    "chamberTemp" smallint NOT NULL,
    "timeSwitchCoolingMode" smallint NOT NULL,
    "coolingModeTemp" smallint NOT NULL,
    "materialUnloadSpeed" smallint NOT NULL,
    "materialUnloadTemp" smallint NOT NULL,
    "materialLoadSpeed" smallint NOT NULL,
    "materialCleanLength" smallint NOT NULL,
    "materialServeCoef" smallint NOT NULL,
    "gramsCost" numeric(3,2),
    "markingDeletion" boolean
);


ALTER TABLE public.materials OWNER TO postgres;

--
-- TOC entry 3792 (class 0 OID 0)
-- Dependencies: 225
-- Name: TABLE materials; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.materials IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-110/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%9C%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D1%8B---materials';


--
-- TOC entry 226 (class 1259 OID 26424)
-- Name: materialsInPrinters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."materialsInPrinters" (
    id integer NOT NULL,
    "idPrinter" integer NOT NULL,
    "idMaterial" integer NOT NULL,
    cell smallint NOT NULL,
    "idColor" integer NOT NULL,
    "idPackage" integer NOT NULL
);


ALTER TABLE public."materialsInPrinters" OWNER TO postgres;

--
-- TOC entry 3793 (class 0 OID 0)
-- Dependencies: 226
-- Name: TABLE "materialsInPrinters"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."materialsInPrinters" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-115/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%A1%D0%BE%D0%BE%D1%82%D0%BD%D0%B5%D1%81%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BE%D0%B2-%D1%81-%D0%BC%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B0%D0%BC%D0%B8---materialsInPrinters';


--
-- TOC entry 227 (class 1259 OID 26427)
-- Name: materialsInPrinters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."materialsInPrinters_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."materialsInPrinters_id_seq" OWNER TO postgres;

--
-- TOC entry 3794 (class 0 OID 0)
-- Dependencies: 227
-- Name: materialsInPrinters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."materialsInPrinters_id_seq" OWNED BY public."materialsInPrinters".id;


--
-- TOC entry 228 (class 1259 OID 26428)
-- Name: materials_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.materials_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.materials_id_seq OWNER TO postgres;

--
-- TOC entry 3795 (class 0 OID 0)
-- Dependencies: 228
-- Name: materials_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.materials_id_seq OWNED BY public.materials.id;


--
-- TOC entry 229 (class 1259 OID 26429)
-- Name: nozzlesSizes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."nozzlesSizes" (
    id integer NOT NULL,
    "nozzlesSize" numeric(7,3) NOT NULL,
    "compositesPrinting" boolean,
    "markingDeletion" boolean
);


ALTER TABLE public."nozzlesSizes" OWNER TO postgres;

--
-- TOC entry 3796 (class 0 OID 0)
-- Dependencies: 229
-- Name: TABLE "nozzlesSizes"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."nozzlesSizes" IS 'Документацияч https://yt.omegafuture.ru/articles/RedFabMES-A-106/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%A2%D0%B8%D0%BF%D0%BE%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D1%8B-%D1%81%D0%BE%D0%BF%D0%B5%D0%BB---nozzlesSizes';


--
-- TOC entry 230 (class 1259 OID 26432)
-- Name: nozzlesSizes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."nozzlesSizes_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."nozzlesSizes_id_seq" OWNER TO postgres;

--
-- TOC entry 3797 (class 0 OID 0)
-- Dependencies: 230
-- Name: nozzlesSizes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."nozzlesSizes_id_seq" OWNED BY public."nozzlesSizes".id;


--
-- TOC entry 231 (class 1259 OID 26433)
-- Name: nozzlesTypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."nozzlesTypes" (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "compositesPrinting" boolean,
    "tempIncrease" smallint,
    "markingDeletion" boolean
);


ALTER TABLE public."nozzlesTypes" OWNER TO postgres;

--
-- TOC entry 3798 (class 0 OID 0)
-- Dependencies: 231
-- Name: TABLE "nozzlesTypes"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."nozzlesTypes" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-105/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%92%D0%B8%D0%B4-%D1%81%D0%BE%D0%BF%D0%BB%D0%B0---nozzlesTypes';


--
-- TOC entry 232 (class 1259 OID 26436)
-- Name: nozzlesTypes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."nozzlesTypes_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."nozzlesTypes_id_seq" OWNER TO postgres;

--
-- TOC entry 3799 (class 0 OID 0)
-- Dependencies: 232
-- Name: nozzlesTypes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."nozzlesTypes_id_seq" OWNED BY public."nozzlesTypes".id;


--
-- TOC entry 233 (class 1259 OID 26437)
-- Name: operGroups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."operGroups" (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "idCluster" integer NOT NULL,
    "idNozzleType" integer NOT NULL,
    "idNozzleSize" integer NOT NULL,
    "markingDeletion" boolean
);


ALTER TABLE public."operGroups" OWNER TO postgres;

--
-- TOC entry 3800 (class 0 OID 0)
-- Dependencies: 233
-- Name: TABLE "operGroups"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."operGroups" IS 'документация https://yt.omegafuture.ru/articles/RedFabMES-A-89/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%8B---operGroups';


--
-- TOC entry 234 (class 1259 OID 26440)
-- Name: operGroups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."operGroups_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."operGroups_id_seq" OWNER TO postgres;

--
-- TOC entry 3801 (class 0 OID 0)
-- Dependencies: 234
-- Name: operGroups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."operGroups_id_seq" OWNED BY public."operGroups".id;


--
-- TOC entry 235 (class 1259 OID 26441)
-- Name: packing; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.packing (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    weight numeric(5,2),
    "markingDeletion" boolean
);


ALTER TABLE public.packing OWNER TO postgres;

--
-- TOC entry 3802 (class 0 OID 0)
-- Dependencies: 235
-- Name: TABLE packing; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.packing IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-113/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%A4%D0%B0%D1%81%D0%BE%D0%B2%D0%BA%D0%B0---packing';


--
-- TOC entry 236 (class 1259 OID 26444)
-- Name: packing_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.packing_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.packing_id_seq OWNER TO postgres;

--
-- TOC entry 3803 (class 0 OID 0)
-- Dependencies: 236
-- Name: packing_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.packing_id_seq OWNED BY public.packing.id;


--
-- TOC entry 237 (class 1259 OID 26445)
-- Name: partners; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.partners (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    inn character varying(12),
    kpp character varying(9),
    address text,
    comment text,
    "markingDeletion" boolean,
    created timestamp with time zone NOT NULL
);


ALTER TABLE public.partners OWNER TO postgres;

--
-- TOC entry 3804 (class 0 OID 0)
-- Dependencies: 237
-- Name: TABLE partners; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.partners IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-121/%5B%D0%9E%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8%5D-%D0%9A%D0%BE%D0%BD%D1%82%D1%80%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%8B---partners';


--
-- TOC entry 238 (class 1259 OID 26450)
-- Name: partners_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.partners_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.partners_id_seq OWNER TO postgres;

--
-- TOC entry 3805 (class 0 OID 0)
-- Dependencies: 238
-- Name: partners_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.partners_id_seq OWNED BY public.partners.id;


--
-- TOC entry 239 (class 1259 OID 26451)
-- Name: polymerBases; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."polymerBases" (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "markingDeletion" boolean
);


ALTER TABLE public."polymerBases" OWNER TO postgres;

--
-- TOC entry 3806 (class 0 OID 0)
-- Dependencies: 239
-- Name: TABLE "polymerBases"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."polymerBases" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-111/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%9F%D0%BE%D0%BB%D0%B8%D0%BC%D0%B5%D1%80%D0%BD%D1%8B%D0%B5-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B---polymerBases';


--
-- TOC entry 240 (class 1259 OID 26454)
-- Name: polymerBases_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."polymerBases_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."polymerBases_id_seq" OWNER TO postgres;

--
-- TOC entry 3807 (class 0 OID 0)
-- Dependencies: 240
-- Name: polymerBases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."polymerBases_id_seq" OWNED BY public."polymerBases".id;


--
-- TOC entry 241 (class 1259 OID 26455)
-- Name: printStatusHistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."printStatusHistory" (
    id integer NOT NULL,
    period timestamp with time zone NOT NULL,
    "idPrinterStatus" integer NOT NULL,
    "idPrinter" integer NOT NULL
);


ALTER TABLE public."printStatusHistory" OWNER TO postgres;

--
-- TOC entry 3808 (class 0 OID 0)
-- Dependencies: 241
-- Name: TABLE "printStatusHistory"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."printStatusHistory" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-125/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%BE%D0%B2-%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BE%D0%B2---printerStatusHistory';


--
-- TOC entry 242 (class 1259 OID 26458)
-- Name: printStatusHistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."printStatusHistory_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."printStatusHistory_id_seq" OWNER TO postgres;

--
-- TOC entry 3809 (class 0 OID 0)
-- Dependencies: 242
-- Name: printStatusHistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."printStatusHistory_id_seq" OWNED BY public."printStatusHistory".id;


--
-- TOC entry 243 (class 1259 OID 26459)
-- Name: printerStatus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."printerStatus" (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public."printerStatus" OWNER TO postgres;

--
-- TOC entry 3810 (class 0 OID 0)
-- Dependencies: 243
-- Name: TABLE "printerStatus"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."printerStatus" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-124/%5B%D0%9E%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8%5D-%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81%D1%8B-%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BE%D0%B2---printerStatuses';


--
-- TOC entry 244 (class 1259 OID 26464)
-- Name: printerStatus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."printerStatus_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."printerStatus_id_seq" OWNER TO postgres;

--
-- TOC entry 3811 (class 0 OID 0)
-- Dependencies: 244
-- Name: printerStatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."printerStatus_id_seq" OWNED BY public."printerStatus".id;


--
-- TOC entry 245 (class 1259 OID 26465)
-- Name: printers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.printers (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "idOperGroups" integer NOT NULL,
    "idStand" integer NOT NULL,
    "modulePlace" smallint NOT NULL,
    "idVacuumSystem" integer NOT NULL,
    "vacuumSystemValve" integer NOT NULL,
    "serialNumber" character varying(255) NOT NULL,
    "printerIP" character varying(16) NOT NULL,
    "printerPort" integer NOT NULL,
    "idTableType" integer NOT NULL,
    "basicCellQuantity" smallint,
    "supportCellQuantity" smallint,
    "activeBasicCell" smallint,
    "activeSupportCell" smallint,
    "webIs" boolean,
    "webcamURL" character varying(255),
    "markingDeletion" boolean
);


ALTER TABLE public.printers OWNER TO postgres;

--
-- TOC entry 3812 (class 0 OID 0)
-- Dependencies: 245
-- Name: TABLE printers; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.printers IS 'документация https://yt.omegafuture.ru/articles/RedFabMES-A-102/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%9F%D1%80%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%8B---printers';


--
-- TOC entry 246 (class 1259 OID 26470)
-- Name: printers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.printers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.printers_id_seq OWNER TO postgres;

--
-- TOC entry 3813 (class 0 OID 0)
-- Dependencies: 246
-- Name: printers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.printers_id_seq OWNED BY public.printers.id;


--
-- TOC entry 247 (class 1259 OID 26471)
-- Name: priorities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.priorities (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.priorities OWNER TO postgres;

--
-- TOC entry 3814 (class 0 OID 0)
-- Dependencies: 247
-- Name: TABLE priorities; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.priorities IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-120/%5B%D0%9E%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8%5D-%D0%9F%D1%80%D0%B8%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D1%82%D1%8B-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8---priorities';


--
-- TOC entry 248 (class 1259 OID 26474)
-- Name: priorities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.priorities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.priorities_id_seq OWNER TO postgres;

--
-- TOC entry 3815 (class 0 OID 0)
-- Dependencies: 248
-- Name: priorities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.priorities_id_seq OWNED BY public.priorities.id;


--
-- TOC entry 249 (class 1259 OID 26475)
-- Name: projectStatusHistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."projectStatusHistory" (
    id integer NOT NULL,
    period timestamp(2) with time zone NOT NULL,
    "idProject" integer NOT NULL,
    "idProjectStatus" integer NOT NULL
);


ALTER TABLE public."projectStatusHistory" OWNER TO postgres;

--
-- TOC entry 3816 (class 0 OID 0)
-- Dependencies: 249
-- Name: TABLE "projectStatusHistory"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."projectStatusHistory" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-157/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%BE%D0%B2-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%B2---projectStatusHistory';


--
-- TOC entry 250 (class 1259 OID 26478)
-- Name: projectStatusHistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."projectStatusHistory_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."projectStatusHistory_id_seq" OWNER TO postgres;

--
-- TOC entry 3817 (class 0 OID 0)
-- Dependencies: 250
-- Name: projectStatusHistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."projectStatusHistory_id_seq" OWNED BY public."projectStatusHistory".id;


--
-- TOC entry 251 (class 1259 OID 26479)
-- Name: projectStatuses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."projectStatuses" (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public."projectStatuses" OWNER TO postgres;

--
-- TOC entry 3818 (class 0 OID 0)
-- Dependencies: 251
-- Name: TABLE "projectStatuses"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."projectStatuses" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-130/%5B%D0%9E%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8%5D-%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81%D1%8B-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0---projectStatuses';


--
-- TOC entry 252 (class 1259 OID 26482)
-- Name: projectStatuses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."projectStatuses_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."projectStatuses_id_seq" OWNER TO postgres;

--
-- TOC entry 3819 (class 0 OID 0)
-- Dependencies: 252
-- Name: projectStatuses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."projectStatuses_id_seq" OWNED BY public."projectStatuses".id;


--
-- TOC entry 253 (class 1259 OID 26483)
-- Name: projects; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.projects (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "idPriority" integer,
    "createDate" time with time zone NOT NULL,
    "deadLine" timestamp with time zone,
    "changeDate" timestamp with time zone NOT NULL,
    "orderNumber" character varying(255),
    "idPartner" integer,
    cost bigint,
    "idResponsible" integer,
    "idAuthor" integer,
    comment text,
    "markingDeletion" boolean
);


ALTER TABLE public.projects OWNER TO postgres;

--
-- TOC entry 3820 (class 0 OID 0)
-- Dependencies: 253
-- Name: TABLE projects; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.projects IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-118/%5B%D0%9E%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8%5D-%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B---projects';


--
-- TOC entry 254 (class 1259 OID 26488)
-- Name: projects_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.projects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.projects_id_seq OWNER TO postgres;

--
-- TOC entry 3821 (class 0 OID 0)
-- Dependencies: 254
-- Name: projects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.projects_id_seq OWNED BY public.projects.id;


--
-- TOC entry 255 (class 1259 OID 26489)
-- Name: reactions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reactions (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE public.reactions OWNER TO postgres;

--
-- TOC entry 3822 (class 0 OID 0)
-- Dependencies: 255
-- Name: TABLE reactions; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.reactions IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-147/%5B%D0%9E%D0%BF%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%5D-%D0%A0%D0%B5%D0%B0%D0%BA%D1%86%D0%B8%D0%B8-%D0%BD%D0%B0-%D0%BE%D0%BF%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D0%B5---reactions';


--
-- TOC entry 256 (class 1259 OID 26492)
-- Name: reactions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reactions_id_seq OWNER TO postgres;

--
-- TOC entry 3823 (class 0 OID 0)
-- Dependencies: 256
-- Name: reactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reactions_id_seq OWNED BY public.reactions.id;


--
-- TOC entry 291 (class 1259 OID 28687)
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- TOC entry 257 (class 1259 OID 26493)
-- Name: sensorData; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."sensorData" (
    id bigint NOT NULL,
    period timestamp with time zone,
    "idSensor" bigint,
    data text,
    "dataType" public."sensorDataType",
    "idPrinter" integer
);


ALTER TABLE public."sensorData" OWNER TO postgres;

--
-- TOC entry 258 (class 1259 OID 26498)
-- Name: sensorData_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."sensorData_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."sensorData_id_seq" OWNER TO postgres;

--
-- TOC entry 3824 (class 0 OID 0)
-- Dependencies: 258
-- Name: sensorData_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."sensorData_id_seq" OWNED BY public."sensorData".id;


--
-- TOC entry 259 (class 1259 OID 26499)
-- Name: sensorGroups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."sensorGroups" (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE public."sensorGroups" OWNER TO postgres;

--
-- TOC entry 3825 (class 0 OID 0)
-- Dependencies: 259
-- Name: TABLE "sensorGroups"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."sensorGroups" IS 'Документация таблицы https://yt.omegafuture.ru/articles/RedFabMES-A-109/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%93%D1%80%D1%83%D0%BF%D0%BF%D1%8B-%D0%B4%D0%B0%D1%82%D1%87%D0%B8%D0%BA%D0%BE%D0%B2---sensorGroups';


--
-- TOC entry 260 (class 1259 OID 26502)
-- Name: sensorGroups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."sensorGroups_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."sensorGroups_id_seq" OWNER TO postgres;

--
-- TOC entry 3826 (class 0 OID 0)
-- Dependencies: 260
-- Name: sensorGroups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."sensorGroups_id_seq" OWNED BY public."sensorGroups".id;


--
-- TOC entry 261 (class 1259 OID 26503)
-- Name: sensors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sensors (
    id bigint NOT NULL,
    name character varying(1000),
    "nameIdentifier" character varying(255),
    "dataType" public."sensorDataType",
    description text,
    "requiredUsed" boolean,
    "CanDeactivate" boolean,
    "markingDeletion" boolean,
    "idSensorGroup" integer
);


ALTER TABLE public.sensors OWNER TO postgres;

--
-- TOC entry 262 (class 1259 OID 26508)
-- Name: sensorsInPrinters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."sensorsInPrinters" (
    id bigint NOT NULL,
    "idPrinter" integer NOT NULL,
    "idSensor" bigint NOT NULL,
    "isUsed" boolean
);


ALTER TABLE public."sensorsInPrinters" OWNER TO postgres;

--
-- TOC entry 3827 (class 0 OID 0)
-- Dependencies: 262
-- Name: TABLE "sensorsInPrinters"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."sensorsInPrinters" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-117/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%A1%D0%BE%D0%BE%D1%82%D0%BD%D0%B5%D1%81%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BE%D0%B2-%D1%81-%D0%B4%D0%B0%D1%82%D1%87%D0%B8%D0%BA%D0%B0%D0%BC%D0%B8---sensorsInPrinters';


--
-- TOC entry 263 (class 1259 OID 26511)
-- Name: sensorsInPrinters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."sensorsInPrinters_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."sensorsInPrinters_id_seq" OWNER TO postgres;

--
-- TOC entry 3828 (class 0 OID 0)
-- Dependencies: 263
-- Name: sensorsInPrinters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."sensorsInPrinters_id_seq" OWNED BY public."sensorsInPrinters".id;


--
-- TOC entry 264 (class 1259 OID 26512)
-- Name: sensors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sensors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sensors_id_seq OWNER TO postgres;

--
-- TOC entry 3829 (class 0 OID 0)
-- Dependencies: 264
-- Name: sensors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sensors_id_seq OWNED BY public.sensors.id;


--
-- TOC entry 265 (class 1259 OID 26513)
-- Name: serviceOperationHistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."serviceOperationHistory" (
    id integer NOT NULL,
    "startAt" timestamp with time zone NOT NULL,
    "endAt" timestamp with time zone NOT NULL,
    "idPrinter" integer NOT NULL,
    "idServiceOperation" integer NOT NULL,
    "idUser" integer NOT NULL
);


ALTER TABLE public."serviceOperationHistory" OWNER TO postgres;

--
-- TOC entry 3830 (class 0 OID 0)
-- Dependencies: 265
-- Name: TABLE "serviceOperationHistory"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."serviceOperationHistory" IS 'Документация  https://yt.omegafuture.ru/articles/RedFabMES-A-133/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BD%D1%8B%D1%85-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B9---serviceOperationHistory';


--
-- TOC entry 266 (class 1259 OID 26516)
-- Name: serviceOperationHistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."serviceOperationHistory_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."serviceOperationHistory_id_seq" OWNER TO postgres;

--
-- TOC entry 3831 (class 0 OID 0)
-- Dependencies: 266
-- Name: serviceOperationHistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."serviceOperationHistory_id_seq" OWNED BY public."serviceOperationHistory".id;


--
-- TOC entry 267 (class 1259 OID 26517)
-- Name: serviceOperations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."serviceOperations" (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "functionName" character varying(255) NOT NULL
);


ALTER TABLE public."serviceOperations" OWNER TO postgres;

--
-- TOC entry 3832 (class 0 OID 0)
-- Dependencies: 267
-- Name: TABLE "serviceOperations"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."serviceOperations" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-131/%5B%D0%A1%D0%B5%D1%80%D0%B2%D0%B8%D1%81%5D-%D0%A1%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8---serviceOperations';


--
-- TOC entry 268 (class 1259 OID 26522)
-- Name: serviceOperations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."serviceOperations_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."serviceOperations_id_seq" OWNER TO postgres;

--
-- TOC entry 3833 (class 0 OID 0)
-- Dependencies: 268
-- Name: serviceOperations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."serviceOperations_id_seq" OWNED BY public."serviceOperations".id;


--
-- TOC entry 269 (class 1259 OID 26523)
-- Name: servicePositions ; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."servicePositions " (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    "positionX" smallint NOT NULL,
    "positionY" smallint NOT NULL,
    "positionZ" smallint NOT NULL
);


ALTER TABLE public."servicePositions " OWNER TO postgres;

--
-- TOC entry 3834 (class 0 OID 0)
-- Dependencies: 269
-- Name: TABLE "servicePositions "; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."servicePositions " IS 'документация https://yt.omegafuture.ru/articles/RedFabMES-A-132/%5B%D0%A1%D0%B5%D1%80%D0%B2%D0%B8%D1%81%5D-%D0%A1%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D0%B7%D0%B8%D1%86%D0%B8%D0%B8';


--
-- TOC entry 270 (class 1259 OID 26526)
-- Name: servicePositions _id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."servicePositions _id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."servicePositions _id_seq" OWNER TO postgres;

--
-- TOC entry 3835 (class 0 OID 0)
-- Dependencies: 270
-- Name: servicePositions _id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."servicePositions _id_seq" OWNED BY public."servicePositions ".id;


--
-- TOC entry 271 (class 1259 OID 26527)
-- Name: stands; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stands (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "markingDeletion" boolean,
    "idCluster" integer
);


ALTER TABLE public.stands OWNER TO postgres;

--
-- TOC entry 3836 (class 0 OID 0)
-- Dependencies: 271
-- Name: TABLE stands; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.stands IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-90/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%A1%D1%82%D0%BE%D0%B9%D0%BA%D0%B8---stands';


--
-- TOC entry 272 (class 1259 OID 26530)
-- Name: stands_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stands_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stands_id_seq OWNER TO postgres;

--
-- TOC entry 3837 (class 0 OID 0)
-- Dependencies: 272
-- Name: stands_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stands_id_seq OWNED BY public.stands.id;


--
-- TOC entry 273 (class 1259 OID 26531)
-- Name: tablesTypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."tablesTypes" (
    id integer NOT NULL,
    name character(32)[] NOT NULL,
    "conveyorPrinting" boolean,
    "stretchingLength" smallint,
    "tempIncrease" smallint,
    "markingDeletion" boolean
);


ALTER TABLE public."tablesTypes" OWNER TO postgres;

--
-- TOC entry 3838 (class 0 OID 0)
-- Dependencies: 273
-- Name: TABLE "tablesTypes"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."tablesTypes" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-107/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%A2%D0%B8%D0%BF%D1%8B-%D1%81%D1%82%D0%BE%D0%BB%D0%BE%D0%B2---tablesTypes';


--
-- TOC entry 274 (class 1259 OID 26536)
-- Name: tablesTypes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."tablesTypes_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."tablesTypes_id_seq" OWNER TO postgres;

--
-- TOC entry 3839 (class 0 OID 0)
-- Dependencies: 274
-- Name: tablesTypes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."tablesTypes_id_seq" OWNED BY public."tablesTypes".id;


--
-- TOC entry 275 (class 1259 OID 26537)
-- Name: taskFiles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."taskFiles" (
    id integer NOT NULL,
    "nameFile" character varying(255) NOT NULL,
    "extFile" character varying(5) NOT NULL,
    "idTask" integer NOT NULL,
    "idOwner" integer NOT NULL,
    "sizeFile" numeric(7,3) NOT NULL,
    "hashFile" character varying(32) NOT NULL,
    path character varying(64) NOT NULL,
    created timestamp with time zone NOT NULL
);


ALTER TABLE public."taskFiles" OWNER TO postgres;

--
-- TOC entry 3840 (class 0 OID 0)
-- Dependencies: 275
-- Name: TABLE "taskFiles"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."taskFiles" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-122/%5B%D0%9E%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8%5D-%D0%A4%D0%B0%D0%B9%D0%BB%D1%8B-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9---taskFiles';


--
-- TOC entry 276 (class 1259 OID 26540)
-- Name: taskFiles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."taskFiles_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."taskFiles_id_seq" OWNER TO postgres;

--
-- TOC entry 3841 (class 0 OID 0)
-- Dependencies: 276
-- Name: taskFiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."taskFiles_id_seq" OWNED BY public."taskFiles".id;


--
-- TOC entry 277 (class 1259 OID 26541)
-- Name: taskPrinting; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."taskPrinting" (
    id integer NOT NULL,
    "idTask" integer NOT NULL,
    "startAt" timestamp with time zone NOT NULL,
    "idPrinter" integer NOT NULL
);


ALTER TABLE public."taskPrinting" OWNER TO postgres;

--
-- TOC entry 3842 (class 0 OID 0)
-- Dependencies: 277
-- Name: TABLE "taskPrinting"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."taskPrinting" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-129/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BA-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8---taskPrinting';


--
-- TOC entry 278 (class 1259 OID 26544)
-- Name: taskPrinting_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."taskPrinting_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."taskPrinting_id_seq" OWNER TO postgres;

--
-- TOC entry 3843 (class 0 OID 0)
-- Dependencies: 278
-- Name: taskPrinting_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."taskPrinting_id_seq" OWNED BY public."taskPrinting".id;


--
-- TOC entry 279 (class 1259 OID 26545)
-- Name: taskStatusHistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."taskStatusHistory" (
    id integer NOT NULL,
    period timestamp(2) with time zone NOT NULL,
    "idTask" integer NOT NULL,
    "idTaskStatus" integer NOT NULL,
    "idPrinter" integer NOT NULL
);


ALTER TABLE public."taskStatusHistory" OWNER TO postgres;

--
-- TOC entry 3844 (class 0 OID 0)
-- Dependencies: 279
-- Name: TABLE "taskStatusHistory"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."taskStatusHistory" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-128/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%BE%D0%B2-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9---taskPrintingHistory';


--
-- TOC entry 280 (class 1259 OID 26548)
-- Name: taskStatusHistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."taskStatusHistory_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."taskStatusHistory_id_seq" OWNER TO postgres;

--
-- TOC entry 3845 (class 0 OID 0)
-- Dependencies: 280
-- Name: taskStatusHistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."taskStatusHistory_id_seq" OWNED BY public."taskStatusHistory".id;


--
-- TOC entry 281 (class 1259 OID 26549)
-- Name: taskStatuses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."taskStatuses" (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public."taskStatuses" OWNER TO postgres;

--
-- TOC entry 3846 (class 0 OID 0)
-- Dependencies: 281
-- Name: TABLE "taskStatuses"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."taskStatuses" IS 'документация https://yt.omegafuture.ru/articles/RedFabMES-A-127/%5B%D0%9E%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8%5D-%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81%D1%8B-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8---taskStatuses';


--
-- TOC entry 282 (class 1259 OID 26554)
-- Name: taskStatuses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."taskStatuses_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."taskStatuses_id_seq" OWNER TO postgres;

--
-- TOC entry 3847 (class 0 OID 0)
-- Dependencies: 282
-- Name: taskStatuses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."taskStatuses_id_seq" OWNED BY public."taskStatuses".id;


--
-- TOC entry 283 (class 1259 OID 26555)
-- Name: tasks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tasks (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "idProject" integer NOT NULL,
    "idPriority" integer NOT NULL,
    "numberCopies" smallint NOT NULL,
    "planPrintTime" interval NOT NULL,
    "factPrintTime" interval,
    "idOperGroup" integer NOT NULL,
    "twoExtrPrint" boolean NOT NULL,
    "idBasicMaterial" integer NOT NULL,
    "idBasicColor" integer,
    "idSupportMaterial" integer,
    "idSupportColor" integer,
    "markingDeletion" boolean NOT NULL,
    update timestamp with time zone NOT NULL
);


ALTER TABLE public.tasks OWNER TO postgres;

--
-- TOC entry 3848 (class 0 OID 0)
-- Dependencies: 283
-- Name: TABLE tasks; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.tasks IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-119/%5B%D0%9E%D1%87%D0%B5%D1%80%D0%B5%D0%B4%D1%8C-%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%B8%5D-%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F---tasks';


--
-- TOC entry 284 (class 1259 OID 26558)
-- Name: tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tasks_id_seq OWNER TO postgres;

--
-- TOC entry 3849 (class 0 OID 0)
-- Dependencies: 284
-- Name: tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;


--
-- TOC entry 285 (class 1259 OID 26559)
-- Name: triggersHystory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."triggersHystory" (
    id bigint NOT NULL,
    period timestamp with time zone NOT NULL,
    "idPrinter" integer NOT NULL,
    "idTrigger" integer NOT NULL,
    "idUser" integer NOT NULL,
    "idReaction" integer NOT NULL
);


ALTER TABLE public."triggersHystory" OWNER TO postgres;

--
-- TOC entry 3850 (class 0 OID 0)
-- Dependencies: 285
-- Name: TABLE "triggersHystory"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."triggersHystory" IS 'документация';


--
-- TOC entry 286 (class 1259 OID 26562)
-- Name: triggersHystory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."triggersHystory_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."triggersHystory_id_seq" OWNER TO postgres;

--
-- TOC entry 3851 (class 0 OID 0)
-- Dependencies: 286
-- Name: triggersHystory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."triggersHystory_id_seq" OWNED BY public."triggersHystory".id;


--
-- TOC entry 287 (class 1259 OID 26563)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    "passwordHash" character varying(32) NOT NULL,
    login character varying(32) NOT NULL,
    "markingDeletion" boolean,
    firstname character varying,
    "position" character varying,
    "idRole" integer
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 3852 (class 0 OID 0)
-- Dependencies: 287
-- Name: TABLE users; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.users IS 'документация https://yt.omegafuture.ru/articles/RedFabMES-A-92/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8---users';


--
-- TOC entry 288 (class 1259 OID 26566)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 3853 (class 0 OID 0)
-- Dependencies: 288
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 289 (class 1259 OID 26567)
-- Name: vacuumSystem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."vacuumSystem" (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    ip character varying(16) NOT NULL,
    port integer NOT NULL,
    "markingDeletion" boolean
);


ALTER TABLE public."vacuumSystem" OWNER TO postgres;

--
-- TOC entry 3854 (class 0 OID 0)
-- Dependencies: 289
-- Name: TABLE "vacuumSystem"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."vacuumSystem" IS 'Документация https://yt.omegafuture.ru/articles/RedFabMES-A-103/%5B%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8%5D-%D0%92%D0%B0%D0%BA%D1%83%D1%83%D0%BC%D0%BD%D0%B0%D1%8F-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0---vacuumSystem';


--
-- TOC entry 290 (class 1259 OID 26570)
-- Name: vacuumSystem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."vacuumSystem_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."vacuumSystem_id_seq" OWNER TO postgres;

--
-- TOC entry 3855 (class 0 OID 0)
-- Dependencies: 290
-- Name: vacuumSystem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."vacuumSystem_id_seq" OWNED BY public."vacuumSystem".id;


--
-- TOC entry 3371 (class 2604 OID 26571)
-- Name: clusters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clusters ALTER COLUMN id SET DEFAULT nextval('public.clusters_id_seq'::regclass);


--
-- TOC entry 3372 (class 2604 OID 26572)
-- Name: colors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.colors ALTER COLUMN id SET DEFAULT nextval('public.colors_id_seq'::regclass);


--
-- TOC entry 3373 (class 2604 OID 26573)
-- Name: currentPrinterStatuses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."currentPrinterStatuses" ALTER COLUMN id SET DEFAULT nextval('public."currentPrinterStatuses_id_seq"'::regclass);


--
-- TOC entry 3374 (class 2604 OID 26574)
-- Name: errorTriggers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."errorTriggers" ALTER COLUMN id SET DEFAULT nextval('public."errorTriggers_id_seq"'::regclass);


--
-- TOC entry 3375 (class 2604 OID 26575)
-- Name: errorTypes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."errorTypes" ALTER COLUMN id SET DEFAULT nextval('public."errorTypes_id_seq"'::regclass);


--
-- TOC entry 3376 (class 2604 OID 26576)
-- Name: extruders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.extruders ALTER COLUMN id SET DEFAULT nextval('public.extruders_id_seq'::regclass);


--
-- TOC entry 3377 (class 2604 OID 26577)
-- Name: extrudersInPrinters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."extrudersInPrinters" ALTER COLUMN id SET DEFAULT nextval('public."extrudersInPrinters_id_seq"'::regclass);


--
-- TOC entry 3378 (class 2604 OID 26578)
-- Name: makers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.makers ALTER COLUMN id SET DEFAULT nextval('public.makers_id_seq'::regclass);


--
-- TOC entry 3379 (class 2604 OID 26579)
-- Name: materials id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materials ALTER COLUMN id SET DEFAULT nextval('public.materials_id_seq'::regclass);


--
-- TOC entry 3380 (class 2604 OID 26580)
-- Name: materialsInPrinters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."materialsInPrinters" ALTER COLUMN id SET DEFAULT nextval('public."materialsInPrinters_id_seq"'::regclass);


--
-- TOC entry 3381 (class 2604 OID 26581)
-- Name: nozzlesSizes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."nozzlesSizes" ALTER COLUMN id SET DEFAULT nextval('public."nozzlesSizes_id_seq"'::regclass);


--
-- TOC entry 3382 (class 2604 OID 26582)
-- Name: nozzlesTypes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."nozzlesTypes" ALTER COLUMN id SET DEFAULT nextval('public."nozzlesTypes_id_seq"'::regclass);


--
-- TOC entry 3383 (class 2604 OID 26583)
-- Name: operGroups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."operGroups" ALTER COLUMN id SET DEFAULT nextval('public."operGroups_id_seq"'::regclass);


--
-- TOC entry 3384 (class 2604 OID 26584)
-- Name: packing id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.packing ALTER COLUMN id SET DEFAULT nextval('public.packing_id_seq'::regclass);


--
-- TOC entry 3385 (class 2604 OID 26585)
-- Name: partners id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partners ALTER COLUMN id SET DEFAULT nextval('public.partners_id_seq'::regclass);


--
-- TOC entry 3386 (class 2604 OID 26586)
-- Name: polymerBases id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."polymerBases" ALTER COLUMN id SET DEFAULT nextval('public."polymerBases_id_seq"'::regclass);


--
-- TOC entry 3387 (class 2604 OID 26587)
-- Name: printStatusHistory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."printStatusHistory" ALTER COLUMN id SET DEFAULT nextval('public."printStatusHistory_id_seq"'::regclass);


--
-- TOC entry 3388 (class 2604 OID 26588)
-- Name: printerStatus id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."printerStatus" ALTER COLUMN id SET DEFAULT nextval('public."printerStatus_id_seq"'::regclass);


--
-- TOC entry 3389 (class 2604 OID 26589)
-- Name: printers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.printers ALTER COLUMN id SET DEFAULT nextval('public.printers_id_seq'::regclass);


--
-- TOC entry 3390 (class 2604 OID 26590)
-- Name: priorities id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.priorities ALTER COLUMN id SET DEFAULT nextval('public.priorities_id_seq'::regclass);


--
-- TOC entry 3391 (class 2604 OID 26591)
-- Name: projectStatusHistory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."projectStatusHistory" ALTER COLUMN id SET DEFAULT nextval('public."projectStatusHistory_id_seq"'::regclass);


--
-- TOC entry 3392 (class 2604 OID 26592)
-- Name: projectStatuses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."projectStatuses" ALTER COLUMN id SET DEFAULT nextval('public."projectStatuses_id_seq"'::regclass);


--
-- TOC entry 3393 (class 2604 OID 26593)
-- Name: projects id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.projects ALTER COLUMN id SET DEFAULT nextval('public.projects_id_seq'::regclass);


--
-- TOC entry 3394 (class 2604 OID 26594)
-- Name: reactions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reactions ALTER COLUMN id SET DEFAULT nextval('public.reactions_id_seq'::regclass);


--
-- TOC entry 3395 (class 2604 OID 26595)
-- Name: sensorData id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorData" ALTER COLUMN id SET DEFAULT nextval('public."sensorData_id_seq"'::regclass);


--
-- TOC entry 3396 (class 2604 OID 26596)
-- Name: sensorGroups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorGroups" ALTER COLUMN id SET DEFAULT nextval('public."sensorGroups_id_seq"'::regclass);


--
-- TOC entry 3397 (class 2604 OID 26597)
-- Name: sensors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensors ALTER COLUMN id SET DEFAULT nextval('public.sensors_id_seq'::regclass);


--
-- TOC entry 3398 (class 2604 OID 26598)
-- Name: sensorsInPrinters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorsInPrinters" ALTER COLUMN id SET DEFAULT nextval('public."sensorsInPrinters_id_seq"'::regclass);


--
-- TOC entry 3399 (class 2604 OID 26599)
-- Name: serviceOperationHistory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."serviceOperationHistory" ALTER COLUMN id SET DEFAULT nextval('public."serviceOperationHistory_id_seq"'::regclass);


--
-- TOC entry 3400 (class 2604 OID 26600)
-- Name: serviceOperations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."serviceOperations" ALTER COLUMN id SET DEFAULT nextval('public."serviceOperations_id_seq"'::regclass);


--
-- TOC entry 3401 (class 2604 OID 26601)
-- Name: servicePositions  id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."servicePositions " ALTER COLUMN id SET DEFAULT nextval('public."servicePositions _id_seq"'::regclass);


--
-- TOC entry 3402 (class 2604 OID 26602)
-- Name: stands id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stands ALTER COLUMN id SET DEFAULT nextval('public.stands_id_seq'::regclass);


--
-- TOC entry 3403 (class 2604 OID 26603)
-- Name: tablesTypes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."tablesTypes" ALTER COLUMN id SET DEFAULT nextval('public."tablesTypes_id_seq"'::regclass);


--
-- TOC entry 3404 (class 2604 OID 26604)
-- Name: taskFiles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskFiles" ALTER COLUMN id SET DEFAULT nextval('public."taskFiles_id_seq"'::regclass);


--
-- TOC entry 3405 (class 2604 OID 26605)
-- Name: taskPrinting id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskPrinting" ALTER COLUMN id SET DEFAULT nextval('public."taskPrinting_id_seq"'::regclass);


--
-- TOC entry 3406 (class 2604 OID 26606)
-- Name: taskStatusHistory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskStatusHistory" ALTER COLUMN id SET DEFAULT nextval('public."taskStatusHistory_id_seq"'::regclass);


--
-- TOC entry 3407 (class 2604 OID 26607)
-- Name: taskStatuses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskStatuses" ALTER COLUMN id SET DEFAULT nextval('public."taskStatuses_id_seq"'::regclass);


--
-- TOC entry 3408 (class 2604 OID 26608)
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);


--
-- TOC entry 3409 (class 2604 OID 26609)
-- Name: triggersHystory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."triggersHystory" ALTER COLUMN id SET DEFAULT nextval('public."triggersHystory_id_seq"'::regclass);


--
-- TOC entry 3410 (class 2604 OID 26610)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3411 (class 2604 OID 26611)
-- Name: vacuumSystem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."vacuumSystem" ALTER COLUMN id SET DEFAULT nextval('public."vacuumSystem_id_seq"'::regclass);


--
-- TOC entry 3687 (class 0 OID 26387)
-- Dependencies: 209
-- Data for Name: clusters; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3689 (class 0 OID 26391)
-- Dependencies: 211
-- Data for Name: colors; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3691 (class 0 OID 26395)
-- Dependencies: 213
-- Data for Name: currentPrinterStatuses; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3693 (class 0 OID 26399)
-- Dependencies: 215
-- Data for Name: errorTriggers; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3695 (class 0 OID 26403)
-- Dependencies: 217
-- Data for Name: errorTypes; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3697 (class 0 OID 26407)
-- Dependencies: 219
-- Data for Name: extruders; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3698 (class 0 OID 26410)
-- Dependencies: 220
-- Data for Name: extrudersInPrinters; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3701 (class 0 OID 26415)
-- Dependencies: 223
-- Data for Name: makers; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3703 (class 0 OID 26419)
-- Dependencies: 225
-- Data for Name: materials; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3704 (class 0 OID 26424)
-- Dependencies: 226
-- Data for Name: materialsInPrinters; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3707 (class 0 OID 26429)
-- Dependencies: 229
-- Data for Name: nozzlesSizes; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3709 (class 0 OID 26433)
-- Dependencies: 231
-- Data for Name: nozzlesTypes; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3711 (class 0 OID 26437)
-- Dependencies: 233
-- Data for Name: operGroups; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3713 (class 0 OID 26441)
-- Dependencies: 235
-- Data for Name: packing; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3715 (class 0 OID 26445)
-- Dependencies: 237
-- Data for Name: partners; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3717 (class 0 OID 26451)
-- Dependencies: 239
-- Data for Name: polymerBases; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3719 (class 0 OID 26455)
-- Dependencies: 241
-- Data for Name: printStatusHistory; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3721 (class 0 OID 26459)
-- Dependencies: 243
-- Data for Name: printerStatus; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3723 (class 0 OID 26465)
-- Dependencies: 245
-- Data for Name: printers; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3725 (class 0 OID 26471)
-- Dependencies: 247
-- Data for Name: priorities; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3727 (class 0 OID 26475)
-- Dependencies: 249
-- Data for Name: projectStatusHistory; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3729 (class 0 OID 26479)
-- Dependencies: 251
-- Data for Name: projectStatuses; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3731 (class 0 OID 26483)
-- Dependencies: 253
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3733 (class 0 OID 26489)
-- Dependencies: 255
-- Data for Name: reactions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3769 (class 0 OID 28687)
-- Dependencies: 291
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.roles (id, name) VALUES (1, 'Техническая поддержка');
INSERT INTO public.roles (id, name) VALUES (2, 'SUDO');
INSERT INTO public.roles (id, name) VALUES (3, 'Локальный администратор');
INSERT INTO public.roles (id, name) VALUES (4, 'Менеджер');
INSERT INTO public.roles (id, name) VALUES (5, 'Начальник производства');
INSERT INTO public.roles (id, name) VALUES (6, 'Оператор 3D-принтера');
INSERT INTO public.roles (id, name) VALUES (7, 'Техник');


--
-- TOC entry 3735 (class 0 OID 26493)
-- Dependencies: 257
-- Data for Name: sensorData; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3737 (class 0 OID 26499)
-- Dependencies: 259
-- Data for Name: sensorGroups; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3739 (class 0 OID 26503)
-- Dependencies: 261
-- Data for Name: sensors; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3740 (class 0 OID 26508)
-- Dependencies: 262
-- Data for Name: sensorsInPrinters; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3743 (class 0 OID 26513)
-- Dependencies: 265
-- Data for Name: serviceOperationHistory; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3745 (class 0 OID 26517)
-- Dependencies: 267
-- Data for Name: serviceOperations; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3747 (class 0 OID 26523)
-- Dependencies: 269
-- Data for Name: servicePositions ; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3749 (class 0 OID 26527)
-- Dependencies: 271
-- Data for Name: stands; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3751 (class 0 OID 26531)
-- Dependencies: 273
-- Data for Name: tablesTypes; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3753 (class 0 OID 26537)
-- Dependencies: 275
-- Data for Name: taskFiles; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3755 (class 0 OID 26541)
-- Dependencies: 277
-- Data for Name: taskPrinting; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3757 (class 0 OID 26545)
-- Dependencies: 279
-- Data for Name: taskStatusHistory; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3759 (class 0 OID 26549)
-- Dependencies: 281
-- Data for Name: taskStatuses; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3761 (class 0 OID 26555)
-- Dependencies: 283
-- Data for Name: tasks; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3763 (class 0 OID 26559)
-- Dependencies: 285
-- Data for Name: triggersHystory; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3765 (class 0 OID 26563)
-- Dependencies: 287
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (5, 'done', '76a2173be6393254e72ffa4d6df1030a', 'sergey111', false, 'sergey', 'eng', 5);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (6, 'frfrg', 'b45cffe084dd3d20d928bee85e7b0f21', 'aaaaaa', false, 'frfrfra', 'string', 1);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (7, 'fgrg', '89c400d8fe088ae5bf1b57e46e5465dd', 'bgtnyhmn', false, 'vdfbgdfbg', 'fvswgfasw', 4);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (9, 'gerag', '905a2e28c12530d5641aa52d3c6561b5', 'veshst', false, 'vehrtjh', 'vfrwegerg', 6);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (10, 'gerag', '905a2e28c12530d5641aa52d3c6561b5', 'veshst', false, 'vehrtjh', 'vfrwegerg', 6);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (11, 'gerag', '905a2e28c12530d5641aa52d3c6561b5', 'veshst', false, 'vehrtjh', 'vfrwegerg', 6);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (12, 'gerag', '905a2e28c12530d5641aa52d3c6561b5', 'veshst', false, 'vehrtjh', 'vfrwegerg', 6);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (13, 'string', 'b45cffe084dd3d20d928bee85e7b0f21', 'string', false, 'string', 'string', 0);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (14, 'string', 'b45cffe084dd3d20d928bee85e7b0f21', 'string', false, 'string', 'string', 6);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (15, 'string', 'b45cffe084dd3d20d928bee85e7b0f21', 'string', false, 'string', 'string', 6);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (16, 'string', 'string', 'string', false, 'string', 'string', 0);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (17, 'string', 'string', 'string', false, 'string', 'string', 0);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (19, 'saga', '0068fc517522df2e490237fa86ec1006', 'lohin', false, 'cdeaswfsdg', 'fwreaf', 4);
INSERT INTO public.users (id, name, "passwordHash", login, "markingDeletion", firstname, "position", "idRole") VALUES (18, 'Dima', '4085c6bd955d1445b1bd70ece5baf454', 'Dima', false, 'Dima', 'Dima', 5);


--
-- TOC entry 3767 (class 0 OID 26567)
-- Dependencies: 289
-- Data for Name: vacuumSystem; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3856 (class 0 OID 0)
-- Dependencies: 210
-- Name: clusters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clusters_id_seq', 1, false);


--
-- TOC entry 3857 (class 0 OID 0)
-- Dependencies: 212
-- Name: colors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.colors_id_seq', 1, false);


--
-- TOC entry 3858 (class 0 OID 0)
-- Dependencies: 214
-- Name: currentPrinterStatuses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."currentPrinterStatuses_id_seq"', 1, false);


--
-- TOC entry 3859 (class 0 OID 0)
-- Dependencies: 216
-- Name: errorTriggers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."errorTriggers_id_seq"', 1, false);


--
-- TOC entry 3860 (class 0 OID 0)
-- Dependencies: 218
-- Name: errorTypes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."errorTypes_id_seq"', 1, false);


--
-- TOC entry 3861 (class 0 OID 0)
-- Dependencies: 221
-- Name: extrudersInPrinters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."extrudersInPrinters_id_seq"', 1, false);


--
-- TOC entry 3862 (class 0 OID 0)
-- Dependencies: 222
-- Name: extruders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.extruders_id_seq', 1, false);


--
-- TOC entry 3863 (class 0 OID 0)
-- Dependencies: 224
-- Name: makers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.makers_id_seq', 1, false);


--
-- TOC entry 3864 (class 0 OID 0)
-- Dependencies: 227
-- Name: materialsInPrinters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."materialsInPrinters_id_seq"', 1, false);


--
-- TOC entry 3865 (class 0 OID 0)
-- Dependencies: 228
-- Name: materials_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.materials_id_seq', 1, false);


--
-- TOC entry 3866 (class 0 OID 0)
-- Dependencies: 230
-- Name: nozzlesSizes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."nozzlesSizes_id_seq"', 1, false);


--
-- TOC entry 3867 (class 0 OID 0)
-- Dependencies: 232
-- Name: nozzlesTypes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."nozzlesTypes_id_seq"', 1, false);


--
-- TOC entry 3868 (class 0 OID 0)
-- Dependencies: 234
-- Name: operGroups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."operGroups_id_seq"', 1, false);


--
-- TOC entry 3869 (class 0 OID 0)
-- Dependencies: 236
-- Name: packing_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.packing_id_seq', 1, false);


--
-- TOC entry 3870 (class 0 OID 0)
-- Dependencies: 238
-- Name: partners_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.partners_id_seq', 1, false);


--
-- TOC entry 3871 (class 0 OID 0)
-- Dependencies: 240
-- Name: polymerBases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."polymerBases_id_seq"', 1, false);


--
-- TOC entry 3872 (class 0 OID 0)
-- Dependencies: 242
-- Name: printStatusHistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."printStatusHistory_id_seq"', 1, false);


--
-- TOC entry 3873 (class 0 OID 0)
-- Dependencies: 244
-- Name: printerStatus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."printerStatus_id_seq"', 1, false);


--
-- TOC entry 3874 (class 0 OID 0)
-- Dependencies: 246
-- Name: printers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.printers_id_seq', 1, false);


--
-- TOC entry 3875 (class 0 OID 0)
-- Dependencies: 248
-- Name: priorities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.priorities_id_seq', 1, false);


--
-- TOC entry 3876 (class 0 OID 0)
-- Dependencies: 250
-- Name: projectStatusHistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."projectStatusHistory_id_seq"', 1, false);


--
-- TOC entry 3877 (class 0 OID 0)
-- Dependencies: 252
-- Name: projectStatuses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."projectStatuses_id_seq"', 1, false);


--
-- TOC entry 3878 (class 0 OID 0)
-- Dependencies: 254
-- Name: projects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.projects_id_seq', 1, false);


--
-- TOC entry 3879 (class 0 OID 0)
-- Dependencies: 256
-- Name: reactions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reactions_id_seq', 1, false);


--
-- TOC entry 3880 (class 0 OID 0)
-- Dependencies: 258
-- Name: sensorData_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."sensorData_id_seq"', 1, false);


--
-- TOC entry 3881 (class 0 OID 0)
-- Dependencies: 260
-- Name: sensorGroups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."sensorGroups_id_seq"', 1, false);


--
-- TOC entry 3882 (class 0 OID 0)
-- Dependencies: 263
-- Name: sensorsInPrinters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."sensorsInPrinters_id_seq"', 1, false);


--
-- TOC entry 3883 (class 0 OID 0)
-- Dependencies: 264
-- Name: sensors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensors_id_seq', 1, false);


--
-- TOC entry 3884 (class 0 OID 0)
-- Dependencies: 266
-- Name: serviceOperationHistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."serviceOperationHistory_id_seq"', 1, false);


--
-- TOC entry 3885 (class 0 OID 0)
-- Dependencies: 268
-- Name: serviceOperations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."serviceOperations_id_seq"', 1, false);


--
-- TOC entry 3886 (class 0 OID 0)
-- Dependencies: 270
-- Name: servicePositions _id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."servicePositions _id_seq"', 1, false);


--
-- TOC entry 3887 (class 0 OID 0)
-- Dependencies: 272
-- Name: stands_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.stands_id_seq', 1, false);


--
-- TOC entry 3888 (class 0 OID 0)
-- Dependencies: 274
-- Name: tablesTypes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."tablesTypes_id_seq"', 1, false);


--
-- TOC entry 3889 (class 0 OID 0)
-- Dependencies: 276
-- Name: taskFiles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."taskFiles_id_seq"', 1, false);


--
-- TOC entry 3890 (class 0 OID 0)
-- Dependencies: 278
-- Name: taskPrinting_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."taskPrinting_id_seq"', 1, false);


--
-- TOC entry 3891 (class 0 OID 0)
-- Dependencies: 280
-- Name: taskStatusHistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."taskStatusHistory_id_seq"', 1, false);


--
-- TOC entry 3892 (class 0 OID 0)
-- Dependencies: 282
-- Name: taskStatuses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."taskStatuses_id_seq"', 1, false);


--
-- TOC entry 3893 (class 0 OID 0)
-- Dependencies: 284
-- Name: tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tasks_id_seq', 1, false);


--
-- TOC entry 3894 (class 0 OID 0)
-- Dependencies: 286
-- Name: triggersHystory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."triggersHystory_id_seq"', 1, false);


--
-- TOC entry 3895 (class 0 OID 0)
-- Dependencies: 288
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 19, true);


--
-- TOC entry 3896 (class 0 OID 0)
-- Dependencies: 290
-- Name: vacuumSystem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."vacuumSystem_id_seq"', 1, false);


--
-- TOC entry 3413 (class 2606 OID 26613)
-- Name: clusters clusters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clusters
    ADD CONSTRAINT clusters_pkey PRIMARY KEY (id);


--
-- TOC entry 3415 (class 2606 OID 26615)
-- Name: colors colors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.colors
    ADD CONSTRAINT colors_pkey PRIMARY KEY (id);


--
-- TOC entry 3417 (class 2606 OID 26617)
-- Name: currentPrinterStatuses currentPrinterStatuses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."currentPrinterStatuses"
    ADD CONSTRAINT "currentPrinterStatuses_pkey" PRIMARY KEY (id);


--
-- TOC entry 3419 (class 2606 OID 26619)
-- Name: errorTriggers errorTriggers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."errorTriggers"
    ADD CONSTRAINT "errorTriggers_pkey" PRIMARY KEY (id);


--
-- TOC entry 3421 (class 2606 OID 26621)
-- Name: errorTypes errorTypes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."errorTypes"
    ADD CONSTRAINT "errorTypes_pkey" PRIMARY KEY (id);


--
-- TOC entry 3425 (class 2606 OID 26623)
-- Name: extrudersInPrinters extrudersInPrinters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."extrudersInPrinters"
    ADD CONSTRAINT "extrudersInPrinters_pkey" PRIMARY KEY (id);


--
-- TOC entry 3423 (class 2606 OID 26625)
-- Name: extruders extruders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.extruders
    ADD CONSTRAINT extruders_pkey PRIMARY KEY (id);


--
-- TOC entry 3427 (class 2606 OID 26627)
-- Name: makers makers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.makers
    ADD CONSTRAINT makers_pkey PRIMARY KEY (id);


--
-- TOC entry 3431 (class 2606 OID 26629)
-- Name: materialsInPrinters materialsInPrinters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."materialsInPrinters"
    ADD CONSTRAINT "materialsInPrinters_pkey" PRIMARY KEY (id);


--
-- TOC entry 3429 (class 2606 OID 26631)
-- Name: materials materials_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materials
    ADD CONSTRAINT materials_pkey PRIMARY KEY (id);


--
-- TOC entry 3433 (class 2606 OID 26633)
-- Name: nozzlesSizes nozzlesSizes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."nozzlesSizes"
    ADD CONSTRAINT "nozzlesSizes_pkey" PRIMARY KEY (id);


--
-- TOC entry 3435 (class 2606 OID 26635)
-- Name: nozzlesTypes nozzlesTypes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."nozzlesTypes"
    ADD CONSTRAINT "nozzlesTypes_pkey" PRIMARY KEY (id);


--
-- TOC entry 3437 (class 2606 OID 26637)
-- Name: operGroups operGroups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."operGroups"
    ADD CONSTRAINT "operGroups_pkey" PRIMARY KEY (id);


--
-- TOC entry 3439 (class 2606 OID 26639)
-- Name: packing packing_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.packing
    ADD CONSTRAINT packing_pkey PRIMARY KEY (id);


--
-- TOC entry 3441 (class 2606 OID 26641)
-- Name: partners partners_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partners
    ADD CONSTRAINT partners_pkey PRIMARY KEY (id);


--
-- TOC entry 3443 (class 2606 OID 26643)
-- Name: polymerBases polymerBases_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."polymerBases"
    ADD CONSTRAINT "polymerBases_pkey" PRIMARY KEY (id);


--
-- TOC entry 3445 (class 2606 OID 26645)
-- Name: printStatusHistory printStatusHistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."printStatusHistory"
    ADD CONSTRAINT "printStatusHistory_pkey" PRIMARY KEY (id);


--
-- TOC entry 3447 (class 2606 OID 26647)
-- Name: printerStatus printerStatus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."printerStatus"
    ADD CONSTRAINT "printerStatus_pkey" PRIMARY KEY (id);


--
-- TOC entry 3449 (class 2606 OID 26649)
-- Name: printers printers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.printers
    ADD CONSTRAINT printers_pkey PRIMARY KEY (id);


--
-- TOC entry 3451 (class 2606 OID 26651)
-- Name: priorities priorities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.priorities
    ADD CONSTRAINT priorities_pkey PRIMARY KEY (id);


--
-- TOC entry 3453 (class 2606 OID 26653)
-- Name: projectStatusHistory projectStatusHistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."projectStatusHistory"
    ADD CONSTRAINT "projectStatusHistory_pkey" PRIMARY KEY (id);


--
-- TOC entry 3455 (class 2606 OID 26655)
-- Name: projectStatuses projectStatuses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."projectStatuses"
    ADD CONSTRAINT "projectStatuses_pkey" PRIMARY KEY (id);


--
-- TOC entry 3457 (class 2606 OID 26657)
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);


--
-- TOC entry 3459 (class 2606 OID 26659)
-- Name: reactions reactions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reactions
    ADD CONSTRAINT reactions_pkey PRIMARY KEY (id);


--
-- TOC entry 3495 (class 2606 OID 28691)
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- TOC entry 3461 (class 2606 OID 26661)
-- Name: sensorData sensorData_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorData"
    ADD CONSTRAINT "sensorData_pkey" PRIMARY KEY (id);


--
-- TOC entry 3463 (class 2606 OID 26663)
-- Name: sensorGroups sensorGroups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorGroups"
    ADD CONSTRAINT "sensorGroups_pkey" PRIMARY KEY (id);


--
-- TOC entry 3467 (class 2606 OID 26665)
-- Name: sensorsInPrinters sensorsInPrinters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorsInPrinters"
    ADD CONSTRAINT "sensorsInPrinters_pkey" PRIMARY KEY (id);


--
-- TOC entry 3465 (class 2606 OID 26667)
-- Name: sensors sensors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensors
    ADD CONSTRAINT sensors_pkey PRIMARY KEY (id);


--
-- TOC entry 3469 (class 2606 OID 26669)
-- Name: serviceOperationHistory serviceOperationHistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."serviceOperationHistory"
    ADD CONSTRAINT "serviceOperationHistory_pkey" PRIMARY KEY (id);


--
-- TOC entry 3471 (class 2606 OID 26671)
-- Name: serviceOperations serviceOperations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."serviceOperations"
    ADD CONSTRAINT "serviceOperations_pkey" PRIMARY KEY (id);


--
-- TOC entry 3473 (class 2606 OID 26673)
-- Name: servicePositions  servicePositions _pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."servicePositions "
    ADD CONSTRAINT "servicePositions _pkey" PRIMARY KEY (id);


--
-- TOC entry 3475 (class 2606 OID 26675)
-- Name: stands stands_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stands
    ADD CONSTRAINT stands_pkey PRIMARY KEY (id);


--
-- TOC entry 3477 (class 2606 OID 26677)
-- Name: tablesTypes tablesTypes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."tablesTypes"
    ADD CONSTRAINT "tablesTypes_pkey" PRIMARY KEY (id);


--
-- TOC entry 3479 (class 2606 OID 26679)
-- Name: taskFiles taskFiles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskFiles"
    ADD CONSTRAINT "taskFiles_pkey" PRIMARY KEY (id);


--
-- TOC entry 3481 (class 2606 OID 26681)
-- Name: taskPrinting taskPrinting_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskPrinting"
    ADD CONSTRAINT "taskPrinting_pkey" PRIMARY KEY (id);


--
-- TOC entry 3483 (class 2606 OID 26683)
-- Name: taskStatusHistory taskStatusHistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskStatusHistory"
    ADD CONSTRAINT "taskStatusHistory_pkey" PRIMARY KEY (id);


--
-- TOC entry 3485 (class 2606 OID 26685)
-- Name: taskStatuses taskStatuses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskStatuses"
    ADD CONSTRAINT "taskStatuses_pkey" PRIMARY KEY (id);


--
-- TOC entry 3487 (class 2606 OID 26687)
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);


--
-- TOC entry 3489 (class 2606 OID 26689)
-- Name: triggersHystory triggersHystory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."triggersHystory"
    ADD CONSTRAINT "triggersHystory_pkey" PRIMARY KEY (id);


--
-- TOC entry 3491 (class 2606 OID 26691)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3493 (class 2606 OID 26693)
-- Name: vacuumSystem vacuumSystem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."vacuumSystem"
    ADD CONSTRAINT "vacuumSystem_pkey" PRIMARY KEY (id);


--
-- TOC entry 3544 (class 2606 OID 26694)
-- Name: triggersHystory connectToReactions; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."triggersHystory"
    ADD CONSTRAINT "connectToReactions" FOREIGN KEY ("idReaction") REFERENCES public.reactions(id) NOT VALID;


--
-- TOC entry 3527 (class 2606 OID 26699)
-- Name: sensors connectToSensorGroup; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensors
    ADD CONSTRAINT "connectToSensorGroup" FOREIGN KEY ("idSensorGroup") REFERENCES public."sensorGroups"(id) NOT VALID;


--
-- TOC entry 3528 (class 2606 OID 26704)
-- Name: sensorsInPrinters connectToSensors; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorsInPrinters"
    ADD CONSTRAINT "connectToSensors" FOREIGN KEY ("idSensor") REFERENCES public.sensors(id);


--
-- TOC entry 3496 (class 2606 OID 26709)
-- Name: currentPrinterStatuses currentPrinterStatuses_idPrinterStatus_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."currentPrinterStatuses"
    ADD CONSTRAINT "currentPrinterStatuses_idPrinterStatus_fkey" FOREIGN KEY ("idPrinterStatus") REFERENCES public."printerStatus"(id) NOT VALID;


--
-- TOC entry 3497 (class 2606 OID 26714)
-- Name: currentPrinterStatuses currentPrinterStatuses_printerId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."currentPrinterStatuses"
    ADD CONSTRAINT "currentPrinterStatuses_printerId_fkey" FOREIGN KEY ("printerId") REFERENCES public.printers(id);


--
-- TOC entry 3498 (class 2606 OID 26719)
-- Name: errorTriggers errorTriggers_idErrorType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."errorTriggers"
    ADD CONSTRAINT "errorTriggers_idErrorType_fkey" FOREIGN KEY ("idErrorType") REFERENCES public."errorTypes"(id) NOT VALID;


--
-- TOC entry 3499 (class 2606 OID 26724)
-- Name: errorTriggers errorTriggers_idPrinterStatus_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."errorTriggers"
    ADD CONSTRAINT "errorTriggers_idPrinterStatus_fkey" FOREIGN KEY ("idPrinterStatus") REFERENCES public."printerStatus"(id) NOT VALID;


--
-- TOC entry 3500 (class 2606 OID 26729)
-- Name: errorTriggers errorTriggers_idSensor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."errorTriggers"
    ADD CONSTRAINT "errorTriggers_idSensor_fkey" FOREIGN KEY ("idSensor") REFERENCES public.sensors(id) NOT VALID;


--
-- TOC entry 3501 (class 2606 OID 26734)
-- Name: errorTriggers errorTriggers_idServiceOperation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."errorTriggers"
    ADD CONSTRAINT "errorTriggers_idServiceOperation_fkey" FOREIGN KEY ("idServiceOperation") REFERENCES public."serviceOperations"(id) NOT VALID;


--
-- TOC entry 3502 (class 2606 OID 26739)
-- Name: extrudersInPrinters extrudersInPrinters_idExtruder_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."extrudersInPrinters"
    ADD CONSTRAINT "extrudersInPrinters_idExtruder_fkey" FOREIGN KEY ("idExtruder") REFERENCES public.extruders(id) NOT VALID;


--
-- TOC entry 3503 (class 2606 OID 26744)
-- Name: extrudersInPrinters extrudersInPrinters_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."extrudersInPrinters"
    ADD CONSTRAINT "extrudersInPrinters_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id);


--
-- TOC entry 3506 (class 2606 OID 26749)
-- Name: materialsInPrinters materialsInPrinters_idColor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."materialsInPrinters"
    ADD CONSTRAINT "materialsInPrinters_idColor_fkey" FOREIGN KEY ("idColor") REFERENCES public.colors(id) NOT VALID;


--
-- TOC entry 3507 (class 2606 OID 26754)
-- Name: materialsInPrinters materialsInPrinters_idMaterial_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."materialsInPrinters"
    ADD CONSTRAINT "materialsInPrinters_idMaterial_fkey" FOREIGN KEY ("idMaterial") REFERENCES public.materials(id) NOT VALID;


--
-- TOC entry 3508 (class 2606 OID 26759)
-- Name: materialsInPrinters materialsInPrinters_idPackage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."materialsInPrinters"
    ADD CONSTRAINT "materialsInPrinters_idPackage_fkey" FOREIGN KEY ("idPackage") REFERENCES public.packing(id) NOT VALID;


--
-- TOC entry 3509 (class 2606 OID 26764)
-- Name: materialsInPrinters materialsInPrinters_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."materialsInPrinters"
    ADD CONSTRAINT "materialsInPrinters_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id);


--
-- TOC entry 3504 (class 2606 OID 26769)
-- Name: materials materials_idMaker_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materials
    ADD CONSTRAINT "materials_idMaker_fkey" FOREIGN KEY ("idMaker") REFERENCES public.makers(id) NOT VALID;


--
-- TOC entry 3505 (class 2606 OID 26774)
-- Name: materials materials_idPolymerBase_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materials
    ADD CONSTRAINT "materials_idPolymerBase_fkey" FOREIGN KEY ("idPolymerBase") REFERENCES public."polymerBases"(id) NOT VALID;


--
-- TOC entry 3510 (class 2606 OID 26779)
-- Name: operGroups operGroups_idCluster_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."operGroups"
    ADD CONSTRAINT "operGroups_idCluster_fkey" FOREIGN KEY ("idCluster") REFERENCES public.clusters(id) NOT VALID;


--
-- TOC entry 3511 (class 2606 OID 26784)
-- Name: operGroups operGroups_idNozzleSize_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."operGroups"
    ADD CONSTRAINT "operGroups_idNozzleSize_fkey" FOREIGN KEY ("idNozzleSize") REFERENCES public."nozzlesSizes"(id);


--
-- TOC entry 3512 (class 2606 OID 26789)
-- Name: operGroups operGroups_idNozzleType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."operGroups"
    ADD CONSTRAINT "operGroups_idNozzleType_fkey" FOREIGN KEY ("idNozzleType") REFERENCES public."nozzlesTypes"(id);


--
-- TOC entry 3513 (class 2606 OID 26794)
-- Name: printStatusHistory printStatusHistory_idPrinterStatus_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."printStatusHistory"
    ADD CONSTRAINT "printStatusHistory_idPrinterStatus_fkey" FOREIGN KEY ("idPrinterStatus") REFERENCES public."printerStatus"(id) NOT VALID;


--
-- TOC entry 3514 (class 2606 OID 26799)
-- Name: printStatusHistory printStatusHistory_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."printStatusHistory"
    ADD CONSTRAINT "printStatusHistory_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id) NOT VALID;


--
-- TOC entry 3515 (class 2606 OID 26804)
-- Name: printers printers_idOperGroups_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.printers
    ADD CONSTRAINT "printers_idOperGroups_fkey" FOREIGN KEY ("idOperGroups") REFERENCES public."operGroups"(id) NOT VALID;


--
-- TOC entry 3516 (class 2606 OID 26809)
-- Name: printers printers_idStand_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.printers
    ADD CONSTRAINT "printers_idStand_fkey" FOREIGN KEY ("idStand") REFERENCES public.stands(id) NOT VALID;


--
-- TOC entry 3517 (class 2606 OID 26814)
-- Name: printers printers_idTableType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.printers
    ADD CONSTRAINT "printers_idTableType_fkey" FOREIGN KEY ("idTableType") REFERENCES public."tablesTypes"(id) NOT VALID;


--
-- TOC entry 3518 (class 2606 OID 26819)
-- Name: printers printers_idVacuumSystem_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.printers
    ADD CONSTRAINT "printers_idVacuumSystem_fkey" FOREIGN KEY ("idVacuumSystem") REFERENCES public."vacuumSystem"(id) NOT VALID;


--
-- TOC entry 3519 (class 2606 OID 26824)
-- Name: projectStatusHistory projectStatusHistory_idProjectStatus_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."projectStatusHistory"
    ADD CONSTRAINT "projectStatusHistory_idProjectStatus_fkey" FOREIGN KEY ("idProjectStatus") REFERENCES public."projectStatuses"(id) NOT VALID;


--
-- TOC entry 3520 (class 2606 OID 26829)
-- Name: projectStatusHistory projectStatusHistory_idProject_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."projectStatusHistory"
    ADD CONSTRAINT "projectStatusHistory_idProject_fkey" FOREIGN KEY ("idProject") REFERENCES public.projects(id) NOT VALID;


--
-- TOC entry 3521 (class 2606 OID 26834)
-- Name: projects projects_idAuthor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT "projects_idAuthor_fkey" FOREIGN KEY ("idAuthor") REFERENCES public.users(id) NOT VALID;


--
-- TOC entry 3522 (class 2606 OID 26839)
-- Name: projects projects_idPartner_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT "projects_idPartner_fkey" FOREIGN KEY ("idPartner") REFERENCES public.partners(id) NOT VALID;


--
-- TOC entry 3523 (class 2606 OID 26844)
-- Name: projects projects_idPriority_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT "projects_idPriority_fkey" FOREIGN KEY ("idPriority") REFERENCES public.priorities(id);


--
-- TOC entry 3524 (class 2606 OID 26849)
-- Name: projects projects_idResponsible_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT "projects_idResponsible_fkey" FOREIGN KEY ("idResponsible") REFERENCES public.users(id) NOT VALID;


--
-- TOC entry 3525 (class 2606 OID 26854)
-- Name: sensorData sensorData_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorData"
    ADD CONSTRAINT "sensorData_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id) NOT VALID;


--
-- TOC entry 3526 (class 2606 OID 26859)
-- Name: sensorData sensorData_idSensor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorData"
    ADD CONSTRAINT "sensorData_idSensor_fkey" FOREIGN KEY ("idSensor") REFERENCES public.sensors(id) NOT VALID;


--
-- TOC entry 3529 (class 2606 OID 26864)
-- Name: sensorsInPrinters sensorsInPrinters_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sensorsInPrinters"
    ADD CONSTRAINT "sensorsInPrinters_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id) NOT VALID;


--
-- TOC entry 3530 (class 2606 OID 26869)
-- Name: serviceOperationHistory serviceOperationHistory_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."serviceOperationHistory"
    ADD CONSTRAINT "serviceOperationHistory_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id);


--
-- TOC entry 3531 (class 2606 OID 26874)
-- Name: serviceOperationHistory serviceOperationHistory_idServiceOperation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."serviceOperationHistory"
    ADD CONSTRAINT "serviceOperationHistory_idServiceOperation_fkey" FOREIGN KEY ("idServiceOperation") REFERENCES public."serviceOperations"(id);


--
-- TOC entry 3532 (class 2606 OID 26879)
-- Name: serviceOperationHistory serviceOperationHistory_idUser_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."serviceOperationHistory"
    ADD CONSTRAINT "serviceOperationHistory_idUser_fkey" FOREIGN KEY ("idUser") REFERENCES public.users(id) NOT VALID;


--
-- TOC entry 3533 (class 2606 OID 26884)
-- Name: stands stands_idCluster_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stands
    ADD CONSTRAINT "stands_idCluster_fkey" FOREIGN KEY ("idCluster") REFERENCES public.clusters(id) NOT VALID;


--
-- TOC entry 3534 (class 2606 OID 26889)
-- Name: taskFiles taskFiles_idOwner_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskFiles"
    ADD CONSTRAINT "taskFiles_idOwner_fkey" FOREIGN KEY ("idOwner") REFERENCES public.users(id);


--
-- TOC entry 3535 (class 2606 OID 26894)
-- Name: taskFiles taskFiles_idTask_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskFiles"
    ADD CONSTRAINT "taskFiles_idTask_fkey" FOREIGN KEY ("idTask") REFERENCES public.tasks(id);


--
-- TOC entry 3536 (class 2606 OID 26899)
-- Name: taskPrinting taskPrinting_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskPrinting"
    ADD CONSTRAINT "taskPrinting_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id) NOT VALID;


--
-- TOC entry 3537 (class 2606 OID 26904)
-- Name: taskPrinting taskPrinting_idTask_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskPrinting"
    ADD CONSTRAINT "taskPrinting_idTask_fkey" FOREIGN KEY ("idTask") REFERENCES public.tasks(id) NOT VALID;


--
-- TOC entry 3538 (class 2606 OID 26909)
-- Name: taskStatusHistory taskStatusHistory_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskStatusHistory"
    ADD CONSTRAINT "taskStatusHistory_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id) NOT VALID;


--
-- TOC entry 3539 (class 2606 OID 26914)
-- Name: taskStatusHistory taskStatusHistory_idTaskStatus_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskStatusHistory"
    ADD CONSTRAINT "taskStatusHistory_idTaskStatus_fkey" FOREIGN KEY ("idTaskStatus") REFERENCES public."taskStatuses"(id);


--
-- TOC entry 3540 (class 2606 OID 26919)
-- Name: taskStatusHistory taskStatusHistory_idTask_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."taskStatusHistory"
    ADD CONSTRAINT "taskStatusHistory_idTask_fkey" FOREIGN KEY ("idTask") REFERENCES public.tasks(id) NOT VALID;


--
-- TOC entry 3541 (class 2606 OID 26924)
-- Name: tasks tasks_idOperGroup_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT "tasks_idOperGroup_fkey" FOREIGN KEY ("idOperGroup") REFERENCES public."operGroups"(id);


--
-- TOC entry 3542 (class 2606 OID 26929)
-- Name: tasks tasks_idPriority_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT "tasks_idPriority_fkey" FOREIGN KEY ("idPriority") REFERENCES public.priorities(id);


--
-- TOC entry 3543 (class 2606 OID 26934)
-- Name: tasks tasks_idProject_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT "tasks_idProject_fkey" FOREIGN KEY ("idProject") REFERENCES public.projects(id);


--
-- TOC entry 3545 (class 2606 OID 26939)
-- Name: triggersHystory triggersHystory_idPrinter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."triggersHystory"
    ADD CONSTRAINT "triggersHystory_idPrinter_fkey" FOREIGN KEY ("idPrinter") REFERENCES public.printers(id) NOT VALID;


--
-- TOC entry 3546 (class 2606 OID 26944)
-- Name: triggersHystory triggersHystory_idTrigger_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."triggersHystory"
    ADD CONSTRAINT "triggersHystory_idTrigger_fkey" FOREIGN KEY ("idTrigger") REFERENCES public."errorTriggers"(id) NOT VALID;


--
-- TOC entry 3547 (class 2606 OID 26949)
-- Name: triggersHystory triggersHystory_idUser_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."triggersHystory"
    ADD CONSTRAINT "triggersHystory_idUser_fkey" FOREIGN KEY ("idUser") REFERENCES public.users(id) NOT VALID;


--
-- TOC entry 3775 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

REVOKE ALL ON SCHEMA public FROM postgres;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO pg_database_owner;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2023-02-09 11:43:24

--
-- PostgreSQL database dump complete
--

