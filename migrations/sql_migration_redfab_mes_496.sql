ALTER TABLE IF EXISTS public."operGroups"
    ALTER COLUMN "markingDeletion" SET DEFAULT False;

ALTER TABLE IF EXISTS public."operGroups"
    ALTER COLUMN "markingDeletion" SET NOT NULL;

ALTER TABLE IF EXISTS public.printers
    ADD COLUMN "selectiveSystemIP" character varying SET NOT NULL;

ALTER TABLE IF EXISTS public.printers
    ADD COLUMN "selectiveSystemPort" integer SET NOT NULL;