from django.http import JsonResponse, HttpRequest
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from medicine_module.forms import SearchForm
from medicine_module.models import Medicine
from .forms import PatientForm
from . models import Prescription,PrescriptionDetails


# Create your views here.

class PrescriptionView(TemplateView):
    template_name = 'prescription_module/prescription.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm
        context['patient'] = PatientForm
        current_prescriptions, created = Prescription.objects.prefetch_related('prescriptiondetails_set').get_or_create(
            is_submitted=False, doctor=self.request.user)
        context['prescription'] = current_prescriptions
        return context

def add_medicine_to_prescription(request):
    medicine_id = request.GET.get('medicine_id')
    count = request.GET.get('count')

    medicine = Medicine.objects.filter(id=medicine_id).first()
    if medicine is not None:
        current_prescriptions, created = Prescription.objects.get_or_create(is_submitted=False, doctor=request.user)
        current_prescriptions_detail = current_prescriptions.prescriptiondetails_set.filter(medicine_id=medicine_id).first()
        if current_prescriptions_detail is not None:
            current_prescriptions_detail.count += int(count)
            current_prescriptions_detail.save()
        else:
            new_detail = PrescriptionDetails(prescription_id=current_prescriptions.id,medicine_id=medicine_id, count=count)
            new_detail.save()

        context = {
            'prescription': current_prescriptions,
        }

        return JsonResponse({
            'status': 'success',
            'icon':'success',
            'html': "دارو با موفقیت اضافه شد",
            'body': render_to_string('prescription_module/prescription_basket_content.html', context),
        })
    else:
        return JsonResponse({
            'status': 'success',
            'icon':'error',
            'html': "با خطا مواجه شد",
        })


def remove_prescription_basket_detail(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id',
        })

    deleted_count,deleted_dict = PrescriptionDetails.objects.filter(id=detail_id,prescription__is_submitted=False, prescription__doctor_id=request.user).delete()
    if deleted_count is None:
        return JsonResponse({
            'status': 'not_found',
        })

    current_prescriptions, created = Prescription.objects.prefetch_related('prescriptiondetails_set').get_or_create(is_submitted=False, doctor=request.user)

    context = {
        'prescription': current_prescriptions
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('prescription_module/prescription_basket_content.html' ,context),
    })

def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')

    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_id_or_state',
        })

    prescription_detail = PrescriptionDetails.objects.filter(id=detail_id, prescription__doctor_id=request.user, prescription__is_submitted=False).first()
    if prescription_detail is None:
        return JsonResponse({
            'status': 'detail_not_found',
        })

    if state == 'increase':
        prescription_detail.count += 1
        prescription_detail.save()
    elif state == 'decrease':
        if prescription_detail.count == 1:
            prescription_detail.delete()
        else:
            prescription_detail.count -= 1
            prescription_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid',
        })

    current_prescriptions, created = Prescription.objects.prefetch_related('prescriptiondetails_set').get_or_create(
        is_submitted=False, doctor=request.user)

    context = {
        'prescription': current_prescriptions
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('prescription_module/prescription_basket_content.html', context),
    })