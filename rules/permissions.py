from .rulesets import RuleSet


permissions = RuleSet()


def add_perm(name, pred):
    permissions.add_rule(name, pred)


def remove_perm(name):
    permissions.remove_rule(name)


def perm_exists(name):
    return permissions.rule_exists(name)


def has_perm(name, *args, **kwargs):
    return permissions.test_rule(name, *args, **kwargs)


class ObjectPermissionBackend(object):
    supports_object_permissions = True

    def authenticate(self, username, password):
        return None

    def has_perm(self, user, perm, *args, **kwargs):
        return has_perm(perm, user, *args, **kwargs)

    def has_module_perms(self, user, app_label):
        return has_perm(app_label, user)
