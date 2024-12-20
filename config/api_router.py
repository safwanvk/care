from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from care.emr.api.otp_viewsets.login import OTPLoginView
from care.emr.api.otp_viewsets.patient import PatientOTPView
from care.emr.api.otp_viewsets.slot import OTPSlotViewSet
from care.emr.api.viewsets.allergy_intolerance import AllergyIntoleranceViewSet
from care.emr.api.viewsets.batch_request import BatchRequestView
from care.emr.api.viewsets.condition import DiagnosisViewSet, SymptomViewSet
from care.emr.api.viewsets.encounter import EncounterViewSet
from care.emr.api.viewsets.medication_request import MedicationRequestViewSet
from care.emr.api.viewsets.observation import ObservationViewSet
from care.emr.api.viewsets.organization import OrganizationViewSet
from care.emr.api.viewsets.questionnaire import QuestionnaireViewSet
from care.emr.api.viewsets.questionnaire_response import QuestionnaireResponseViewSet
from care.emr.api.viewsets.scheduling import ScheduleViewSet, SlotViewSet
from care.emr.api.viewsets.scheduling.availability_exceptions import (
    AvailabilityExceptionsViewSet,
)
from care.emr.api.viewsets.scheduling.booking import TokenBookingViewSet
from care.emr.api.viewsets.units import UnitsView
from care.emr.api.viewsets.valueset import ValueSetViewSet
from care.facility.api.viewsets.ambulance import AmbulanceViewSet
from care.facility.api.viewsets.asset import (
    AssetLocationViewSet,
    AssetPublicQRViewSet,
    AssetPublicViewSet,
    AssetRetrieveConfigViewSet,
    AssetServiceViewSet,
    AssetTransactionViewSet,
    AssetViewSet,
    AvailabilityViewSet,
)
from care.facility.api.viewsets.bed import (
    AssetBedViewSet,
    BedViewSet,
    ConsultationBedViewSet,
    PatientAssetBedViewSet,
)
from care.facility.api.viewsets.camera_preset import (
    AssetBedCameraPresetViewSet,
    CameraPresetViewSet,
)
from care.facility.api.viewsets.consultation_diagnosis import (
    ConsultationDiagnosisViewSet,
)
from care.facility.api.viewsets.daily_round import DailyRoundsViewSet
from care.facility.api.viewsets.encounter_symptom import EncounterSymptomViewSet
from care.facility.api.viewsets.events import (
    EventTypeViewSet,
    PatientConsultationEventViewSet,
)
from care.facility.api.viewsets.facility import (
    AllFacilityViewSet,
    FacilityHubsViewSet,
    FacilitySpokesViewSet,
    FacilityViewSet,
)
from care.facility.api.viewsets.facility_capacity import FacilityCapacityViewSet
from care.facility.api.viewsets.facility_users import FacilityUserViewSet
from care.facility.api.viewsets.file_upload import FileUploadViewSet
from care.facility.api.viewsets.hospital_doctor import HospitalDoctorViewSet
from care.facility.api.viewsets.icd import ICDViewSet
from care.facility.api.viewsets.inventory import (
    FacilityInventoryItemViewSet,
    FacilityInventoryLogViewSet,
    FacilityInventoryMinQuantityViewSet,
    FacilityInventorySummaryViewSet,
)
from care.facility.api.viewsets.notification import NotificationViewSet
from care.facility.api.viewsets.patient import (
    FacilityDischargedPatientViewSet,
    FacilityPatientStatsHistoryViewSet,
    PatientNotesEditViewSet,
    PatientNotesViewSet,
    PatientSearchViewSet,
    PatientViewSet,
)
from care.facility.api.viewsets.patient_consultation import (
    PatientConsentViewSet,
    PatientConsultationViewSet,
)
from care.facility.api.viewsets.patient_external_test import PatientExternalTestViewSet
from care.facility.api.viewsets.patient_investigation import (
    InvestigationGroupViewset,
    InvestigationValueViewSet,
    PatientInvestigationSummaryViewSet,
    PatientInvestigationViewSet,
)
from care.facility.api.viewsets.patient_sample import PatientSampleViewSet
from care.facility.api.viewsets.prescription import (
    ConsultationPrescriptionViewSet,
    MedibaseViewSet,
    MedicineAdministrationViewSet,
)
from care.facility.api.viewsets.resources import (
    ResourceRequestCommentViewSet,
    ResourceRequestViewSet,
)
from care.facility.api.viewsets.shifting import (
    ShifitngRequestCommentViewSet,
    ShiftingViewSet,
)
from care.facility.api.viewsets.summary import (
    DistrictPatientSummaryViewSet,
    FacilityCapacitySummaryViewSet,
    PatientSummaryViewSet,
    TestsSummaryViewSet,
    TriageSummaryViewSet,
)
from care.users.api.viewsets.lsg import (
    DistrictViewSet,
    LocalBodyViewSet,
    StateViewSet,
    WardViewSet,
)
from care.users.api.viewsets.plug_config import PlugConfigViewset
from care.users.api.viewsets.skill import SkillViewSet
from care.users.api.viewsets.users import UserViewSet
from care.users.api.viewsets.userskill import UserSkillViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet, basename="users")

