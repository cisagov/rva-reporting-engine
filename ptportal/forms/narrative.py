# Risk & Vulnerability Reporting Engine

# Copyright 2022 Carnegie Mellon University.

# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.

# Released under a BSD (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.

# [DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.

# Carnegie Mellon® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.

# This Software includes and/or makes use of Third-Party Software each subject to its own license.

# DM22-0744s
from django import forms
from django_summernote.widgets import SummernoteWidget
from ptportal.models import Narrative

from . import BaseModelForm


class NarrativeForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tool_output_description'].widget.attrs.update(
            {'class': 'form-control', 'rows': 2, 'required': True, 'tabIndex': '-1'}
        )
        self.fields['tools'].widget.attrs.update(
            {'class': 'form-control', 'rows': 2, 'required': False, 'tabIndex': '-1'}
        )

    class Meta:
        model = Narrative
        fields = ['tools', 'tool_output', 'tool_output_description']
        widgets = {
            'tool_output': SummernoteWidget(
                attrs={
                    'class': 'form-control',
                    'summernote': {
                        'toolbar': [['font', ['bold', 'underline', 'italic']]]
                    },
                }
            )
        }