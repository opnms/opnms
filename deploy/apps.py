from django.apps import AppConfig
from django.db.models import signals
from deploy.signal import set_saltgroup_abbr_name

class DeployConfig(AppConfig):
    name = 'deploy'

    def ready(self):
        SaltGroupModel = self.get_model('SaltGroup')
        signals.pre_save.connect(set_saltgroup_abbr_name,
                                 sender=SaltGroupModel,
                                 dispatch_uid="set_saltgroup_abbr_name_when_edit_idc")
