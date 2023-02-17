-- 1.
CREATE TABLE IF NOT EXISTS public."modulePlaces"
(
    id serial NOT NULL,
    name character varying NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public."modulePlaces"
    OWNER to postgres;

COMMENT ON TABLE public."modulePlaces"
    IS 'https://yt.omegafuture.ru/articles/RedFabMES-A-163/%5B%D0%A1%5D-%D0%9C%D0%B5%D1%81%D1%82%D0%B0-%D0%B2-%D1%81%D1%82%D0%BE%D0%B9%D0%BA%D0%B5---modulePlaces?edit=true';


-- 2.
ALTER TABLE IF EXISTS public.printers
    RENAME "modulePlace" TO "idModulePlace";

ALTER TABLE IF EXISTS public.printers
    ADD CONSTRAINT "printers_idModulePlace_fkey" FOREIGN KEY ("idModulePlace")
    REFERENCES public."modulePlaces" (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
CREATE INDEX IF NOT EXISTS "fki_printers_idModulePlace_fkey"
    ON public.printers("idModulePlace");


-- 3.
ALTER TABLE IF EXISTS public."currentPrinterStatuses" DROP COLUMN IF EXISTS "printerId";

ALTER TABLE IF EXISTS public."currentPrinterStatuses" DROP COLUMN IF EXISTS update;

ALTER TABLE IF EXISTS public."currentPrinterStatuses"
    ADD COLUMN "idPrinter" integer NOT NULL;
ALTER TABLE IF EXISTS public."currentPrinterStatuses" DROP CONSTRAINT IF EXISTS "currentPrinterStatuses_idPrinter_fkey";

ALTER TABLE IF EXISTS public."currentPrinterStatuses"
    ADD CONSTRAINT "currentPrinterStatuses_idPrinter_fkey" FOREIGN KEY ("idPrinter")
    REFERENCES public.printers (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


-- 4.
ALTER TABLE IF EXISTS public."nozzlesSizes" DROP COLUMN IF EXISTS "markingDeletion";
ALTER TABLE IF EXISTS public."nozzlesTypes" DROP COLUMN IF EXISTS "markingDeletion";


-- 5.
DROP TABLE IF EXISTS public.extruders CASCADE;
DROP TABLE IF EXISTS public."extrudersInPrinters";


-- 6.
ALTER TABLE IF EXISTS public.sensors DROP COLUMN IF EXISTS "markingDeletion";

ALTER TABLE IF EXISTS public.sensors
    RENAME "CanDeactivate" TO "canDeactivate";


-- 7.
ALTER TABLE IF EXISTS public.materials
    ALTER COLUMN composite SET NOT NULL;

ALTER TABLE IF EXISTS public.materials
    ALTER COLUMN "markingDeletion" SET NOT NULL;

ALTER TABLE IF EXISTS public.materials
    ADD COLUMN "materialUnloadLength" smallint NOT NULL;


-- 8.
ALTER TABLE IF EXISTS public.colors
    RENAME "colorMaterialRGB" TO "colorMaterialHEX";


-- 9.
ALTER TABLE IF EXISTS public.colors
    RENAME "colorPointRGB" TO "colorPointHEX";

-- 10.
ALTER TABLE IF EXISTS public.packing DROP COLUMN IF EXISTS "markingDeletion";


-- 11.
ALTER TABLE IF EXISTS public."polymerBases" DROP COLUMN IF EXISTS "markingDeletion";


-- 12.
ALTER TABLE IF EXISTS public."materialsInPrinters"
    ADD COLUMN period timestamp with time zone NOT NULL;


-- 13.
CREATE TABLE IF NOT EXISTS public."useMaterial"
(
    id serial NOT NULL,
    "idPrinter" integer NOT NULL,
    "idMaterial" integer NOT NULL,
    cell smallint NOT NULL,
    "idColor" integer NOT NULL,
    period timestamp with time zone NOT NULL,
    "isFilling" boolean NOT NULL,
    weight numeric(8,3) NOT NULL,
    CONSTRAINT "useMaterial_pkey" PRIMARY KEY ("idPrinter"),
    CONSTRAINT "useMaterials_idColor_fkey" FOREIGN KEY ("idColor")
        REFERENCES public.colors (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "useMaterials_idMaterials_fkey" FOREIGN KEY ("idMaterial")
        REFERENCES public.materials (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "useMaterials_idPrinter_fkey" FOREIGN KEY ("idPrinter")
        REFERENCES public.printers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."useMaterial"
    OWNER to postgres;

COMMENT ON TABLE public."useMaterial"
    IS 'https://yt.omegafuture.ru/articles/RedFabMES-A-158/%5B%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%5D-%D0%A3%D1%87%D0%B5%D1%82-%D0%B7%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B8-%D0%B8-%D1%80%D0%B0%D1%81%D1%85%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2---useMaterial';


-- 14.
ALTER TABLE IF EXISTS public.tasks
    ADD COLUMN volume numeric(8, 3) NOT NULL;


-- 15.
CREATE TABLE public."tasksCopies"
(
    id serial NOT NULL,
    "idTask" integer NOT NULL,
    "numCopy" smallint NOT NULL,
    "printTime" integer,
    "startAt" timestamp with time zone,
    "idTaskStatus" integer,
    "markingDeletion" boolean NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT "tasksCopies_idTask_fkey" FOREIGN KEY ("idTask")
        REFERENCES public.tasks (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "tasksCopies_idTasksStatus_fkey" FOREIGN KEY ("idTaskStatus")
        REFERENCES public."taskStatuses" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public."tasksCopies"
    OWNER to postgres;

COMMENT ON TABLE public."useMaterial"
    IS 'https://yt.omegafuture.ru/articles/RedFabMES-A-170/%5B%D0%9E%D0%9F%5D-%D0%9A%D0%BE%D0%BF%D0%B8%D0%B8-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9---tasksCopies';


-- 16.
ALTER TABLE IF EXISTS public."taskPrinting" DROP COLUMN IF EXISTS "idTask";

ALTER TABLE IF EXISTS public."taskPrinting"
    ADD COLUMN "idTasksCopy" integer NOT NULL;
ALTER TABLE IF EXISTS public."taskPrinting"
    ADD CONSTRAINT "taskPrinting_idTasksCopy_fkey" FOREIGN KEY ("idTasksCopy")
    REFERENCES public."taskPrinting" (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


-- 17.
ALTER TABLE IF EXISTS public."errorTriggers" DROP COLUMN IF EXISTS "automaticServiceOperation";


-- 18.
ALTER TABLE IF EXISTS public."serviceOperations" DROP COLUMN IF EXISTS "functionName";
ALTER TABLE IF EXISTS public."serviceOperations"
    ADD COLUMN automatic boolean;

-- 19.
ALTER TABLE IF EXISTS public.printers
    ALTER COLUMN "basicCellQuantity" SET NOT NULL;

ALTER TABLE IF EXISTS public.printers
    ALTER COLUMN "supportCellQuantity" SET NOT NULL;

ALTER TABLE IF EXISTS public.printers
    ALTER COLUMN "webIs" SET NOT NULL;

ALTER TABLE IF EXISTS public.printers
    ALTER COLUMN "markingDeletion" SET DEFAULT False;

ALTER TABLE IF EXISTS public.printers
    ALTER COLUMN "markingDeletion" SET NOT NULL;

ALTER TABLE IF EXISTS public.printers
    ADD COLUMN "inPrintQueue" boolean NOT NULL DEFAULT True;