router.register("plug_config", PlugConfigViewset, basename="plug_configs")

user_nested_router = NestedSimpleRouter(router, r"users", lookup="users")
user_nested_router.register("skill", UserSkillViewSet, basename="users-skill")

router.register("skill", SkillViewSet, basename="skill")

# Local Body / LSG Viewsets
router.register("state", StateViewSet, basename="state")
router.register("district", DistrictViewSet, basename="district")
router.register("local_body", LocalBodyViewSet, basename="local-body")
router.register("ward", WardViewSet, basename="ward")

router.register("files", FileUploadViewSet, basename="files")

router.register("ambulance", AmbulanceViewSet, basename="ambulance")

router.register("icd", ICDViewSet, basename="icd")

router.register("otp", OTPLoginView, basename="otp-login")

router.register("otp/patient", PatientOTPView, basename="otp-patient")

router.register("otp/slots", OTPSlotViewSet, basename="otp-slots")


router.register("notification", NotificationViewSet, basename="notification")

router.register("batch_requests", BatchRequestView, basename="batch-requests")

router.register("units", UnitsView, basename="units")

router.register("valueset", ValueSetViewSet, basename="value-set")

router.register("questionnaire", QuestionnaireViewSet, basename="questionnaire")


# Summarisation
router.register(
    "facility_summary", FacilityCapacitySummaryViewSet, basename="summary-facility"
)
router.register("patient_summary", PatientSummaryViewSet, basename="summary-patient")
router.register("tests_summary", TestsSummaryViewSet, basename="summary-tests")
router.register("triage_summary", TriageSummaryViewSet, basename="summary-triage")


# District Summary
router.register(
    "district_patient_summary",
    DistrictPatientSummaryViewSet,
    basename="district-summary-patient",
)

router.register("items", FacilityInventoryItemViewSet, basename="items")

router.register("shift", ShiftingViewSet, basename="patient-shift")
shifting_nested_router = NestedSimpleRouter(router, r"shift", lookup="shift")
shifting_nested_router.register(
    r"comment", ShifitngRequestCommentViewSet, basename="patient-shift-comment"
)

router.register("resource", ResourceRequestViewSet, basename="resource-request")
resource_nested_router = NestedSimpleRouter(router, r"resource", lookup="resource")
resource_nested_router.register(
    r"comment", ResourceRequestCommentViewSet, basename="resource-request-comment"
)

router.register(
    "investigation/group", InvestigationGroupViewset, basename="investigation-group"
)
router.register("investigation", PatientInvestigationViewSet, basename="investigation")

router.register("facility", FacilityViewSet, basename="facility")
router.register("getallfacilities", AllFacilityViewSet, basename="getallfacilities")
facility_nested_router = NestedSimpleRouter(router, r"facility", lookup="facility")
facility_nested_router.register(
    r"get_users", FacilityUserViewSet, basename="facility-users"
)
facility_nested_router.register(
    r"hospital_doctor", HospitalDoctorViewSet, basename="hospital-doctor"
)
facility_nested_router.register(
    r"capacity", FacilityCapacityViewSet, basename="facility-capacity"
)
facility_nested_router.register(
    r"patient_stats",
    FacilityPatientStatsHistoryViewSet,
    basename="facility-patient-stats",
)
facility_nested_router.register(
    r"inventory", FacilityInventoryLogViewSet, basename="facility-inventory"
)
facility_nested_router.register(
    r"inventorysummary",
    FacilityInventorySummaryViewSet,
    basename="facility-inventory-summary",
)
facility_nested_router.register(
    r"min_quantity",
    FacilityInventoryMinQuantityViewSet,
    basename="facility-inventory-min-quantity",
)
facility_nested_router.register(
    r"asset_location", AssetLocationViewSet, basename="facility-location"
)

facility_location_nested_router = NestedSimpleRouter(
    facility_nested_router, r"asset_location", lookup="asset_location"
)
facility_location_nested_router.register(
    r"availability", AvailabilityViewSet, basename="facility-location-availability"
)

facility_nested_router.register(
    r"patient_asset_beds",
    PatientAssetBedViewSet,
    basename="facility-patient-asset-beds",
)
facility_nested_router.register(
    r"discharged_patients",
    FacilityDischargedPatientViewSet,
    basename="facility-discharged-patients",
)
facility_nested_router.register(
    r"spokes", FacilitySpokesViewSet, basename="facility-spokes"
)
facility_nested_router.register(r"hubs", FacilityHubsViewSet, basename="facility-hubs")

facility_nested_router.register(
    r"organizations", OrganizationViewSet, basename="organization"
)
facility_nested_router.register(r"schedule", ScheduleViewSet, basename="schedule")

facility_nested_router.register(r"slots", SlotViewSet, basename="slot")

facility_nested_router.register(
    r"appointments", TokenBookingViewSet, basename="appointments"
)

facility_nested_router.register(
    r"schedule_exceptions",
    AvailabilityExceptionsViewSet,
    basename="schedule-exceptions",
)

