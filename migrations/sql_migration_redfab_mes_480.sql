ALTER TABLE IF EXISTS public."sensorData"
    ALTER COLUMN period SET NOT NULL;

ALTER TABLE IF EXISTS public."sensorData"
    ALTER COLUMN "idSensor" SET NOT NULL;

ALTER TABLE IF EXISTS public."sensorData"
    ALTER COLUMN data SET NOT NULL;

ALTER TABLE IF EXISTS public."sensorData"
    ALTER COLUMN "dataType" SET NOT NULL;

ALTER TABLE IF EXISTS public."sensorData"
    ALTER COLUMN "idPrinter" SET NOT NULL;

ALTER TABLE IF EXISTS public."sensorGroups"
    ALTER COLUMN name SET NOT NULL;

ALTER TABLE IF EXISTS public.sensors
    ALTER COLUMN name SET NOT NULL;

ALTER TABLE IF EXISTS public.sensors
    ALTER COLUMN "nameIdentifier" SET NOT NULL;

ALTER TABLE IF EXISTS public.sensors
    ALTER COLUMN "dataType" SET NOT NULL;

ALTER TABLE IF EXISTS public.sensors
    ALTER COLUMN description SET NOT NULL;

ALTER TABLE IF EXISTS public.sensors
    ALTER COLUMN "requiredUsed" SET NOT NULL;

ALTER TABLE IF EXISTS public.sensors
    ALTER COLUMN "canDeactivate" SET NOT NULL;

ALTER TABLE IF EXISTS public."sensorsInPrinters"
    ALTER COLUMN "isUsed" SET NOT NULL;