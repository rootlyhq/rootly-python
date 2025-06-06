from enum import Enum


class AuditItemType(str, Enum):
    APIKEY = "ApiKey"
    CAUSE = "Cause"
    CUSTOMFIELD = "CustomField"
    CUSTOMFIELDOPTION = "CustomFieldOption"
    CUSTOMFORM = "CustomForm"
    DASHBOARD = "Dashboard"
    ENVIRONMENT = "Environment"
    ESCALATIONPOLICY = "EscalationPolicy"
    ESCALATIONPOLICYPATH = "EscalationPolicyPath"
    EXPORTJOB = "ExportJob"
    FORMFIELD = "FormField"
    FUNCTIONALITY = "Functionality"
    GENIUSWORKFLOW = "GeniusWorkflow"
    GENIUSWORKFLOWGROUP = "GeniusWorkflowGroup"
    GENIUSWORKFLOWRUN = "GeniusWorkflowRun"
    GROUP = "Group"
    HEARTBEAT = "Heartbeat"
    INCIDENT = "Incident"
    INCIDENTACTIONITEM = "IncidentActionItem"
    INCIDENTEVENT = "IncidentEvent"
    INCIDENTFORMFIELDSELECTION = "IncidentFormFieldSelection"
    INCIDENTFORMFIELDSELECTIONUSER = "IncidentFormFieldSelectionUser"
    INCIDENTPOSTMORTEM = "IncidentPostMortem"
    INCIDENTROLEASSIGNMENT = "IncidentRoleAssignment"
    INCIDENTROLETASK = "IncidentRoleTask"
    INCIDENTSTATUSPAGEEVENT = "IncidentStatusPageEvent"
    INCIDENTTASK = "IncidentTask"
    INCIDENTTYPE = "IncidentType"
    LIVECALLROUTER = "LiveCallRouter"
    ONCALLROLE = "OnCallRole"
    PLAYBOOK = "Playbook"
    PLAYBOOKTASK = "PlaybookTask"
    ROLE = "Role"
    SCHEDULE = "Schedule"
    SERVICE = "Service"
    SEVERITY = "Severity"
    STATUSPAGE = "StatusPage"

    def __str__(self) -> str:
        return str(self.value)
