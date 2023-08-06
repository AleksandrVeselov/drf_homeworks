from rest_framework.permissions import BasePermission


class IsOwnerOrModerator(BasePermission):
    """Проверка прав доступа"""

    def has_permission(self, request, view):

        # если пользователь относится к группе модераторы то возвращаем True
        if request.user.groups.filter(name='moderator').exists():
            return True

        return request.user == view.get_object().owner  # если пользователь это владелец, то возвращаем True


class IsNotModerator(BasePermission):
    """Проверка прав доступа"""

    def has_permission(self, request, view):

        # если пользователь относится к группе модераторы то возвращаем False
        if request.user.groups.filter(name='moderator').exists():
            return False


class IsOwner(BasePermission):
    """Проверка прав доступа"""

    def has_permission(self, request, view):
        return request.user == view.get_object().owner  # если пользователь это владелец, то возвращаем True

