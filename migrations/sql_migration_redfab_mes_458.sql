ALTER TABLE IF EXISTS public.tasks
    ALTER COLUMN "idBasicColor" SET NOT NULL;

ALTER TABLE IF EXISTS public.tasks
    ADD CONSTRAINT "tasks_idBasicMaterial_fkey" FOREIGN KEY ("idBasicMaterial")
    REFERENCES public.materials (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS public.tasks
    ADD CONSTRAINT "tasks_idBasicColor_fkey" FOREIGN KEY ("idBasicColor")
    REFERENCES public.colors (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS public.tasks
    ADD CONSTRAINT "tasks_idSupportMaterial_fkey" FOREIGN KEY ("idSupportMaterial")
    REFERENCES public.materials (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS public.tasks
    ADD CONSTRAINT "tasks_idSupportColor_fkey" FOREIGN KEY ("idSupportColor")
    REFERENCES public.colors (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;