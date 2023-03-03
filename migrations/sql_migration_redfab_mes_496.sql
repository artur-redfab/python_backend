ALTER TABLE IF EXISTS public."operGroups"
    ALTER COLUMN "markingDeletion" SET DEFAULT False;

ALTER TABLE IF EXISTS public."operGroups"
    ALTER COLUMN "markingDeletion" SET NOT NULL;