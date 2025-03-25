from .base_api import BaseAPI


class ProjectsAPI(BaseAPI):
    def create_project(self, project_data):
        """Создание нового проекта"""
        return self._request('POST', '/api-v2/projects', json=project_data)

    def get_project(self, project_id):
        """Получение проекта по ID"""
        return self._request('GET', f'/api-v2/projects/{project_id}')

    def update_project(self, project_id, update_data):
        """Обновление проекта"""
        return self._request('PUT', f'/api-v2/projects/{project_id}', json=update_data)