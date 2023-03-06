-- Статусы принтеров
insert into "printerStatus" values
	(1, 'Нет соединения'),
	(2, 'Свободен'),
	(3, 'Работает'),
	(4, 'Пауза'),
	(5, 'Пауза по ошибке'),
	(6, 'Ошибка');

-- Группы датчиков
insert into "sensorsGroups" values
	(1, 'Механизм принтера'),
	(2, 'Механизм селективной подачи'),
	(3, 'Отсек материалов'),
	(4, 'Отсек электроники'),
	(5, 'Общий на комплекс'),
	(6, 'Вакуумная система'),
	(7, 'Стойка');

-- Статусы проекта
insert into "projectStatuses" values
	(1, 'В подготовке'),
	(2, 'На утверждении'),
	(3, 'В печати'),
	(4, 'Завершен'),
	(5, 'Отменен');

-- Статусы заданий
insert into "taskStatuses" values
	(1, 'В очереди'),
	(2, 'В печати'),
	(3, 'Пауза'),
	(4, 'Отменено'),
	(5, 'Брак'),
	(6, 'Завершено');

-- Приоритеты печати
insert into priorities values
	(1, 'Вперед остальных'),
	(2, 'В порядке очереди'),
	(3, 'Во время простоев');

-- Реакции на оповещение
insert into reactions values
	(1, 'Прочитано'),
	(2, 'Не отображать повторно'),
	(3, 'Отключить датчик'),
	(4, 'Не проводить автоматическую сервисную операцию повторно');

-- Материалы

-- 1. Полимерные основы:
insert into "polymerBases" values
	(1, 'ABS'),
	(2, 'ABS/PA'),
	(3, 'ASA'),
	(4, 'ASA/PC'),
	(5, 'Flex'),
	(6, 'HIPS'),
	(7, 'Nylon/PA'),
	(8, 'PBT'),
	(9, 'PC'),
	(10, 'PC/ABS'),
	(11, 'PCL'),
	(12, 'PEEK'),
	(13, 'PEI'),
	(14, 'PEKK'),
	(15, 'PET'),
	(16, 'PETG'),
	(17, 'PLA'),
	(18, 'PMMA'),
	(19, 'PND'),
	(20, 'POM'),
	(21, 'PP'),
	(22, 'PPS'),
	(23, 'PSU'),
	(24, 'PVA'),
	(25, 'SAN'),
	(26, 'SBS'),
	(27, 'TPE'),
	(28, 'TPU'),
	(29, 'WAX');

-- 2. Производители
insert into makers (id, name) values
	(1, 'BestFilament'),
	(2, 'Filamentarno F!'),
	(3, 'PrintProduct'),
	(4, 'REC'),
	(5, 'u3print');

-- 3. Материалы
insert into materials (id, name, "idPolymerBase", composite, "idMaker", density, "printingTemp", "maxRadiatorTemp", "tableTemp", "blowingParts", "chamberTemp", "timeSwitchCoolingMode", "coolingModeTemp", "materialUnloadSpeed", "materialUnloadTemp", "materialUnloadLength", "materialLoadSpeed", "materialCleanLength", "materialServeCoef", "gramsCost", "markingDeletion") values
	-- (1, 'ABS', 1, 'False', 1, 1.05, 245, 80, 95, 10, 60, 100, 80, 30, 99, 100, 10, 50, 100, 0, 'False'),
	-- (2, 'ABS/PA2', 2, 'True', 2, 1.07, 260, 100, 115, 10, 80, 60, 80, 30, 99, 100, 10, 50, 100, 0, 'False'),
	-- (3, 'WAX 3D Base', 29, 'False',	2, 0.98, 135, 50, 24, 0, 40, 100, 50, 30, 99, 100, 30, 100, 100, 0, 'False');

