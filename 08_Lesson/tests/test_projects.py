import pytest


@pytest.mark.usefixtures("projects_api")
class TestProjects:
    # Позитивные тесты
    def test_create_project_positive(self, projects_api):
        """Позитивный тест создания проекта"""
        project_data = {
            "name": "Test Project",
            "description": "This is a test project"
        }
        response = projects_api.create_project(project_data)

        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["name"] == project_data["name"]

    def test_get_project_positive(self, projects_api, created_project_id):
        """Позитивный тест получения проекта"""
        response = projects_api.get_project(created_project_id)

        assert response.status_code == 200
        assert response.json()["id"] == created_project_id

    def test_update_project_positive(self, projects_api, created_project_id):
        """Позитивный тест обновления проекта"""
        update_data = {
            "name": "Updated Project Name",
            "description": "Updated description"
        }
        response = projects_api.update_project(created_project_id, update_data)

        assert response.status_code == 200
        assert response.json()["name"] == update_data["name"]

    # Негативные тесты
    def test_create_project_negative(self, projects_api):
        """Негативный тест создания проекта (без обязательного поля name)"""
        project_data = {
            "description": "Project without name"
        }
        response = projects_api.create_project(project_data)

        assert response.status_code == 400

    def test_get_project_negative(self, projects_api):
        """Негативный тест получения проекта (несуществующий ID)"""
        non_existent_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.get_project(non_existent_id)

        assert response.status_code == 404

    def test_update_project_negative(self, projects_api, created_project_id):
        """Негативный тест обновления проекта (некорректные данные)"""
        update_data = {
            "name": "",  # Пустое имя недопустимо
            "description": "Invalid update"
        }
        response = projects_api.update_project(created_project_id, update_data)

        assert response.status_code == 400