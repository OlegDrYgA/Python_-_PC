from models import Student


def test_create_student(db_session):
    """Тест создания студента"""
    # Создаем нового студента
    new_student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Проверяем, что студент создан
    student = db_session.query(Student).filter_by(email="ivan@example.com").first()
    assert student is not None
    assert student.name == "Иван Иванов"
    assert student.email == "ivan@example.com"


def test_update_student(db_session):
    """Тест обновления студента"""
    # Сначала создаем студента
    new_student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Обновляем данные
    student = db_session.query(Student).filter_by(email="petr@example.com").first()
    student.name = "Петр Сидоров"
    db_session.commit()

    # Проверяем обновление
    updated_student = db_session.query(Student).filter_by(email="petr@example.com").first()
    assert updated_student.name == "Петр Сидоров"


def test_delete_student(db_session):
    """Тест удаления студента"""
    # Сначала создаем студента
    new_student = Student(name="Сергей Сергеев", email="sergey@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Удаляем студента
    student = db_session.query(Student).filter_by(email="sergey@example.com").first()
    db_session.delete(student)
    db_session.commit()

    # Проверяем, что студент удален
    deleted_student = db_session.query(Student).filter_by(email="sergey@example.com").first()
    assert deleted_student is None