router.register("asset", AssetViewSet, basename="asset")
asset_nested_router = NestedSimpleRouter(router, r"asset", lookup="asset")
asset_nested_router.register(
    r"camera_presets", CameraPresetViewSet, basename="asset-camera-presets"
)
asset_nested_router.register(
    r"availability", AvailabilityViewSet, basename="asset-availability"
)
asset_nested_router.register(
    r"service_records", AssetServiceViewSet, basename="asset-service-records"
)

router.register("asset_config", AssetRetrieveConfigViewSet, basename="asset-config")
router.register("asset_transaction", AssetTransactionViewSet)

router.register("bed", BedViewSet, basename="bed")
bed_nested_router = NestedSimpleRouter(router, r"bed", lookup="bed")
bed_nested_router.register(
    r"camera_presets", CameraPresetViewSet, basename="bed-camera-presets"
)

router.register("assetbed", AssetBedViewSet, basename="asset-bed")
router.register("consultationbed", ConsultationBedViewSet, basename="consultation-bed")
assetbed_nested_router = NestedSimpleRouter(router, r"assetbed", lookup="assetbed")
assetbed_nested_router.register(
    r"camera_presets", AssetBedCameraPresetViewSet, basename="assetbed-camera-presets"
)

router.register("patient/search", PatientSearchViewSet, basename="patient-search")
router.register("patient", PatientViewSet, basename="patient")
patient_nested_router = NestedSimpleRouter(router, r"patient", lookup="patient")
patient_nested_router.register(
    r"test_sample", PatientSampleViewSet, basename="patient-test-sample"
)
patient_nested_router.register(
    r"investigation",
    PatientInvestigationSummaryViewSet,
    basename="patient-investigation",
)
patient_nested_router.register(r"notes", PatientNotesViewSet, basename="patient-notes")
patient_notes_nested_router = NestedSimpleRouter(
    patient_nested_router, r"notes", lookup="notes"
)
patient_notes_nested_router.register(
    r"edits", PatientNotesEditViewSet, basename="patient-notes-edits"
)

patient_nested_router.register(
    r"allergy_intolerance", AllergyIntoleranceViewSet, basename="allergy-intolerance"
)

patient_nested_router.register(r"symptom", SymptomViewSet, basename="symptom")
patient_nested_router.register(r"diagnosis", DiagnosisViewSet, basename="diagnosis")


patient_nested_router.register(r"encounter", EncounterViewSet, basename="encounter")

patient_nested_router.register(
    "observation", ObservationViewSet, basename="observation"
)

patient_nested_router.register(
    "questionnaire_response",
    QuestionnaireResponseViewSet,
    basename="questionnaire-response",
)


patient_nested_router.register(
    r"medication/request",
    MedicationRequestViewSet,
    basename="medication-request",
)

router.register(
    "external_result", PatientExternalTestViewSet, basename="patient-external-result"
)
router.register("test_sample", PatientSampleViewSet, basename="patient-test-sample")

router.register(
    "consultation", PatientConsultationViewSet, basename="patient-consultation"
)
consultation_nested_router = NestedSimpleRouter(
    router, r"consultation", lookup="consultation"
)


consultation_nested_router.register(
    r"daily_rounds", DailyRoundsViewSet, basename="consultation-daily-rounds"
)


consultation_nested_router.register(
    r"diagnoses", ConsultationDiagnosisViewSet, basename="consultation-diagnoses"
)
consultation_nested_router.register(
    r"symptoms", EncounterSymptomViewSet, basename="consultation-symptoms"
)
consultation_nested_router.register(
    r"investigation", InvestigationValueViewSet, basename="consultation-investigation"
)
consultation_nested_router.register(
    r"prescriptions",
    ConsultationPrescriptionViewSet,
    basename="consultation-prescriptions",
)
consultation_nested_router.register(
    r"prescription_administration",
    MedicineAdministrationViewSet,
    basename="consultation-prescription-administration",
)
consultation_nested_router.register(
    r"events", PatientConsultationEventViewSet, basename="consultation-events"
)

consultation_nested_router.register(
    r"consents", PatientConsentViewSet, basename="consultation-consents"
)

router.register("event_types", EventTypeViewSet, basename="event-types")

router.register("medibase", MedibaseViewSet, basename="medibase")

# Public endpoints
router.register("public/asset", AssetPublicViewSet, basename="public-asset")
router.register("public/asset_qr", AssetPublicQRViewSet, basename="public-asset-qr")

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("", include(user_nested_router.urls)),
    path("", include(facility_nested_router.urls)),
    path("", include(facility_location_nested_router.urls)),
    path("", include(asset_nested_router.urls)),
    path("", include(bed_nested_router.urls)),
    path("", include(assetbed_nested_router.urls)),
    path("", include(patient_nested_router.urls)),
    path("", include(patient_notes_nested_router.urls)),
    path("", include(consultation_nested_router.urls)),
    path("", include(resource_nested_router.urls)),
    path("", include(shifting_nested_router.urls)),
]
