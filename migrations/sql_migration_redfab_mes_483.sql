ALTER TABLE IF EXISTS public.partners DROP COLUMN IF EXISTS created;

ALTER TABLE IF EXISTS public.partners
    ALTER COLUMN inn SET NOT NULL;

ALTER TABLE IF EXISTS public.partners
    ALTER COLUMN "markingDeletion" SET DEFAULT False;

ALTER TABLE IF EXISTS public.partners
    ALTER COLUMN "markingDeletion" SET NOT NULL;