# resources.py
from import_export import resources
from .models import Students,Grades

class StudentsResource(resources.ModelResource):

    class Meta:
        model = Students
        fields = ('sname', 'sgender','sage','scontend','isDelete','lastTime','createTime','sgrade')


class GradesResource(resources.ModelResource):

    class Meta:
        model = Grades
        fields = ('gname', 'gdate', 'ggirlnum', 'ggirlnum','isDelete')
