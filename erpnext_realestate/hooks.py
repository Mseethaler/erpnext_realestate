app_name = "erpnext_realestate"
app_title = "ERPNext Real Estate"
app_publisher = "Digital Sovereignty"
app_description = "Real estate broker workflow for ERPNext - Triangle Commercial Real Estate"
app_version = "0.0.1"
app_email = "info@digital-sovereignty.cc"
app_license = "MIT"

after_install = "erpnext_realestate.setup.install.after_install"

# Doctypes whose custom fields belong to this app
RE_PARENT_DOCTYPES = ["Item", "Lead", "Customer", "Opportunity", "Contact"]

fixtures = [
    # Custom DocType: Listing
    {
        "dt": "DocType",
        "filters": [["name", "=", "Listing"]]
    },
    # Custom Fields on RE-relevant parent doctypes only, prefixed custom_re_ or custom_
    # Note: tighten the prefix once you decide on a convention. Recommend `custom_re_*`.
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "in", RE_PARENT_DOCTYPES],
            ["fieldname", "like", "custom_%"],
        ]
    },
    # Workspace
    {
        "dt": "Workspace",
        "filters": [["name", "=", "Real Estate"]]
    },
    # Custom DocPerms — scoped to RE parent doctypes + Listing only
    {
        "dt": "Custom DocPerm",
        "filters": [["parent", "in", RE_PARENT_DOCTYPES + ["Listing"]]]
    },
    # NOTE: Kanban Boards are created programmatically in setup/install.py
    # because they reference custom fields that don't exist at fixture-import time.
]

doctype_js = {}
