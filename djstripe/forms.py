# -*- coding: utf-8 -*-
"""
.. module:: djstripe.forms.

   :synopsis: dj-stripe Forms.

.. moduleauthor:: Daniel Greenfeld (@pydanny)

"""
from __future__ import absolute_import, division, print_function, unicode_literals

from django import forms

from .models import Plan


class PlanForm(forms.Form):
    """A form used when creating a Plan."""

    plan = forms.ModelChoiceField(queryset=Plan.objects.all())


class QuantityPlanForm(PlanForm):
    """A plan form that allows setting the quantity attribute for a Plan."""
    plan_quantity = forms.IntegerField(initial=1, required=True)


class CancelSubscriptionForm(forms.Form):
    """A form used when canceling a Subscription."""

    pass
