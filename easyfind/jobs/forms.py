from django.forms import ModelForm, fields

from jobs.models import Job


class JobForm(ModelForm):

    geoposition_0 = fields.DecimalField()
    geoposition_1 = fields.DecimalField()

    class Meta:
        model = Job
        fields = ['title', 'start_asap',]