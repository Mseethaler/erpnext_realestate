app_name = "erpnext_realestate"
app_title = "ERPNext Real Estate"
app_publisher = "Digital Sovereignty"
app_description = "Real estate broker workflow for ERPNext - Triangle Commercial Real Estate"
app_version = "0.0.1"
app_email = "info@digital-sovereignty.cc"
app_license = "MIT"

after_install = "erpnext_realestate.setup.install.after_install"

fixtures = [
    # Item (Property) custom fields
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Item"],
            ["fieldname", "like", "custom_%"],
        ]
    },
    # Lead custom fields
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Lead"],
            ["fieldname", "like", "custom_%"],
        ]
    },
    # Customer custom fields
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Customer"],
            ["fieldname", "like", "custom_%"],
        ]
    },
    # Opportunity custom fields
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Opportunity"],
            ["fieldname", "like", "custom_%"],
        ]
    },
    # Contact custom fields
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Contact"],
            ["fieldname", "like", "custom_%"],
        ]
    },
    # Workspaces
    {
        "dt": "Workspace",
        "filters": [["name", "=", "Real Estate"]]
    },
    # Kanban Boards
    {
        "dt": "Kanban Board",
        "filters": [["name", "in", [
            "Lead Status Board",
            "RE Sales",
            "RE Buys",
            "RE Leases (Landlord)",
            "RE Leases (Tenant)"
        ]]]
    },
    # Custom DocType Permissions
    {
        "dt": "Custom DocPerm"
    },
]

doctype_js = {}
