from care.emr.models.organziation import FacilityOrganizationUser
from care.security.authorization.base import (
    AuthorizationController,
    AuthorizationHandler,
)
from care.security.permissions.encounter import EncounterPermissions


class EncounterAccess(AuthorizationHandler):
    def can_create_encounter_obj(self, user, facility):
        """
        Check if the user has permission to create encounter under this facility
        """
        return self.check_permission_in_facility_organization(
            [EncounterPermissions.can_create_encounter.name], user, facility=facility
        )

    def can_view_encounter_obj(self, user, facility):
        """
        Check if the user has permission to read encounter under this facility
        """
        return self.check_permission_in_facility_organization(
            [EncounterPermissions.can_read_encounter.name], user, facility=facility
        )

    def can_update_encounter_obj(self, user, encounter):
        """
        Check if the user has permission to create encounter under this facility
        """
        # TODO check if encounter has been closed
        return self.check_permission_in_facility_organization(
            [EncounterPermissions.can_write_encounter.name],
            user,
            orgs=encounter.facility_organization_cache,
        )

    def get_filtered_encounters(self, qs, user, facility):
        if user.is_superuser:
            return qs
        roles = self.get_role_from_permissions(
            [EncounterPermissions.can_list_encounter.name]
        )
        organization_ids = list(
            FacilityOrganizationUser.objects.filter(
                user=user, organization__facility=facility, role_id__in=roles
            ).values_list("organization_id", flat=True)
        )
        return qs.filter(facility_organization_cache__overlap=organization_ids)


AuthorizationController.register_internal_controller(EncounterAccess)
