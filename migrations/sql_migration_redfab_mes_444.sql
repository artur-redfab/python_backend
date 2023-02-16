ALTER TABLE IF EXISTS public.projects DROP COLUMN IF EXISTS cost;

ALTER TABLE IF EXISTS public.projects
    ALTER COLUMN "idPriority" SET NOT NULL;

ALTER TABLE IF EXISTS public.projects
    ALTER COLUMN "deadLine" SET NOT NULL;

ALTER TABLE IF EXISTS public.projects
    ALTER COLUMN "changeDate" DROP NOT NULL;

ALTER TABLE IF EXISTS public.projects
    ALTER COLUMN "orderNumber" SET NOT NULL;

ALTER TABLE IF EXISTS public.projects
    ALTER COLUMN "idResponsible" SET NOT NULL;

ALTER TABLE IF EXISTS public.projects
    ALTER COLUMN "idAuthor" SET NOT NULL;

ALTER TABLE IF EXISTS public.projects
    ALTER COLUMN "markingDeletion" SET DEFAULT False;

ALTER TABLE IF EXISTS public.projects
    ALTER COLUMN "markingDeletion" SET NOT NULL;