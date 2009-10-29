# Job Board: a simple Django-based job board
# Copyright (C) 2008  Imaginary Landscape
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

try:
    from django import forms
except ImportError:
    # for pre 1.0 compatibility
    from django import newforms as forms

from jobboard import models


class JobPost(forms.Form):
    """
    The submission form for a visitor submitting a new job post.
    """
    posters_name = forms.CharField(max_length=80)
    work_hours = forms.CharField(max_length=80, required=False)
    description = forms.CharField(required=False, widget=forms.Textarea)
    position = forms.ModelChoiceField(models.Position.objects.all())
    email = forms.EmailField(required=False)
    contact_information = forms.CharField(widget=forms.Textarea)

    def clean_posters_name(self):
        """
        Clean up the `posters_name` field to reduce it to one line
        """
        return self.cleaned_data['posters_name'].split('\n')[0]


class ApplicantPost(forms.Form):
    """
    The submission form for a visitor submitting a new applicant post.
    """
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    phone_number = forms.CharField(max_length=25)
    position = forms.ModelChoiceField(models.Position.objects.all())
    email = forms.EmailField(required=False)
    resume = forms.CharField(widget=forms.Textarea)

    full_time = forms.BooleanField(required=False)
    part_time = forms.BooleanField(required=False)
    other_time = forms.BooleanField(required=False)

    def clean_first_name(self):
        """
        Clean up the `first_name` field to reduce it to one line
        """
        return self.cleaned_data['first_name'].split('\n')[0]

    def clean_last_name(self):
        """
        Clean up the `last_name` field to reduce it to one line
        """
        return self.cleaned_data['last_name'].split('\n')[0]