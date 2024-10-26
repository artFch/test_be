### Решение

Проблема изначального кода
    Код:
 ```php
class SomeObject {
    protected $name;
    public function __construct(string $name) { }
    public function getObjectName() { }
}
class SomeObjectsHandler {
    public function __construct() { }
    public function handleObjects(array $objects): array {
        $handlers = [];
        foreach ($objects as $object) {
            if ($object->getObjectName() == 'object_1')
                $handlers[] = 'handle_object_1';
            if ($object->getObjectName() == 'object_2')
                $handlers[] = 'handle_object_2';
        }
        return $handlers;
    }
}
$objects = [
    new SomeObject('object_1'),
    new SomeObject('object_2')
];
$soh = new SomeObjectsHandler();
$soh->handleObjects($objects);
```

Обработка объектов привязана в метод handleObjects
Если появится object_3, то нам нужно будет изменить код класса SomeObjectsHandler, добавив новые условия это нарушение OCP.
А так мы добавим в список handlers handler для object_3 и не будем модифицировать класс и есть возможность для расширения.