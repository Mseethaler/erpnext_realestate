import frappe

KANBAN_BOARDS = [
    {
        "name": "RE Sales",
        "reference_doctype": "Opportunity",
        "field_name": "custom_re_sale_stage",
        "filters": [
            ["Opportunity", "opportunity_type", "=", "RE Sale", False],
            ["Opportunity", "status", "!=", "Closed", False],
        ],
        "columns": [
            "Property Listed", "Active Marketing", "Offer Received",
            "Negotiation", "Under Contract", "Due Diligence / Appraisal",
            "Closing / Settlement Scheduled", "Closed (Sold)", "Withdrawn / Lost",
        ],
    },
    {
        "name": "RE Buys",
        "reference_doctype": "Opportunity",
        "field_name": "custom_re_buy_stage",
        "filters": [
            ["Opportunity", "opportunity_type", "=", "RE Buy", False],
            ["Opportunity", "status", "!=", "Closed", False],
        ],
        "columns": [
            "Property Identified", "Viewing / Showing Scheduled",
            "Offer Preparation", "Trigger Offer Submit", "Negotiation",
            "Under Contract", "Due Diligence / Inspection Period",
            "Closing / Settlement Scheduled", "Closed (Won)", "Closed (Lost)",
        ],
    },
    {
        "name": "RE Leases (Landlord)",
        "reference_doctype": "Opportunity",
        "field_name": "custom_re_lease_stage_landlord",
        "filters": [
            ["Opportunity", "opportunity_type", "=", "RE Lease (Landlord)", False],
            ["Opportunity", "status", "!=", "Closed", False],
        ],
        "columns": [
            "Listing Agreement Signed", "Marketing / Showings Active",
            "Application Received", "Tenant Screening / Review",
            "Negotiation", "Lease Signed", "Move-in Coordination",
            "Lease Commenced (Closed Won)", "Listing Withdrawn / Lost",
        ],
    },
    {
        "name": "RE Leases (Tenant)",
        "reference_doctype": "Opportunity",
        "field_name": "custom_re_lease_stage_tenant",
        "filters": [
            ["Opportunity", "opportunity_type", "=", "RE Lease (Tenant)", False],
            ["Opportunity", "status", "!=", "Closed", False],
        ],
        "columns": [
            "Property Identified", "Showing / Viewing Scheduled",
            "Application Submitted", "Negotiation", "Lease Approved",
            "Lease Signed", "Move-in Coordination",
            "Lease Commenced (Closed Won)", "Lease Not Executed (Closed Lost)",
        ],
    },
    {
        "name": "Lead Status Board",
        "reference_doctype": "Lead",
        "field_name": "custom_lead_status",
        "filters": [],
        "columns": [
            "Lead", "Qualifying", "Converted", "Not Qualified",
            "Cold", "Do Not Contact", "Junk",
        ],
    },
]


def after_install():
    create_kanban_boards()
    create_setup_tasks()


def create_kanban_boards():
    """
    Kanban Boards are created here (not as fixtures) because their
    `before_insert` hook queries the reference doctype using the kanban's
    field_name. If that field is a Custom Field, the DB column doesn't
    exist yet during fixture import — only after migrate has run.
    By the time after_install fires, sync_fixtures + migrate have
    already materialized the columns, so it's safe.
    """
    for kb in KANBAN_BOARDS:
        if frappe.db.exists("Kanban Board", kb["name"]):
            continue

        meta = frappe.get_meta(kb["reference_doctype"])
        if not meta.has_field(kb["field_name"]):
            frappe.log_error(
                f"Skipping Kanban Board '{kb['name']}': field "
                f"'{kb['field_name']}' not found on {kb['reference_doctype']}",
                "erpnext_realestate install"
            )
            continue

        doc = frappe.get_doc({
            "doctype": "Kanban Board",
            "name": kb["name"],
            "kanban_board_name": kb["name"],
            "reference_doctype": kb["reference_doctype"],
            "field_name": kb["field_name"],
            "filters": frappe.as_json(kb["filters"]) if kb["filters"] else None,
            "private": 0,
            "columns": [
                {
                    "column_name": col,
                    "indicator": "Gray",
                    "status": "Active",
                    "order": "[]",
                }
                for col in kb["columns"]
            ],
        })
        doc.insert(ignore_permissions=True)

    frappe.db.commit()


def create_setup_tasks():
    tasks = [
        "Set company name and logo in ERPNext Settings",
        "Configure email account for outbound communications",
        "Add Sales Partners (agents/brokers) in CRM > Sales Partner",
        "Add Supplier Partners (attorneys, lenders, inspectors) in Buying > Supplier",
        "Configure Opportunity Types: RE Sales, RE Buy, RE Lease (Landlord), RE Lease (Tenant)",
        "Import properties via Costar or Crexi import workflow",
        "Configure SMS Settings for client notifications",
        "Set up Lead Sources in CRM settings",
        "Review and configure Lead qualification fields",
        "Remove extra genders",
        "Test end-to-end workflow: Lead -> Opportunity -> Close",
    ]

    for task in tasks:
        frappe.get_doc({
            "doctype": "ToDo",
            "description": task,
            "status": "Open",
            "owner": frappe.session.user
        }).insert(ignore_permissions=True)
