import frappe

def after_install():
    create_setup_tasks()

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
        "Remove extra genders"
        "Test end-to-end workflow: Lead -> Opportunity -> Close",
    ]

    for task in tasks:
        frappe.get_doc({
            "doctype": "ToDo",
            "description": task,
            "status": "Open",
            "owner": frappe.session.user
        }).insert(ignore_permissions=True)
